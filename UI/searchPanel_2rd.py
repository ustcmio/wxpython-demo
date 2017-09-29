import wx
from wx.lib.splitter import MultiSplitterWindow


class SearchPanel(MultiSplitterWindow):
    def __init__(self, parent):
        MultiSplitterWindow.__init__(self, parent)
        self.SetOrientation(wx.VERTICAL)
        self.AppendWindow(wx.Panel(self, id=1,style=wx.SUNKEN_BORDER), parent.GetSize()[1] / 4)
        self.AppendWindow(wx.Panel(self, id=2, style=wx.SUNKEN_BORDER), parent.GetSize()[1] / 4)
        self.AppendWindow(wx.Panel(self, id=3,style=wx.SUNKEN_BORDER), parent.GetSize()[1] / 2)


class MyApp(wx.App):
    def OnInit(self):
        return True


if __name__ == '__main__':
    app = MyApp()
    fra = wx.Frame(None, title='MutiSplitterWondow', size=(800, 600))
    s = SearchPanel(fra)

    s.GetWindow(0).Hide()
    fra.Show()
    app.MainLoop()
