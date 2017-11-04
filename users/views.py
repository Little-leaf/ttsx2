from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
# from utils.wrppers import *
from order.models import *
from django.core.paginator import Paginator
import re
from .models import *
from .function import *


@check_permission
def index(request):
    """用户信息"""
    # 接受用户数据
    user = User.objects.user_by_name(get_session(request, 'user_name'))
    # records = RecordBrowse.objects.filter(browse_user_id=get_session(request, 'uid')).order_by('-create_time')

    return render(request, 'users/user_center_info.html', locals())


def register(request):
    """用户注册"""
    mess = get_massages(request)
    print(mess)
    return render(request, 'users/register.html', locals())


def register_handle(request):
    """处理用户信息页面"""
    if check_register_info(request):
        # 判断flag是不是TRUE

        User.objects.save_by_info(request)
        print('格式正确')
        return redirect(reverse('users:login'))

    else:
        # 保存用户输入
        print('flag=False')
        return redirect(reverse('users:register'))


def login(request):
    """用户登录"""
    return render(request, 'users/login.html', locals())


@check_permission
def user_order(request):
    """用户订单"""
    orders = Order.objects.filter(order_user_id=get_session(request, 'uid'))
    # 分页
    paginator = Paginator(orders, 2)

    current_page = get(request, 'page')
    if not current_page:
        current_page = 1

    # 获得当前页面
    orders = paginator.page(current_page)
    for order in orders:
        order.total = 0
        for goods in order.goodsdetail_set.all():
            order.total += goods.detail_amount * goods.detail_price
    return render(request, 'users/user_center_order.html', locals())


@check_permission
def user_site(request):
    """用户地址"""
    user = User.objects.user_by_name(get_session(request, 'user_name'))
    return render(request, 'users/user_center_site.html', locals())


# 校验用户是否已经存在
# def check_username(request):
#     if name_is_exist(request):
#         print('存在')
#         # 用户存在
#         return JsonResponse({'ret': 1})
#     else:
#         print('不存在')
#         return JsonResponse({'ret': 0})
def check_username(request):
    if name_is_exist(request):
        return JsonResponse({'ret': 1})
    else:
        return JsonResponse({"ret": 0})

# 跳转登录跳转页面
# def login_handle(request):
#     # 对用户登录做简单的验证
#     if check_login_parms(request):
#         # 如果返回Ｔｒｕｅ，说明验证正确，就保存状态（session）
#         keep_user_online(request)
#         # 获取到上次访问的页面
#         pre_url = get_pre_url(request)
#         # 登录成功后跳转原来的页面
#         response = redirect(pre_url)
#
#         # 是否cookie 保存
#         print('11111111111111111')
#         remember_checkbox(request, response)
#         return response
#
#     else:
#         return redirect(reverse('users:login'))


def login_handle(request):
    if check_login_parms(request):
        # 保持登录状态
        keep_user_online(request)
        # 是否记住用户名
        # 获得上级ｕｒｌ
        url = get_pre_url(request)
        # 跳转上级页面
        response = redirect(url)
        remember_checkbox(request, response)

        return response
    else:
        return redirect(reverse('users:login'))


def logout(request):
    # 注销
    url = get_pre_url(request)

    print('logout_pre_url;', url)

    del_session(request)
    return redirect(url)


def address_edit(request):
    # 修改地址验证
    if check_addr_edit(request):
        # 保存到数据库
        User.objects.save_addr(request)
    return redirect(reverse('users:user_site'))




















# # 注销页面
# def logout(request):
#     url = get_pre_url(request)
#     print('logout', url)
#     del_session(request)
#     return redirect(url)
