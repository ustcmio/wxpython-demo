import wx

class LoginScreen(wx.Frame):
    def __init__(self,present,title):
        wx.Frame.__init__(self,present,title=title,style=wx.DEFAULT_FRAME_STYLE^wx.RESIZE_BORDER)
        self.CenterOnScreen()
        self.p = wx.Panel(self,style=wx.SUNKEN_BORDER)
        self.sizer = wx.GridBagSizer(self.p,hgap=8,vgap=8)
        head = wx.StaticText(self.p,label="用户登录")
        username = wx.StaticText(self.p,label='用户名：')
        password = wx.StaticText(self.p,label='密  码：')
        input_username = wx.TextCtrl(self.p,size=(100,-1))
        input_password = wx.TextCtrl(self.p, size=(100, -1))
        btn_clear = wx.Button(self.p,label='清空')
        btn_login = wx.Button(self.p, label='登录')
        self.sizer.Add(head,pos=(0,0),span=(1,2))
        self.sizer.Add(username,pos=(1,0))
        self.sizer.Add(password, pos=(2, 0))
        self.sizer.Add(input_username,pos=(1,1))
        self.sizer.Add(input_password,pos=(2,1))
        self.sizer.Add(btn_clear,pos=(3,0))
        self.sizer.Add(btn_login,pos=(3,1))
        self.p.SetSizer(self.sizer)
        self.p.Fit()