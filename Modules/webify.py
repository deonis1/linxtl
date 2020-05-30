#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import wx.html
class webb(wx.Dialog):
    def __init__(self,  event, page, title):
        
        displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        sizes = [display.GetGeometry().GetSize() for display in displays]
        displaySize=sizes[0].Get()
        xres,yres=  displaySize[0]/1.2, displaySize[1]/1.2
        si=(xres/6*xres/yres,yres/2)
        wx.Dialog.__init__(self, None, -1, title,  style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER  , size=si)
        html = wx.html.HtmlWindow(self)
        self.SetMinSize((750,400))
        if "gtk2" in wx.PlatformInfo:
            html.SetStandardFonts()
        html.SetPage(page)

