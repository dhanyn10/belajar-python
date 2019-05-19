import wx

class HelloFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(HelloFrame, self).__init__(*args, **kw)
        panel = wx.Panel(self)

        #set static text properties
        st      = wx.StaticText(panel, label="Hello World", pos=(50,50))
        #set font properties for static text
        font    = st.GetFont()
        font.PointSize += 20
        font    = font.Bold()
        #apply font settings to static text
        st.SetFont(font)
        
        self.makeMenuBar()
    def makeMenuBar(self):
        #initiate menu bar for "File" menu
        fileMenu    = wx.Menu()
        fileMenu.Append(-1, "hello")
        fileMenu.Append(-1, "python here")
        menuBar     = wx.MenuBar()
        menu1Menu   = wx.Menu()
        #initiate menu bar for "Menu 1" menu
        menu1Menu.Append(-1, "item 1")
        menu1Menu.AppendSeparator()
        menu1Menu.Append(-1, "item 2")
        menu1Menu.Append(-1, "item 3")

        #insert menu bar item "fileMenu" in menu bar with title "File"
        menuBar.Append(fileMenu, "File")
        menuBar.Append(menu1Menu, "Menu 1")
        self.SetMenuBar(menuBar)

if __name__ == "__main__":
    app = wx.App()
    frm = HelloFrame(None, title = "Hello World")
    frm.Show()
    app.MainLoop()