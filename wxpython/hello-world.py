import wx

#creating application object
app = wx.App()

#application frame
frame = wx.Frame(None, title = "Hello World")

#show the application
frame.Show()

#event loop
app.MainLoop()