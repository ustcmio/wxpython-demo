import wx
import threading


# 计算fib函数
def showfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return showfib(n - 1) + showfib(n - 2)


# Fib计算的线程类
class FibThread(threading.Thread):
    def __init__(self, window, n):
        super(FibThread, self).__init__()

        self.window = window
        self.n = n

    # 重写run方法，计算完成fib函数后，调用CallAfter(函数名，参数)方法
    def run(self):
        result = showfib(self.n)
        wx.CallAfter(self.window.output.SetValue, str(result))
        wx.CallAfter(self.window.StopBusy)


# 应用框架Frame类
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        # 调用父类初始化
        super(MyFrame, self).__init__(*args, **kwargs)
        # 内置一个Panel窗口界面
        self.panel = MyPanel(self)
        # 通过Sizer来管理界面布局
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetInitialSize()


# 窗口界面Panel类
class MyPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        # 调用父类初始化
        super(MyPanel, self).__init__(*args, **kwargs)
        # 使用Sizer来管理布局
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        gsizer = wx.GridSizer(2, 2, 5, 5)

        # 界面控件
        self.input = wx.SpinCtrl(self, value='35', min=1)  # 可选输入
        self.output = wx.TextCtrl(self)  # 结果输出
        self.btn_block = wx.Button(self, label='Block')  # 按钮Block
        self.btn_non_block = wx.Button(self, label='Non-Block')  # 按钮Non-Block
        # self.timer = wx.Timer(self)
        self.prog = wx.Gauge(self)  # 进度条

        # 界面控件的布局
        gsizer.Add(wx.StaticText(self, label="fab(n):"))
        gsizer.Add(self.input)
        gsizer.Add((wx.StaticText(self, label='result:')))
        gsizer.Add(self.output)
        hsizer.Add(self.btn_block)
        hsizer.Add(self.btn_non_block)
        vsizer.Add(self.prog, 0, wx.EXPAND | wx.ALL, border=5)
        vsizer.Add(gsizer, flag=wx.ALL, border=5)
        vsizer.Add(hsizer, flag=wx.ALIGN_CENTRE | wx.ALL, border=5)

        # 加载布局到Panel上
        self.SetSizer(vsizer)

        # 绑定事件处理函数
        self.Bind(wx.EVT_BUTTON, self.OnButton)  # 绑定按键事件处理
        # self.Bind(wx.EVT_TIMER, self.OnPulse, self.timer)   # 绑定进度条事件处理

    def OnButton(self, event):
        input = self.input.GetValue()
        self.output.SetValue('')
        self.StartBusy()
        if event.GetEventObject() == self.btn_block:
            result = showfib(input)
            self.output.SetValue(str(result))
            self.StopBusy()
        else:
            task= FibThread(self,input)
            task.start()

    def OnPulse(self, event):
        self.prog.Pulse()

    def StartBusy(self):
        self.prog.Pulse()
        # self.timer.Start(100)
        self.btn_block.Disable()
        self.btn_non_block.Disable()

    def StopBusy(self):
        # self.timer.Stop()
        self.prog.SetValue(0)
        self.btn_block.Enable()
        self.btn_non_block.Enable()


# App类
class MyApp(wx.App):
    # 重写OnInit()方法
    def OnInit(self):
        frame = MyFrame(None, title='Non-Blocking')
        frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
