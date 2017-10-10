import wx
import threading
from types import FunctionType, MethodType


# 简单的装饰器，用来判断是否是主线程？直接调用 or 使用CallAfter()调用
def callafter(funct):
    def callafterwrap(*args, **kwargs):
        if wx.IsMainThread():
            return funct(*args, **kwargs)
        else:
            wx.CallAfter(funct, *args, **kwargs)

    callafterwrap.__name__ = funct.__name__
    callafterwrap.__doc__ = funct.__doc__
    return callafterwrap


class Synchronizer(object):
    def __init__(self, funct, args, kwargs):
        super(Synchronizer, self).__init__()

        self.funct = funct
        self.args = args
        self.kwargs = kwargs
        self._synch = threading.Semaphore(0)

    # 执行异步操作
    def _AsynchWrapper(self):
        try:
            self.result = self.funct(*self.args, **self.kwargs)
        except Exception as msg:
            self.exception = msg
        self._synch.release()

    def Run(self):
        assert not wx.IsMainThread(), 'Deadlock'
        wx.CallAfter(self._AsynchWrapper())
        self._synch.acquire()
        try:
            return self.result
        except AttributeError:
            raise self.exception


def synchfunct(funct):
    def synchwrap(*args, **kwargs):
        if wx.IsMainThread():
            return funct(*args, **kwargs)
        else:
            synchobj = Synchronizer(funct, args, kwargs)
            return synchobj.Run()

    synchwrap.__name__ = funct.__name__
    synchwrap.__doc__ = funct.__doc__
    return synchwrap


# 元类
class ClassSynchronizer(type):
    def __call__(mcs, *args, **kwargs):
        obj = type.__call__(mcs, *args, **kwargs)

        for attrname in dir(obj):
            attr = getattr(obj, attrname)
            if type(attr) in (MethodType, FunctionType):
                nfunct = synchfunct(attr)
                setattr(obj, attrname, nfunct)
        return obj
