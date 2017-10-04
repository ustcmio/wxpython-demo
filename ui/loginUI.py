import wx


class LoginScreen(wx.Frame):
    def __init__(self, present, title):
        wx.Frame.__init__(self, present, title=title, style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER)
        self.CenterOnScreen()
        self.p = wx.Panel(self, style=wx.SUNKEN_BORDER)
        self.p.SetBackgroundColour('#BFEFFF')
        self.sizer = wx.GridBagSizer(hgap=8, vgap=8)
        head = wx.StaticText(self.p, label="幸福东亭信息系统 || User Login")
        username = wx.StaticText(self.p, label='用户名：')
        password = wx.StaticText(self.p, label='密  码：')
        self.input_username = wx.TextCtrl(self.p, size=(180, -1))
        self.input_password = wx.TextCtrl(self.p, size=(180, -1))
        self.btn_clear = wx.Button(self.p, label='清空', name='btn_clear')
        self.btn_login = wx.Button(self.p, label='登录', name='btn_login')
        self.btn_login_offline = wx.Button(self.p, label='离线登录', name='btn_login_offline')
        self.msg = wx.StaticText(self.p)
        self.msg.SetForegroundColour('red')
        self.sizer.Add((50, 20), pos=(0, 0))
        self.sizer.Add((50, 20), pos=(5, 4))
        self.sizer.Add(head, pos=(1, 1), span=(1, 3), flag=wx.ALIGN_LEFT)
        self.sizer.Add(username, pos=(2, 1), flag=wx.ALIGN_CENTER)
        self.sizer.Add(password, pos=(3, 1), flag=wx.ALIGN_CENTER)
        self.sizer.Add(self.input_username, pos=(2, 2), span=(1, 2))
        self.sizer.Add(self.input_password, pos=(3, 2), span=(1, 2))
        self.sizer.Add(self.btn_clear, pos=(4, 1))
        self.sizer.Add(self.btn_login, pos=(4, 2))
        self.sizer.Add(self.btn_login_offline, pos=(4, 3))
        self.sizer.Add(self.msg, pos=(5,0),span=(1,3))
        self.p.SetSizer(self.sizer)
        self.sizer.Fit(self)
        # self.Bind(wx.EVT_BUTTON, self.OnClick)

    # def OnClick(self, event):
    #     obj = event.GetEventObject().GetName()
    #     if obj == 'btn_clear':
    #         self.input_username.Clear()
    #         self.input_password.Clear()
    #     if obj == 'btn_login':
    #         pass
    #     if obj == 'btn_login_offline':
    #         pass

    def clear(self):
        self.input_password.Clear()
        self.input_username.Clear()

    def showErrMsg(self,msg):
        self.msg.SetLabelText(msg)

    def getLogininfo(self):
        return (self.input_username.GetValue(),self.input_password.GetValue())


class MyApp(wx.App):
    def OnInit(self):
        s = LoginScreen(None, 'Login Page')
        self.SetTopWindow(s)
        s.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
