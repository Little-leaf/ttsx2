from db.AbstractModel import *
from utils.wrppers import *


class UserManager(models.Manager):
    """创建管理器类"""
    # 判断用户名是否一样
    def user_by_name(self, name):
        try:
            return self.get(user_name=name)
        except User.DoesNotExist:
            return None

    # 保存用户注册信息
    def save_by_info(self, request):
        user = User()
        user.user_name = post(request, 'user_name')
        user_password = post(request, 'cpwd')
        user.user_pass = set_password(user_password)
        user.user_email = post(request, 'user_email')

        user.save()

    # 保存用户修改
    def save_addr(self, request):
        user = User.objects.user_by_name(get_session(request, 'user_name'))
        user.user_recv = post(request, 'user_recv')
        user.user_addr = post(request, 'user_addr')
        user.user_tel = post(request, 'user_tel')
        user.user_code = post(request, 'user_code')
        user.save()



# 继承基类
class User(AbstractModel):
    """创建用户模型类"""
    user_name = models.CharField(max_length=40)
    user_pass = models.CharField(max_length=65)
    user_email = models.CharField(max_length=50)
    user_addr = models.CharField(max_length=1000)
    user_code = models.CharField(max_length=20)
    user_tel = models.CharField(max_length=11)
    user_recv = models.CharField(max_length=30, default='')  # 默认不为空，但是我们需求可以为空
    objects = UserManager()


class RecordBrowse(AbstractModel):
    """用户浏览纪录类"""
    # 浏览商品
    browse_goods = models.ForeignKey('goods.goods_info')
    # 浏览者
    browse_user = models.ForeignKey('User')
