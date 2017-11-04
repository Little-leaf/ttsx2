from django.conf.urls import url
from . import views
urlpatterns = [
    # 用户中心男页面
    url(r'^index/$', views.index, name='index'),
    # 用户注册页面
    url(r'^register/$', views.register, name='register'),
    # 用户登录页面
    url(r'^login/$', views.login, name='login'),
    # 用户订单页面
    url(r'^user_order/$', views.user_order, name='user_order'),
    # 用户地址页面
    url(r'^user_site/$', views.user_site, name='user_site'),
    # 用户注册跳转页面
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    # 判断用户登录跳转页面
    url(r'^check_username/$', views.check_username, name='check_username'),
    # 判断用户登录信息验证页面
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    # 注销登录
    url(r'^logout/$', views.logout, name='logout'),
    # 修改地址
    url(r'^address_edit/$', views.address_edit, name='address_edit'),

]
