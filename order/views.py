from django.shortcuts import render
from users.models import *
from carts.models import *
import time
from .models import *
import random
from django.http import JsonResponse
from utils.wrppers import *
from django.db import transaction


@check_permission
def index(request):
    goods_ids = post_list(request, 'goods_id')
    # __in 表示，在这中间

    goods_string = ','.join(goods_ids)

    carts = Cart.objects.filter(cart_goods_id__in=goods_ids, cart_user_id=get_session(request, 'uid'))

    total_num = 0
    total_money = 0

    for cart in carts:
        # 单品的总价
        cart.price = cart.cart_amount * cart.cart_goods.goods_price

        # 单品的数量
        total_num += cart.cart_amount
        total_money += cart.price

    # 动态绑定
    carts.total_num = total_num
    carts.total_money = total_money

    user = User.objects.get(id=get_session(request, 'uid'))

    # print()
    return render(request, 'order/place_order.html', locals())


def order_handle(request):
    # 获得商品ｉｄ列表
    goods_ids = post(request, 'ids').split(',')
    print(goods_ids)

    # 获得商品付款方式
    pay = post(request, 'pay')
    print(pay)
    user_id = get_session(request, 'uid')
    print(user_id)

    # 获得商品列表
    carts = Cart.objects.filter(cart_user_id=user_id, cart_goods_id__in=goods_ids)
    print(carts)
    # 获得用户信息
    user = User.objects.get(id=user_id)

    # 创建一个存档(保存点)
    save_point = transaction.savepoint()
    print('1')
    try:

        print('2')
        # 创建一个订单对象
        order = Order()
        # 订单的地址
        order.order_addr = user.user_addr
        # 订单的编号
        order.order_number = str(user_id) + str(int(time.time())) + str(random.randint(1000, 9999))
        # 付款方式
        order.order_pay = pay
        # 收件人
        order.order_recv = user.user_recv
        # 订单的所属者(外键)
        order.order_user = user
        print(order.order_addr)
        print(order.order_number)
        print(order.order_pay)
        print(order.order_recv)
        print('---')
        order.save()
        print('保存')
        # except Exception as ret:
        #     print(ret)
        for cart in carts:

            try:
                detail = GoodsDetail()
                detail.detail_amount = cart.cart_amount
                detail.detail_goodsid = cart.cart_goods_id
                detail.detail_img = cart.cart_goods.goods_image
                detail.detail_price = cart.cart_goods.goods_price
                detail.detail_name = cart.cart_goods.goods_name
                detail.detail_unit = cart.cart_goods.goods_unit
                detail.detail_goods = order
                detail.save()
            except Exception as ret:
                print(ret)

        # 删除购物车中的商品
        carts.delete()
        print('删除了')

        transaction.savepoint_commit(save_point)
    except:
        # 回滚到保存点
        transaction.savepoint_rollback(save_point)
        return JsonResponse({'ret': 0})

    return JsonResponse({'ret': 1})