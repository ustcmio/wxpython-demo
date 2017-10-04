import wx
import requests
from ui.loginUI import LoginScreen
from ui.mainUI import MainScreen

class Present(object):
    def __init__(self):
        self.loginScreen = LoginScreen(None,'Login Page')


class MyApp(wx.App):
    def OnInit(self):
        Present().loginScreen.Show()
        self.Bind(wx.EVT_BUTTON, self.OnClick)

    def OnClick(self,event):
        objName = event.GetEventObject().GetName()
        if objName == 'btn_clear':
            Present.loginScreen.Clear()