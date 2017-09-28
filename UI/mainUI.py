import wx


class MainScreen(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.Size(1280, 800))
        self.CenterOnScreen()
        self.sp = wx.SplitterWindow(self)
        self.p_top = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p_top.Hide()
        self.sp_main = wx.SplitterWindow(self.sp)
        # self.sp_main.Hide()
        self.sp.SplitHorizontally(self.p_top, self.sp_main, sashPosition=self.GetSize()[1] / 6)

        self.p_left = wx.Panel(self.sp_main, style=wx.SUNKEN_BORDER)
        self.p_main = wx.Panel(self.sp_main, style=wx.SUNKEN_BORDER)
        self.p_left.Hide()
        self.p_main.Hide()
        self.sp_main.SplitVertically(self.p_left, self.p_main, sashPosition=self.GetSize()[0] / 5)

        self.btn_s1 = wx.Button(self.p_left, size=wx.Size(80,80),label='查询')
        self.btn_s2 = wx.Button(self.p_left, size=wx.Size(80, 80),label='审核')
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add((50,50))
        self.sizer.Add(self.btn_s1, flag= wx.ALIGN_CENTER)
        self.sizer.Add((50, 50))
        self.sizer.Add(self.btn_s2, flag=wx.ALIGN_CENTER)
        self.p_left.SetSizer(self.sizer)



class MyApp(wx.App):
    def OnInit(self):
        return True


if __name__ == '__main__':
    app = MyApp()
    frame = MainScreen(None, 'SplitterDemo')
    frame.Show()
    app.SetTopWindow(frame)
    app.MainLoop()
