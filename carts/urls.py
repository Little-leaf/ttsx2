from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^add_goods/$', views.add_goods, name='add_goods'),
    url(r'^edit_goods_num/$', views.edit_goods_num, name='edit_goods_num'),
    url(r'^remove_goods/$', views.remove_goods, name='remove_goods'),

]
