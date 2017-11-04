from django.shortcuts import render
from utils.wrppers import *
from .functions import *
from django.core.paginator import Paginator
from .models import *


@get_cart_goods_amount
def index(request):
    """商品首页"""
    ad1 = Advertise.objects.all()[:4]
    ad2 = Advertise.objects.all()[4:]

    cates = Category.objects.all()
    for cate in cates:
        print(cate.cag_name)
        new_goods = goods_info.objects.new_goods(cate)
        hot_goods = goods_info.objects.hot_goods(cate)
        cate.new = new_goods
        cate.hot = hot_goods

    return render(request, 'goods/index.html', locals())


@get_cart_goods_amount
def detail(request):
    # 获取ｉｄ　，和对象
    goods = goods_info.objects.get(pk=get(request, 'id'))
    # 获得最新的２个商品
    new_goods = goods_info.objects.get_new_2()

    # 更新用户浏览商品信息
    update_goods_info(request)

    return render(request, 'goods/detail.html', locals())


@get_cart_goods_amount
def goods_list(request, cag_id, page_id):

    # 获取商品分类表
    cags = Category.objects.all()
    # 获取show的参数，
    show = get(request, 'show')
    # 分类对应的商品表
    goods = goods_info.objects.get_goodlist_by_cagid(cag_id, show)

    # 创建分页对象
    paginator = Paginator(goods, 10)
    current_page = paginator.page(page_id)

    # 获取最新的商品
    new_good = goods_info.objects.get_new_2()
    return render(request, 'goods/list.html', locals())
#
#
# def aaa(request):
#     from django.http import HttpResponse
#     return HttpResponse('ok')
