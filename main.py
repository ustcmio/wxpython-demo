import wx
from ui.loginUI import LoginScreen
from ui.mainUI import MainScreen
import requests


class MyApp(wx.App):
    def OnInit(self):
        self.loginscreen = LoginScreen(None, 'Login Page')
        self.mainscreen = None
        self.SetTopWindow(self.loginscreen)
        self.loginscreen.Show()
        self.Bind(wx.EVT_BUTTON, self.onClick)
        return True

    def onClick(self, event):
        objName = event.GetEventObject().GetName()
        if objName == 'btn_clear':
            self.loginscreen.clear()
        if objName == 'btn_login':
            username, password = self.loginscreen.getLogininfo()
            login_result, msg = self.login(username, password)
            if login_result:
                self.mainscreen = MainScreen(None, 'Main Page')
                self.loginscreen.Hide()
                self.mainscreen.Show()
                self.loginscreen.Destroy()
            else:
                self.loginscreen.showErrMsg(msg)
                self.loginscreen.clear()

    def login(self, username, password):
        if not username or not password:
            return (False, '用户名或密码不能为空')
        if username == '123' and password == '321':
            return (True, '登录成功')
        else:
            return (False, '登录失败：用户名或密码不正确！')


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
