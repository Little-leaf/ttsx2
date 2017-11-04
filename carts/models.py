from django.db import models
from db.AbstractModel import *


class Cart_Manager(models.Manager):
    """购物车管理器"""
    pass


class Cart(AbstractModel):
    """购物车类"""
    # 购买商品
    cart_goods = models.ForeignKey('goods.goods_info')
    # 购买的商品数量
    cart_amount = models.IntegerField()
    # 购买者
    cart_user = models.ForeignKey('users.User')

    objects = Cart_Manager()