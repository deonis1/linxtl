webmol.py
import wx
import wx.html2 as webview
import os, sys
import json
import _thread
#----------------------------------------------------------------------
#https://wxpython.org/Phoenix/docs/html/stock_items.html
class webchem(wx.Frame):
    def __init__(self, event, parent,  paths, *args, **kwds):
        wx.Frame.__init__(self, event, parent, *args, **kwds)
        self.fnamefull = False
        if "path" in paths:
            self.fnamefull=paths["file"]
            self.path = paths["path"]
        else:
            self.path = sys.path[0]
        self.fname = os.path.join(self.path, "chem3d","main.html")
        self.dirname = os.curdir
        self.frame = self.GetTopLevelParent()
        self.titleBase = self.frame.GetTitle()
        sizer = wx.BoxSizer(wx.VERTICAL)
        btnSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.wv = webview.WebView.New(self)
        # self.toolbar = self.CreateToolBar(wx.TB_VERTICAL|wx.TB_RIGHT)
        # qtool = self.toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('../icon/coot.png'))
        # self.toolbar.Realize()
        # self.toolbar.SetToolBitmapSize((16,16))
        # self.Bind(wx.EVT_TOOL, self.OpenFile, qtool)


        self.Bind(webview.EVT_WEBVIEW_ERROR, self.OnWebViewError, self.wv)
        btn = wx.Button(self, -1, "Open", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OpenFile, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        btn = wx.Button(self, -1, "Labels", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.labels, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        btn = wx.Button(self, -1, "Rotate X", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.rotatex, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        btn = wx.Button(self, -1, "Rotate Y", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.rotatey, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        btn = wx.Button(self, -1, "Rotate Z", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.rotatez, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        btn = wx.Button(self, -1, "Optomize", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.optimize, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        btn = wx.Button(self, -1, "Refresh", style=wx.BU_EXACTFIT)
        self.Bind(wx.EVT_BUTTON, self.OnRefreshPageButton, btn)
        btnSizer.Add(btn, 0, wx.EXPAND|wx.ALL, 2)

        sizer.Add(btnSizer, 0, wx.EXPAND)
        sizer.Add(self.wv, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.current = u'file://' + str(self.fname)
        self.loadfile(event)
        # self.start()
        #self.wv.LoadURL(self.current)

    def getfile(self):
       datadict = {}
       # self.filename = "/home/denis/Dropbox/X-ray/GregWelch1/gregw.res"
       file_to_read= open(self.fnamefull, 'r')
       data = [l.lstrip() for l in file_to_read]
       print(os.path.splitext(self.fnamefull)[1])
       datadict["ext"] = os.path.splitext(self.fnamefull)[1][1:]
       datadict["data"] = data
       return datadict


    def writetmp(self):
        if self.fnamefull:
           print(os.path.join(os.path.dirname(self.fname), "main.js"))
           with open(os.path.join(os.path.dirname(self.fname), "main.js"), 'w') as f:
               f.write("var thefile ="+json.dumps(self.getfile()))

    def OnWebViewNavigated(self, evt):
        self.frame.SetStatusText("Loading %s..." % evt.GetURL())

    def OnWebViewError(self, evt):
        print(evt)
        # self.frame.SetStatusText("Loading %s..." % evt.GetURL())


    def OnWebViewLoaded(self, evt):
        # The full document has loaded
        self.current = evt.GetURL()

    def OnWebViewTitleChanged(self, evt):
        # Set the frame's title to include the document's title
        self.frame.SetTitle("%s -- %s" % (self.titleBase, evt.GetString()))

    def loadfile(self, evt):
        self.wv.LoadURL(self.current)
        self.writetmp()

    def loadfile(self, evt):
        self.wv.LoadURL(self.current)
        self.writetmp()

    def labels(self, evt):
       self.wv.RunScript("showLabels()")

    def rotatex(self, evt):
       self.wv.RunScript("RotateMolecule('x')")

    def rotatey(self, evt):
       self.wv.RunScript("RotateMolecule('y')")

    def rotatez(self, evt):
       self.wv.RunScript("RotateMolecule('z')")

    def optimize(self, evt):
       self.wv.RunScript("mechanics()")

    def threadreload(self, a, b):
        import time
        a=b=""
        while True:
            time.sleep(1)
            self.wv.Reload()

    def start(self):
        _thread.start_new_thread(self.threadreload, ("Thread-1", 2, ))

    def OpenFile(self, event):
        self.wildcard = "SHELX file (*.res)|*.res;*.RES|Crystallographic information file (*.cif)|*.cif;*.CIF|Protein Data Bank file (*.pdb)|*.pdb;*.PDB|SHELX file (*.ins)|*.ins;*.INS|All Files (*)|*"
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirname = dlg.GetDirectory()
            self.filename = dlg.GetFilename()
            self.fnamefull = os.path.join(self.dirname, self.filename)
            self.loadfile(event)


    def OnRefreshPageButton(self, evt):
        self.wv.Reload()


#----------------------------------------------------------------------


def main():
    app = wx.App()
    paths = {}
    web = webchem(None, -1,  paths, size=(720, 830))
    app.SetTopWindow(web)
    web.Show()
    app.MainLoop()


#----------------------------------------------------------------------

if __name__ == '__main__':
    main()