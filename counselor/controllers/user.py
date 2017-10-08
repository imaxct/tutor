from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from ..models import *
from ..beans import *


def user_login(request):
    """
    用户登录
    :return:
    """
    user = authenticate(request, username=request.POST['stu_no'], password=request.POST['id_no'])
    if user is not None:
        login(request, user)
        return JsonResponse(Msg.ok(msg=u'登录成功').__dict__, safe=False)
    else:
        return JsonResponse(Msg.err(msg=u'登录失败, 学号或身份证号错误').__dict__, safe=False)


def user_logout(request):
    """
    用户登出
    :return:
    """
    logout(request)
    return HttpResponse(u'退出成功')


def user_submit():
    """
    用户提交问卷
    :return:
    """
    pass
