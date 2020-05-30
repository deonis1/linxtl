#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This module is the part of LINXTL
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
import wx, sys, os

global path
path = sys.path[0]
global ossystem
ossystem = sys.platform

import json


# begin wxGlade: extracode
# end wxGlade
# external version 3

class cexternal(wx.Dialog):
    def __init__(self):
        # apps = ["XL(Shelxl)", "XH", "XS(Shelxs)" , "XPREP via Wine in OSX and linux (or native)", "XM(Shelxd)",
        #         "XPRO", "XC(Shelxc)", "XE(Shelxe)", "XT(Shelxt)", "Anode", "Platon", "XCIF", "CELL_NOW",
        #         "SADABS",  "Sir", "TWINABS", "PUBLCIF", "XP(XPX)", "XSHELL 5 (via Wine in linux and OSX. Compatibility mode on Win 7-10)",
        #         "XSHELL6", "OLEX", "SHELXLE", "RASMOL", "Pointless", "Aimless", "XDS2SAD", "MERCURY",  "PyMOL",  "COOT", "Avogadro",
        #         "DrawXTL", "Jmol",  "ORTEP3 (via Wine in Linux and Mac)", "DIAMOND", "Chimera",  "Sf_convert", "DIRDIF (via Wine in Linux and Mac)",
        #         "enCIFer", "Sxgraph (via Wine in Linux and Mac)", "X-SEED (via wine in Linux)", "Saint", "XDS", "Path to Wine",
        #         "Any cif file reading program", "Povray"]
        displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        sizes = [display.GetGeometry().GetSize() for display in displays]
        displaySize = sizes[0].Get()
        wx.Dialog.__init__(self, None, -1, 'External Programs', size=(displaySize[0] / 3, displaySize[1] / 3))
        ###############################################################
        self.path = path
        if os.path.exists(os.path.join(self.path, "user", "external")):
            exconfig = open(os.path.join(self.path, 'user', 'external'), 'r')
            self.exconfig = exconfig.read()
            exconfig.close()
        else:
            exconfig = open(os.path.join(self.path, 'user', 'external'), 'w')
            exconfig.writelines("\n" * 50)
            exconfig.close()
        #############################################################
        self.notebook_1 = wx.Notebook(self, -1, style=0)
        # self.notebook_1.SetPadding(wx.Size(20, 20))
        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, -1)

        self.xl = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xl = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xl_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "XL(Shelxl)")
        self.sizer_xl_staticbox.SetForegroundColour((255, 0, 0))

        self.xh = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xh = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xh_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "XH")
        self.sizer_xh_staticbox.SetForegroundColour((255, 0, 0))

        self.xs = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xs = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xs_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "XS(Shelxs)")
        self.sizer_xs_staticbox.SetForegroundColour((255, 0, 0))

        self.xprep = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xprep = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xprep_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1,
                                                  "XPREP via Wine in OSX and linux (or native)")
        self.sizer_xprep_staticbox.SetForegroundColour((255, 0, 0))

        self.xm = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xm = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xm_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "XM(Shelxd)")
        self.sizer_xm_staticbox.SetForegroundColour((255, 0, 0))

        self.xpro = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xpro = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xpro_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "XPRO")
        self.sizer_xpro_staticbox.SetForegroundColour((255, 0, 0))

        self.xc = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xc = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xc_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "XC(Shelxc)")
        self.sizer_xc_staticbox.SetForegroundColour((255, 0, 0))

        self.xe = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xe = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xe_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "XE(Shelxe)")
        self.sizer_xe_staticbox.SetForegroundColour((255, 0, 0))

        self.xt = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_xt = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_xt_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "XT(Shelxt)")
        self.sizer_xt_staticbox.SetForegroundColour((255, 0, 0))

        self.anode = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_anode = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_anode_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "Anode")
        self.sizer_anode_staticbox.SetForegroundColour((255, 0, 0))

        self.platon = wx.TextCtrl(self.notebook_1_pane_1, -1, "")
        self.Open_platon = wx.Button(self.notebook_1_pane_1, -1, "Browse")
        self.sizer_platon_staticbox = wx.StaticBox(self.notebook_1_pane_1, -1, "Platon")
        self.sizer_platon_staticbox.SetForegroundColour((255, 0, 0))

        self.notebook_1_pane_2 = wx.Panel(self.notebook_1, -1)

        self.xcif = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_xcif = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_xcif_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "XCIF")
        self.sizer_xcif_staticbox.SetForegroundColour((255, 0, 0))

        self.cellnow = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_cellnow = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_cellnow_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "CELL_NOW")
        self.sizer_cellnow_staticbox.SetForegroundColour((255, 0, 0))

        self.sadabs = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_sadabs = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_sadabs_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "SADABS")
        self.sizer_sadabs_staticbox.SetForegroundColour((255, 0, 0))

        self.xabs2 = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_xabs2 = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_xabs2_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "XABS2")
        self.sizer_xabs2_staticbox.SetForegroundColour((255, 0, 0))

        self.sir = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_sir = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_sir_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "Sir")
        self.sizer_sir_staticbox.SetForegroundColour((255, 0, 0))

        self.twinabs = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_twinabs = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_twinabs_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "TWINABS")
        self.sizer_twinabs_staticbox.SetForegroundColour((255, 0, 0))

        self.publcif = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_publcif = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_publcif_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "PUBLCIF")
        self.sizer_publcif_staticbox.SetForegroundColour((255, 0, 0))

        self.xp = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_xp = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_xp_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "XP(XPX)")
        self.sizer_xp_staticbox.SetForegroundColour((255, 0, 0))

        self.xshell5 = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_oldxshell = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_xshell_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1,
                                                   "XSHELL 5 (via Wine in linux and OSX. Compatibility mode on Win 7-10)")
        self.sizer_xshell_staticbox.SetForegroundColour((255, 0, 0))

        self.xshell6 = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_xshell6 = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_xshell6_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "XSHELL6")
        self.sizer_xshell6_staticbox.SetForegroundColour((255, 0, 0))

        self.olex = wx.TextCtrl(self.notebook_1_pane_2, -1, "")
        self.Open_olex = wx.Button(self.notebook_1_pane_2, -1, "Browse")
        self.sizer_olex_staticbox = wx.StaticBox(self.notebook_1_pane_2, -1, "OLEX")
        self.sizer_olex_staticbox.SetForegroundColour((255, 0, 0))

        self.notebook_1_pane_3 = wx.Panel(self.notebook_1, -1)
        self.shelxle = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_shelxle = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_shelxle_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "SHELXLE")

        self.sizer_shelxle_staticbox.SetForegroundColour((255, 0, 0))
        self.rasmol = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_rasmol = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_rasmol_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "RASMOL")
        self.sizer_rasmol_staticbox.SetForegroundColour((255, 0, 0))

        self.pointless = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_pointless = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_pointless_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "Pointless")
        self.sizer_pointless_staticbox.SetForegroundColour((255, 0, 0))

        self.aimless = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_aimless = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_aimless_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "Aimless")
        self.sizer_aimless_staticbox.SetForegroundColour((255, 0, 0))

        self.xds2sad = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_xds2sad = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_xds2sad_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "XDS2SAD")
        self.sizer_xds2sad_staticbox.SetForegroundColour((255, 0, 0))

        self.mercury = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_mercury = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_mercury_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "MERCURY")
        self.sizer_mercury_staticbox.SetForegroundColour((255, 0, 0))

        self.pymol = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_pymol = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_pymol_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "PyMOL")
        self.sizer_pymol_staticbox.SetForegroundColour((255, 0, 0))

        self.coot = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_coot = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_coot_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "COOT")
        self.sizer_coot_staticbox.SetForegroundColour((255, 0, 0))

        self.avogadro = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_avogadro = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_avogadro_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "Avogadro")
        self.sizer_avogadro_staticbox.SetForegroundColour((255, 0, 0))

        self.drawxtl = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_drawxtl = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_drawxtl_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "DrawXTL")
        self.sizer_drawxtl_staticbox.SetForegroundColour((255, 0, 0))

        self.jmol = wx.TextCtrl(self.notebook_1_pane_3, -1, "")
        self.Open_jmol = wx.Button(self.notebook_1_pane_3, -1, "Browse")
        self.sizer_jmol_staticbox = wx.StaticBox(self.notebook_1_pane_3, -1, "Jmol")
        self.sizer_jmol_staticbox.SetForegroundColour((255, 0, 0))

        self.notebook_1_pane_4 = wx.Panel(self.notebook_1, -1)
        self.ortep3 = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_ortep3 = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_ortep_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "ORTEP3 (via Wine in Linux and Mac)")
        self.sizer_ortep_staticbox.SetForegroundColour((255, 0, 0))

        self.diamond = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_diamond = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_diamand_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "DIAMOND")
        self.sizer_diamand_staticbox.SetForegroundColour((255, 0, 0))

        self.Chimera = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_Chimera = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_Chimera_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "Chimera")
        self.sizer_Chimera_staticbox.SetForegroundColour((255, 0, 0))

        self.sfconvert = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_sfconvert = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_sfconvert_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "Sf_convert")
        self.sizer_sfconvert_staticbox.SetForegroundColour((255, 0, 0))

        self.dirdif = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_dirdif = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_dirdif_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "DIRDIF (via Wine in Linux and Mac)")
        self.sizer_dirdif_staticbox.SetForegroundColour((255, 0, 0))

        self.enCifer = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_enCifer = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_encifer_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "enCIFer")
        self.sizer_encifer_staticbox.SetForegroundColour((255, 0, 0))

        self.Sxgraph = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_Sxgraph = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_Sxgraph_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "Sxgraph (via Wine in Linux and Mac)")
        self.sizer_Sxgraph_staticbox.SetForegroundColour((255, 0, 0))

        self.xseed = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_xseed = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_xseed_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "X-SEED (via wine in Linux)")
        self.sizer_xseed_staticbox.SetForegroundColour((255, 0, 0))

        # self.saint = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        # self.Open_saint = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        # self.sizer_saint_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "Saint")
        # self.sizer_saint_staticbox.SetForegroundColour((255,0,0))

        self.xds = wx.TextCtrl(self.notebook_1_pane_4, -1, "")
        self.Open_xds = wx.Button(self.notebook_1_pane_4, -1, "Browse")
        self.sizer_xds_staticbox = wx.StaticBox(self.notebook_1_pane_4, -1, "XDS")
        self.sizer_xds_staticbox.SetForegroundColour((255, 0, 0))

        self.notebook_1_pane_5 = wx.Panel(self.notebook_1, -1)
        self.wine = wx.TextCtrl(self.notebook_1_pane_5, -1, "")
        self.Open_wine = wx.Button(self.notebook_1_pane_5, -1, "Browse")
        self.sizer_wine_staticbox = wx.StaticBox(self.notebook_1_pane_5, -1, "Path to Wine")
        self.sizer_wine_staticbox.SetForegroundColour((255, 0, 0))

        self.anycif = wx.TextCtrl(self.notebook_1_pane_5, -1, "")
        self.Open_anycif = wx.Button(self.notebook_1_pane_5, -1, "Browse")
        self.sizer_anycif_staticbox = wx.StaticBox(self.notebook_1_pane_5, -1, "Any cif file reading program")
        self.sizer_anycif_staticbox.SetForegroundColour((255, 0, 0))

        self.povray = wx.TextCtrl(self.notebook_1_pane_5, -1, "")
        self.Open_povray = wx.Button(self.notebook_1_pane_5, -1, "Browse")
        self.sizer_povray_staticbox = wx.StaticBox(self.notebook_1_pane_5, -1, "Povray")
        self.sizer_povray_staticbox.SetForegroundColour((255, 0, 0))

        self.button_1 = wx.Button(self, -1, "OK")
        self.button_2 = wx.Button(self, -1, "Cancel")
        self.button_3 = wx.Button(self, -1, "Scan")
        self.sizer_2_staticbox = wx.StaticBox(self, -1)

        self.__do_layout()
        # end wxGlade
        self.Bind(wx.EVT_BUTTON, self.ontOk, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.onScan, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.onOpenrasmol, self.Open_rasmol)
        self.Bind(wx.EVT_BUTTON, self.onOpenolex, self.Open_olex)
        self.Bind(wx.EVT_BUTTON, self.onOpenxseed, self.Open_xseed)
        self.Bind(wx.EVT_BUTTON, self.onOpenxshell, self.Open_oldxshell)
        self.Bind(wx.EVT_BUTTON, self.onOpenshelxle, self.Open_shelxle)
        self.Bind(wx.EVT_BUTTON, self.onOpencellnow, self.Open_cellnow)
        self.Bind(wx.EVT_BUTTON, self.onOpenxl, self.Open_xl)
        self.Bind(wx.EVT_BUTTON, self.onOpenxh, self.Open_xh)
        self.Bind(wx.EVT_BUTTON, self.onOpenxs, self.Open_xs)
        self.Bind(wx.EVT_BUTTON, self.onOpenxprep, self.Open_xprep)
        self.Bind(wx.EVT_BUTTON, self.onOpenxm, self.Open_xm)
        self.Bind(wx.EVT_BUTTON, self.onOpenxpro, self.Open_xpro)
        self.Bind(wx.EVT_BUTTON, self.onOpenpub, self.Open_publcif)
        self.Bind(wx.EVT_BUTTON, self.onOpenxcif, self.Open_xcif)
        self.Bind(wx.EVT_BUTTON, self.onOpenxshell6, self.Open_xshell6)
        self.Bind(wx.EVT_BUTTON, self.onOpenxp, self.Open_xp)
        self.Bind(wx.EVT_BUTTON, self.onOpensadabs, self.Open_sadabs)
        self.Bind(wx.EVT_BUTTON, self.onOpenxabs2, self.Open_xabs2)
        self.Bind(wx.EVT_BUTTON, self.onOpenplaton, self.Open_platon)
        self.Bind(wx.EVT_BUTTON, self.onOpensir, self.Open_sir)
        self.Bind(wx.EVT_BUTTON, self.onOpenxe, self.Open_xe)
        self.Bind(wx.EVT_BUTTON, self.onOpenxc, self.Open_xc)
        self.Bind(wx.EVT_BUTTON, self.onOpenxt, self.Open_xt)
        self.Bind(wx.EVT_BUTTON, self.onOpenmercury, self.Open_mercury)
        self.Bind(wx.EVT_BUTTON, self.onOpenavogadro, self.Open_avogadro)
        self.Bind(wx.EVT_BUTTON, self.onOpenpymol, self.Open_pymol)
        self.Bind(wx.EVT_BUTTON, self.onOpencoot, self.Open_coot)
        self.Bind(wx.EVT_BUTTON, self.onsfconvert, self.Open_sfconvert)
        self.Bind(wx.EVT_BUTTON, self.onTwinabs, self.Open_twinabs)
        self.Bind(wx.EVT_BUTTON, self.onDrawxtl, self.Open_drawxtl)
        self.Bind(wx.EVT_BUTTON, self.onJmol, self.Open_jmol)
        self.Bind(wx.EVT_BUTTON, self.onOrtep3, self.Open_ortep3)
        self.Bind(wx.EVT_BUTTON, self.onDiamond, self.Open_diamond)
        self.Bind(wx.EVT_BUTTON, self.onChimera, self.Open_Chimera)
        self.Bind(wx.EVT_BUTTON, self.onDirdif, self.Open_dirdif)
        self.Bind(wx.EVT_BUTTON, self.onenCifer, self.Open_enCifer)
        self.Bind(wx.EVT_BUTTON, self.onSxgraph, self.Open_Sxgraph)
        # self.Bind(wx.EVT_BUTTON, self.onsaint, self.Open_saint)
        self.Bind(wx.EVT_BUTTON, self.onwine, self.Open_wine)
        self.Bind(wx.EVT_BUTTON, self.onanycif, self.Open_anycif)
        self.Bind(wx.EVT_BUTTON, self.onpovray, self.Open_povray)
        self.Bind(wx.EVT_BUTTON, self.onanode, self.Open_anode)
        self.Bind(wx.EVT_BUTTON, self.onxds, self.Open_xds)
        self.Bind(wx.EVT_BUTTON, self.onpointless, self.Open_pointless)
        self.Bind(wx.EVT_BUTTON, self.onaimless, self.Open_aimless)
        self.Bind(wx.EVT_BUTTON, self.onxds2sad, self.Open_xds2sad)
        #        self.Bind(wx.EVT_BUTTON, self.onOpenplaton, self.Open_platon_copy)
        self.Bind(wx.EVT_BUTTON, self.Closeex, self.button_2)
        self.Bind(wx.EVT_CLOSE, self.Closeex)

    def __do_layout(self):
        # begin wxGlade: cexternal.__do_layout
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(1, 3, wx.ALL, 5)
        sizer_5_copy_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_6_copy_2 = wx.BoxSizer(wx.VERTICAL)

        # self.sizer_saint_staticbox.Lower()
        # sizer_saint = wx.StaticBoxSizer(self.sizer_saint_staticbox, wx.HORIZONTAL)

        self.sizer_xds_staticbox.Lower()
        sizer_xds = wx.StaticBoxSizer(self.sizer_xds_staticbox, wx.HORIZONTAL)

        self.sizer_Sxgraph_staticbox.Lower()
        sizer_Sxgraph = wx.StaticBoxSizer(self.sizer_Sxgraph_staticbox, wx.HORIZONTAL)

        self.sizer_encifer_staticbox.Lower()
        sizer_encifer = wx.StaticBoxSizer(self.sizer_encifer_staticbox, wx.HORIZONTAL)

        self.sizer_dirdif_staticbox.Lower()
        sizer_dirdif = wx.StaticBoxSizer(self.sizer_dirdif_staticbox, wx.HORIZONTAL)

        self.sizer_Chimera_staticbox.Lower()
        sizer_Chimera = wx.StaticBoxSizer(self.sizer_Chimera_staticbox, wx.HORIZONTAL)

        self.sizer_sfconvert_staticbox.Lower()
        sizer_sfconvert = wx.StaticBoxSizer(self.sizer_sfconvert_staticbox, wx.HORIZONTAL)

        self.sizer_diamand_staticbox.Lower()
        sizer_diamand = wx.StaticBoxSizer(self.sizer_diamand_staticbox, wx.HORIZONTAL)

        self.sizer_ortep_staticbox.Lower()
        sizer_ortep = wx.StaticBoxSizer(self.sizer_ortep_staticbox, wx.HORIZONTAL)
        sizer_5_copy_1 = wx.BoxSizer(wx.VERTICAL)

        self.sizer_jmol_staticbox.Lower()
        sizer_jmol = wx.StaticBoxSizer(self.sizer_jmol_staticbox, wx.HORIZONTAL)

        self.sizer_drawxtl_staticbox.Lower()
        sizer_drawxtl = wx.StaticBoxSizer(self.sizer_drawxtl_staticbox, wx.HORIZONTAL)

        self.sizer_avogadro_staticbox.Lower()
        sizer_avogadro = wx.StaticBoxSizer(self.sizer_avogadro_staticbox, wx.HORIZONTAL)

        self.sizer_coot_staticbox.Lower()
        sizer_coot = wx.StaticBoxSizer(self.sizer_coot_staticbox, wx.HORIZONTAL)

        self.sizer_pymol_staticbox.Lower()
        sizer_pymol = wx.StaticBoxSizer(self.sizer_pymol_staticbox, wx.HORIZONTAL)

        self.sizer_mercury_staticbox.Lower()
        sizer_mercury = wx.StaticBoxSizer(self.sizer_mercury_staticbox, wx.HORIZONTAL)

        self.sizer_rasmol_staticbox.Lower()
        sizer_rasmol = wx.StaticBoxSizer(self.sizer_rasmol_staticbox, wx.HORIZONTAL)

        self.sizer_pointless_staticbox.Lower()
        sizer_pointless = wx.StaticBoxSizer(self.sizer_pointless_staticbox, wx.HORIZONTAL)

        self.sizer_aimless_staticbox.Lower()
        sizer_aimless = wx.StaticBoxSizer(self.sizer_aimless_staticbox, wx.HORIZONTAL)

        self.sizer_xds2sad_staticbox.Lower()
        sizer_xds2sad = wx.StaticBoxSizer(self.sizer_xds2sad_staticbox, wx.HORIZONTAL)

        self.sizer_shelxle_staticbox.Lower()
        sizer_shelxle = wx.StaticBoxSizer(self.sizer_shelxle_staticbox, wx.HORIZONTAL)

        sizer_5_copy = wx.BoxSizer(wx.VERTICAL)

        self.sizer_xc_staticbox.Lower()
        sizer_xc = wx.StaticBoxSizer(self.sizer_xc_staticbox, wx.HORIZONTAL)

        self.sizer_xt_staticbox.Lower()
        sizer_xt = wx.StaticBoxSizer(self.sizer_xt_staticbox, wx.HORIZONTAL)

        self.sizer_olex_staticbox.Lower()
        sizer_olex = wx.StaticBoxSizer(self.sizer_olex_staticbox, wx.HORIZONTAL)

        self.sizer_xseed_staticbox.Lower()
        sizer_xseed = wx.StaticBoxSizer(self.sizer_xseed_staticbox, wx.HORIZONTAL)

        self.sizer_xshell6_staticbox.Lower()
        sizer_xshell6 = wx.StaticBoxSizer(self.sizer_xshell6_staticbox, wx.HORIZONTAL)

        self.sizer_xshell_staticbox.Lower()
        sizer_xshell = wx.StaticBoxSizer(self.sizer_xshell_staticbox, wx.HORIZONTAL)

        self.sizer_publcif_staticbox.Lower()
        sizer_publcif = wx.StaticBoxSizer(self.sizer_publcif_staticbox, wx.HORIZONTAL)

        self.sizer_twinabs_staticbox.Lower()
        sizer_twinabs = wx.StaticBoxSizer(self.sizer_twinabs_staticbox, wx.HORIZONTAL)

        self.sizer_xabs2_staticbox.Lower()
        sizer_xabs2 = wx.StaticBoxSizer(self.sizer_xabs2_staticbox, wx.HORIZONTAL)

        self.sizer_sadabs_staticbox.Lower()
        sizer_sadabs = wx.StaticBoxSizer(self.sizer_sadabs_staticbox, wx.HORIZONTAL)

        self.sizer_cellnow_staticbox.Lower()
        sizer_cellnow = wx.StaticBoxSizer(self.sizer_cellnow_staticbox, wx.HORIZONTAL)

        self.sizer_xcif_staticbox.Lower()
        sizer_xcif = wx.StaticBoxSizer(self.sizer_xcif_staticbox, wx.HORIZONTAL)

        sizer_5 = wx.BoxSizer(wx.VERTICAL)

        self.sizer_sir_staticbox.Lower()
        sizer_sir = wx.StaticBoxSizer(self.sizer_sir_staticbox, wx.HORIZONTAL)

        self.sizer_platon_staticbox.Lower()
        sizer_platon = wx.StaticBoxSizer(self.sizer_platon_staticbox, wx.HORIZONTAL)

        self.sizer_xe_staticbox.Lower()
        sizer_xe = wx.StaticBoxSizer(self.sizer_xe_staticbox, wx.HORIZONTAL)

        self.sizer_xp_staticbox.Lower()
        sizer_xp = wx.StaticBoxSizer(self.sizer_xp_staticbox, wx.HORIZONTAL)

        self.sizer_xpro_staticbox.Lower()
        sizer_xpro = wx.StaticBoxSizer(self.sizer_xpro_staticbox, wx.HORIZONTAL)

        self.sizer_xm_staticbox.Lower()
        sizer_xm = wx.StaticBoxSizer(self.sizer_xm_staticbox, wx.HORIZONTAL)

        self.sizer_anode_staticbox.Lower()
        sizer_anode = wx.StaticBoxSizer(self.sizer_anode_staticbox, wx.HORIZONTAL)

        self.sizer_xprep_staticbox.Lower()
        sizer_xprep = wx.StaticBoxSizer(self.sizer_xprep_staticbox, wx.HORIZONTAL)

        self.sizer_xs_staticbox.Lower()
        sizer_xs = wx.StaticBoxSizer(self.sizer_xs_staticbox, wx.HORIZONTAL)

        self.sizer_xh_staticbox.Lower()
        sizer_xh = wx.StaticBoxSizer(self.sizer_xh_staticbox, wx.HORIZONTAL)

        self.sizer_xl_staticbox.Lower()

        sizer_xl = wx.StaticBoxSizer(self.sizer_xl_staticbox, wx.HORIZONTAL)
        sizer_xl.Add(self.xl, 4, wx.ALL, 5)
        sizer_xl.Add(self.Open_xl, 0, wx.ALL, 5)
        sizer_5.Add(sizer_xl, 0, wx.EXPAND , 0)

        sizer_xh.Add(self.xh, 4, wx.ALL, 5)
        sizer_xh.Add(self.Open_xh, 0, wx.ALL, 5)
        sizer_5.Add(sizer_xh, 0, wx.EXPAND , 0)

        sizer_xs.Add(self.xs, 4, wx.ALL, 5)
        sizer_xs.Add(self.Open_xs, 0, wx.ALL, 5)
        sizer_5.Add(sizer_xs, 0, wx.EXPAND , 0)

        sizer_xprep.Add(self.xprep, 4, wx.ALL, 5)
        sizer_xprep.Add(self.Open_xprep, 0, wx.ALL, 5)
        sizer_5.Add(sizer_xprep, 0, wx.EXPAND , 0)

        sizer_xc.Add(self.xc, 4, wx.ALL, 5)
        sizer_xc.Add(self.Open_xc, 0, wx.ALL, 5)
        sizer_5.Add(sizer_xc, 0, wx.EXPAND , 0)

        sizer_xm.Add(self.xm, 4, wx.ALL, 5)
        sizer_xm.Add(self.Open_xm, 0, wx.ALL, 5)
        sizer_5.Add(sizer_xm, 0, wx.EXPAND , 0)

        sizer_xe.Add(self.xe, 4, wx.ALL, 5)
        sizer_xe.Add(self.Open_xe, 0, wx.ALL, 5)
        sizer_5.Add(sizer_xe, 0, wx.EXPAND , 0)

        sizer_xpro.Add(self.xpro, 4, wx.ALL, 5)
        sizer_xpro.Add(self.Open_xpro, 0, wx.ALL, 5)
        sizer_5.Add(sizer_xpro, 0, wx.EXPAND , 0)

        sizer_platon.Add(self.platon, 4, wx.ALL, 5)
        sizer_platon.Add(self.Open_platon, 0, wx.ALL, 5)
        sizer_5.Add(sizer_platon, 0, wx.EXPAND , 0)

        sizer_sir.Add(self.sir, 4, wx.ALL, 5)
        sizer_sir.Add(self.Open_sir, 0, wx.ALL, 5)
        sizer_5.Add(sizer_sir, 0, wx.EXPAND , 0)

        sizer_anode.Add(self.anode, 4, wx.ALL, 5)
        sizer_anode.Add(self.Open_anode, 0, wx.ALL, 5)
        sizer_5.Add(sizer_anode, 0, wx.EXPAND , 0)

        self.notebook_1_pane_1.SetSizer(sizer_5)

        sizer_xcif.Add(self.xcif, 4, wx.ALL, 5)
        sizer_xcif.Add(self.Open_xcif, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_xcif, 0, wx.EXPAND , 0)

        sizer_cellnow.Add(self.cellnow, 4, wx.ALL, 5)
        sizer_cellnow.Add(self.Open_cellnow, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_cellnow, 0, wx.EXPAND , 0)

        sizer_sadabs.Add(self.sadabs, 4, wx.ALL, 5)
        sizer_sadabs.Add(self.Open_sadabs, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_sadabs, 0, wx.EXPAND , 0)

        sizer_twinabs.Add(self.twinabs, 4, wx.ALL, 5)
        sizer_twinabs.Add(self.Open_twinabs, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_twinabs, 0, wx.EXPAND , 0)

        sizer_publcif.Add(self.publcif, 4, wx.ALL, 5)
        sizer_publcif.Add(self.Open_publcif, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_publcif, 0, wx.EXPAND , 0)

        sizer_xshell.Add(self.xshell5, 4, wx.ALL, 5)
        sizer_xshell.Add(self.Open_oldxshell, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_xshell, 0, wx.EXPAND , 0)

        sizer_xshell6.Add(self.xshell6, 4, wx.ALL, 5)
        sizer_xshell6.Add(self.Open_xshell6, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_xshell6, 0, wx.EXPAND , 0)

        sizer_olex.Add(self.olex, 4, wx.ALL, 5)
        sizer_olex.Add(self.Open_olex, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_olex, 0, wx.EXPAND , 0)

        sizer_xp.Add(self.xp, 4, wx.ALL, 5)
        sizer_xp.Add(self.Open_xp, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_xp, 0, wx.EXPAND , 0)

        sizer_xt.Add(self.xt, 4, wx.ALL, 5)
        sizer_xt.Add(self.Open_xt, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_xt, 0, wx.EXPAND , 0)

        sizer_xabs2.Add(self.xabs2, 4, wx.ALL, 5)
        sizer_xabs2.Add(self.Open_xabs2, 0, wx.ALL, 5)
        sizer_5_copy.Add(sizer_xabs2, 0, wx.EXPAND , 0)

        self.notebook_1_pane_2.SetSizer(sizer_5_copy)

        sizer_shelxle.Add(self.shelxle, 4, wx.ALL, 5)
        sizer_shelxle.Add(self.Open_shelxle, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_shelxle, 0, wx.EXPAND , 0)

        sizer_rasmol.Add(self.rasmol, 4, wx.ALL, 5)
        sizer_rasmol.Add(self.Open_rasmol, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_rasmol, 0, wx.EXPAND , 0)

        sizer_pointless.Add(self.pointless, 4, wx.ALL, 5)
        sizer_pointless.Add(self.Open_pointless, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_pointless, 0, wx.EXPAND , 0)

        sizer_aimless.Add(self.aimless, 4, wx.ALL, 5)
        sizer_aimless.Add(self.Open_aimless, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_aimless, 0, wx.EXPAND , 0)

        sizer_xds2sad.Add(self.xds2sad, 4, wx.ALL, 5)
        sizer_xds2sad.Add(self.Open_xds2sad, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_xds2sad, 0, wx.EXPAND , 0)

        sizer_mercury.Add(self.mercury, 4, wx.ALL, 5)
        sizer_mercury.Add(self.Open_mercury, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_mercury, 0, wx.EXPAND , 0)

        sizer_pymol.Add(self.pymol, 4, wx.ALL, 5)
        sizer_pymol.Add(self.Open_pymol, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_pymol, 0, wx.EXPAND , 0)

        sizer_coot.Add(self.coot, 4, wx.ALL, 5)
        sizer_coot.Add(self.Open_coot, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_coot, 0, wx.EXPAND , 0)

        sizer_avogadro.Add(self.avogadro, 4, wx.ALL, 5)
        sizer_avogadro.Add(self.Open_avogadro, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_avogadro, 0, wx.EXPAND , 0)

        sizer_drawxtl.Add(self.drawxtl, 4, wx.ALL, 5)
        sizer_drawxtl.Add(self.Open_drawxtl, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_drawxtl, 0, wx.EXPAND , 0)

        sizer_jmol.Add(self.jmol, 4, wx.ALL, 5)
        sizer_jmol.Add(self.Open_jmol, 0, wx.ALL, 5)
        sizer_5_copy_1.Add(sizer_jmol, 0, wx.EXPAND , 0)

        self.notebook_1_pane_3.SetSizer(sizer_5_copy_1)
        sizer_ortep.Add(self.ortep3, 4, wx.ALL, 5)
        sizer_ortep.Add(self.Open_ortep3, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_ortep, 0, wx.EXPAND , 0)

        sizer_diamand.Add(self.diamond, 4, wx.ALL, 5)
        sizer_diamand.Add(self.Open_diamond, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_diamand, 0, wx.EXPAND , 0)

        sizer_Chimera.Add(self.Chimera, 4, wx.ALL, 5)
        sizer_Chimera.Add(self.Open_Chimera, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_Chimera, 0, wx.EXPAND , 0)

        sizer_sfconvert.Add(self.sfconvert, 4, wx.ALL, 5)
        sizer_sfconvert.Add(self.Open_sfconvert, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_sfconvert, 0, wx.EXPAND , 0)

        sizer_dirdif.Add(self.dirdif, 4, wx.ALL, 5)
        sizer_dirdif.Add(self.Open_dirdif, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_dirdif, 0, wx.EXPAND , 0)

        sizer_encifer.Add(self.enCifer, 4, wx.ALL, 5)
        sizer_encifer.Add(self.Open_enCifer, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_encifer, 0, wx.EXPAND , 0)

        sizer_Sxgraph.Add(self.Sxgraph, 4, wx.ALL, 5)
        sizer_Sxgraph.Add(self.Open_Sxgraph, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_Sxgraph, 0, wx.EXPAND , 0)

        # sizer_saint.Add(self.saint, 4, wx.ALL, 5)
        # sizer_saint.Add(self.Open_saint, 0, wx.ALL, 5)
        # sizer_5_copy_2.Add(sizer_saint, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_xds.Add(self.xds, 4, wx.ALL, 5)
        sizer_xds.Add(self.Open_xds, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_xds, 0, wx.EXPAND , 0)

        sizer_xseed.Add(self.xseed, 4, wx.ALL, 5)
        sizer_xseed.Add(self.Open_xseed, 0, wx.ALL, 5)
        sizer_5_copy_2.Add(sizer_xseed, 0, wx.EXPAND , 0)

        self.notebook_1_pane_4.SetSizer(sizer_5_copy_2)
        self.sizer_wine_staticbox.Lower()
        sizer_wine = wx.StaticBoxSizer(self.sizer_wine_staticbox, wx.HORIZONTAL)
        self.sizer_anycif_staticbox.Lower()
        sizer_anycif = wx.StaticBoxSizer(self.sizer_anycif_staticbox, wx.HORIZONTAL)
        self.sizer_povray_staticbox.Lower()
        sizer_povray = wx.StaticBoxSizer(self.sizer_povray_staticbox, wx.HORIZONTAL)
        sizer_wine.Add(self.wine, 4, wx.ALL, 5)
        sizer_wine.Add(self.Open_wine, 0, wx.ALL, 5)
        sizer_6_copy_2.Add(sizer_wine, 0, wx.EXPAND , 0)

        sizer_anycif.Add(self.anycif, 4, wx.ALL, 5)
        sizer_anycif.Add(self.Open_anycif, 0, wx.ALL, 5)
        sizer_6_copy_2.Add(sizer_anycif, 0, wx.EXPAND , 0)

        sizer_povray.Add(self.povray, 4, wx.ALL, 5)
        sizer_povray.Add(self.Open_povray, 0, wx.ALL, 5)
        sizer_6_copy_2.Add(sizer_povray, 0, wx.EXPAND , 0)

        self.notebook_1_pane_5.SetSizer(sizer_6_copy_2)

        self.notebook_1.AddPage(self.notebook_1_pane_1, "Programs 1")
        self.notebook_1.AddPage(self.notebook_1_pane_2, "Programs 2")
        self.notebook_1.AddPage(self.notebook_1_pane_3, "Programs 3")
        self.notebook_1.AddPage(self.notebook_1_pane_4, "Programs 4")
        self.notebook_1.AddPage(self.notebook_1_pane_5, "Programs 5")

        sizer_3.Add(self.notebook_1, 7, wx.EXPAND | wx.ALL, 13)

        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        #        grid_sizer_1.Add((20, 34), 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.button_3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        #        grid_sizer_1.Add((20, 34), 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, wx.ALL | wx.EXPAND, 0)

        self.Center()
        self.CenterOnScreen()
        self.Layout()
        self.SetSizerAndFit(sizer_2)
        self.SetBackgroundColour(wx.Colour(245, 245, 245))
        self.notebook_1_pane_1.SetBackgroundColour(wx.Colour(245, 245, 245))
        self.notebook_1_pane_2.SetBackgroundColour(wx.Colour(245, 245, 245))
        self.notebook_1_pane_3.SetBackgroundColour(wx.Colour(245, 245, 245))
        self.notebook_1_pane_4.SetBackgroundColour(wx.Colour(245, 245, 245))
        self.notebook_1_pane_5.SetBackgroundColour(wx.Colour(245, 245, 245))

        # end wxGlade
        self.getvalues()

    def getvalues(self):
        json_file = os.path.join(self.path, "user", "external.json")
        json_file_obj = open(json_file, 'r')
        self.external_config = json.load(json_file_obj)
        json_file_obj.close()
        self.xl.SetValue(self.external_config['shelxl'])
        self.xh.SetValue(self.external_config['shelxh'])
        self.xs.SetValue(self.external_config['shelxs'])
        self.xprep.SetValue(self.external_config['xprep'])
        self.sir.SetValue(self.external_config['sir'])
        self.xpro.SetValue(self.external_config['xpro'])
        self.publcif.SetValue(self.external_config['publcif'])
        self.xp.SetValue(self.external_config['xp'])
        self.platon.SetValue(self.external_config['platon'])
        self.xshell5.SetValue(self.external_config['xshell5'])
        self.xshell6.SetValue(self.external_config['xshell6'])
        self.shelxle.SetValue(self.external_config['shelxle'])
        self.rasmol.SetValue(self.external_config['rasmol'])
        self.olex.SetValue(self.external_config['olex'])
        self.cellnow.SetValue(self.external_config['cellnow'])
        self.sadabs.SetValue(self.external_config['sadabs'])
        self.xcif.SetValue(self.external_config['xcif'])
        self.mercury.SetValue(self.external_config['mercury'])
        self.avogadro.SetValue(self.external_config['avogadro'])
        self.pymol.SetValue(self.external_config['pymol'])
        self.coot.SetValue(self.external_config['coot'])
        self.twinabs.SetValue(self.external_config['twinabs'])
        self.drawxtl.SetValue(self.external_config['drawxtl'])
        self.jmol.SetValue(self.external_config['jmol'])
        self.ortep3.SetValue(self.external_config['ortep3'])
        self.diamond.SetValue(self.external_config['diamond'])
        self.Chimera.SetValue(self.external_config['chimera'])
        self.dirdif.SetValue(self.external_config['dirdif'])
        self.enCifer.SetValue(self.external_config['encifer'])
        self.Sxgraph.SetValue(self.external_config['sxgraph'])
        # self.saint.SetValue(self.external_config['saint'])
        self.xm.SetValue(self.external_config['shelxd'])
        self.xe.SetValue(self.external_config['shelxe'])
        self.xc.SetValue(self.external_config['shelxc'])
        self.wine.SetValue(self.external_config['wine'])
        self.anycif.SetValue(self.external_config['anycif'])
        self.povray.SetValue(self.external_config['povray'])
        self.xt.SetValue(self.external_config['shelxt'])
        self.xseed.SetValue(self.external_config['xseed'])
        self.sfconvert.SetValue(self.external_config['sfconvert'])
        self.anode.SetValue(self.external_config['anode'])
        self.xabs2.SetValue(self.external_config['xabs'])
        self.xds.SetValue(self.external_config['xds'])
        self.pointless.SetValue(self.external_config['pointless'])
        self.aimless.SetValue(self.external_config['aimless'])

    def onOpenxl(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.path, "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()
            fnamefull = dirname + "/" + fname
            self.xl.SetValue(fnamefull)

    def onScan(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            listprograms = ['shelxl', 'xl', 'shelxh', 'shelxs', 'xprep', 'shelxm', 'shelxd', 'xpro', 'xpx', 'shelxle',
                            'platon', 'sir2011', 'sir97', 'cell_now', 'cellnow', 'xshell.exe', 'shelxc', 'shelxle',
                            'rasmol', 'mercury', 'avogadro', 'ortep.exe', 'jmol', 'coot', 'xshell', 'pymol', 'chimera']
            self.listprograms = listprograms
            try:
                xlist = []
                lpath = []
                for dirpath, dirnames, filenames in os.walk(str(dlg.GetPath())):
                    for program in listprograms:
                        for filename in filenames:
                            if program.lower() in filename.lower():
                                xlist.append(os.path.join(dirpath, filename))
                self.checklist(event, xlist)
            except UnicodeEncodeError:
                pass

    def checklist(self, event, xlist):
        self.xlist = xlist
        sellist = []
        if ossystem.startswith('win'):
            if not len(xlist) == 0:
                dialog = wx.MultiChoiceDialog(self, 'Programs found', 'Programs', xlist)
                dialog.SetSelections(range(len(xlist)))
                if (dialog.ShowModal() == wx.ID_OK):
                    lists = dialog.GetSelections()
                    dialog.Destroy()
                    for item in lists:
                        sellist.append(xlist[item])
                for paths in sellist:
                    if paths.endswith('xl.exe') or paths.endswith('shelxl.exe'):
                        self.xl.SetValue(paths)
                    if paths.endswith('xh.exe'):
                        self.xh.SetValue(paths)
                    if paths.endswith('xs.exe') or paths.endswith('shelxs.exe'):
                        self.xs.SetValue(paths)
                    if paths.endswith('xprep.exe'):
                        self.xprep.SetValue(paths)
                    if 'sir' in paths:
                        self.sir.SetValue(paths)
                    if (paths.lower()).endswith('xpro.exe'):
                        self.xpro.SetValue(paths)
                    if (paths.lower()).endswith('publcif.exe'):
                        self.publcif.SetValue(paths)
                    if (paths.lower()).endswith('xpx.exe'):
                        self.xp.SetValue(paths)
                    if (paths.lower()).endswith('platon.exe'):
                        self.platon.SetValue(paths)
                    if (paths.lower()).endswith('xshell.exe'):
                        self.xshell5.SetValue(paths)
                    #                if (paths.lower()).endswith('xshell.exe'):
                    #                    self.xshell6.SetValue(paths)
                    if (paths.lower()).endswith('shelxle.exe'):
                        self.shelxle.SetValue(paths)
                    if (paths.lower()).endswith('rasmol.exe'):
                        self.rasmol.SetValue(paths)
                    if (paths.lower()).endswith('olex.exe'):
                        self.olex.SetValue(paths)
                    if (paths.lower()).endswith('xseed.exe'):
                        self.xseed.SetValue(paths)
                    if (paths.lower()).endswith('cell_now.exe'):
                        self.cellnow.SetValue(paths)
                    if (paths.lower()).endswith('sadabs.exe'):
                        self.sadabs.SetValue(paths)
                    if (paths.lower()).endswith('xcif.exe'):
                        self.xcif.SetValue(paths)
                    if (paths.lower()).endswith('mercury.exe'):
                        self.mercury.SetValue(paths)
                    if (paths.lower()).endswith('avogadro.exe'):
                        self.avogadro.SetValue(paths)
                    if (paths.lower()).endswith('pymol.exe'):
                        self.pymol.SetValue(paths)
                    if (paths.lower()).endswith('coot.exe'):
                        self.coot.SetValue(paths)
                    if (paths.lower()).endswith('twinabs.exe'):
                        self.twinabs.SetValue(paths)
                    if (paths.lower()).endswith('drawxtl.exe'):
                        self.drawxtl.SetValue(paths)
                    if (paths.lower()).endswith('jmol.exe'):
                        self.jmol.SetValue(paths)
                    if (paths.lower()).endswith('ortep.exe'):
                        self.ortep3.SetValue(paths)
                    if (paths.lower()).endswith('diamond.exe'):
                        self.diamond.SetValue(paths)
                    if (paths.lower()).endswith('chimera.exe'):
                        self.Chimera.SetValue(paths)
                    if (paths.lower()).endswith('dirdif.exe'):
                        self.dirdif.SetValue(paths)
                    if (paths.lower()).endswith('encifer.exe'):
                        self.enCifer.SetValue(paths)
                    if (paths.lower()).endswith('sxgraph.exe'):
                        self.Sxgraph.SetValue(paths)
                    if (paths.lower()).endswith('xm.exe') or paths.endswith('shelxm.exe'):
                        self.xm.SetValue(paths)
                    if (paths.lower()).endswith('xe.exe') or paths.endswith('shelxe.exe'):
                        self.Sxgraph.SetValue(paths)
                    if (paths.lower()).endswith('xc.exe') or paths.endswith('shelxc.exe'):
                        self.xc.SetValue(paths)
                    if (paths.lower()).endswith('xt.exe') or paths.endswith('shelxt.exe'):
                        self.xt.SetValue(paths)
                    if (paths.lower()).endswith('sf_convert'):
                        self.sfconvert.SetValue(paths)
                    if (paths.lower()).endswith('xabs2'):
                        self.sfconvert.SetValue(paths)
            else:
                dlg = wx.MessageDialog(self, "No supported prorgams were found",
                                       'Info', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

        else:
            if not len(xlist) == 0:
                dialog = wx.MultiChoiceDialog(self, 'Programs found', 'Programs', xlist)
                dialog.SetSelections(range(len(xlist)))
                if (dialog.ShowModal() == wx.ID_OK):
                    lists = dialog.GetSelections()
                    dialog.Destroy()
                    for item in lists:
                        sellist.append(xlist[item])
                for paths in sellist:
                    if paths.endswith('xl') or paths.endswith('shelxl'):
                        self.xl.SetValue(paths)
                    if paths.endswith('xh') or paths.endswith('shelxh'):
                        self.xh.SetValue(paths)
                    if paths.endswith('xs') or paths.endswith('shelxs'):
                        self.xs.SetValue(paths)
                    if paths.endswith('xprep'):
                        self.xprep.SetValue(paths)
                    if 'sir' in paths:
                        self.sir.SetValue(paths)

                    if (paths.lower()).endswith('xpro'):
                        self.xpro.SetValue(paths)
                    if (paths.lower()).endswith('publcif'):
                        self.publcif.SetValue(paths)
                    if (paths.lower()).endswith('xpx'):
                        self.xp.SetValue(paths)
                    if (paths.lower()).endswith('platon'):
                        self.platon.SetValue(paths)
                    if (paths.lower()).endswith('xshell.exe'):
                        self.xshell5.SetValue(paths)
                    if (paths.lower()).endswith('pointless'):
                        self.pointless.SetValue(paths)
                    if (paths.lower()).endswith('shelxle'):
                        self.shelxle.SetValue(paths)
                    if (paths.lower()).endswith('rasmol'):
                        self.rasmol.SetValue(paths)
                    if (paths.lower()).endswith('olex'):
                        self.olex.SetValue(paths)
                    if (paths.lower()).endswith('xseed'):
                        self.xseed.SetValue(paths)
                    if (paths.lower()).endswith('cell_now'):
                        self.cellnow.SetValue(paths)
                    if (paths.lower()).endswith('sadabs'):
                        self.sadabs.SetValue(paths)
                    if (paths.lower()).endswith('xcif'):
                        self.xcif.SetValue(paths)
                    if (paths.lower()).endswith('mercury'):
                        self.mercury.SetValue(paths)
                    if (paths.lower()).endswith('avogadro'):
                        self.avogadro.SetValue(paths)
                    if (paths.lower()).endswith('pymol'):
                        self.pymol.SetValue(paths)
                    if (paths.lower()).endswith('coot'):
                        self.coot.SetValue(paths)
                    if (paths.lower()).endswith('twinabs'):
                        self.twinabs.SetValue(paths)
                    if (paths.lower()).endswith('drawxtl'):
                        self.drawxtl.SetValue(paths)
                    if (paths.lower()).endswith('jmol'):
                        self.jmol.SetValue(paths)
                    if (paths.lower()).endswith('ortep.exe'):
                        self.ortep3.SetValue(paths)
                    if (paths.lower()).endswith('diamond'):
                        self.diamond.SetValue(paths)
                    if (paths.lower()).endswith('chimera'):
                        self.Chimera.SetValue(paths)
                    if (paths.lower()).endswith('dirdif'):
                        self.dirdif.SetValue(paths)
                    if (paths.lower()).endswith('encifer'):
                        self.enCifer.SetValue(paths)
                    if (paths.lower()).endswith('sxgraph'):
                        self.Sxgraph.SetValue(paths)
                    if (paths.lower()).endswith('xm') or paths.endswith('shelxm'):
                        self.xm.SetValue(paths)
                    if (paths.lower()).endswith('xe') or paths.endswith('shelxe'):
                        self.Sxgraph.SetValue(paths)
                    if (paths.lower()).endswith('xc') or paths.endswith('shelxc'):
                        self.xc.SetValue(paths)
                    if (paths.lower()).endswith('xt') or paths.endswith('shelxt'):
                        self.xt.SetValue(paths)
                    if (paths.lower()).endswith('sf_convert'):
                        self.sfconvert.SetValue(paths)
                    if (paths.lower()).endswith('xabs2'):
                        self.sfconvert.SetValue(paths)
            else:
                dlg = wx.MessageDialog(self, "No supported prorgams were found",
                                       'Info', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

    def ontOk(self, event):
        xl = self.xl
        xh = self.xh
        xs = self.xs
        xprep = self.xprep
        xpro = self.xpro
        publcif = self.publcif
        xp = self.xp
        platon = self.platon
        xd = self.xm
        xe = self.xe
        xc = self.xc
        sir = self.sir
        xshell = self.xshell5
        xshell6 = self.xshell6
        shelxle = self.shelxle
        rasmol = self.rasmol
        olex = self.olex
        cellnow = self.cellnow
        sadabs = self.sadabs
        xcif = self.xcif
        mercury = self.mercury
        avogadro = self.avogadro
        pymol = self.pymol
        coot = self.coot

        twinabs = self.twinabs
        drawxtl = self.drawxtl
        jmol = self.jmol
        ortep3 = self.ortep3
        diamond = self.diamond
        chimera = self.Chimera
        dirdif = self.dirdif
        encifer = self.enCifer
        sxgraph = self.Sxgraph
        #saint = self.saint
        wine = self.wine
        anycif = self.anycif
        povray = self.povray
        xt = self.xt
        xseed = self.xseed
        sfconvert = self.sfconvert
        anode = self.anode
        xabs = self.xabs2
        xds = self.xds
        pointless = self.pointless
        aimless = self.aimless
        xds2sad = self.xds2sad

        exobj = {
            'shelxl': xl.GetValue(),
            'shelxh': xh.GetValue(),
            'shelxs': xs.GetValue(),
            'shelxt': xt.GetValue(),
            'shelxd': xd.GetValue(),
            'shelxc': xc.GetValue(),
            'shelxe': xe.GetValue(),
            'xprep': xprep.GetValue(),
            'platon': platon.GetValue(),
            'sir': sir.GetValue(),
            'xpro': xpro.GetValue(),
            'publcif': publcif.GetValue(),
            'xp': xp.GetValue(),
            'xshell5': xshell.GetValue(),
            'xshell6': xshell6.GetValue(),
            'shelxle': shelxle.GetValue(),
            'coot': coot.GetValue(),
            'olex': olex.GetValue(),
            'sadabs': sadabs.GetValue(),
            'xcif': xcif.GetValue(),
            'cellnow': cellnow.GetValue(),
            'xabs': xabs.GetValue(),
            'aimless': aimless.GetValue(),
            'pointless': pointless.GetValue(),
            'xds': xds.GetValue(),
            'mercury': mercury.GetValue(),
            'povray': povray.GetValue(),
            'sfconvert': sfconvert.GetValue(),
            'xseed': xseed.GetValue(),
            'sxgraph': sxgraph.GetValue(),
            'diamond': diamond.GetValue(),
            'encifer': encifer.GetValue(),
            'dirdif': dirdif.GetValue(),
            'pymol': pymol.GetValue(),
            'jmol': jmol.GetValue(),
            'avogadro': avogadro.GetValue(),
            'chimera': chimera.GetValue(),
            'wine': wine.GetValue(),
            #'saint': saint.GetValue(),
            'anode': anode.GetValue(),
            'drawxtl': drawxtl.GetValue(),
            'rasmol': rasmol.GetValue(),
            'anycif': anycif.GetValue(),
            'xds2sad': xds2sad.GetValue(),
            'twinabs': twinabs.GetValue(),
            'ortep3': ortep3.GetValue(),
        }

        json_file = os.path.join(self.path, "user", "external.json")
        json_file_obj = open(json_file, 'w')
        json.dump(exobj, json_file_obj)
        json_file_obj.close()
        dlg = wx.MessageDialog(self, "LinXTL has to be restarted for changes to take place",
                               'Info', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()
        self.Destroy()

    def onwine(self, event):
        dlg = wx.FileDialog(self, "Choose a file", "/usr/bin", "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.wine.SetValue(fnamefull)

    def onanycif(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.anycif.SetValue(fnamefull)

    def onOpenxh(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xh.SetValue(fnamefull)

    def onOpenxs(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xs.SetValue(fnamefull)

    def onanode(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.anode.SetValue(fnamefull)

    def onOpenxabs2(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()
            fnamefull = os.path.join(dirname, fname)
            self.xabs2.SetValue(fnamefull)

    def onOpenxprep(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xprep.SetValue(fnamefull)

    def onsfconvert(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()
            fnamefull = os.path.join(dirname, fname)
            self.sfconvert.SetValue(fnamefull)

    def onOpenxm(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xm.SetValue(fnamefull)

    def onOpenxpro(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xpro.SetValue(fnamefull)

    def onOpenpub(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.publcif.SetValue(fnamefull)

    def onOpenxp(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xp.SetValue(fnamefull)

    def onOpenplaton(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.platon.SetValue(fnamefull)

    def onOpensir(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.sir.SetValue(fnamefull)

    def onxds(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()
            fnamefull = os.path.join(dirname, fname)
            self.xds.SetValue(fnamefull)

    def onaimless(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()
            fnamefull = os.path.join(dirname, fname)
            self.aimless.SetValue(fnamefull)

    def onpointless(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()
            fnamefull = os.path.join(dirname, fname)
            self.pointless.SetValue(fnamefull)

    def onxds2sad(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()
            fnamefull = os.path.join(dirname, fname)
            self.xds2sad.SetValue(fnamefull)

    def onOpenxe(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xe.SetValue(fnamefull)

    def onOpenxc(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xc.SetValue(fnamefull)

    def onOpenxt(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xt.SetValue(fnamefull)

    def onOpenxshell(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xshell5.SetValue(fnamefull)

    def onOpenxshell6(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xshell6.SetValue(fnamefull)

    def onOpenshelxle(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.shelxle.SetValue(fnamefull)

    def onOpenrasmol(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.rasmol.SetValue(fnamefull)

    def onOpenolex(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.olex.SetValue(fnamefull)

    def onOpenxseed(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xseed.SetValue(fnamefull)

    def onOpencellnow(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.cellnow.SetValue(fnamefull)

    def onOpensadabs(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.sadabs.SetValue(fnamefull)

    def onOpenxcif(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.xcif.SetValue(fnamefull)

    def onOpenmercury(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.mercury.SetValue(fnamefull)

    def onOpenavogadro(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.avogadro.SetValue(fnamefull)

    def onOpenpymol(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.pymol.SetValue(fnamefull)

    def onOpencoot(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.coot.SetValue(fnamefull)

    def onTwinabs(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.twinabs.SetValue(fnamefull)

    def onDrawxtl(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.drawxtl.SetValue(fnamefull)

    def onJmol(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.jmol.SetValue(fnamefull)

    def onOrtep3(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.ortep3.SetValue(fnamefull)

    def onDiamond(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.diamond.SetValue(fnamefull)

    def onChimera(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.Chimera.SetValue(fnamefull)

    def onDirdif(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.dirdif.SetValue(fnamefull)

    def onenCifer(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.enCifer.SetValue(fnamefull)

    def onSxgraph(self, event):

        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.Sxgraph.SetValue(fnamefull)

    # def onsaint(self, event):
    #     dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
    #     if dlg.ShowModal() == wx.ID_OK:
    #         dirname = dlg.GetDirectory()
    #         fname = dlg.GetFilename()
    #
    #         fnamefull = os.path.join(dirname, fname)
    #
    #         self.saint.SetValue(fnamefull)

    def onpovray(self, event):
        dlg = wx.FileDialog(self, "Choose a file", os.path.join(self.path, "bin"), "", "*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = dlg.GetDirectory()
            fname = dlg.GetFilename()

            fnamefull = os.path.join(dirname, fname)

            self.povray.SetValue(fnamefull)
        ###############################################################

    def Closeex(self, event):
        self.Destroy()


class onchecklist(wx.Dialog):
    def __init__(self, xlist):
        wx.Dialog.__init__(self, None, -1, 'Tables')
        # begin wxGlade: MyFrame.__init__
        self.xlist = xlist
        self.lpath = []
        self.list_ctrl_1 = wx.CheckListBox(self, -1, wx.DefaultPosition, (500, 500), xlist)
        for x, items in enumerate(xlist):
            self.list_ctrl_1.Check(x, check=True)
        self.OK = wx.Button(self, wx.ID_ANY, ("OK"))
        self.button_3 = wx.Button(self, wx.ID_CANCEL, ("Cancel"))
        self.Bind(wx.EVT_BUTTON, self.onOK, self.OK)
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        self.OK.SetMinSize((90, 40))
        self.button_3.SetMinSize((90, 40))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.list_ctrl_1, 8, wx.EXPAND, 0)
        sizer_3.Add(self.OK, 1, wx.ALL, 5)
        sizer_3.Add((196, 20), 0, wx.EXPAND, 5)
        sizer_3.Add(self.button_3, 1, wx.ALL, 5)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 5)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()

    def onOK(self, event):
        lpath = self.list_ctrl_1.GetCheckedStrings()
        self.lpath = lpath
