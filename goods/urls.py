from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^list/(\d+)/(\d+)/$', views.goods_list, name='list'),

    # url(r'^aaa/(?:page-(?P<page_number>\d+)/)?$', views.aaa),


]
