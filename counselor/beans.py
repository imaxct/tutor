class Msg(object):
    ok = False
    msg = None
    obj = None

    def __init__(self, ok, msg, obj):
        self.ok = ok
        self.msg = msg
        self.obj = obj

    @staticmethod
    def ok(msg='ok', obj=None):
        return Msg(ok=True, msg=msg, obj=obj)

    @staticmethod
    def err(msg='fail', obj=None):
        return Msg(ok=False, msg=msg, obj=obj)
