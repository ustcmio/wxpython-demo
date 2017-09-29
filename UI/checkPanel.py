import wx


class CheckPanel(wx.Panel):
    def __init__(self,parent,style):
        wx.Panel.__init__(self,parent,style=style)
        wx.StaticText(self,label='在线审核页面')