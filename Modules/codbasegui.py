#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GUI generated with help of wxGlade 0.6.3 on Thu Jan 14 23:40:49 2010
# Author is grateful to people who constantly help in developing of the LinXTL:
# Michel Simard; Theirry Moris; Hein Schaper; Government of Canada and University of Montreal for financial support 
# of my Ph.D theses.
# License: GPL
# GNU GENERAL PUBLIC LICENSE
# Version 3, 29 June 2007
# Copyright (C) Denis Spasyuk
# Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
# Preamble
# The GNU General Public License is a free, copyleft license for software and other kinds of works.
# The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.
# When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.
# To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.
# For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.
# Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.
# For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.
# Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.
# Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.
from __future__ import print_function

import wx
import os
import re
import sys
import webbrowser
# begin wxGlade: dependencies
import gettext
import sqlite3

# end wxGlade
ID_SAVE = 1
ID_NEW = 2
ID_DOWNLOADCOD = 3
ID_CHANGEDB = 4
ID_DROPDB = 5
ID_ABOUT = 6
ID_CLOSE = 7
from os.path import expanduser
# begin wxGlade: extracode
# end wxGlade
global ossystem
ossystem = sys.platform
import wx.html2 as webview


class crystalbase_main(wx.Frame):
    def __init__(self, event, parent,  source, paths, *args, **kwds):
        # begin wxGlade: crystalbase_main.__init__
        #        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        self.home = expanduser("~")
        wx.Frame.__init__(self, event, parent, source, *args, **kwds)
        self.version = '0.1 '
        if "path" in paths:
            self.path = paths["path"]
        else:
            self.path = sys.path[0]
        # ib = wx.IconBundle()
        # ib.AddIconFromFile(os.path.join(self.path,"icon", "cod96.ico"), wx.BITMAP_TYPE_ANY)
        # self.SetIcons(ib)
        ########WEBVIEW#####################
        self.fnamefull = False
        # self.current = "/home/denis/Dropbox/linxtlphonex/chem3d/index2.html"

        self.fname = os.path.join( self.path , "chem3d","main.html")
        self.dirname = os.curdir
        self.wv = webview.WebView.New(self)
        self.wv.EnableContextMenu(False)
        self.Bind(webview.EVT_WEBVIEW_ERROR, self.OnWebViewError, self.wv)
        ########WEBVIEW#####################
        self.SetIcon(wx.Icon(os.path.join(self.path, "icon", "cod96.ico")))
        self.label_a = wx.StaticText(self, wx.ID_ANY, ("a"))
        self.text_a = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_b = wx.StaticText(self, wx.ID_ANY, ("b"))
        self.text_b = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_c = wx.StaticText(self, wx.ID_ANY, ("c"))
        self.text_c = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_alpha = wx.StaticText(self, wx.ID_ANY, (u'\N{GREEK SMALL LETTER ALPHA}:'))
        self.text_alpha = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_beta = wx.StaticText(self, wx.ID_ANY, (u'\N{GREEK SMALL LETTER BETA}:'))
        self.text_beta = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_gamma = wx.StaticText(self, wx.ID_ANY, (u'\N{GREEK SMALL LETTER GAMMA}:'))
        self.text_gamma = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_volume = wx.StaticText(self, wx.ID_ANY, ("Volume:"))
        self.text_volume = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_space_group_number = wx.StaticText(self, wx.ID_ANY, ("Space group number:"))
        self.text_space_group_number = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_wavelength = wx.StaticText(self, wx.ID_ANY, ("Wavelength:"))
        self.text_w = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_Z = wx.StaticText(self, wx.ID_ANY, ("Z:"))
        self.text_Z = wx.TextCtrl(self, wx.ID_ANY, "")
        self.pubyear_text = wx.TextCtrl(self, wx.ID_ANY, "")
        self.pubvolume_text = wx.TextCtrl(self, wx.ID_ANY, "")
        self.labelyear = wx.StaticText(self, wx.ID_ANY, ("Publ. year:"))
        self.labelvolume = wx.StaticText(self, wx.ID_ANY, ("Publ. volume:"))
        self.label_formula = wx.StaticText(self, wx.ID_ANY, ("Formula:"))
        self.text_formula = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_formula.SetToolTip(wx.ToolTip("Enter formula"))
        self.sizer_9_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Search parameters"))
        self.label_sigma_a = wx.StaticText(self, wx.ID_ANY, (u"\u03C3 (a):"))
        self.text_sigma_a = wx.TextCtrl(self, wx.ID_ANY, "0.1")
        self.label_sigma_b = wx.StaticText(self, wx.ID_ANY, (u"\u03C3 (b):"))
        self.text_sigma_b = wx.TextCtrl(self, wx.ID_ANY, "0.1")
        self.label_sigma_c = wx.StaticText(self, wx.ID_ANY, (u"\u03C3 (c):"))
        self.text_sigma_c = wx.TextCtrl(self, wx.ID_ANY, "0.1")
        self.label_sigma_alpha = wx.StaticText(self, wx.ID_ANY, (u"\u03C3 (\N{GREEK SMALL LETTER ALPHA}):"))
        self.text_sigma_alpha = wx.TextCtrl(self, wx.ID_ANY, "0.5")
        self.label_sigma_beta = wx.StaticText(self, wx.ID_ANY, (u"\u03C3 (\N{GREEK SMALL LETTER BETA}):"))
        self.text_sigma_beta = wx.TextCtrl(self, wx.ID_ANY, "0.5")
        self.label_sigma_gamma = wx.StaticText(self, wx.ID_ANY, (u"\u03C3 (\N{GREEK SMALL LETTER GAMMA}):"))
        self.text_sigma_gamma = wx.TextCtrl(self, wx.ID_ANY, "0.5")
        self.label_sigma_formula = wx.StaticText(self, wx.ID_ANY, ("Formula filter:"))
        self.text_sigma_formula = wx.TextCtrl(self, wx.ID_ANY, "")
        self.text_sigma_formula.SetToolTip(wx.ToolTip(
            "To remove searches with an ellemnt from results simply list them in order like so: Li, Na, Ca, or use (M) to remove all metals"))
        self.label_7_copy = wx.StaticText(self, wx.ID_ANY, (u"\u03C3 Volume:"))
        self.text_sigma_volume = wx.TextCtrl(self, wx.ID_ANY, "100")
        self.label_sigma_w = wx.StaticText(self, wx.ID_ANY, (u"\u03C3 Wavelength:"))
        self.text_sigma_w = wx.TextCtrl(self, wx.ID_ANY, "0.1")
        self.sizer_9_copy_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, (u"\u03C3 for search parameters"))
        self.text_ctrl_9 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.HSCROLL)
        self.sizer_12_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Cif File"))
        self.list_box_1 = wx.ListBox(self, wx.ID_ANY, choices=[])
        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        self.search = wx.Button(self, wx.ID_ANY, ("Search"))
        self.read_cif = wx.Button(self, wx.ID_ANY, ("View Cif "))
        self.close = wx.Button(self, ID_CLOSE, ("Close"))
        self.Dir = wx.Button(self, wx.ID_ANY, ("Navigate"))
        self.text_path = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_3_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Searches"))
        # Menu Bar
        self.crystalbase_menubar = wx.MenuBar()
        self.statusbar = self.CreateStatusBar(1, wx.CAPTION | wx.ALL, 1)
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-1, 350])
        file = wx.Menu()
        file.Append(ID_SAVE, "Save Cif File\tctrl-s", "", wx.ITEM_NORMAL)
        self.crystalbase_menubar.Append(file, ("File"))
        database = wx.Menu()
        database.Append(ID_NEW, ("Create SQL Database"), "", wx.ITEM_NORMAL)
        #        database.Append(ID_DOWNLOADCOD, ("Download COD database"), "", wx.ITEM_NORMAL)
        database.Append(ID_CHANGEDB, ("Load SQL Database"), "", wx.ITEM_NORMAL)
        #        database.Append(ID_DROPDB, ("Drop SQL Database"), "", wx.ITEM_NORMAL)
        self.crystalbase_menubar.Append(database, ("Database"))
        about = wx.Menu()
        about.Append(ID_ABOUT, ("About"), "", wx.ITEM_NORMAL)
        self.crystalbase_menubar.Append(about, ("About"))
        self.SetMenuBar(self.crystalbase_menubar)
        self.Centre()
        self.CenterOnScreen()
        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.onsave, id=ID_SAVE)
        self.Bind(wx.EVT_MENU, self.onnewdb, id=ID_NEW)
        self.Bind(wx.EVT_BUTTON, self.onclose, id=ID_CLOSE)
        self.Bind(wx.EVT_MENU, self.ondownloadcod, id=ID_DOWNLOADCOD)
        self.Bind(wx.EVT_MENU, self.onchangedb, id=ID_CHANGEDB)
        self.Bind(wx.EVT_MENU, self.ondropdatabase, id=ID_DROPDB)
        self.Bind(wx.EVT_MENU, self.onabout, id=ID_ABOUT)
        self.Bind(wx.EVT_BUTTON, self.onsearch, self.search)
        self.Bind(wx.EVT_BUTTON, self.onnavigate, self.Dir)
        self.Bind(wx.EVT_BUTTON, self.onviewcif, self.read_cif)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.doubleclick, self.list_box_1)
        self.list_box_1.Bind(wx.EVT_MIDDLE_UP, self.middleclick)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: crystalbase_main.__set_properties
        self.SetTitle(("CODBASE %s" % self.version))
        self.text_formula.SetMinSize((150, -1))
        self.text_a.SetSize((150, -1))
        self.text_b.SetSize((150, -1))
        self.text_c.SetSize((150, -1))
        self.text_alpha.SetSize((150, -1))
        self.text_beta.SetSize((150, -1))
        self.text_gamma.SetSize((150, -1))
        self.text_volume.SetSize((150, -1))
        self.text_space_group_number.SetSize((150, -1))
        self.text_w.SetSize((150, -1))
        self.text_sigma_a.SetSize((50, -1))
        self.text_sigma_b.SetSize((50, -1))
        self.text_sigma_c.SetSize((50, -1))
        self.text_sigma_alpha.SetSize((50, -1))
        self.text_sigma_beta.SetSize((50, -1))
        self.text_sigma_gamma.SetSize((50, -1))
        self.text_sigma_formula.SetSize((50, -1))
        self.pubyear_text.SetSize((150, -1))
        self.pubvolume_text.SetSize((150, -1))
        self.text_sigma_volume.SetSize((50, -1))
        self.text_sigma_w.SetSize((50, -1))
        self.text_Z.SetSize((150, -1))
        self.text_ctrl_9.SetMinSize((500, 250))
        self.list_box_1.SetBackgroundColour(wx.Colour(245, 245, 245))
        self.list_box_1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.list_box_1.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.static_line_1.SetSize((-1, 2))
        self.search.SetSize((200, -1))
        self.text_path.SetMinSize((200, -1))

        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: crystalbase_main.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_12_staticbox.Lower()
        sizer_12 = wx.StaticBoxSizer(self.sizer_12_staticbox, wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_9_copy_copy_staticbox.Lower()
        sizer_9_copy_copy = wx.StaticBoxSizer(self.sizer_9_copy_copy_staticbox, wx.HORIZONTAL)
        grid_sizer_1_copy = wx.FlexGridSizer(9, 2, 0, 0)
        self.sizer_9_copy_staticbox.Lower()
        sizer_9_copy = wx.StaticBoxSizer(self.sizer_9_copy_staticbox, wx.HORIZONTAL)
        grid_sizer_1 = wx.FlexGridSizer(13, 2, 0, 0)
        grid_sizer_1.Add(self.label_formula, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_formula, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.label_a, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_a, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.label_b, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_b, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.label_c, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_c, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1.Add(self.label_alpha, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_alpha, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1.Add(self.label_beta, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_beta, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1.Add(self.label_gamma, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_gamma, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1.Add(self.label_volume, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_volume, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1.Add(self.label_wavelength, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_w, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)

        grid_sizer_1.Add(self.label_Z, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_Z, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.label_space_group_number, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.text_space_group_number, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1.Add(self.labelyear, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.pubyear_text, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.labelvolume, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1.Add(self.pubvolume_text, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)



        sizer_9_copy.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_10.Add(sizer_9_copy, 0, wx.ALL, 10)
        grid_sizer_1_copy.Add(self.label_sigma_formula, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_formula, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1_copy.Add(self.label_sigma_a, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_a, 0,
                              wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.label_sigma_b, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_b, 0,
                              wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.label_sigma_c, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_c, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1_copy.Add(self.label_sigma_alpha, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_alpha, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1_copy.Add(self.label_sigma_beta, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_beta, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1_copy.Add(self.label_sigma_gamma, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_gamma, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1_copy.Add(self.label_7_copy, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_volume, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        grid_sizer_1_copy.Add(self.label_sigma_w, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.ALIGN_CENTER_VERTICAL, 10)
        grid_sizer_1_copy.Add(self.text_sigma_w, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)


        sizer_9_copy_copy.Add(grid_sizer_1_copy, 0, wx.EXPAND, 0)

        sizer_10.Add(sizer_9_copy_copy, 0, wx.ALL | wx.EXPAND, 10)
        sizer_6.SetMinSize(500, 500)


        sizer_6.Add(self.wv, 1, wx.ALL | wx.EXPAND, 5)
        sizer_10.Add(sizer_6, 1, wx.ALL | wx.EXPAND, 10)
        sizer_9.Add(sizer_10, 0, wx.EXPAND, 0)
        sizer_12.Add(self.text_ctrl_9, 1, wx.EXPAND, 10)
        sizer_9.Add(sizer_12, 1, wx.EXPAND, 30)
        sizer_2.Add(sizer_9, 3, wx.EXPAND, 0)
        sizer_4.Add(self.list_box_1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.search, 0, wx.ALL, 10)
        #        sizer_5.Add(self.Stop, 0, wx.ALL, 10)
        sizer_5.Add(self.read_cif, 0, wx.ALL, 10)
        sizer_5.Add(self.close, 0, wx.ALL, 10)
        sizer_3.Add(sizer_5, 0, wx.EXPAND, 0)
        sizer_13.Add(self.Dir, 0, wx.ALL, 10)
        sizer_13.Add(self.text_path, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer_3.Add(sizer_13, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 2, wx.EXPAND, 0)
        self.SetSizerAndFit(sizer_1)
        self.Layout()
        self.readdatabase()
        self.writetmp()
        self.current = u'file://' + str(self.fname)
        self.wv.LoadURL(self.current)
        self.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.Centre()
        self.CenterOnScreen()
        # end wxGlade

    ########WEBVIEW##############
    def getfile(self):
        datadict = {}
        # self.filename = "/home/denis/Dropbox/X-ray/GregWelch1/gregw.res"
        file_to_read = open(self.fnamefull, 'r')
        data = [l.rstrip("\n") for l in file_to_read]
        print(os.path.splitext(self.fnamefull)[1])
        datadict["ext"] = os.path.splitext(self.fnamefull)[1][1:]
        datadict["data"] = data
        return datadict

    def writetmp(self):
        if self.fnamefull:
            print(os.path.join(os.path.dirname(self.fname), "main.js"))
            with open(os.path.join(os.path.dirname(self.fname), "main.js"), 'w') as f:
                f.write("var thefile =" + str(self.getfile()))

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

    def OpenFile(self, event):

        self.wildcard = "SHELX file (*.res)|*.res;*.RES|Protein Data Bank file (*.pdb)|*.pdb;*.PDB|SHELX file (*.ins)|*.ins;*.INS|Crystallographic information file (*.cif)|*.cif;*.CIF|All Files (*)|*"
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.dirname = dlg.GetDirectory()
            self.filename = dlg.GetFilename()
            self.fnamefull = os.path.join(self.dirname, self.filename)
            self.writetmp()
            self.wv.Reload()

    def OnRefreshPageButton(self, evt):
        self.wv.Reload()

    ########WEBVIEW##############

    def onsave(self, event):  # wxGlade: crystalbase_main.<event_handler>
        fileset = self.text_path.GetValue()
        dlg = wx.FileDialog(self, "Save a file", self.home, fileset, "*.cif",
                            wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetFilename()
            dir = dlg.GetDirectory()
            from shutil import copyfile
            copyfile(fileset, os.path.join(dir, filename + '.cif'))

    def onloaddb(self):
        if os.path.exists(os.path.join(self.maindir, "STRUCTURAL_DATABASE.db")):
            self.database = sqlite3.connect(
                os.path.join(self.maindir, "STRUCTURAL_DATABASE.db"))  # or use :memory: to put it in RAM
            self.cursor = self.database.cursor()
        else:
            dlg = wx.MessageDialog(self, "Error!!! File " + os.path.join(self.maindir,
                                                                         "STRUCTURAL_DATABASE.db") + " does not exist",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def readdatabase(self):
        if os.path.exists(os.path.join(self.home, ".coddb")):
            tmpf = open(os.path.join(self.home, ".coddb"), 'r')
            self.maindir = tmpf.read()
            tmpf.close()
            self.onloaddb()

    def setdatabase(self):
        tmpf = open(os.path.join(self.home, ".coddb"), 'w')
        tmpf.write(self.maindir)
        tmpf.close()

    def decidedb(self):
        ids = filelink = formula = ca = cb = cc = alpha = beta = gamma = volume = csystem = number = cname = Z = wavelength = R = publisher = pubyear = pubvolume = pubpgfirst = pubpglast = None
        if os.path.exists(os.path.join(self.maindir, "STRUCTURAL_DATABASE.db")):
            dialog = wx.MessageDialog(self,
                                      "The database file already exist in the destination directory. This will erase the database file. Do you want to continue?",
                                      "Continue?", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
            dialog.Centre()
            result = dialog.ShowModal()
            dialog.Destroy()
            if result == wx.ID_YES:
                ###########################CREATE DATABASE##################################################
                os.remove(os.path.join(self.maindir, "STRUCTURAL_DATABASE.db"))
                from sqdatabase import getinfocif
                getinfocif(ids, filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number, cname, Z,
                           wavelength, R, publisher, pubyear, pubvolume, pubpgfirst, pubpglast, self.maindir)
            else:
                print("Aborted")
        else:
            from sqdatabase import getinfocif
            getinfocif(ids, filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number, cname, Z,
                       wavelength, R, publisher, pubyear, pubvolume, pubpgfirst, pubpglast, self.maindir)

    def onnewdb(self, event):  # wxGlade: crystalbase_main.<event_handler>
        dialog = wx.MessageDialog(self,
                                  "This will analyse a list of cif files in specified directory and make an SQL database. This operation might take anywhere from a minute to a few hours, depending on the size of a database. Database file will be saved in the target directory as STRUCTURAL_DATABASE.db. Continue?",
                                  "Create?", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
        dialog.Centre()
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_YES:
            dlg = wx.DirDialog(self, "Choose a directory with cif files",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                self.maindir = str(dlg.GetPath())
                self.setdatabase()
                self.decidedb()
                dlg.Destroy()

    def onnavigate(self, event):
        fileset = self.text_path.GetValue()
        print(fileset)
        webbrowser.open(os.path.dirname(fileset))

    def onviewcif(self, event):
        fileset = self.text_path.GetValue()
        webbrowser.open(fileset)

    def middleclick(self, event):
        self.doubleclick(event)
        fileset = self.text_path.GetValue()
        webbrowser.open(fileset)

    def ondownloadcod(self, event):  # wxGlade: crystalbase_main.<event_handler>
        dialog = wx.MessageDialog(self,
                                  "This will download COD database (13+ Gb) from http://www.crystallography.net/cif/",
                                  "Download?", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
        dialog.Centre()
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_YES:
            dlg = wx.DirDialog(self, "Choose a directory to store the database",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
            if dlg.ShowModal() == wx.ID_OK:
                self.maindir = str(dlg.GetPath())
                self.setdatabase()
                dlg.Destroy()
                import urllib
                urllib.urlretrieve("http://www.crystallography.net/cif/", self.maindir)

    def onchangedb(self, event):  # wxGlade: crystalbase_main.<event_handler>
        dlg = wx.DirDialog(self, "Choose a directory with the databse file",
                           style=wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            self.maindir = str(dlg.GetPath())
            self.setdatabase()
            dlg.Destroy()

    def ondropdatabase(self, event):  # wxGlade: crystalbase_main.<event_handler>
        print("Event handler 'ondropdatabase' not implemented!")
        event.Skip()

    def values(self):
        self.a = self.text_a.GetValue()
        self.b = self.text_b.GetValue()
        self.c = self.text_c.GetValue()
        self.aang = self.text_alpha.GetValue()
        self.bang = self.text_beta.GetValue()
        self.cang = self.text_gamma.GetValue()
        self.vol = self.text_volume.GetValue()
        self.spnum = self.text_space_group_number.GetValue()
        self.wave = self.text_w.GetValue()
        self.zds = self.text_Z.GetValue()
        self.formu = self.text_formula.GetValue()
        self.sigma_formu = self.text_sigma_formula.GetValue()
        self.sia = self.text_sigma_a.GetValue()
        self.sib = self.text_sigma_b.GetValue()
        self.sic = self.text_sigma_c.GetValue()
        self.siaang = self.text_sigma_alpha.GetValue()
        self.sibang = self.text_sigma_beta.GetValue()
        self.sicang = self.text_sigma_gamma.GetValue()
        self.sivol = self.text_sigma_volume.GetValue()
        self.swave = self.text_sigma_w.GetValue()
        self.pub_volume = self.pubvolume_text.GetValue()
        self.pub_year = self.pubyear_text.GetValue()
        self.sigmafomula = self.text_sigma_formula.GetValue()

    #        self.text_ctrl_9.SetValue()
    #    def getexisting(self):
    def onclose(self, event):
        self.Close()

    def oncorrectpath(self, fpath):
        if ossystem.startswith("win"):
            fpath = fpath.replace("/", "\\")
            return fpath
        else:
            fpath = fpath.replace("\\", "/")
            return fpath

    def formulafilter(self, value):
        metals = ['Ru', 'Re', 'Rf', 'Ra', 'Rb', 'Rn', 'Rh', 'Be', 'Ba', 'Bi', 'Bk', 'Os', 'Hg', 'Ge', 'Gd', 'Ga', 'Pr',
                  'Pt', 'Pu', 'Pb', 'Pa', 'Pd', 'Po', 'Pm', 'Ho', 'Ha', 'Hf', 'Mo', 'Md', 'Mg', 'K', 'Mn', 'Zr', 'Un',
                  'W', 'Zn', 'Eu', 'Es', 'Er',
                  'Ni', 'No', 'Na', 'Nb', 'Nd', 'Np', 'Fr', 'Fe', 'Fm', 'Sr', 'Sn', 'Sm', 'V', 'Sc', 'Sb', 'Co', 'Cm',
                  'Ca', 'Cf', 'Ce', 'Cd', 'Tm',
                  'Cs', 'Cr', 'Cu', 'La', 'Li', 'Tl', 'Lu', 'Lr', 'Th', 'Ti', 'Te', 'Tb', 'Tc', 'Ta', 'Yb', 'Dy', 'U',
                  'Y', 'Ac', 'Ag', 'Ir', 'Am',
                  'Al', 'Au', 'At', 'In']
        allatoms = ['Ru', 'Re', 'Rf', 'Ra', 'Rb', 'Rn', 'Rh', 'Be', 'Ba', 'Bi', 'Bk', 'Br', 'H', 'P', 'Os', 'Hg', 'Ge',
                    'Gd',
                    'Ga', 'Pr', 'Pt', 'Pu', 'C', 'Pb', 'Pa', 'Pd', 'Xe', 'Po', 'Pm', 'Ho', 'Ha', 'Hf', 'Mo', 'He', 'Md',
                    'Mg', 'K', 'Mn', 'O', 'Zr',
                    'S', 'Un', 'W', 'Zn', 'Eu', 'Es', 'Er', 'Ni', 'No', 'Na', 'Nb', 'Nd', 'Ne', 'Np', 'Fr', 'Fe', 'Fm',
                    'B', 'F', 'Sr', 'N', 'Kr', 'Si',
                    'Sn', 'Sm', 'V', 'Sc', 'Sb', 'Se', 'Co', 'Cm', 'Cl', 'Ca', 'Cf', 'Ce', 'Cd', 'Tm', 'Cs', 'Cr', 'Cu',
                    'La', 'Li', 'Tl', 'Lu', 'Lr',
                    'Th', 'Ti', 'Te', 'Tb', 'Tc', 'Ta', 'Yb', 'Dy', 'I', 'U', 'Y', 'Ac', 'Ag', 'Ir', 'Am', 'Al', 'As',
                    'Ar', 'Au', 'At', 'In']
        nonmetal = list(set(allatoms) - set(metals))
        if len(self.sigmafomula.split()) > 0:
            if '(M)' in self.sigmafomula:
                filterlist = metals
            #                print('metal')
            else:
                filterlist = self.sigmafomula.split()
            if any(item in value for item in filterlist):
                return True
            else:
                return False
        else:
            return False

    def doubleclick(self, event):
        fileset = self.list_box_1.GetStringSelection()
        fileselect = os.path.join(self.maindir, fileset.split('   ')[-1].rstrip().lstrip())
        self.text_path.SetValue(fileselect)
        self.text_ctrl_9.LoadFile(fileselect)
        self.fnamefull = fileselect
        self.writetmp()
        self.wv.Reload()

    def parseformula(self, formulagiven, formulafound):
        list1 = re.findall(r'([A-Z][a-z]*)(\d*)', formulagiven)
        list1 = sorted(list1, key=lambda tup: tup[0])
        list2 = re.findall(r'([A-Z][a-z]*)(\d*)', formulafound)
        list2 = sorted(list2, key=lambda tup: tup[0])
        return len(set(x for x in list1).intersection(y for y in list2))

    def onsearch(self, event):  # wxGlade: crystalbase_main.<event_handler>
        self.values()
        print("vars", self.a, self.b, self.c, self.aang, self.bang, self.cang, self.zds, self.formu, self.vol,
              self.pub_year, self.pub_volume, self.wave)
        if self.a or self.b or self.c or self.aang or self.bang or self.cang or self.formu or self.vol or self.wave or self.zds or self.spnum or self.pub_year or self.pub_volume:
            #        sql = "SELECT ids, filelink, ca FROM structures ORDER BY ids"
            sql = "SELECT ids, filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number, cname, Z, wavelength, R, publisher,  pubyear, pubvolume, pubpgfirst, pubpglast FROM structures ORDER BY ids"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            self.list_box_1.Clear()
            c = 1
            for row in rows:
                try:
                    try:
                        try:
                            rowa = float(format(float((row[3]).split('(')[0]), '.1f'))
                            rowb = float(format(float((row[4]).split('(')[0]), '.1f'))
                            rowc = float(format(float((row[5]).split('(')[0]), '.1f'))
                            rowalpha = float(format(float((row[6]).split('(')[0]), '.1f'))
                            rowbeta = float(format(float((row[7]).split('(')[0]), '.1f'))
                            rowgamma = float(format(float((row[8]).split('(')[0]), '.1f'))
                            rowvol = float(format(float((row[9]).split('(')[0]), '.1f'))

                            #                            rowspcn=row[11]
                            #                            rowzds=row[13]
                            rowwave = float(format(float((row[14]).split('(')[0]), '.1f'))
                            #                            print(row[14])

                            ###########################CELL######################################################
                            filepath = self.oncorrectpath(str(row[1]))
                            if self.a and self.b and self.c:
                                if float(self.a) - float(self.sia) <= rowa <= float(self.a) + float(self.sia) and float(
                                        self.b) - float(self.sib) <= rowb <= float(self.b) + float(self.sib) and float(
                                        self.c) - float(self.sic) <= rowc <= float(self.c) + float(self.sic):
                                    self.list_box_1.Append(str(rowa) + u" \u212B   " + str(rowb) + u" \u212B   " + str(
                                        rowc) + u" \u212B   " + filepath)
                                    wx.Yield()
                            if self.a and self.b and not self.c:
                                if float(self.a) - float(self.sia) <= rowa <= float(self.a) + float(self.sia) and float(
                                        self.b) - float(self.sib) <= rowb <= float(self.b) + float(self.sib):
                                    self.list_box_1.Append(
                                        str(rowa) + u" \u212B   " + str(rowb) + u" \u212B   " + filepath)
                                    wx.Yield()
                            if self.a and not self.b and not self.c:
                                if float(self.a) - float(self.sia) <= rowa <= float(self.a) + float(self.sia):
                                    self.list_box_1.Append(str(rowa) + u" \u212B   " + filepath)
                                    c = c + 1
                                    wx.Yield()
                            if self.b and not self.a and not self.c:
                                if float(self.b) - float(self.sib) <= rowb <= float(self.b) + float(self.sib):
                                    self.list_box_1.Append(str(rowb) + u" \u212B   " + filepath)
                                    wx.Yield()
                            if self.c and not self.a and not self.b:
                                if float(self.c) - float(self.sic) <= rowc <= float(self.c) + float(self.sic):
                                    self.list_box_1.Append(str(rowc) + u" \u212B   " + filepath)
                                    wx.Yield()
                            if self.a and self.c and not self.b:
                                if float(self.a) - float(self.sia) <= rowa <= float(self.a) + float(self.sia) and float(
                                        self.c) - float(self.sic) <= rowc <= float(self.c) + float(self.sic):
                                    self.list_box_1.Append(
                                        str(rowa) + u" \u212B   " + str(rowc) + u" \u212B   " + filepath)
                                    wx.Yield()
                                    ###########################ANGLE######################################################
                            if self.aang and self.bang and self.cang:
                                if float(self.aang) - float(self.siaang) <= float(row[6][0:4]) <= float(
                                        self.aang) + float(self.siaang) and float(self.bang) - float(
                                        self.sibang) <= float(row[7][0:4]) <= float(self.bang) + float(
                                        self.sibang) and float(self.cang) - float(self.sicang) <= float(
                                        row[8][0:4]) <= float(self.cang) + float(self.sicang):
                                    self.list_box_1.Append(
                                        str(rowalpha) + u"\u00B0   " + str(rowbeta) + u"\u00B0   " + str(
                                            rowgamma) + u"\u00B0   " + filepath)
                                    wx.Yield()
                            if self.aang and self.bang and not self.cang:
                                if float(self.aang) - float(self.siaang) <= rowalpha <= float(self.aang) + float(
                                        self.siaang) and float(self.bang) - float(self.sibang) <= rowbeta <= float(
                                        self.bang) + float(self.sibang):
                                    self.list_box_1.Append(
                                        str(rowalpha) + u"\u00B0   " + str(rowbeta) + u"\u00B0   " + filepath)
                                    wx.Yield()
                            if self.aang and not self.bang and not self.cang:
                                if float(self.aang) - float(self.siaang) <= rowalpha <= float(self.aang) + float(
                                        self.siaang):
                                    self.list_box_1.Append(str(rowalpha) + u"\u00B0   " + filepath)
                                    wx.Yield()
                            if self.bang and not self.aang and not self.cang:
                                if float(self.bang) - float(self.sibang) <= rowbeta <= float(self.bang) + float(
                                        self.sibang):
                                    self.list_box_1.Append(str(rowbeta) + u"\u00B0   " + filepath)
                                    wx.Yield()
                            if self.cang and not self.aang and not self.bang:
                                if float(self.cang) - float(self.sicang) <= rowgamma <= float(self.cang) + float(
                                        self.sicang):
                                    self.list_box_1.Append(str(rowgamma) + u"\u00B0   " + filepath)
                                    wx.Yield()
                            ###########################FORMULA######################################################        
                            #                            if self.formu:
                            #                                list1=re.findall(r'([A-Z][a-z]*)(\d*)', self.formu)
                            #                                list1 = sorted(list1, key=lambda tup: tup[0])
                            #                                lengthofformula=len(list1)
                            #                                if self.parseformula(self.formu, row[2])==lengthofformula:
                            #                                   self.list_box_1.Append(str(row[2])+"   "+filepath)
                            #                                   wx.Yield()
                            if self.formu:
                                list1 = re.findall(r'([A-Z][a-z]*)(\d*)', self.formu)
                                list1 = sorted(list1, key=lambda tup: tup[0])
                                lengthofformula = len(list1)
                                if self.parseformula(self.formu, row[2]) == lengthofformula:
                                    if not self.formulafilter(str(row[2])):
                                        self.list_box_1.Append(str(row[2]) + "   " + filepath)
                                        wx.Yield()
                            ###########################WAVELENGTH######################################################
                            if self.wave:
                                #                                print (row[14])
                                if float(self.wave) - float(self.swave) <= rowwave <= float(self.wave) + float(
                                        self.swave):  #### float argument must be string or a number
                                    self.list_box_1.Append(str(rowwave) + u" \u212B   " + filepath)
                                    wx.Yield()
                            if self.spnum and not self.zds:
                                #                        print(row[11], int(self.spnum))
                                if int(row[11]) == int(self.spnum):
                                    self.list_box_1.Append("   " + filepath)
                                    wx.Yield()
                            if self.zds and not self.spnum:
                                #                                print(int(self.zds), self.spnum)
                                if float(self.zds) + 0.2 <= float(row[13]) <= float(self.zds) + 0.2:
                                    self.list_box_1.Append(str(row[13]) + "   " + filepath)
                                    wx.Yield()
                            if self.spnum and self.zds:
                                if int(row[11]) == int(self.spnum) and int(row[13]) == int(self.zds):
                                    self.list_box_1.Append(str(row[13]) + "   " + str(row[11]) + "   " + filepath)
                                    wx.Yield()
                            ###########################Volume######################################################
                            if self.vol:
                                if float(self.vol) - float(self.sivol) <= rowvol <= float(self.vol) + float(self.sivol):
                                    self.list_box_1.Append(str(rowvol) + u" \u212B\u00B3   " + filepath)
                                    wx.Yield()
                            if self.pub_volume:
                                if int(self.pub_volume) == int(row[19]):
                                    self.list_box_1.Append(str(row[19]) + "   " + filepath)
                                    wx.Yield()
                            if self.pub_year:
                                if int(self.pub_year) == int(row[18]):
                                    self.list_box_1.Append(str(row[18]) + "   " + filepath)
                                    wx.Yield()
                        except TypeError:
                            pass
                    except AttributeError:
                        pass
                except ValueError:
                    pass
            self.SetStatusText('Total entries: %s' % len(rows), 1)
            counts = self.list_box_1.GetCount()
            print(c)
            self.SetStatusText('Number of hits: %s' % counts)
            if int(counts) < 1:
                self.list_box_1.Append("Nothing Found or no search parameters provided")

    def onabout(self, event):  # wxGlade: crystalbase_main.<event_handler>
        import wx.adv
        info = wx.adv.AboutDialogInfo()
        info.Name = "CODBASE"
        info.Version = self.version
        info.Copyright = "Copyright (C) 2019 Denis Spasyuk, Canadian Light Source"
        info.Description = '''GUI interface for COD database http://www.crystallography.net/'''
        info.WebSite = ("http://sourceforge.net/projects/linxtl/")  # , "Home page")

        wx.adv.AboutBox(info)


if __name__ == "__main__":
    app = wx.App(0)
    displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
    sizes = [display.GetGeometry().GetSize() for display in displays]
    displaySize = sizes[0].Get()
    paths ={}
    crystal = crystalbase_main(None, -1, "", paths, size=(displaySize[0] / 3, displaySize[1] / 1.5))
    app.SetTopWindow(crystal)
    crystal.Show()
    app.MainLoop()
