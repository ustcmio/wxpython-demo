import wx


class UpdataPanel(wx.Panel):
    def __init__(self,parent,style):
        wx.Panel.__init__(self,parent,style=style)
        wx.StaticText(self,label='在线更新数据库页面')