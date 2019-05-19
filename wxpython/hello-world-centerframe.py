import wx

#creating application object
app = wx.App()

#application frame
frame = wx.Frame(None, title = "Hello World")

#show the application
frame.Show()

#set the apps frame in center of screen display
frame.Centre()

#event loop
app.MainLoop()