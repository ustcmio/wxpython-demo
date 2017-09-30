import wx


class MyApp(wx.App):
    def OnInit(self):

        return True


if __name__ == '__main__':
    app = MyApp()
    frame = wx.Frame(None, -1, "MyAppDemo", size=(800, 600))
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(wx.Button(frame, label='Hello World'), flag=wx.ALIGN_CENTER)
    sizer.Add(wx.Button(frame, label='Hello World',size=(100,50)), flag=wx.EXPAND|wx.ALL,border=200, proportion=1)
    frame.SetSizer(sizer)
    sizer.Fit(frame)
    frame.Show()
    app.MainLoop()
