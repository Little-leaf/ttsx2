from utils.wrppers import *
from .models import *
import re
from django.core.urlresolvers import reverse
import hashlib
from django.contrib import messages


def check_register_info(request):
    # 注册验证
    user_name = post(request, 'user_name')
    # print("user_name:", user_name)
    user_pwd = post(request, 'pwd')
    user_cpwd = post(request, 'cpwd')
    user_email = post(request, 'user_email')
    flag = True
    if not (5 < len(user_name) < 20):
        flag = False
        add_massages(request, "user_name", "您的用户名长度不对")
    if not (8 < len(user_cpwd) < 20):
        flag = False
        add_massages(request, "user_pwd", "您的密码长度不对")
        # print('m1', m1)

    if user_pwd != user_cpwd:
        flag = False
        add_massages(request, 'user_cpwd', '两次密码不一样')

    # 判断邮箱
    ret = '^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$'
    if not re.match(ret, user_email):
        flag = False
        add_massages(request, "user_email", "您的邮箱格式不对")
    # 判断用户名是否存在

    if User.objects.user_by_name(user_name):
        flag = False
        add_massages(request, 'user_name', '你的用户名已经注册')
    return flag


# def name_is_exist(request):
#     检测用户是否存在
#     获取ajax的user）name数据
    # name = get(request, 'user_name')
    # print('name', name)
    # return User.objects.user_by_name(name)


def name_is_exist(request):
    name = post(request, 'user_name')
    return User.objects.user_by_name(name)


# def check_login_parms(request):
#     # 判断用户登录信息验证
#     print('jjjjjj')
#     user_name = post(request, 'user_name')
#     user_pass = post(request, 'user_pass')
#     print(user_name)
#     print(user_pass)
#     if not (5 < len(user_name) < 20):
#         return False
#     if not (8 < len(user_pass) < 20):
#         return False
#     user = User.objects.user_by_name(user_name)
#     print(user)
#     if not user:
#         # 判断用户名是否存在
#         return False
#     else:
#         # 已经存在，判断密码是否正确,注意是和加密后密码判断
#         if user.user_pass == set_password(user_pass):
#             return True
#         else:
#             return False


# def remember_checkbox(request, response):
#     # 判断是否需要记住用户名
#     if post(request, 'user_rem'):
#         make_cookie(response, 'user_name', post(request, 'user_name'))


# def keep_user_online(request):
#     make_session(request, 'user_name', post(request, 'user_name'))

def keep_user_online(request):
    user = User.objects.user_by_name(post(request, 'user_name'))
    make_session(request, 'user_name', user.user_name)
    make_session(request, 'uid', user.id)



# def get_pre_url(request):
#     url = get_session(request, 'pre_url')
#     print('get_pre_url:', url)
#     if not url:
#         url = reverse('users:index')
#     return url
def get_pre_url(request):

    # pre_url = get_session(request, 'pre_url')
    pre_url = get_cookie(request, 'pre_url')
    if pre_url:
        print('有上级url')
        print(pre_url)
        return pre_url
    else:
        print('没有上级页面')
        return reverse('users:index')


def check_login_parms(request):
    name = post(request, 'user_name')
    password = post(request, 'user_pass')
    if not (5 < len(name) < 20):
        return False
    if not (8 < len(password) < 20):
        return False
    user = User.objects.user_by_name(name)
    if user:
        if user.user_pass == set_password(password):
            return True
        else:
            return False
    else:
        return False


def remember_checkbox(request, response):
    user_rem = post(request, 'user_rem')

    if user_rem:
        make_cookie(response, 'user_name', post(request, 'user_name'))


# 地址修改验证
def check_addr_edit(request):
    user_recv = post(request, 'user_recv')
    user_addr = post(request, 'user_addr')
    user_code = post(request, 'user_code')
    user_tel = post(request, 'user_tel')
    if len(user_recv) == 0:
        return False
    if len(user_addr) == 0:
        return False
    if len(user_code) != 6:
        return False
    if len(user_tel) != 11:
        return False
    return True

