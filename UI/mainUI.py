import wx
from wx.grid import Grid


class MainScreen(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.Size(1280, 800))
        self.CenterOnScreen()
        self.sp = wx.SplitterWindow(self)
        self.p_top = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p_top.Hide()
        self.sp_main = wx.SplitterWindow(self.sp)
        self.sp.SplitHorizontally(self.p_top, self.sp_main, sashPosition=self.GetSize()[1] / 6)

        self.p_left = wx.Panel(self.sp_main, style=wx.SUNKEN_BORDER)
        self.p_left.SetBackgroundColour('#E0FFFF')
        self.p_main = wx.Panel(self.sp_main, style=wx.SUNKEN_BORDER)
        self.p_main.SetBackgroundColour('#E0FFFF')
        self.p_left.Hide()
        self.p_main.Hide()
        self.sp_main.SplitVertically(self.p_left, self.p_main, sashPosition=self.GetSize()[0] / 6)

        self.btn_s1 = wx.Button(self.p_left, size=wx.Size(60, 40), label='查询')
        self.btn_s1.SetBackgroundColour('#9AFF9A')
        self.btn_s2 = wx.Button(self.p_left, size=wx.Size(60, 40), label='审核')
        self.btn_s2.SetBackgroundColour('#9AFF9A')
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add((50, 5))
        self.sizer.Add(self.btn_s1, flag=wx.EXPAND)
        self.sizer.Add((50, 5))
        self.sizer.Add(self.btn_s2, flag=wx.EXPAND)
        self.p_left.SetSizer(self.sizer)

        self.Bind(wx.EVT_BUTTON, self.OnClick, self.btn_s1)

        sizer_s = wx.BoxSizer(wx.VERTICAL)
        sizer_s_top = wx.BoxSizer(wx.HORIZONTAL)

        sizer_s_top.Add(wx.StaticText(self.p_main,label='姓名:   '),flag=wx.ALIGN_CENTER | wx.ALL^wx.RIGHT,border=40)
        sizer_s_top.Add(wx.TextCtrl(self.p_main,size=(150,-1)), flag=wx.ALIGN_CENTER)
        sizer_s_top.Add(wx.StaticText(self.p_main, label='身份证号:   '), flag=wx.ALIGN_CENTER | wx.ALL^wx.RIGHT, border=40)
        sizer_s_top.Add(wx.TextCtrl(self.p_main,size=(300,-1)), flag=wx.ALIGN_CENTER)
        sizer_s_top.Add(wx.Button(self.p_main,label='查询'), flag=wx.EXPAND | wx.ALL,border=40)

        sizer_s.Add(sizer_s_top,flag=wx.EXPAND)
        self.mul_text1 = wx.TextCtrl(self.p_main,style=wx.TE_MULTILINE|wx.TE_READONLY,size=(1,200))
        sizer_s.Add(self.mul_text1,flag=wx.EXPAND|wx.ALL,border=10)

        self.mul_text2 = wx.TextCtrl(self.p_main, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(1, 200))
        sizer_s.Add(self.mul_text2, flag=wx.EXPAND|wx.ALL,border=10)
        self.p_main.SetSizer(sizer_s)

    def OnClick(self, event):
        self.mul_text1.AppendText("aAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


class MyApp(wx.App):
    def OnInit(self):
        return True


if __name__ == '__main__':
    app = MyApp()
    frame = MainScreen(None, 'SplitterDemo')
    frame.Show()
    app.SetTopWindow(frame)
    app.MainLoop()
