from utils.wrppers import *


def user_is_login(request):
    return get_session(request, 'user_name')