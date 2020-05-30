#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GUI generated with help of wxGlade 0.6.3 on Thu Jan 14 23:40:49 2010
# Author is grateful to people who constantly help in developing of the LinXTL:
# Michel Simard; Theirry Moris; Hein Schaper; Government of Canada and University of Montreal for financial support 
# of my Ph.D theses.
# License: GPL
#GNU GENERAL PUBLIC LICENSE
#Version 3, 29 June 2007
#Copyright (C) Denis Spasyuk
#Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.
#Preamble
#The GNU General Public License is a free, copyleft license for software and other kinds of works.
#The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.
#When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.
#To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.
#For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.
#Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.
#For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.
#Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.
#Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.
from __future__ import print_function
import wx
import gettext
import os, sys
import subprocess
import webbrowser
import wx.stc
global ossystem
ossystem=sys.platform
#global path
#path = sys.path[0]

class mxmain(wx.Frame):
    def __init__(self,  event, parent, path, dirname, phtocoot, phtoxc, phtoxm, phtoxe):
        xres,yres= wx.DisplaySize()
        size=(xres/5*xres/yres, yres/4)
        wx.Frame.__init__(self,  event, parent, 'MX_MAP 0.1', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER  , size=size)
        self.dirname=dirname
#        if not len(fnoe)==0:
#           self.fnoe=fnoe
#        else:
#           self.fnoe=''

        self.path=path    
        self.dirname=dirname
        self.ossystem=ossystem
        self.phtoCoot=phtocoot
        self.phtoxc=phtoxc
        self.phtoxe=phtoxe
        self.phtoxm=phtoxm
#        ib = wx.IconBundle()
#        ib.AddIconFromFile(os.path.join(self.path,"icon", "main.ico"), wx.BITMAP_TYPE_ANY)
#        self.SetIcons(ib)
        self.wildcard = "HKL2000 (*.sca)|*.sca|Reflection file (*.hkl)|*.hkl"
        self.originalsca = wx.StaticText(self, wx.ID_ANY, ("NAT in:"))
        self.text_original = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_original = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.originalsca_copy = wx.StaticText(self, wx.ID_ANY, ("PEAK in, MAD:"))
        self.text_peak = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_peak = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.originalsca_copy_1 = wx.StaticText(self, wx.ID_ANY, ("INFL in, MAD:"))
        self.text_infl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_infl = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.originalsca_copy_2 = wx.StaticText(self, wx.ID_ANY, ("HREM in, MAD:"))
        self.text_hrem = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_hrem = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.originalsca_copy_3 = wx.StaticText(self, wx.ID_ANY, ("LREM in, MAD:"))
        self.text_lrem = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_lrem = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.inputfile = wx.StaticText(self, wx.ID_ANY, ("Input file:"))
        self.text_input = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_input = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.label_outhkl = wx.StaticText(self, wx.ID_ANY, ("Out hkl:"))
        self.text_outhkl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_outhkl = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.label_hklfa = wx.StaticText(self, wx.ID_ANY, ("Out hkl_fa:"))
        self.text_hklfa = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_hklfa = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.label_scaout = wx.StaticText(self, wx.ID_ANY, ("Original SCA or HKL out:"))
        self.text_scaout = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_scaout = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.labelinsfile = wx.StaticText(self, wx.ID_ANY, ("INS file"))
        self.text_insfile = wx.TextCtrl(self, wx.ID_ANY, "")
        self.button_insfile = wx.Button(self, wx.ID_ANY, ("Browse"))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, ("Method:"))
        self.methods = wx.ComboBox(self, wx.ID_ANY, choices=[("SAD"), ("MAD")], style=wx.CB_DROPDOWN)
        self.lcell = wx.StaticText(self, wx.ID_ANY, ("Cell   a:"))
        self.text_a = wx.TextCtrl(self, wx.ID_ANY, "")
        self.lcell_copy = wx.StaticText(self, wx.ID_ANY, ("b:"))
        self.text_b = wx.TextCtrl(self, wx.ID_ANY, "")
        self.lcell_copy_1 = wx.StaticText(self, wx.ID_ANY, ("c:"))
        self.text_c = wx.TextCtrl(self, wx.ID_ANY, "")
        self.lcell_copy_2 = wx.StaticText(self, wx.ID_ANY, (u'\N{GREEK SMALL LETTER ALPHA}:'))
        self.text_alpha = wx.TextCtrl(self, wx.ID_ANY, "")
        self.lcell_copy_3 = wx.StaticText(self, wx.ID_ANY, (u'\N{GREEK SMALL LETTER BETA}:'))
        self.text_beta = wx.TextCtrl(self, wx.ID_ANY, "")
        self.lcell_copy_4 = wx.StaticText(self, wx.ID_ANY, (u'\N{GREEK SMALL LETTER GAMMA}:'))
        self.text_gamma = wx.TextCtrl(self, wx.ID_ANY, "")
        self.lcell_copy_5 = wx.StaticText(self, wx.ID_ANY, ("Volume:"))
        self.text_volume = wx.TextCtrl(self, wx.ID_ANY, "")
        self.lcell_copy_6 = wx.StaticText(self, wx.ID_ANY, ("Space group:"))
        self.text_space = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_10 = wx.StaticText(self, wx.ID_ANY, ("          SFAC:"))
        self.sfac = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_7 = wx.StaticText(self, wx.ID_ANY, ("SHLEXC Input:"))
        self.text_shelxc = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_8 = wx.StaticText(self, wx.ID_ANY, ("SHLEXD Input:"))
        self.text_shelxd = wx.TextCtrl(self, wx.ID_ANY, "")
        self.label_9 = wx.StaticText(self, wx.ID_ANY, ("SHLEXE Input:"))
        self.text_shelxe = wx.TextCtrl(self, wx.ID_ANY, "")
        self.viewinput = wx.Button(self, wx.ID_ANY, ("View/Make input file"))
        self.viewpdb = wx.Button(self, wx.ID_ANY, ("View pdb in Coot"))
        self.refresh = wx.Button(self, wx.ID_ANY, ("Default Command Line"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, ("Execute:"))
        self.shelxc = wx.Button(self, wx.ID_ANY, ("SHELXC"))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, (">>>>"))
        self.shelxd = wx.Button(self, wx.ID_ANY, ("SHELXD"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, (">>>>"))
        self.shelxe = wx.Button(self, wx.ID_ANY, ("SHELXE"))
        self.cancelb = wx.Button(self, wx.ID_ANY, ("Close"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
#        self.SetTitle(("MXMAP"))
        self.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.SetForegroundColour(wx.Colour(20, 19, 81))
        self.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.originalsca.SetSize((-1, -1))
        self.originalsca.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.originalsca_copy.SetSize((-1, -1))
        self.originalsca_copy.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.originalsca_copy_1.SetSize((-1, -1))
        self.originalsca_copy_1.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.originalsca_copy_2.SetSize((-1, -1))
        self.originalsca_copy_2.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.originalsca_copy_3.SetSize((-1, -1))
        self.originalsca_copy_3.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.inputfile.SetSize((-1, -1))
        self.inputfile.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.label_outhkl.SetSize((-1, -1))
        self.label_outhkl.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.label_hklfa.SetSize((-1, -1))
        self.label_hklfa.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.label_scaout.SetSize((-1, -1))
        self.label_scaout.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.labelinsfile.SetSize((-1, -1))
        self.labelinsfile.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.label_6.SetSize((-1, -1))
        self.label_6.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.methods.SetMinSize((200, -1))
        self.methods.SetBackgroundColour(wx.Colour(0, 206, 209))
        self.methods.SetForegroundColour(wx.Colour(8, 16, 87))
        self.methods.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.methods.SetSelection(0)
        self.lcell.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_a.SetMinSize((150, -1))
        self.text_a.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_a.SetForegroundColour(wx.Colour(0, 0, 0))
        self.lcell_copy.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_b.SetMinSize((150, -1))
        self.text_b.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_b.SetForegroundColour(wx.Colour(0, 0, 0))
        self.lcell_copy_1.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_c.SetMinSize((150, -1))
        self.text_c.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_c.SetForegroundColour(wx.Colour(0, 0, 0))
        self.lcell_copy_2.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_alpha.SetMinSize((150, -1))
        self.text_alpha.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_alpha.SetForegroundColour(wx.Colour(0, 0, 0))
        self.lcell_copy_3.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_beta.SetMinSize((150, -1))
        self.text_beta.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_beta.SetForegroundColour(wx.Colour(0, 0, 0))
        self.lcell_copy_4.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_gamma.SetMinSize((150, -1))
        self.text_gamma.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_gamma.SetForegroundColour(wx.Colour(0, 0, 0))
        self.lcell_copy_5.SetSize((-1, -1))
        self.lcell_copy_5.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_volume.SetMinSize((200, -1))
        self.lcell_copy_6.SetSize((-1, -1))
        self.lcell_copy_6.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_space.SetMinSize((200, -1))
        self.label_10.SetSize((-1, -1))
        self.label_10.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.sfac.SetMinSize((200, -1))
        self.label_7.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.label_7.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_shelxc.SetMinSize((80,-1))
        self.text_shelxc.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_shelxc.SetForegroundColour(wx.Colour(0, 0, 0))
        self.label_8.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_shelxd.SetMinSize((80, -1))
        self.text_shelxd.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_shelxd.SetForegroundColour(wx.Colour(0, 0, 0))
        self.label_9.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.text_shelxe.SetMinSize((80, -1))
        self.text_shelxe.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_shelxe.SetForegroundColour(wx.Colour(0, 0, 0))
        self.viewinput.SetMinSize((-1, -1))
        self.viewpdb.SetSize((-1, -1))
        self.refresh.SetSize((-1, -1))
        self.label_3.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.label_1.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.label_2.SetBackgroundColour(wx.Colour(241, 241, 241))
#        self.cancelb.SetBackgroundColour(wx.Colour(255, 0, 0))
#        self.cancelb.SetForegroundColour(wx.Colour(0,0, 0))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(1, 7, 0, 0)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_3 = wx.GridSizer(1, 12, 0, 0)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
       # sizer_19 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_20 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_18 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6.Add(self.originalsca, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_6.Add(self.text_original, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_6.Add(self.button_original, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_8.Add(self.originalsca_copy, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_8.Add(self.text_peak, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_8.Add(self.button_peak, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_10.Add(self.originalsca_copy_1, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_10.Add(self.text_infl, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_10.Add(self.button_infl, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_10, 1, wx.EXPAND, 0)
        sizer_11.Add(self.originalsca_copy_2, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_11.Add(self.text_hrem, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_11.Add(self.button_hrem, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_12.Add(self.originalsca_copy_3, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_12.Add(self.text_lrem, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_12.Add(self.button_lrem, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_13.Add(self.inputfile, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_13.Add(self.text_input, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_13.Add(self.button_input, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_14.Add(self.label_outhkl, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_14.Add(self.text_outhkl, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_14.Add(self.button_outhkl, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_15.Add(self.label_hklfa, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_15.Add(self.text_hklfa, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_15.Add(self.button_hklfa, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_15, 1, wx.EXPAND, 0)
        sizer_16.Add(self.label_scaout, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_16.Add(self.text_scaout, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_16.Add(self.button_scaout, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_17.Add(self.labelinsfile, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_17.Add(self.text_insfile, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_17.Add(self.button_insfile, 0, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_4.Add(sizer_17, 1, wx.EXPAND, 0)
        sizer_18.Add(self.label_6, 1, wx.LEFT | wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_18.Add(self.methods, 2, wx.TOP | wx.BOTTOM | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_18.Add((110, 20), 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(sizer_18, 1, wx.EXPAND, 0)
 #       sizer_19.Add((23, 30), 0, 0, 0)
  #      sizer_19.Add((23, 30), 0, 0, 0)
   #     sizer_19.Add((20, 20), 0, 0, 0)
    #    sizer_4.Add(sizer_19, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        
        
        sizer_20.Add(self.lcell, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_20.Add(self.text_a, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_20.Add(self.lcell_copy, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_20.Add(self.text_b, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_20.Add(self.lcell_copy_1, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_20.Add(self.text_c, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_20.Add(self.lcell_copy_2, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_20.Add(self.text_alpha, 1,  wx.RIGHT |wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_20.Add(self.lcell_copy_3, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_20.Add(self.text_beta, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_20.Add(self.lcell_copy_4, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 3)
        sizer_20.Add(self.text_gamma, 1, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        
        
        sizer_3.Add(sizer_20, 1, wx.EXPAND, 0)
        sizer_7.Add(self.lcell_copy_5, 1, wx.LEFT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_7.Add(self.text_volume, 1, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add(self.lcell_copy_6, 1, wx.LEFT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 20)
        sizer_7.Add(self.text_space, 1, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_7.Add(self.label_10, 1, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add(self.sfac, 1, wx.RIGHT | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_5.Add(self.label_7, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_5.Add(self.text_shelxc, 4, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_5_copy.Add(self.label_8, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_5_copy.Add(self.text_shelxd, 4, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(sizer_5_copy, 1, wx.EXPAND, 0)
        sizer_5_copy_1.Add(self.label_9, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_5_copy_1.Add(self.text_shelxe, 4, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(sizer_5_copy_1, 1, wx.EXPAND, 0)
        sizer_9.Add(self.viewinput,1 , wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_9.Add(self.viewpdb, 1, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_9.Add(self.refresh, 1,wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_3.Add(sizer_9, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.label_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.shelxc, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.shelxd, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.shelxe, 0, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL, 40)
        grid_sizer_1.Add(self.cancelb, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        self.SetSizerAndFit(sizer_1)
        sizer_1.SetSizeHints(self)
        #self.SetMinSize((1100, 800))
        self.Layout()
        self.Center()
        self.CenterOnScreen()
        # end wxGlade
     
        self.Bind(wx.EVT_BUTTON, self.oninput, self.button_input)       
        self.Bind(wx.EVT_BUTTON, self.original,  self.button_original)
        self.Bind(wx.EVT_BUTTON, self.outfa, self.button_hklfa)
        self.Bind(wx.EVT_BUTTON, self.outhkl, self.button_outhkl) 
        self.Bind(wx.EVT_BUTTON, self.sout, self.button_scaout) 
        self.Bind(wx.EVT_BUTTON, self.insin,  self.button_insfile)
        self.Bind(wx.EVT_BUTTON, self.makeinput,  self.viewinput)
        self.Bind(wx.EVT_BUTTON, self.onxe,  self.shelxe)
        self.Bind(wx.EVT_BUTTON, self.onxm,  self.shelxd)
        self.Bind(wx.EVT_BUTTON, self.onxc,  self.shelxc)
        self.Bind(wx.EVT_BUTTON, self.onviewpdb,  self.viewpdb)
        self.Bind(wx.EVT_BUTTON, self.onrefresh,  self.refresh)
        self.Bind(wx.EVT_BUTTON, self.onpeak,  self.button_peak)
        self.Bind(wx.EVT_BUTTON, self.oninfl,  self.button_infl)
        self.Bind(wx.EVT_BUTTON, self.onhrem,  self.button_hrem)
        self.Bind(wx.EVT_BUTTON, self.onlrem,  self.button_lrem)
        self.Bind(wx.EVT_BUTTON, self.onClose, self.cancelb)
        self.methods.Bind(wx.EVT_COMBOBOX, self.onrefresh) 
        
    def onrefresh(self, event):
        if self.methods.GetString(self.methods.GetSelection())=="SAD":
            ##################sxc####################################
            sxc=self.phtoxc+" "+self.filenamenoext+" "+" < "+self.filenamenoext+".inp"
            self.text_shelxc.SetValue(sxc)                
            ##################sxm####################################    
            sxm=self.phtoxm+" "+self.filenamenoext+"_fa"
            self.text_shelxd.SetValue(sxm)
            ##################sxe####################################
            sxe=self.phtoxe+" "+self.filenamenoext+" "+self.filenamenoext+"_fa"+" "+"-a -h"
            self.text_shelxe.SetValue(sxe)         
        elif self.methods.GetString(self.methods.GetSelection())=="MAD":
            sxc=self.phtoxc+" "+self.filenamenoext.split('_')[0]+" "+" < "+self.filenamenoext+".inp"
            self.text_shelxc.SetValue(sxc)
            #######################sxm##################################
            sxm=self.phtoxm+" "+self.filenamenoext.split('_')[0]+"_fa"
            self.text_shelxd.SetValue(sxm)
            #######################sxe##################################
            sxe=self.phtoxe+" "+self.filenamenoext.split('_')[0]+" "+self.filenamenoext.split('_')[0]+"_fa"+" "+"-a -i"
            self.text_shelxe.SetValue(sxe)
        else:
                dlg = wx.MessageDialog(self, "Method is not defined",
                                            'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
    def command(self, event):
        
        if self.methods.GetString(self.methods.GetSelection())=="SAD":
            ##################sxc####################################
            sxc=self.phtoxc+" "+self.filenamenoext+" "+" < "+self.filenamenoext+".inp"
            vsxc=self.text_shelxc.GetValue()
            if len(vsxc)==len(sxc):
                self.text_shelxc.SetValue(sxc)
            else:
                if len(vsxc)==0:
                   sxc=sxc
                   self.text_shelxc.SetValue(sxc)
                else:
                    sxc=vsxc
                
            ##################sxm####################################    
            sxm=self.phtoxm+" "+self.filenamenoext+"_fa"
            vsxm=self.text_shelxd.GetValue()
            if len(vsxm)==len(sxm):
               self.text_shelxd.SetValue(sxm)
            else:
                if len(vsxm)==0:
                   sxm=sxm
                   self.text_shelxd.SetValue(sxm)
                else:
                   sxm=vsxm
            ##################sxe####################################
            vsxe=self.text_shelxe.GetValue()
            sxe=self.phtoxe+" "+self.filenamenoext+" "+self.filenamenoext+"_fa"+" "+"-a -h"
            if len(vsxe)==len(sxe):
               self.text_shelxe.SetValue(sxe)
            else:
                if len(vsxe)==0:
                   sxe=sxe
                   self.text_shelxe.SetValue(sxe)
                else:
                   sxe=vsxe
          
            return sxc, sxm, sxe
        elif self.methods.GetString(self.methods.GetSelection())=="MAD":
            sxc=self.phtoxc+" "+self.filenamenoext.split('_')[0]+" "+" < "+self.filenamenoext+".inp"
            vsxc=self.text_shelxc.GetValue()
            if len(vsxc)==len(sxc):
               self.text_shelxc.SetValue(sxc)
            else:
                if len(vsxc)==0:
                   sxc=sxc
                   self.text_shelxc.SetValue(sxc)
                else:
                   sxc=vsxc
            #######################sxm##################################
            sxm=self.phtoxm+" "+self.filenamenoext.split('_')[0]+"_fa"
            vsxm=self.text_shelxd.GetValue()
            if len(vsxm)==len(sxm):
               self.text_shelxd.SetValue(sxm)
            else:
                if len(vsxm)==0:
                   sxm=sxm
                   self.text_shelxd.SetValue(sxm)
                else:
                   sxm=vsxm
            #######################sxe##################################
            sxe=self.phtoxe+" "+self.filenamenoext.split('_')[0]+" "+self.filenamenoext.split('_')[0]+"_fa"+" "+"-a -i"
            vsxe=self.text_shelxe.GetValue()
            if len(vsxe)==len(sxe):
               self.text_shelxe.SetValue(sxe)
            else:
                if len(vsxe)==0:
                   sxe=sxe
                   self.text_shelxe.SetValue(sxe)
                else:
                   sxe=vsxe
            return sxc, sxm, sxe
           
        else:
                dlg = wx.MessageDialog(self, "Method is not defined",
                                            'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
    def onxc(self, event): # wxGlade: MyFrame.<event_handler>
            os.chdir(self.dirname)
            sxc, sxm, sxe=self.command(event)
            try:
                    if ossystem.startswith("win"):
                        xc=subprocess.Popen(sxc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                        self.onterminal(event, xc)
                    elif ossystem.startswith("darwin"):
                        xc=subprocess.Popen(sxc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                        self.onterminal(event, xc)
                    else:
                        xc=subprocess.Popen(sxc, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                        self.onterminal(event, xc)   
            except OSError:
                  pass
      
        
    
    def onxe(self, event): # wxGlade: MyFrame.<event_handler>
            os.chdir(self.dirname)
            sxc, sxm, sxe=self.command(event)
            try:

                 if ossystem.startswith("win"):
                    xe=subprocess.Popen(sxe, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                    self.onterminal(event, xe)
                 elif ossystem.startswith("darwin"):
                    xe=subprocess.Popen(sxe, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                    self.onterminal(event, xe)
                 else:
                    xe=subprocess.Popen(sxe, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                    self.onterminal(event, xe)
            except OSError:
                pass
 

    def onxm(self, event): # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        sxc, sxm, sxe=self.command(event)
        try:
                if ossystem.startswith("win"):
                    xs=subprocess.Popen(sxm, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                    self.onterminal(event, xs)
                elif ossystem.startswith("darwin"):
                    xs=subprocess.Popen(sxm, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                    self.onterminal(event, xs)
                else:
                    xs=subprocess.Popen(sxm, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                    self.onterminal(event, xs)
        except OSError:
                  pass
   
    def onterminal(self, event, shell):
        from terminal import terminal
        ter = terminal(event, shell)
        ter.ShowModal()
        ter.Destroy()
        
    def oninputfile(self, event):
        if self.methods.GetString(self.methods.GetSelection())=="SAD":
            if len(self.sfac.GetValue())>0:
                inp='CELL '+self.getcell(event)[0]
                inp1="SPAG "+self.getcell(event)[1]
                inp2="FIND 12"
                inp3="NTRY 100"
                inp4="SFAC "+self.sfac.GetValue()
                inp5="SAD "+ os.path.split(self.filename)[1]
                full=inp+"\n"+inp1+"\n"+inp2+"\n"+inp3+"\n"+inp4+"\n"+inp5
                return full
            else:
                dlg = wx.MessageDialog(self, "Error sfac field is empty",
                                            'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
        elif self.methods.GetString(self.methods.GetSelection())=="MAD": 
                inp='CELL '+self.getcell(event)[0]
                inp1="SPAG "+self.getcell(event)[1]
                inp2="FIND 12"
                inp3="NTRY 100"
                inp4="NAT "+ self.filename
                inp5="PEAK "+ os.path.split(self.text_peak.GetValue())[1]
                inp6="INFL "+ os.path.split(self.text_infl.GetValue())[1]
                inp7="HREM "+ os.path.split(self.text_hrem.GetValue())[1]
                inp8="LREM "+ os.path.split(self.text_lrem.GetValue())[1]
                full=inp+"\n"+inp1+"\n"+inp2+"\n"+inp3+"\n"+inp4+"\n"+inp5+"\n"+inp6+"\n"+inp7+"\n"+inp8
                return full
    def onviewpdb(self, event):
        os.chdir(self.dirname)
        if self.methods.GetString(self.methods.GetSelection())=="SAD": 
            if ossystem.startswith("win"):
                subprocess.Popen([self.phtoCoot, self.fnoe+".pdb"])
            elif ossystem.startswith("darwin"):
               subprocess.call(['open', '-a', self.phtoCoot, self.fnoe+".pdb"])
            else:
                subprocess.Popen([self.phtoCoot, self.fnoe+".pdb"])
        elif self.methods.GetString(self.methods.GetSelection())=="MAD": 
            if ossystem.startswith("win"):
                subprocess.Popen([self.phtoCoot, self.filename.split('_')[0]+"_i.pdb"])
            elif ossystem.startswith("darwin"):
               subprocess.call(['open', '-a', self.phtoCoot, self.filename.split('_')[0]+"_i.pdb"])
            else:
                subprocess.Popen([self.phtoCoot, self.filename.split('_')[0]+"_i.pdb"])
        else:

            if ossystem.startswith("win"):
                subprocess.Popen([self.phtoCoot, self.fnoe+".pdb"])
            elif ossystem.startswith("darwin"):
               subprocess.call(['open', '-a', self.phtoCoot, self.fnoe+".pdb"])
            else:
                subprocess.Popen([self.phtoCoot, self.fnoe+".pdb"])
    def makeinput(self, event):
            f=self.text_input.GetValue()
            if f:
               if os.path.exists(f):
                   webbrowser.open(f)
            else:    
               origin=self.text_original.GetValue()
               fbase=os.path.splitext(self.filename)[0]
               input=open(self.fnoe+".inp", 'w')
               intext=self.oninputfile(event)
               input.writelines(intext)
               input.close()
               self.text_input.SetValue(self.fnoe+".inp")
    def oninput(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.inp", style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            name=dlg.GetPath()
            self.text_input.SetValue(name)
            sfac=self.getsfac(event, name)
            self.sfac.SetValue(sfac)
    def getsfac(self, event, inp):
            if self.methods.GetString(self.methods.GetSelection())=="SAD": 
                f=open(inp, 'r')
                tx=f.readlines()
                for line in tx:
                    if line.upper().startswith("SFAC"):
                        line=line.upper().replace("SFAC", "").replace("\n", "")
                        sfac=line
                return sfac
    def getcell(self, event):
            f=open(self.fullname, 'r')
            line=f.readlines()[2]
            line=line.split()
            a=line[0]
            b=line[1]
            c=line[2]
            alpha=line[3]
            beta=line[4]
            gamma=line[5]
            volume=float(a)*float(b)*float(c)
            volume=round(volume, 3)
            space=line[6]
            self.text_a.SetValue(a)
            self.text_b.SetValue(b)
            self.text_c.SetValue(c)
            self.text_alpha.SetValue(alpha)
            self.text_beta.SetValue(beta)
            self.text_gamma.SetValue(gamma)
            self.text_volume.SetValue(str(volume))
            self.text_space.SetValue(space)
            celll=a+"   "+b+"   "+c+"   "+alpha+"   "+beta+"   "+gamma+"   "
            f.close()
            return celll, space
    def clearall(self, event):
        self.text_outhkl.Clear()
        self.text_hklfa.Clear()
        self.text_insfile.Clear()
        self.text_input.Clear()
        self.text_scaout.Clear()
        self.text_peak.Clear()
        self.text_hrem.Clear()
        self.text_lrem.Clear()
        self.text_shelxc.Clear()
        self.text_shelxd.Clear()
        self.text_shelxe.Clear()
    def original(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.fullname=dlg.GetPath()
            self.text_original.SetValue(self.fullname)
            self.clearall(event)
            self.getcell(event)
            self.dirname, self.filename=os.path.split(self.fullname)
            self.filenamenoext=self.filename.split('.')[0]
            self.fnoe=os.path.join(self.dirname, self.filenamenoext)
            self.command(event)
            if os.path.exists(self.fnoe+".hkl"):
                self.text_outhkl.SetValue(self.fnoe+".hkl")
            if os.path.exists(self.fnoe+"_fa.hkl"):   
                self.text_hklfa.SetValue(self.fnoe+"_fa.hkl")
            if os.path.exists(self.fnoe+"_fa.ins"): 
                self.text_insfile.SetValue(self.fnoe+"_fa.ins")
            if os.path.exists(self.fnoe+".inp"):  
                self.text_input.SetValue(self.fnoe+".inp")
                if self.methods.GetString(self.methods.GetSelection())=="SAD": 
                    sfac=self.getsfac(event, self.fnoe+".inp")
                    self.sfac.SetValue(sfac)
            if os.path.exists(self.fnoe+".hkl"):
               self.text_scaout.SetValue(self.fnoe+".hkl")
#            print self.fnoe+"_fa.hkl", self.fnoe+"_fa.ins", self.fnoe+".inp"
    def onpeak(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            name=dlg.GetPath()
            self.text_peak.SetValue(name)   
    def oninfl(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            name=dlg.GetPath()
            self.text_infl.SetValue(name) 
    def onhrem(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            name=dlg.GetPath()
            self.text_hrem.SetValue(name) 
    def onlrem(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            name=dlg.GetPath()
            self.text_lrem.SetValue(name) 
    def outhkl(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.hkl", style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            name=dlg.GetPath()
            self.text_outhkl.SetValue(name)
    def outfa(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*_fa.hkl", style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            name=dlg.GetPath()
         
            self.text_hklfa.SetValue(name)
    def sout(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            name=dlg.GetPath()
        
            self.text_scaout.SetValue(name)
    def insin(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.ins", style = wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dir=dlg.GetPath()
            fi=dlg.GetFilename()
            name=os.path.join(dir, fi)
            self.text_insfile.SetValue(name)
    def onClose(self, event):
            self.Destroy()
