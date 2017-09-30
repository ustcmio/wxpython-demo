import wx


class SearchPanelByOffline(wx.Panel):
    def __init__(self,parent,style):
        wx.Panel.__init__(self,parent,style=style)
        wx.StaticText(self,label='离线查询页面')