import wx
from wx.lib.splitter import MultiSplitterWindow


class TestPanel(wx.Panel):
    def __init__(self, parent,label,style=wx.SUNKEN_BORDER):
        wx.Panel.__init__(self,parent,style = style)
        label = wx.TextCtrl(self,value=label)

class SearchPanel(MultiSplitterWindow):
    def __init__(self, parent):
        MultiSplitterWindow.__init__(self, parent)
        self.SetOrientation(wx.VERTICAL)
        self.p1 = TestPanel(self,"aaaaaaaaa")
        btn = wx.Button(self.p1,label='btn',pos=(300,-1))
        self.Bind(wx.EVT_BUTTON,self.OnClick,btn)
        self.p2 = TestPanel(self, "bbbbbbbbb")
        self.p3 = TestPanel(self, "ccccccccc")
        self.p4 = TestPanel(self, "ddddddddd")

        # p1.Hide()
        # p2.Hide()
        # p3.Hide()

        self.AppendWindow(self.p1, parent.GetSize()[1] / 4)
        self.AppendWindow(self.p2, parent.GetSize()[1] / 4)
        self.AppendWindow(self.p3, parent.GetSize()[1] / 2)

        # p1.Hide()
        # p2.Show()
        # p3.Hide()

    def OnClick(self,event):
        self.ReplaceWindow(self.p2,self.p4)

class MyApp(wx.App):
    def OnInit(self):
        fra = wx.Frame(None, title='MutiSplitterWondow', size=(800, 600))

        s = SearchPanel(fra)
        fra.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
