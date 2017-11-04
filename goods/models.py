from django.db import models
from db.AbstractModel import *
from tinymce.models import HTMLField
from utils.wrppers import *


class GoodsInfoManger(models.Manager):
    def new_goods(self, cag):
        # 获得最新的４个商品
        return self.filter(goods_cag=cag).order_by('-id')[:4]

    def hot_goods(self, cag):
        # 获得最热的商品
        return self.filter(goods_cag=cag).order_by('-goods_visits')[:3]

    def get_new_2(self):
        # 所以商品中最新的２个商品
        return self.filter().all().order_by('-id')[:2]

    def get_goodlist_by_cagid(self, cag_id, show):
        # 根据cag_id返回商品分类列表
        if show == 'price':
            return self.filter(goods_cag_id=cag_id).order_by('-goods_price')

        if show == 'hot':
            return self.filter(goods_cag_id=cag_id).order_by('-goods_visits')
        return self.filter(goods_cag_id=cag_id)




# 分类模型
class Category(AbstractModel):
    # 产品分类名称
    cag_name = models.CharField(max_length=30)


class goods_info(AbstractModel):
    """商品类"""
    # 商品名称
    goods_name = models.CharField(max_length=50)
    # 商品价格
    goods_price = models.DecimalField(max_digits=10, decimal_places=2)
    # 商品图片
    goods_image = models.ImageField()
    # 商品简述
    goods_short = HTMLField()
    # 商品详情
    goods_desc = models.CharField(max_length=1000)
    # 商品上架
    goods_status = models.BooleanField(default=True)
    # 商品价格单位
    goods_unit = models.CharField(max_length=10)
    # 商品访问量
    goods_visits = models.IntegerField(default=0)
    # 商品销量
    goods_sales = models.IntegerField(default=0)
    # 商品分类
    goods_cag = models.ForeignKey(Category)

    objects = GoodsInfoManger()


# 广告模型类
class Advertise(AbstractModel):
    # 名字
    ad_name = models.CharField(max_length=20)
    # 图片
    ad_image = models.ImageField(upload_to='ad')
    # 链接
    ad_link = models.CharField(max_length=100)
