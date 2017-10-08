from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

from .controllers.user import *
from .controllers.admin import *


def index(request):
    """
    主页
    :return:
    """
    return render(request, 'user/index.html')
