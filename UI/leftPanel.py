import wx


class LeftPanel(wx.Panel):
    def __init__(self, parent,style):
        wx.Panel.__init__(self, parent,style=style)
        # left_panel部分
        self.btn_s1 = wx.Button(self, size=wx.Size(60, 40), label='在线查询', name='btn_search')
        self.btn_s1.SetBackgroundColour('#9AFF9A')
        self.btn_s2 = wx.Button(self, size=wx.Size(60, 40), label='在线审核', name='btn_check')
        self.btn_s2.SetBackgroundColour('#9AFF9A')
        self.btn_s3 = wx.Button(self, size=wx.Size(60, 40), label='更新离线数据库', name='btn_updata')
        self.btn_s3.SetBackgroundColour('#9AFF9A')
        self.btn_s4 = wx.Button(self, size=wx.Size(60, 40), label='离线查询', name='btn_search_offline')
        self.btn_s4.SetBackgroundColour('#9AFF9A')
        # 将button装入sizer管理
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add((50, 5))
        self.sizer.Add(self.btn_s1, flag=wx.EXPAND)
        self.sizer.Add((50, 5))
        self.sizer.Add(self.btn_s2, flag=wx.EXPAND)
        self.sizer.Add((50, 5))
        self.sizer.Add(self.btn_s3, flag=wx.EXPAND)
        self.sizer.Add((50, 5))
        self.sizer.Add(self.btn_s4, flag=wx.EXPAND)
        # sizer装入left_panel
        self.SetSizer(self.sizer)

        # 绑定按键出发
        self.Bind(wx.EVT_BUTTON, None, self.btn_s1)
        self.Bind(wx.EVT_BUTTON, None, self.btn_s2)
        self.Bind(wx.EVT_BUTTON, None, self.btn_s3)
        self.Bind(wx.EVT_BUTTON, None, self.btn_s4)
