from django.core.urlresolvers import reverse
from utils.wrppers import *
from django.utils import deprecation


class MiddlePreUrlWare(deprecation.MiddlewareMixin):

    # 列举不需要跳转的页面
    def process_response(self, request, response):
        exclude_url = [
            # localhost:8000/users/index/?a=1
            reverse('users:index'),
            reverse('users:register'),
            reverse('users:user_order'),
            reverse('users:user_site'),
            reverse('users:register_handle'),
            reverse('users:login'),
            reverse('users:login_handle'),
            reverse('users:logout'),
            reverse('users:check_username'),
            reverse('carts:index'),

        ]
        # print('aaaaa', request.session['pre_url'])
        # if request.path not in exclude_url and response.status_code == 200:
        #     # 纪录上一次的url
        #     request.session['pre_url'] = request.get_full_path()

        # return response
        # 获得上级ｕｒｌ
        if request.path not in exclude_url and response.status_code == 200:
            # request.session['pre_url'] = request.get_full_path()
            make_cookie(response, 'pre_url', request.get_full_path())
        return response
