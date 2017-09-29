import wx
from searchPanel import SearchPanel
from leftPanel import LeftPanel
from checkPanel import CheckPanel
from updataPanel import UpdataPanel
from searchPanel_offline import SearchPanelByOffline


class MainScreen(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.Size(1280, 800))
        # 窗口居中
        self.CenterOnScreen()
        # 分割窗口
        self.sp = wx.SplitterWindow(self)
        # Top窗口：panel
        self.p_top = wx.Panel(self.sp, style=wx.SUNKEN_BORDER)
        self.p_top.Hide()
        # 下部分窗口：左右分割的splitter
        self.sp_main = wx.SplitterWindow(self.sp)
        # 上下两部分窗口填充
        self.sp.SplitHorizontally(self.p_top, self.sp_main, sashPosition=self.GetSize()[1] / 6)

        # 下部分窗口的left:panel
        self.p_left = LeftPanel(self.sp_main, style=wx.SUNKEN_BORDER)
        self.p_left.Hide()
        # 下部分窗口的right：panel
        self.p_mains = [SearchPanel(self.sp_main, style=wx.SUNKEN_BORDER),
                        CheckPanel(self.sp_main, style=wx.SUNKEN_BORDER),
                        UpdataPanel(self.sp_main, style=wx.SUNKEN_BORDER),
                        SearchPanelByOffline(self.sp_main, style=wx.SUNKEN_BORDER)
                        ]
        for p in self.p_mains:
            p.Hide()

        # 下部分窗口默认填充查询页面
        self.sp_main.SplitVertically(self.p_left, self.p_mains[0], sashPosition=self.GetSize()[0] / 6)
        self.main_index = 0

        self.Bind(wx.EVT_BUTTON, self.OnClick)

    def OnClick(self, event):
        obj = event.GetEventObject().GetName()
        # print(obj, self.main_index)
        if obj == 'btn_search' and self.main_index != 0:
            self.changePanel(0)
        if obj == 'btn_check' and self.main_index != 1:
            self.changePanel(1)
        if obj == 'btn_updata' and self.main_index != 2:
            self.changePanel(2)
        if obj == 'btn_search_offline' and self.main_index != 3:
            self.changePanel(3)

    def changePanel(self, index):
        # print(index)
        self.sp_main.Unsplit(toRemove=None)
        self.sp_main.SplitVertically(self.p_left, self.p_mains[index], sashPosition=self.GetSize()[0] / 6)
        # self.sp_main.GetWindow2().Hide()
        # self.sp_main.ReplaceWindow(self.sp_main.GetWindow2(),self.p_mains[index])
        self.main_index = index


class MyApp(wx.App):
    def OnInit(self):
        return True


if __name__ == '__main__':
    app = MyApp()
    frame = MainScreen(None, 'SplitterDemo')
    frame.Show()
    app.SetTopWindow(frame)
    app.MainLoop()
