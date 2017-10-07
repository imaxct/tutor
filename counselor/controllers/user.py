from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from ..models import *
from ..beans import *


def user_login(stu_no, id_no):
    """
    用户登录
    :return:
    """
    try:
        user = User.objects.get({'stu_no': stu_no, 'id_no': id_no})
    except ObjectDoesNotExist:
        return JsonResponse(Msg.ok(msg=u'登录失败, 学号或身份证号错误'))


def user_logout():
    """
    用户登出
    :return:
    """
    pass


def user_submit():
    """
    用户提交问卷
    :return:
    """
    pass
