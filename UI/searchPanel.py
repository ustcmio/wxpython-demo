import wx


class SearchPanel(wx.Panel):
    def __init__(self, parent, style):
        wx.Panel.__init__(self, parent, style=style)
        self.sizer_s = wx.BoxSizer(wx.VERTICAL)
        sizer_s_top = wx.BoxSizer(wx.HORIZONTAL)

        sizer_s_top.Add(wx.StaticText(self, label='姓名:   '), flag=wx.ALIGN_CENTER | wx.ALL ^ wx.RIGHT, border=40)
        self.nameText = wx.TextCtrl(self, size=(150, -1))
        sizer_s_top.Add(self.nameText, flag=wx.ALIGN_CENTER)
        sizer_s_top.Add(wx.StaticText(self, label='身份证号:   '), flag=wx.ALIGN_CENTER | wx.ALL ^ wx.RIGHT,
                        border=40)
        self.idText = wx.TextCtrl(self, size=(300, -1))
        sizer_s_top.Add(self.idText, flag=wx.ALIGN_CENTER)
        btn = wx.Button(self, label='查询',name='btn_search')
        sizer_s_top.Add(btn, flag=wx.EXPAND | wx.ALL, border=40)

        self.sizer_s.Add(sizer_s_top, flag=wx.EXPAND)
        self.mul_text1 = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(1, 200))
        self.sizer_s.Add(self.mul_text1, flag=wx.EXPAND | wx.ALL, border=10)

        self.mul_text2 = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(1, 200))
        self.sizer_s.Add(self.mul_text2, flag=wx.EXPAND | wx.ALL, border=10)
        self.SetSizer(self.sizer_s)

        self.Bind(wx.EVT_BUTTON,self.OnClickSearch,btn)

    def OnClickSearch(self,event):
        name = self.nameText.GetValue()
        id = self.idText.GetValue()
        self.mul_text1.AppendText(name+id)


