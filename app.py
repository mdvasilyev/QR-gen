import wx


if __name__ == "__main__":
    app = wx.App()

    frame = wx.Frame(None, title="Test")
    frame.Show()

    app.MainLoop()