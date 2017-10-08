from django.contrib.auth.models import User as SysUser
from .models import User


class LoginCheck(object):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(stu_no=username, id_no=password)
            s_user = SysUser.objects.get(username=username, password=password)
        except SysUser.DoesNotExist:
            s_user = SysUser(username=username, password=password)
            s_user.is_active = True
            s_user.save()
        except User.DoesNotExist:
            return None
        return s_user

    def get_user(self, user_id):
        try:
            return SysUser.objects.get(pk=user_id)
        except SysUser.DoesNotExist:
            return None
