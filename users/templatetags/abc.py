from django.core.urlresolvers import reverse
from django.template import Library

# 注册
register = Library()


@register.filter
def create_menu(flag):
    menu = [
        {'link': reverse('users:index'), 'name': '个人信息', 'active': flag == 'info' and 'active' or ''},
        {'link': reverse('users:user_order'), 'name': '全部订单', 'active': flag == 'order' and 'active' or ''},
        {'link': reverse('users:user_site'), 'name': '收货地址', 'active': flag == 'site' and 'active' or ''},
    ]

    return menu
register.filter('create_menu', create_menu)


@register.filter
def browse_short(goods_list):
    goods = list()
    for good in goods_list:
        goods.append(good)

    goods.sort(key=lambda obj: obj.set_time, reverse=True)
    return goods

# from django.template import Library
# from django.core.urlresolvers import reverse
#
# register = Library()
#
#
#
#
# def create_menu(flag):
#
#     menu = [
#         {'link': reverse('users:index'), 'name': '个人信息', 'active': flag == 'info' and 'active' or ''},
#         {'link': reverse('users:user_order'), 'name': '全部订单', 'active': flag == 'order' and 'active' or ''},
#         {'link': reverse('users:user_site'), 'name': '收货地址', 'active': flag == 'address' and 'active' or ''},
#     ]
#
#     return menu
#
#
# register.filter('create_menu', create_menu)
