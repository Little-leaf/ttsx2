from django.shortcuts import render
from utils.wrppers import *
from django.http import JsonResponse
from .models import *


@check_permission  # 用户访问权限
def index(request):
    """购物车首页"""
    # 购物车首页显示
    carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'))
    # 商品总价
    money = 0
    # 商品总数量
    total = 0
    for cart in carts:
        # 单品总价
        cart.single_total = cart.cart_amount * cart.cart_goods.goods_price
        # 商品总数量
        total += cart.cart_amount
        money += cart.single_total
    # 动态绑定
    carts.total = total
    # 商品的总价格
    carts.money = money
    return render(request, 'carts/cart.html', locals())


def add_goods(request):
    """添加商品到购物车"""
    # 1. 商品的ID,购物用户的ID，购物车的商品数量
    goods_id = get(request, 'goods_id')
    user_id = get_session(request, 'uid')
    cart_num = get(request, 'goods_num')
    print(goods_id)
    print(user_id)
    print(cart_num)


    # 2. 判断商品是否已经存在
    # 2.1 存在就更新数量
    try:
        cart = Cart.objects.get(cart_goods_id=goods_id, cart_user_id=user_id)
        print('有cart')
        cart.cart_amount = cart.cart_amount + int(cart_num)
        print('save')
        cart.save()

    # 2.2 不存在就添加数据
    except Cart.DoesNotExist:
        cart = Cart()
        cart.cart_goods_id = goods_id
        cart.cart_user_id = user_id
        cart.cart_amount = cart_num
        print('添加成功')
        cart.save()

    # 返回购物车中的商品数量
        # 通过聚合计算商品总数量
        # Cart.objects.filter(cart_user_id=user_id).aggregate(models.Sum('cart_amount'))
    carts = Cart.objects.filter(cart_user_id=user_id)
    total = 0
    for cart in carts:
        total += cart.cart_amount
    return JsonResponse({'total': total})


def edit_goods_num(request):
    """修改商品的数量"""
    # 获的商品的ｉｄ
    id = get(request, 'id')
    print(id)
    # 获得商品的数量
    num = get(request, 'num')
    print(num)

    # 如果有该商品，就修改商品的数量
    try:
        cart = Cart.objects.get(cart_user_id=get_session(request, 'uid'), cart_goods_id=id)
        cart.cart_amount = num
        cart.save()
        print('保存')
        # 如果没有，返回０
    except Cart.DoesNotExist:
        print('么找到')
        return JsonResponse({'ret': 0})
    print('ret:1')
    return JsonResponse({'ret': 1})


def remove_goods(request):
    goods_id = get(request, 'id')
    try:
        cart = Cart.objects.get(cart_goods_id=goods_id, cart_user_id=get_session(request, 'uid'))
        cart.delete()

    except:
        pass
    return JsonResponse({'ret': 1})