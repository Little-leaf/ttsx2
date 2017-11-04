# 用来封装原生函数
import hashlib
from django.contrib import messages
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def post(request, key):
    return request.POST.get(key, '').strip()


def post_list(request, key):
    return request.POST.getlist(key)

def get(request, key):
    return request.GET.get(key, '').strip()


def get_massages(request):
    mess = messages.get_messages(request)
    info = dict()
    for msg in mess:
        content = str(msg).split(':')
        print('mess:', content)
        info[content[0]] = content[1]
    return info


def add_massages(request, key, value):
    # 添加信息
    messages.add_message(request, messages.INFO, key + ":" + value)


def set_password(password, salt=''):
    sha = hashlib.sha256()
    new_password = '#$' + password + salt + '@'
    # print(new_password)
    sha.update(new_password.encode('utf-8'))
    # print(sha.hexdigest())
    return sha.hexdigest()


# 设置session
def make_session(request, key, value):
    request.session[key] = value


# 获取session
def get_session(request, key):
    return request.session.get(key, '')


# 删除session
def del_session(request):
    request.session.flush()


# 设置cookie
def make_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*24)


# 获得cookie
def get_cookie(request, key):
    return request.COOKIES.get(key, '')


# 删除cookie
def del_cookie(response, key):
    response.delete_cookie(key)


# 判断用户是否登录
def check_user_online(request):
    return get_session(request, 'user_name')


# 用户访问权限
def check_permission(views_func):
    def wrapper(request, *args, **kwargs):

        if check_user_online(request):
            return views_func(request, *args, **kwargs)
        else:
            return redirect(reverse('users:login'))
    return wrapper
