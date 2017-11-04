from utils.wrppers import *
from utils.commen import *
from carts.models import *
from users.models import *


def update_goods_info(request):
    """更新用户浏览信息"""
    # 判断用户是否登录
    if not user_is_login(request):
        return
    # 纪录最大的浏览量
    limit = 5
    # 1,如果已经有商品浏览纪录，就更新时间

    # 从模板中接受参数ｉｄ
    goods_id = get(request, 'id')

    # 从session中获取uid
    user_id = get_session(request, 'uid')

    try:
        # 获取浏览纪录
        record = RecordBrowse.objects.get(browse_goods_id=goods_id, browse_user_id=user_id)
        record.save()
    # 2.商品不存在
    except RecordBrowse.DoesNotExist:
        # 这里的前提是用户已经登录，所有会有uid,吧它作为get的条件
        record = RecordBrowse.objects.filter(browse_user_id=user_id).order_by('set_time')

        print(record.values())
        # 判断浏览纪录是否已经有５条，没有就插入纪录
        if record.count() < limit:
            rb = RecordBrowse()
            rb.browse_goods_id = goods_id
            rb.browse_user_id = user_id
            rb.save()
        else:
            rb = record[0]
            print(rb.create_time)
            rb.browse_goods_id = goods_id
            rb.save()


# 定义购物车中的商品总数
def get_cart_goods_amount(views_func):
    def wrapper(request, *args, **kwargs):
        total = 0
        if check_user_online(request):
            carts = Cart.objects.filter(cart_user_id=get_session(request, 'uid'))

            for cart in carts:
                total += cart.cart_amount
        request.total = total
        return views_func(request, *args, **kwargs)
    return wrapper