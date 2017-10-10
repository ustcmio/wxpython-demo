import wx
import threading
from types import FunctionType,MethodType
# 自定义事件
# 1、自定义事件类型，本质上是唯一的整数码
wxEVT_UPDATE_GUI = wx.NewEventType()
# 2、自定义事件绑定器，用于和控件绑定
EVT_UPDATE_GUI = wx.PyEventBinder(wxEVT_UPDATE_GUI, 1)


# 3、自定义事件，继承wx.PyEvent或者wx.PyCommandEvent，用于事件触发时传递给处理函数
class ThreadUpdateEvent(wx.PyCommandEvent):
    def __init__(self, eventType, id):
        super(ThreadUpdateEvent, self).__init__(eventType, id)

        self.value = None

    def SetValue(self, value):
        self.value = value

    def GetValue(self):
        return self.value
