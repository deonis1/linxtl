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

try:
    import wx
    import wx.html
except ImportError:
    raise ImportError(
        '%s (need to run "sudo apt-get install python3-wxgtk4.0" or install wxpython package for windows)' % ("wxpython not found"))


import os
import wx.adv
import zipfile
import webbrowser
import sys
import math
import wx.lib.dialogs
import re
import shutil
import subprocess
import json
import definitions
inputfile = sys.argv
import wx.stc
# import wx.html2 as webview
try:
    import wx.stc
    stc_version = int((wx.stc.StyledTextCtrl.GetLibraryVersionInfo().GetVersionString()).split()[1].replace(".",""))
    if stc_version > 321:
        print("Version of Scintilla library is above 3.21, the linxtl might not work properly")
    else:
        print("Version of Scintilla library is", stc_version)
except ImportError:
    raise ImportError(
        '%s (need to run "sudo apt-get install python3-wxgtk4.0" or install wxpython package for windows)' % ("wxpython not found"))


# from python 3 execute replaced by exec(open(filename).read())

ID_TEXT = 103
ID_OPEN = 104
ID_INS = 105
ID_RES = 106
ID_LST = 107
ID_PCF = 108
ID_CIF = 109
ID_Table = 110
ID_Setwd = 111
ID_Openwd = 112
ID_Fntolc = 113
ID_Tar = 114
ID_Cleanfolder = 124
ID_Quit = 117
ID_SELECT = 118
ID_EReport = 119
ID_Search = 120
ID_HtmlTable = 121
ID_EditOc = 122
ID_XP = 123
ID_History = 125
ID_REM = 126
ID_Copyrti = 127
ID_Copyitr = 128
ID_Final = 129
ID_Invers = 130
ID_Reload = 131
ID_Rasmol = 132
ID_Sort = 133
ID_XL = 141
ID_XH = 142
ID_XS = 143
ID_XPREP = 144
ID_SADABS = 145
ID_CELLNOW = 146
ID_XCIF = 147
ID_CIFTAB = 148
ID_XSHELL = 149
ID_XSHELL6 = 150
ID_XPRO = 151
ID_AddSym = 161
ID_HFIX = 162
ID_ORTEP = 163
ID_Pluton = 164
ID_Squeeze = 165
ID_CifVal = 166
ID_GenTbl = 167
ID_Prepare = 168
ID_RXCIF = 169
ID_MShellx = 172
ID_SolvD = 173
ID_Platon = 174
ID_Publ = 175
ID_Delq = 176
ID_Rename = 177
ID_ISOTR = 178
ID_HDEL = 179
ID_Combine = 180
ID_sir = 181
ID_onRefW = 182
ID_oncifcheck = 183
ID_Appendix = 184
ID_onNew = 185
ID_Fullcif = 186
ID_cmolformula = 187
ID_HTMLReport = 188
ID_HTMLCombine = 189
ID_SSADABS = 190
ID_UNRem = 191
ID_prdevices = 192
ID_prUser = 193
ID_elix = 195
ID_prTable = 194
ID_BonAng = 196
ID_Shelxle = 197
ID_external = 198
ID_mercury = 199
ID_avogadro = 200
ID_pymol = 201
ID_coot = 202
ID_tbu = 203
ID_tbu1 = 204
ID_Phenyl = 205
ID_Chloroform = 230
ID_THF = 231
ID_Update = 232
ID_THF2 = 233
ID_Scan = 206
ID_Preview = 207
ID_HTAB = 208
ID_OMIT = 209
ID_PART = 210
ID_HFIX2 = 211
ID_twinabs = 234
ID_drawxtl = 235
ID_jmol = 236
ID_ortep3 = 237
ID_diamond = 238
ID_Chimera = 239

ID_dirdif = 240
ID_encifer = 241
ID_sxgraph = 242
ID_gnomecrystal = 243
ID_xm = 244
ID_xe = 245
ID_xc = 246
ID_stats = 249
ID_supersadabs = 247
ID_unitformula = 248
ID_simple = 250
ID_dublicates = 251
ID_DelHtab = 252
ID_onOlex = 253
ID_reftable = 254
ID_Batch = 255
ID_saint = 256
ID_flat = 257
ID_simu = 258
ID_eadp = 259
ID_ISOR = 260
ID_sadib = 261
ID_sadia = 262
ID_delu = 263
ID_anycif = 264
ID_fonts = 265
ID_qstoc = 266
ID_Delmol = 267
ID_povray = 268
ID_auto = 269
ID_isor = 270
ID_ziprestore = 271
ID_simplesadabs = 272
ID_unitlst = 273
ID_HTMLBOND = 274
ID_Compare = 275
ID_liststructues = 276
ID_splitcif = 277
ID_Phenylb = 278
ID_XT = 279
ID_renamecarbons = 280
ID_garbage = 281
ID_Fullreport = 282
ID_DFIX = 283
ID_CBUTTON = 284
ID_water = 285
ID_miss = 286
ID_INP = 287
ID_onmxmap = 288
ID_xseed = 290
ID_calcslip = 291
ID_calccentr = 292
ID_atomortho = 293
ID_sfconvert = 294
ID_anode = 296
ID_hkllat = 297
ID_editisotr = 298
ID_XABS2 = 299
ID_CODBASE = 300
ID_reloadres = 301
ID_XLR2I = 302
ID_DFIXASITIS = 303
ID_DUBLICATE = 304
ID_DISP = 305
ID_COLLIDE = 306
ID_DICT_TO_SHELX = 307
ID_PERTURB = 308
ID_DELRESI = 309
ID_ADDTRAILER = 310
ID_FCFPLATON = 311
ID_TWIN_1 = 312
ID_TWIN_2 = 313
ID_TWIN_3 = 314
ID_TWIN_4 = 315
ID_MOVE_1 = 316
ID_MOVE_2 = 317
ID_MOVE_3 = 318
ID_MOVE_4 = 319
ID_MOVE_5 = 320
ID_MOVE_6 = 321
ID_MOVE_7 = 322
ID_findresidue = 323
ID_RESI_DIALOG = 324
ID_wmol = 325
global path
path = sys.path[0]
global ossystem
ossystem = sys.platform
sys.path.append(os.path.join(path, "Modules"))
sys.path.append(os.path.join(path, "Modules", "hkllat"))
from colour import colorify
import libcif


class MyFrame(wx.Frame):
    def __init__(self, event, parent, source, *args, **kwds):
        wx.Frame.__init__(self, event, parent, source, *args, **kwds)
        self.path = path
        self.ossystem = ossystem
        self.fnoe = "x"
        self.inputfile = inputfile
        self.clipborddata = ""
        self.extdeclare()
        self.preference()
        self.linenum_t1 = self.linenum_t2 = self.linenum_t3 = self.linenum_t4 = 0
        self.version = " 6.0.1"
        # self.webify = webview.WebView.New(self)
        import icon.icon as ib
        self.SetIcon(ib.icon_linxtl.GetIcon())
        recent = wx.Menu()
        self.filehistory = wx.FileHistory(25)
        self.filehistory.UseMenu(recent)
        self.filehistory.AddFilesToMenu()
        self.config = wx.Config("Linxtl", style=wx.CONFIG_USE_LOCAL_FILE)
        self.filehistory.Load(self.config)
        #        print self.filehistory.Load(self.config)
        self.linenumber = []

        if self.ossystem.startswith("win"):
            self.wildcard = "SHELX file (*.res)|*.res;*.RES|SHELX file (*.ins)|*.ins;*.INS|SHELXC input file (*.inp)|*.inp;*.INP|Reflection file (*.hkl)|*.hkl;*.HKL|hkl2000 input file (*.sca)|*.sca;*.SCA|Crystallographic information file (*.cif)|*.cif;*.CIF|Data collection parameter file (*.p4p)|*.p4p;*.P4P|All Files (*)|*"
        else:
            self.wildcard = "SHELX file (*.res)|*.res;*.RES|SHELX file (*.ins)|*.ins;*.INS|SHELXC input file (*.inp)|*.inp;*.INP|Reflection file (*.hkl)|*.hkl;*.HKL|hkl2000 input file (*.sca)|*.sca;*.SCA|Crystallographic information file (*.cif)|*.cif;*.CIF|Data collection parameter file (*.p4p)|*.p4p;*.P4P|All Files (*)|*"
        self.main_linxtl_menu = wx.MenuBar()
        filem = wx.Menu()
        # wxglade_tmp_menu.Append(ID_onNew, "New\tctrl-n", "", wx.ITEM_NORMAL)
        ########notebook##########################################
        self.notebook_1 = wx.Notebook(self, -1, style=wx.NB_LEFT)
        # self.notebook_1.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT,
        #                                 wx.FONTWEIGHT_NORMAL,
        #                                 wx.FONTSTYLE_NORMAL))
        # self.init_toolbar(event)
        filem.Append(ID_OPEN, "Open\tctrl-o", "", wx.ITEM_NORMAL)
        filem.Append(wx.ID_SAVE, "Save\tctrl-s", "", wx.ITEM_NORMAL)
        filem.Append(wx.ID_SAVEAS, "Save As\tctrl-shift-s", "", wx.ITEM_NORMAL)
        filem.Append(ID_History, "Recent files", recent)
        filem.Append(wx.ID_PRINT, "Print\tctrl-p", "", wx.ITEM_NORMAL)
        filem.Append(ID_Preview, "Print Preview\tctrl-shift-p", "", wx.ITEM_NORMAL)
        filem.AppendSeparator()
        if len(self.phtosfconvert) > 1:
            filem.Append(ID_sfconvert, "Convert with sf_convert", "", wx.ITEM_NORMAL)
        filem.Append(ID_INS, "Edit INS file", "", wx.ITEM_NORMAL)
        filem.Append(ID_RES, "Edit RES file", "", wx.ITEM_NORMAL)
        filem.Append(ID_LST, "Edit LST file", "", wx.ITEM_NORMAL)
        filem.Append(ID_PCF, "Edit PCF file", "", wx.ITEM_NORMAL)
        filem.Append(ID_INP, "Edit INP file", "", wx.ITEM_NORMAL)
        filem.Append(ID_EReport, "Edit TEX report", "", wx.ITEM_NORMAL)
        filem.Append(ID_HTMLReport, "HTML report", "", wx.ITEM_NORMAL)
        filem.Append(ID_HTMLBOND, "Table of bonds and angles", "", wx.ITEM_NORMAL)
        filem.Append(ID_reftable, "Table of refinement parameters", "", wx.ITEM_NORMAL)
        filem.Append(ID_CIF, "Edit CIF file", "", wx.ITEM_NORMAL)
        filem.Append(ID_Table, "Edit publish.cif", "", wx.ITEM_NORMAL)
        filem.Append(ID_povray, "Render povray file", "", wx.ITEM_NORMAL)
        filem.AppendSeparator()
        filem.Append(ID_stats, "Refinement statistics", "", wx.ITEM_NORMAL)
        filem.Append(ID_Setwd, "Set work Dir", "", wx.ITEM_NORMAL)
        filem.Append(ID_Openwd, "Open work Dir\tctrl-shift-d", "", wx.ITEM_NORMAL)
        #        filem.Append(ID_Scan, "Make a List of local Structures", "", wx.ITEM_NORMAL)
        filem.Append(ID_Cleanfolder, "Clean tmp files in the work dir", "", wx.ITEM_NORMAL)
        filem.Append(ID_garbage, "Move not used files", "", wx.ITEM_NORMAL)
        filem.Append(ID_Fntolc, "FILE NAME -> lower case", "", wx.ITEM_NORMAL)
        filem.Append(ID_Rename, "Bulk rename files", "", wx.ITEM_NORMAL)
        filem.Append(ID_liststructues, "List all structures", "", wx.ITEM_NORMAL)
        filem.Append(ID_splitcif, "Split 2013 cif file on res, cif, and hkl", "", wx.ITEM_NORMAL)
        filem.AppendSeparator()
        filem.Append(ID_Tar, "Archive project Zip\talt-a", "", wx.ITEM_NORMAL)
        filem.Append(ID_ziprestore, "Restore backup", "", wx.ITEM_NORMAL)
        filem.AppendSeparator()
        filem.Append(ID_Quit, "Quit\tctrl-q", "", wx.ITEM_NORMAL)
        self.main_linxtl_menu.Append(filem, "File")
        Editm = wx.Menu()
        Editm.Append(wx.ID_UNDO, "Undo\tctrl-z", "", wx.ITEM_NORMAL)
        Editm.Append(wx.ID_REDO, "Redo\tctrl-y", "", wx.ITEM_NORMAL)
        Editm.AppendSeparator()
        Editm.Append(wx.ID_CUT, "Cut\tctrl-x", "", wx.ITEM_NORMAL)
        Editm.Append(wx.ID_COPY, "Copy\tctrl-c", "", wx.ITEM_NORMAL)
        Editm.Append(wx.ID_PASTE, "Paste\tctrl-v", "", wx.ITEM_NORMAL)
        Editm.Append(wx.ID_DELETE, "Delete", "", wx.ITEM_NORMAL)
        Editm.Append(ID_SELECT, "Select all\tctrl-a", "", wx.ITEM_NORMAL)
        Editm.Append(ID_Search, "Search and replace\tctrl-f", "", wx.ITEM_NORMAL)
        Editm.AppendSeparator()
        Editm.Append(ID_DUBLICATE, "Dublicate text \tctrl-d", "", wx.ITEM_NORMAL)
        Editm.Append(ID_ADDTRAILER, "Add trailer to selected atoms\talt-t", "", wx.ITEM_NORMAL)
        Editm.Append(ID_renamecarbons, "Relable atoms\tctrl-l", "", wx.ITEM_NORMAL)
        Editm.AppendSeparator()
        Editm.Append(ID_Delq, "Kill Q peaks\tctrl-k", "", wx.ITEM_NORMAL)
        Editm.Append(ID_HDEL, "Kill H atoms\tctrl-shift-k", "", wx.ITEM_NORMAL)
        Editm.Append(ID_DelHtab, "Kill HTAB instructions", "", wx.ITEM_NORMAL)
        Editm.Append(ID_Delmol, "Kill MOLE instructions", "", wx.ITEM_NORMAL)
        Editm.Append(ID_DELRESI, "Kill RESI instructions", "", wx.ITEM_NORMAL)
        Editm.Append(ID_REM, "Comment\tctrl-[", "", wx.ITEM_NORMAL)
        Editm.Append(ID_UNRem, "UnComment\tctrl-]", "", wx.ITEM_NORMAL)
        self.main_linxtl_menu.Append(Editm, "Edit")
        optionsm = wx.Menu()
        optionsm.Append(ID_unitformula, "Get Molecular Formula", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_unitlst, "Correct molecular formula", "", wx.ITEM_NORMAL)
        optionsm.AppendSeparator()
        optionsm.Append(ID_ISOTR, "Isotropic\tctrl-i", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_editisotr, "Change U(iso)", "", wx.ITEM_NORMAL)
        optionsm.AppendSeparator()
        optionsm.Append(ID_OMIT, "OMIT reflections with ERROR/ESD>9", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_DISP, "Calculate DISP", "", wx.ITEM_NORMAL)
        optionsm.AppendSeparator()
        optionsm.Append(ID_HFIX2, "HFIX\talt-h", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_Sort, "Sort Atoms\talt-s", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_dublicates, "Find Dublicate Labels\talt-d", "", wx.ITEM_NORMAL)
        # optionsm.Append(ID_findresidue, "Find Residues", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_qstoc, "Assign Q as Carbons", "", wx.ITEM_NORMAL)
        optionsm.AppendSeparator()
        optionsm.Append(ID_Final, "Finalize refinement", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_onRefW, "Weight refinement\tctrl-w", "", wx.ITEM_NORMAL)
        optionsm.AppendSeparator()
        optionsm.Append(ID_Reload, "Reload current file\tF5", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_Copyitr, "Copy ins to res\tshift-ctrl-i", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_Copyrti, "Copy res to ins\tshift-ctrl-r", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_XLR2I, "Copy res to ins and refine \tctrl-r", "", wx.ITEM_NORMAL)
        optionsm.Append(ID_reloadres, "Load RES file\tctrl-F5", "", wx.ITEM_NORMAL)
        self.main_linxtl_menu.Append(optionsm, "Options")
        toolsm = wx.Menu()
        if len(self.phtoxl) > 1:
            toolsm.Append(ID_XL, "XL\tctrl-t", "", wx.ITEM_NORMAL)
        if len(self.phtoxh) > 1:
            toolsm.Append(ID_XH, "XH\tctrl-h", "", wx.ITEM_NORMAL)
        if len(self.phtoxs) > 1:
            toolsm.Append(ID_XS, "XS", "", wx.ITEM_NORMAL)
        if len(self.phtoxp) > 1:
            toolsm.Append(ID_XP, "XP\tF2", "", wx.ITEM_NORMAL)
        if len(self.phtoxt) > 1:
            toolsm.Append(ID_XT, "XT", "", wx.ITEM_NORMAL)
        if len(self.phtoxc) > 1:
            toolsm.Append(ID_xc, "XC", "", wx.ITEM_NORMAL)
        if len(self.phtoxm) > 1:
            toolsm.Append(ID_xm, "XD", "", wx.ITEM_NORMAL)
        if len(self.phtoxe) > 1:
            toolsm.Append(ID_xe, "XE", "", wx.ITEM_NORMAL)
        if len(self.phtoanode) > 1:
            toolsm.Append(ID_anode, "Anode", "", wx.ITEM_NORMAL)
        toolsm.AppendSeparator()
        # toolsm.Append(ID_saint, "SAINTGUI", "", wx.ITEM_NORMAL)
        toolsm.Append(ID_onmxmap, "MX_MAP", "", wx.ITEM_NORMAL)
        toolsm.Append(ID_hkllat, "HKLLAT", "", wx.ITEM_NORMAL)
        toolsm.Append(ID_CODBASE, "CODBASE", "", wx.ITEM_NORMAL)
        toolsm.Append(ID_simplesadabs, "SIMPLESADABS", "", wx.ITEM_NORMAL)
        toolsm.Append(ID_wmol, "WMOL", "", wx.ITEM_NORMAL)
        toolsm.AppendSeparator()
        if len(self.phtosadabs) > 1:
            toolsm.Append(ID_SADABS, "SADABS", "", wx.ITEM_NORMAL)
        if len(self.phtotwinabs) > 1:
            toolsm.Append(ID_twinabs, "TWINABS", "", wx.ITEM_NORMAL)
        if len(self.phtoxabs) > 1:
            toolsm.Append(ID_XABS2, "XABS2", "", wx.ITEM_NORMAL)
        if len(self.phtoxprep) > 1:
            toolsm.Append(ID_XPREP, "XPREP", "", wx.ITEM_NORMAL)
        if len(self.phtocellnow) > 1:
            toolsm.Append(ID_CELLNOW, "CELL_NOW", "", wx.ITEM_NORMAL)
        toolsm.AppendSeparator()
        if len(self.phtoxcif) > 1:
            toolsm.Append(ID_XCIF, "XCIF", "", wx.ITEM_NORMAL)
        if len(self.phtosir) > 1:
            toolsm.Append(ID_sir, "Sir", "", wx.ITEM_NORMAL)
        if len(self.phtoxshell) > 1:
            toolsm.Append(ID_XSHELL, "XSHELL\tF3", "", wx.ITEM_NORMAL)
        if len(self.phtoolex) > 1:
            toolsm.Append(ID_onOlex, "Olex \tF9", "", wx.ITEM_NORMAL)
        if len(self.phtoxshell6) > 1:
            toolsm.Append(ID_XSHELL6, "XSHELL 6\tF4", "", wx.ITEM_NORMAL)
        if len(self.phtoshelxle) > 1:
            toolsm.Append(ID_Shelxle, "Shelxle\tF6", "", wx.ITEM_NORMAL)
        if len(self.phtorasmol) > 1:
            toolsm.Append(ID_Rasmol, "RASMOL\tF8", "", wx.ITEM_NORMAL)

        if len(self.phtoxpro) > 1:
            toolsm.Append(ID_XPRO, "XPRO", "", wx.ITEM_NORMAL)
        if len(self.phtopublcif) > 1:
            toolsm.Append(ID_Publ, "PublCif", "", wx.ITEM_NORMAL)
        if len(self.phtoavogadro) > 1:
            toolsm.Append(ID_avogadro, "Avogadro", "", wx.ITEM_NORMAL)
        if len(self.phtopymol) > 1:
            toolsm.Append(ID_pymol, "PyMol", "", wx.ITEM_NORMAL)
        if len(self.phtomercury) > 1:
            toolsm.Append(ID_mercury, "Mercury", "", wx.ITEM_NORMAL)
        if len(self.phtocoot) > 1:
            toolsm.Append(ID_coot, "Coot\tF7", "", wx.ITEM_NORMAL)
        if len(self.phtodrawxtl) > 1:
            toolsm.Append(ID_drawxtl, "DrawXTL", "", wx.ITEM_NORMAL)
        if len(self.phtojmol) > 1:
            toolsm.Append(ID_jmol, "Jmol", "", wx.ITEM_NORMAL)
        if len(self.phtoortep3) > 1:
            toolsm.Append(ID_ortep3, "Ortep3", "", wx.ITEM_NORMAL)
        if len(self.phtodrawxtl) > 1:
            toolsm.Append(ID_drawxtl, "DrawXtl", "", wx.ITEM_NORMAL)
        if len(self.phtodiamond) > 1:
            toolsm.Append(ID_diamond, "Diamond", "", wx.ITEM_NORMAL)
        if len(self.phtochimera) > 1:
            toolsm.Append(ID_Chimera, "Chimera", "", wx.ITEM_NORMAL)
            # if len(self.phtosupersadabs)>1:
        #       toolsm.Append(ID_supersadabs, "Supersdabs", "", wx.ITEM_NORMAL)
        if len(self.phtodirdif) > 1:
            toolsm.Append(ID_dirdif, "DirDif", "", wx.ITEM_NORMAL)
        if len(self.phtoencifer) > 1:
            toolsm.Append(ID_encifer, "enCifer", "", wx.ITEM_NORMAL)
        if len(self.phtosxgraph) > 1:
            toolsm.Append(ID_sxgraph, "Sxgraph", "", wx.ITEM_NORMAL)
        if len(self.phtoxseed) > 1:
            toolsm.Append(ID_xseed, "XSeed", "", wx.ITEM_NORMAL)
        if len(self.phtoanycif) > 1:
            anyciff = os.path.basename(self.phtoanycif)
            toolsm.Append(ID_anycif, str(anyciff), "", wx.ITEM_NORMAL)

        self.main_linxtl_menu.Append(toolsm, "Tools")
        if len(self.phtoplaton) > 1:
            platonm = wx.Menu()
            platonm.Append(ID_Platon, "Platon", "", wx.ITEM_NORMAL)
            platonm.Append(ID_ORTEP, "Ortep", "", wx.ITEM_NORMAL)
            # platonm.Append(ID_Pluton, "Pluton", "", wx.ITEM_NORMAL)
            platonm.Append(ID_FCFPLATON, "Validate FCF", "", wx.ITEM_NORMAL)
            platonm.AppendSeparator()
            platonm.Append(ID_AddSym, "Add Sym-SXL", "", wx.ITEM_NORMAL)
            platonm.Append(ID_HFIX, "HFIX", "", wx.ITEM_NORMAL)
            platonm.Append(ID_Squeeze, "Squeeze", "", wx.ITEM_NORMAL)
            #            platonm.Append(ID_CifVal, "CIF-Validation", "", wx.ITEM_NORMAL)
            self.main_linxtl_menu.Append(platonm, "Platon")
        imp = wx.Menu()
        imp.Append(ID_THF, 'THF: full disorder')
        imp.Append(ID_THF2, 'THF: only carbons')
        imp.Append(ID_Phenyl, 'Phenyl: 6 atoms')
        imp.Append(ID_Phenylb, 'Phenyl: rotational 5 atoms')
        imp.Append(ID_tbu, 'tBu/CF3 rotational disorder')
        dis = wx.Menu()
        dis.Append(ID_EditOc, "Set atomic occupancy factor\tctrl-e", "", wx.ITEM_NORMAL)
        dis.Append(ID_PART, "Split into parts", "", wx.ITEM_NORMAL)
        dis.AppendSeparator()
        dis.Append(ID_flat, 'Apply FLAT')
        dis.Append(ID_delu, '           DELU')
        dis.Append(ID_simu, '           SIMU')
        dis.Append(ID_eadp, '           EADP')
        dis.Append(ID_isor, '           ISOR')
        dis.Append(ID_DFIX, '           DFIX')
        dis.Append(ID_sadib, '           SADI for bonds')
        dis.Append(ID_sadia, '           SADI for angles')
        dis.Append(ID_DFIXASITIS, 'DFIX as it is')
        dis.AppendSeparator()
        dis.Append(ID_miss, 'Check for atom label mismatch')
        dis.Append(ID_water, 'Water refinment')
        dis.Append(ID_PERTURB, 'Perturb coordinates')
        dis.Append(ID_COLLIDE, 'FREE Collision')
        dis.Append(ID_DICT_TO_SHELX, 'CIF constraints to shelx')
        dis.Append(wx.ID_ANY, 'Restraints for', imp)
        dis.Append(ID_RESI_DIALOG, "Go to Residue\tctrl-g", "", wx.ITEM_NORMAL)
        self.main_linxtl_menu.Append(dis, "Disorder")

        transform = wx.Menu()
        twin = wx.Menu()
        twin.Append(ID_TWIN_1, "Twinning by merohedry; trigonal, tetragonal, hexagonal, cubic", "", wx.ITEM_NORMAL)
        twin.Append(ID_TWIN_2, "Monoclinic with beta ~ 90", "", wx.ITEM_NORMAL)
        twin.Append(ID_TWIN_3, "Monoclinic a~c beta ~ 120", "", wx.ITEM_NORMAL)
        twin.Append(ID_TWIN_4, "Rhombohedral obverse/reverse", "", wx.ITEM_NORMAL)
        transform.Append(wx.ID_ANY, 'Twin', twin)

        move = wx.Menu()

        move.Append(ID_Invers, "Invert the strucure", "", wx.ITEM_NORMAL)
        move.Append(ID_MOVE_1, "Invert for Fdd2", "", wx.ITEM_NORMAL)
        move.Append(ID_MOVE_2, "Invert for I41cd", "", wx.ITEM_NORMAL)
        move.Append(ID_MOVE_3, "Invert for I41", "", wx.ITEM_NORMAL)
        move.Append(ID_MOVE_4, "Invert for I42d", "", wx.ITEM_NORMAL)
        move.Append(ID_MOVE_5, "Invert for I4122", "", wx.ITEM_NORMAL)
        move.Append(ID_MOVE_6, "Invert for F4132", "", wx.ITEM_NORMAL)
        move.Append(ID_MOVE_7, "Invert for I41md", "", wx.ITEM_NORMAL)

        transform.Append(wx.ID_ANY, 'Move', move)

        self.main_linxtl_menu.Append(transform, "Transform")

        reportm = wx.Menu()
        # reportm.Append(ID_GenTbl, "Generate Table for Publiction txt", "", wx.ITEM_NORMAL)
        reportm.Append(ID_Prepare, "Prepare cif for publication", "", wx.ITEM_NORMAL)
        # reportm.Append(ID_Appendix, "Generate Report", "", wx.ITEM_NORMAL)
        reportm.Append(ID_BonAng, "Get bonds and angles", "", wx.ITEM_NORMAL)
        reportm.Append(ID_HtmlTable, "Table of refinement parameters (rtf)", "", wx.ITEM_NORMAL)
        reportm.AppendSeparator()
        reportm.Append(ID_simple, "Create simple cif (no hkl)", "", wx.ITEM_NORMAL)
        if len(self.phtoxcif) > 1:
            reportm.Append(ID_RXCIF, "Rapid report with xcif", "", wx.ITEM_NORMAL)
        reportm.Append(ID_oncifcheck, "CheckCIF (web)", "", wx.ITEM_NORMAL)
        calcs = wx.Menu()
        calcs.Append(ID_calcslip, "Ring slippage (X,Y) - beta", "", wx.ITEM_NORMAL)
        calcs.Append(ID_calccentr, "Centroid", "", wx.ITEM_NORMAL)
        calcs.Append(ID_atomortho, "Calculate orthogonal coordinates", "", wx.ITEM_NORMAL)
        reportm.Append(-1, "Calculate", calcs)
        reportm.AppendSeparator()
        reportm.Append(ID_Combine, "Combine several cif files", "", wx.ITEM_NORMAL)
        reportm.Append(ID_HTMLCombine, "Combine several HTML reports", "", wx.ITEM_NORMAL)
        reportm.AppendSeparator()
        reportm.Append(ID_Fullreport, "Full report", "", wx.ITEM_NORMAL)
        reportm.Append(ID_Batch, "Batch processing", "", wx.ITEM_NORMAL)
        self.main_linxtl_menu.Append(reportm, "Report")
        prefm = wx.Menu()
        prefm.Append(ID_external, "External Programs", "", wx.ITEM_NORMAL)
        #        prefm.Append(ID_CBUTTON, "Custom Button", "", wx.ITEM_NORMAL)
        prefm.Append(ID_prdevices, "Edit Device properties", "", wx.ITEM_NORMAL)
        prefm.Append(ID_prUser, "Edit User informations", "", wx.ITEM_NORMAL)
        prefm.Append(ID_prTable, "Edit table of refinement parameters", "", wx.ITEM_NORMAL)
        prefm.Append(ID_Update, "Update Linxtl", "", wx.ITEM_NORMAL)
        self.main_linxtl_menu.Append(prefm, "Preferences")
        aboutm = wx.Menu()
        aboutm.Append(wx.ID_ABOUT, "About LinXTL\tF1", "", wx.ITEM_NORMAL)
        aboutm.Append(ID_MShellx, "Manual SHELX", "", wx.ITEM_NORMAL)
        aboutm.Append(ID_SolvD, "Solving Disorder", "", wx.ITEM_NORMAL)
        self.main_linxtl_menu.Append(aboutm, "Help")
        self.SetMenuBar(self.main_linxtl_menu)
        self.frame_1_statusbar = self.CreateStatusBar(1, wx.CAPTION | wx.ALL, 1)
        self.frame_1_statusbar.SetFieldsCount(2)
        self.frame_1_statusbar.SetStatusWidths([-1, 200])
        #        self.frame_1_statusbar.SetMinHeight(500)
        self.frame_1_statusbar.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.OPEN = wx.Button(self, -1, " Open ")
        self.OPEN.SetBackgroundColour(wx.Colour(237, 237, 237))
        self.SAVE = wx.Button(self, -1, " Save ")
        self.SAVE.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoxprep) > 1:
            self.XPREP = wx.Button(self, -1, " XPREP ")
            self.XPREP.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoxt) > 1:
            self.XT = wx.Button(self, -1, " XT")
            self.XT.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoxs) > 1:
            self.XS = wx.Button(self, -1, " XS ")
            self.XS.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoxl) > 1:
            self.XL = wx.Button(self, -1, " R2I XL ")
            self.XL.SetBackgroundColour(wx.Colour(237, 237, 237))
            self.XL.SetToolTip(wx.ToolTip("Copy res to ins and refine ctrl+R"))
        if len(self.phtoxp) > 1:
            self.XP = wx.Button(self, -1, "XP")
            self.XP.SetBackgroundColour(wx.Colour(237, 237, 237))
        self.wmolbutton = wx.Button(self, -1, "WMOL")
        self.wmolbutton.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoxshell) > 1:
            self.Xshell = wx.Button(self, -1, " Xshell ")
            self.Xshell.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoolex) > 1:
            self.olex = wx.Button(self, -1, " Olex ")
            self.olex.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoxshell6) > 1:
            self.Xshell6 = wx.Button(self, -1, " Xshell6 ")
            self.Xshell6.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoshelxle) > 1:
            self.onshelxle = wx.Button(self, -1, " Shelxle ")
            self.onshelxle.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtosxgraph) > 1:
            self.sxgraph = wx.Button(self, -1, " Sxgraph ")
            self.sxgraph.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtoxseed) > 1:
            self.xseed = wx.Button(self, -1, " XSeed ")
            self.xseed.SetBackgroundColour(wx.Colour(237, 237, 237))
        if len(self.phtocoot) > 1:
            self.coot = wx.Button(self, -1, " Coot ")
            self.coot.SetBackgroundColour(wx.Colour(237, 237, 237))
        self.restoins = wx.Button(self, -1, " Refresh ")
        self.restoins.SetBackgroundColour(wx.Colour(237, 237, 237))
        self.restoins.SetToolTip(wx.ToolTip("Reload current file"))
        self.SetBackgroundColour(wx.Colour(245, 245, 245))
        from stcclass import stcwindow
        self.text = stcwindow(self.notebook_1, self.fsg, self.main_font)
        self.text2 = stcwindow(self.notebook_1, self.fsg, self.main_font)
        self.text3 = stcwindow(self.notebook_1, self.fsg, self.main_font)
        self.text4 = stcwindow(self.notebook_1, self.fsg, self.main_font)
        self.text.SetMarginWidth(2, 0)
        self.text.SetMarginWidth(1, 0)
        self.text.SetMarginWidth(0, 0)
        self.text.SetMarginLeft(10)
        self.text2.SetMarginLeft(10)
        self.text3.SetMarginLeft(10)
        self.text4.SetMarginLeft(10)
        #        self.text.SetCaretLineBackground(wx.Colour(100,153,203))
        self.__set_properties()
        ###############Setting Work Dir############################

        if os.path.exists(os.path.join(self.path, "workdir")) == True:
            tmpf = open(os.path.join(self.path, "workdir"), 'r')
            self.dirname = tmpf.read()
            #            print self.dirname
            tmpf.close()
        else:
            self.dirname = ''

        self.__do_layout(event)
        #        self.Bind(wx.EVT_MENU, self.onNew, id=ID_onNew)
        self.Bind(wx.EVT_MENU, self.onOpen, id=ID_OPEN)
        self.Bind(wx.EVT_MENU, self.onSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.onSaveAs, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU_RANGE, self.on_file_history, id=wx.ID_FILE1, id2=wx.ID_FILE9)
        self.Bind(wx.EVT_MENU, self.onPrint, id=wx.ID_PRINT)
        self.Bind(wx.EVT_MENU, self.OnPrintPreview, id=ID_Preview)
        self.Bind(wx.EVT_MENU, self.onINS, id=ID_INS)
        self.Bind(wx.EVT_MENU, self.onINP, id=ID_INP)
        self.Bind(wx.EVT_MENU, self.onRes, id=ID_RES)
        self.Bind(wx.EVT_MENU, self.onHTMLBOND, id=ID_HTMLBOND)
        self.Bind(wx.EVT_MENU, self.onLST, id=ID_LST)
        self.Bind(wx.EVT_MENU, self.onEReport, id=ID_EReport)
        self.Bind(wx.EVT_MENU, self.onHTMLReport, id=ID_HTMLReport)
        self.Bind(wx.EVT_MENU, self.onPCF, id=ID_PCF)
        self.Bind(wx.EVT_MENU, self.onCif, id=ID_CIF)
        self.Bind(wx.EVT_MENU, self.reftable, id=ID_reftable)
        self.Bind(wx.EVT_MENU, self.onTable, id=ID_Table)
        self.Bind(wx.EVT_MENU, self.onSetwd, id=ID_Setwd)
        self.Bind(wx.EVT_MENU, self.onOpenwd, id=ID_Openwd)
        self.Bind(wx.EVT_MENU, self.onFntolc, id=ID_Fntolc)
        self.Bind(wx.EVT_MENU, self.onpovray, id=ID_povray)
        # self.Bind(wx.EVT_MENU, self.onscan, id=ID_Scan)
        self.Bind(wx.EVT_MENU, self.ziprestore, id=ID_ziprestore)
        self.Bind(wx.EVT_MENU, self.onTar, id=ID_Tar)
        self.Bind(wx.EVT_MENU, self.onRename, id=ID_Rename)
        self.Bind(wx.EVT_MENU, self.onCleanfolder, id=ID_Cleanfolder)
        self.Bind(wx.EVT_MENU, self.garbage, id=ID_garbage)
        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_Quit)
        self.Bind(wx.EVT_CLOSE, self.onCloselin)
        self.Bind(wx.EVT_MENU, self.onUndo, id=wx.ID_UNDO)
        self.Bind(wx.EVT_MENU, self.onRedu, id=wx.ID_REDO)
        self.Bind(wx.EVT_MENU, self.onCut, id=wx.ID_CUT)
        self.Bind(wx.EVT_MENU, self.onCopy, id=wx.ID_COPY)
        self.Bind(wx.EVT_MENU, self.onPaste, id=wx.ID_PASTE)
        self.Bind(wx.EVT_MENU, self.onDelete, id=wx.ID_DELETE)
        self.Bind(wx.EVT_MENU, self.onSELECT, id=ID_SELECT)
        self.Bind(wx.EVT_MENU, self.onSearch, id=ID_Search)
        self.Bind(wx.EVT_MENU, self.onEditOc, id=ID_EditOc)
        self.Bind(wx.EVT_MENU, self.molformula, id=ID_cmolformula)
        self.Bind(wx.EVT_MENU, self.getMolForm, id=ID_unitformula)
        self.Bind(wx.EVT_MENU, self.getunitlst, id=ID_unitlst)
        self.Bind(wx.EVT_MENU, self.onDelq, id=ID_Delq)
        self.Bind(wx.EVT_MENU, self.HDEL, id=ID_HDEL)
        self.Bind(wx.EVT_MENU, self.Delmol, id=ID_Delmol)
        self.Bind(wx.EVT_MENU, self.delresi, id=ID_DELRESI)
        self.Bind(wx.EVT_MENU, self.editisotr, id=ID_editisotr)
        self.Bind(wx.EVT_MENU, self.ISOR, id=ID_ISOR)
        self.Bind(wx.EVT_MENU, self.ISOTR, id=ID_ISOTR)
        self.Bind(wx.EVT_MENU, self.DELU, id=ID_delu)
        self.Bind(wx.EVT_MENU, self.SIMU, id=ID_simu)
        self.Bind(wx.EVT_MENU, self.SADIb, id=ID_sadib)
        self.Bind(wx.EVT_MENU, self.SADIa, id=ID_sadia)
        self.Bind(wx.EVT_MENU, self.water, id=ID_water)
        self.Bind(wx.EVT_MENU, self.onISOR, id=ID_isor)
        self.Bind(wx.EVT_MENU, self.EADP, id=ID_eadp)
        self.Bind(wx.EVT_MENU, self.FLAT, id=ID_flat)
        self.Bind(wx.EVT_MENU, self.DFIX, id=ID_DFIX)
        self.Bind(wx.EVT_MENU, self.qstoc, id=ID_qstoc)
        self.Bind(wx.EVT_MENU, self.missmatch, id=ID_miss)
        self.Bind(wx.EVT_MENU, self.DelHtab, id=ID_DelHtab)
        self.Bind(wx.EVT_MENU, self.ontBu, id=ID_tbu)
        self.Bind(wx.EVT_MENU, self.onPhenyl, id=ID_Phenyl)
        self.Bind(wx.EVT_MENU, self.ondublicates, id=ID_dublicates)
        self.Bind(wx.EVT_MENU, self.onTHF, id=ID_THF)
        self.Bind(wx.EVT_MENU, self.onTHF2, id=ID_THF2)
        self.Bind(wx.EVT_MENU, self.onParts, id=ID_PART)
        self.Bind(wx.EVT_MENU, self.onRefW, id=ID_onRefW)
        self.Bind(wx.EVT_MENU, self.onBonAng, id=ID_BonAng)
        self.Bind(wx.EVT_MENU, self.onRem, id=ID_REM)
        self.Bind(wx.EVT_MENU, self.onUNRem, id=ID_UNRem)
        self.Bind(wx.EVT_MENU, self.onCopyrti, id=ID_Copyrti)
        self.Bind(wx.EVT_MENU, self.onCopyitr, id=ID_Copyitr)
        self.Bind(wx.EVT_MENU, self.onFinal, id=ID_Final)
        self.Bind(wx.EVT_MENU, self.onHTAB, id=ID_HTAB)
        self.Bind(wx.EVT_MENU, self.onHFIX2, id=ID_HFIX2)
        self.Bind(wx.EVT_MENU, self.onOMIT, id=ID_OMIT)
        self.Bind(wx.EVT_MENU, self.onInvers, id=ID_Invers)
        self.Bind(wx.EVT_MENU, self.onSort, id=ID_Sort)
        self.Bind(wx.EVT_MENU, self.renamecarbons, id=ID_renamecarbons)
        self.Bind(wx.EVT_MENU, self.onReload, id=ID_Reload)
        self.Bind(wx.EVT_MENU, self.onXL, id=ID_XL)
        self.Bind(wx.EVT_MENU, self.onXH, id=ID_XH)
        self.Bind(wx.EVT_MENU, self.onXS, id=ID_XS)
        self.Bind(wx.EVT_MENU, self.onRasmol, id=ID_Rasmol)
        self.Bind(wx.EVT_MENU, self.onXP, id=ID_XP)
        self.Bind(wx.EVT_MENU, self.onXPREP, id=ID_XPREP)
        self.Bind(wx.EVT_MENU, self.onXT, id=ID_XT)
        self.Bind(wx.EVT_MENU, self.shelxle, id=ID_Shelxle)
        self.Bind(wx.EVT_MENU, self.onSADABS, id=ID_SADABS)
        self.Bind(wx.EVT_MENU, self.onXABS2, id=ID_XABS2)
        self.Bind(wx.EVT_MENU, self.onCELLNOW, id=ID_CELLNOW)
        self.Bind(wx.EVT_MENU, self.onXCIF, id=ID_XCIF)
        self.Bind(wx.EVT_MENU, self.onxm, id=ID_xm)
        self.Bind(wx.EVT_MENU, self.onxe, id=ID_xe)
        self.Bind(wx.EVT_MENU, self.onxc, id=ID_xc)
        self.Bind(wx.EVT_MENU, self.onOlex, id=ID_onOlex)
        self.Bind(wx.EVT_MENU, self.onsir, id=ID_sir)
        self.Bind(wx.EVT_MENU, self.onXSHELL, id=ID_XSHELL)
        self.Bind(wx.EVT_MENU, self.onXSHELL6, id=ID_XSHELL6)
        self.Bind(wx.EVT_MENU, self.onXPRO, id=ID_XPRO)
        self.Bind(wx.EVT_MENU, self.onPubl, id=ID_Publ)
        self.Bind(wx.EVT_MENU, self.onAddSym, id=ID_AddSym)
        self.Bind(wx.EVT_MENU, self.onHFIX, id=ID_HFIX)
        self.Bind(wx.EVT_MENU, self.onelix, id=ID_elix)
        self.Bind(wx.EVT_MENU, self.onORTEP, id=ID_ORTEP)
        self.Bind(wx.EVT_MENU, self.onFCFVALIDATE, id=ID_FCFPLATON)
        self.Bind(wx.EVT_MENU, self.onPlaton, id=ID_Platon)
        self.Bind(wx.EVT_MENU, self.onSqueeze, id=ID_Squeeze)
        self.Bind(wx.EVT_MENU, self.onCifVal, id=ID_CifVal)
        self.Bind(wx.EVT_MENU, self.oncifcheck, id=ID_oncifcheck)
        self.Bind(wx.EVT_MENU, self.onRXCIF, id=ID_RXCIF)
        self.Bind(wx.EVT_MENU, self.onPrpare, id=ID_Prepare)
        self.Bind(wx.EVT_MENU, self.Fullreport, id=ID_Fullreport)
        self.Bind(wx.EVT_MENU, self.onelix, id=ID_elix)
        self.Bind(wx.EVT_MENU, self.Combine, id=ID_Combine)
        self.Bind(wx.EVT_MENU, self.HTMLCombine, id=ID_HTMLCombine)
        # self.Bind(wx.EVT_MENU, self.Appendix, id=ID_Appendix)
        self.Bind(wx.EVT_MENU, self.Fullcif, id=ID_Fullcif)
        self.Bind(wx.EVT_MENU, self.onAbout, id=wx.ID_ABOUT)
        self.Bind(wx.EVT_MENU, self.onMShellx, id=ID_MShellx)
        self.Bind(wx.EVT_MENU, self.onHtmlTable, id=ID_HtmlTable)
        self.Bind(wx.EVT_MENU, self.onSolvD, id=ID_SolvD)
        self.Bind(wx.EVT_BUTTON, self.onOpen, self.OPEN)
        self.Bind(wx.EVT_BUTTON, self.onSave, self.SAVE)
        self.Bind(wx.EVT_MENU, self.external, id=ID_external)
        self.Bind(wx.EVT_MENU, self.prdevices, id=ID_prdevices)
        self.Bind(wx.EVT_MENU, self.onUpdate, id=ID_Update)
        self.Bind(wx.EVT_MENU, self.pruser, id=ID_prUser)
        self.Bind(wx.EVT_MENU, self.prtable, id=ID_prTable)
        self.Bind(wx.EVT_MENU, self.onMercury, id=ID_mercury)
        self.Bind(wx.EVT_MENU, self.onAvogadro, id=ID_avogadro)
        self.Bind(wx.EVT_MENU, self.onPyMol, id=ID_pymol)
        self.Bind(wx.EVT_MENU, self.ontwinabs, id=ID_twinabs)
        self.Bind(wx.EVT_MENU, self.ondrawxtl, id=ID_drawxtl)
        self.Bind(wx.EVT_MENU, self.onjmol, id=ID_jmol)
        self.Bind(wx.EVT_MENU, self.onortep3, id=ID_ortep3)
        self.Bind(wx.EVT_MENU, self.ondiamond, id=ID_diamond)
        self.Bind(wx.EVT_MENU, self.onChimera, id=ID_Chimera)
        self.Bind(wx.EVT_MENU, self.onCoot, id=ID_coot)
        self.Bind(wx.EVT_MENU, self.onsupersadabs, id=ID_supersadabs)
        self.Bind(wx.EVT_MENU, self.ondirdif, id=ID_dirdif)
        self.Bind(wx.EVT_MENU, self.onenCifer, id=ID_encifer)
        self.Bind(wx.EVT_MENU, self.onsxgraph, id=ID_sxgraph)
        # self.Bind(wx.EVT_MENU, self.onSaint, id=ID_saint)
        self.Bind(wx.EVT_MENU, self.stats, id=ID_stats)
        self.Bind(wx.EVT_MENU, self.onPhenylb, id=ID_Phenylb)
        self.Bind(wx.EVT_MENU, self.Batch, id=ID_Batch)
        self.Bind(wx.EVT_MENU, self.simplecif, id=ID_simple)
        self.Bind(wx.EVT_MENU, self.calcslip, id=ID_calcslip)
        self.Bind(wx.EVT_MENU, self.calccentr, id=ID_calccentr)
        self.Bind(wx.EVT_MENU, self.calcorttho, id=ID_atomortho)
        self.Bind(wx.EVT_MENU, self.onsfconvert, id=ID_sfconvert)
        self.Bind(wx.EVT_MENU, self.anycif, id=ID_anycif)
        self.Bind(wx.EVT_MENU, self.onfonts, id=ID_fonts)
        #        self.Bind(wx.EVT_MENU, self.onauto, id=ID_auto)
        self.Bind(wx.EVT_MENU, self.onSimpleSadabs, id=ID_simplesadabs)
        self.Bind(wx.EVT_MENU, self.onliststructues, id=ID_liststructues)
        self.Bind(wx.EVT_MENU, self.splitcif, id=ID_splitcif)
        self.Bind(wx.EVT_MENU, self.onmxmap, id=ID_onmxmap)
        self.Bind(wx.EVT_MENU, self.onxseed, id=ID_xseed)
        self.Bind(wx.EVT_MENU, self.onanode, id=ID_anode)
        self.Bind(wx.EVT_MENU, self.onhkllat, id=ID_hkllat)
        self.Bind(wx.EVT_MENU, self.CODBASE, id=ID_CODBASE)
        self.Bind(wx.EVT_MENU, self.onReloadRes, id=ID_reloadres)
        self.Bind(wx.EVT_MENU, self.onXLR2I, id=ID_XLR2I)
        self.Bind(wx.EVT_MENU, self.onDFIXASIS, id=ID_DFIXASITIS)
        self.Bind(wx.EVT_MENU, self.ondublicate, id=ID_DUBLICATE)
        self.Bind(wx.EVT_MENU, self.onDISP, id=ID_DISP)
        self.Bind(wx.EVT_MENU, self.oncollide, id=ID_COLLIDE)
        self.Bind(wx.EVT_MENU, self.cifdicttoshelx, id=ID_DICT_TO_SHELX)
        self.Bind(wx.EVT_MENU, self.PERTURB, id=ID_PERTURB)
        self.Bind(wx.EVT_MENU, self.add_trailer, id=ID_ADDTRAILER)
        self.Bind(wx.EVT_MENU, self.TWIN_1, id=ID_TWIN_1)
        self.Bind(wx.EVT_MENU, self.TWIN_2, id=ID_TWIN_2)
        self.Bind(wx.EVT_MENU, self.TWIN_3, id=ID_TWIN_3)
        self.Bind(wx.EVT_MENU, self.TWIN_4, id=ID_TWIN_4)
        self.Bind(wx.EVT_MENU, self.MOVE_1, id=ID_MOVE_1)
        self.Bind(wx.EVT_MENU, self.MOVE_2, id=ID_MOVE_2)
        self.Bind(wx.EVT_MENU, self.MOVE_3, id=ID_MOVE_3)
        self.Bind(wx.EVT_MENU, self.MOVE_4, id=ID_MOVE_4)
        self.Bind(wx.EVT_MENU, self.MOVE_5, id=ID_MOVE_5)
        self.Bind(wx.EVT_MENU, self.MOVE_6, id=ID_MOVE_6)
        self.Bind(wx.EVT_MENU, self.MOVE_7, id=ID_MOVE_7)
        self.Bind(wx.EVT_MENU, self.find_residue_split, id=ID_findresidue)
        self.Bind(wx.EVT_MENU, self.goto_residue, id=ID_RESI_DIALOG)
        self.Bind(wx.EVT_MENU, self.wmol_run, id=ID_wmol)
        self.Bind(wx.EVT_BUTTON, self.wmol_run, self.wmolbutton)
        self.text.Bind(wx.EVT_KEY_UP, self.caretpos)
        self.text3.Bind(wx.EVT_KEY_UP, self.caretpos)
        self.text4.Bind(wx.EVT_KEY_UP, self.caretpos)
        self.text.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightDown)
        self.text2.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightDown)
        self.text3.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightDown)
        self.text4.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightDown)
        self.text.Bind(wx.EVT_MIDDLE_UP, self.OnMouseMiddleDown)
        if len(self.phtoxprep) > 1:
            self.Bind(wx.EVT_BUTTON, self.onXPREP, self.XPREP)
        if len(self.phtoxt) > 1:
            self.Bind(wx.EVT_BUTTON, self.onXT, self.XT)
        if len(self.phtoxs) > 1:
            self.Bind(wx.EVT_BUTTON, self.onXS, self.XS)
        if len(self.phtoxl) > 1:
            self.Bind(wx.EVT_BUTTON, self.onXLR2I, self.XL)
        if len(self.phtoxp) > 1:
            self.Bind(wx.EVT_BUTTON, self.onXP, self.XP)
        if len(self.phtoxshell) > 1:
            self.Bind(wx.EVT_BUTTON, self.onXSHELL, self.Xshell)
        if len(self.phtoolex) > 1:
            self.Bind(wx.EVT_BUTTON, self.onOlex, self.olex)
        if len(self.phtoxshell6) > 1:
            self.Bind(wx.EVT_BUTTON, self.onXSHELL6, self.Xshell6)
        if len(self.phtoshelxle) > 1:
            self.Bind(wx.EVT_BUTTON, self.shelxle, self.onshelxle)
        if len(self.phtosxgraph) > 1:
            self.Bind(wx.EVT_BUTTON, self.onsxgraph, self.sxgraph)
        if len(self.phtoxseed) > 1:
            self.Bind(wx.EVT_BUTTON, self.onxseed, self.xseed)
        if len(self.phtocoot) > 1:
            self.Bind(wx.EVT_BUTTON, self.onCoot, self.coot)
        self.Bind(wx.EVT_BUTTON, self.onReload, self.restoins)
        ################activation##############################################################
        #        self.text.Bind(wx.stc.EVT_STC_MARGINCLICK, self.OnMarginClick)
        self.text.Bind(wx.stc.EVT_STC_DO_DROP, self.OnDoDrop)
        self.text.Bind(wx.stc.EVT_STC_DRAG_OVER, self.OnDragOver)
        self.text.Bind(wx.stc.EVT_STC_START_DRAG, self.OnStartDrag)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.onpage)

    # def intit_toolbar(self, event):
    #     self.toolbar = self.CreateToolBar(wx.TB_VERTICAL|wx.TB_RIGHT)
    #     qtool = self.toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('icon/coot.png'))
    #     self.toolbar.Realize()
    #     self.toolbar.SetToolBitmapSize((16,16))
    #     self.Bind(wx.EVT_TOOL, self.onCloselin, qtool)
    #     #self.SetSize((350, 250))
    #     save_ico = wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR, (16,16))
    #     saveTool = self.toolbar.AddSimpleTool(wx.ID_ANY, save_ico, "Save", "Saves the Current Worksheet")
    #     self.SetTitle('Simple toolbar')
    #     self.Centre()

    def OnStartDrag(self, event):
        event.SetDragAllowMove(True)  # you can prevent moving of text (only copy)

    def OnDragOver(self, event):
        event.SetDragResult(wx.DragNone)

    def OnDoDrop(self, event):
        result = event.GetDragText()
        if result.startswith("file:"):
            if self.Modified(event):
                self.fnamefull = result.split("file://")[1].replace("\n", "")
                event.SetDragText("")
                self.filehistory.AddFileToHistory(self.fnamefull)
                self.filehistory.Save(self.config)
                self.dirname = os.path.dirname(self.fnamefull)
                self.filename = os.path.basename(self.fnamefull)
                self.fmtime = int(os.stat(self.fnamefull).st_mtime)
                self.Load(event)
            else:
                event.SetDragText("")

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Linxtl v." + self.version)
        #        self.SetSize((850, 630))
        # self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Linxtl"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self, event):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        #        grid_sizer_2 = wx.GridSizer(6, 0, 0, 0)

        grid_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        gridsize = (1, wx.Button.GetDefaultSize()[1])
        grid_sizer_1.Add(self.OPEN, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.SAVE, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoxprep) > 1:
            grid_sizer_1.Add(self.XPREP, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoxt) > 1:
            grid_sizer_1.Add(self.XT, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoxs) > 1:
            grid_sizer_1.Add(self.XS, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoxl) > 1:
            grid_sizer_1.Add(self.XL, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoxp) > 1:
            grid_sizer_1.Add(self.XP, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoxshell) > 1:
            grid_sizer_1.Add(self.Xshell, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoolex) > 1:
            grid_sizer_1.Add(self.olex, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
            # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoxshell6) > 1:
            grid_sizer_1.Add(self.Xshell6, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoshelxle) > 1:
            grid_sizer_1.Add(self.onshelxle, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ADJUST_MINSIZE, 0)
        if len(self.phtosxgraph) > 1:
            grid_sizer_1.Add(self.sxgraph, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ADJUST_MINSIZE, 0)
        if len(self.phtoxseed) > 1:
            grid_sizer_1.Add(self.xseed, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        # grid_sizer_1.Add(gridsize, 0, wx.EXPAND|wx.ALIGN_CENTER|wx.ADJUST_MINSIZE, 0)
        if len(self.phtocoot) > 1:
            grid_sizer_1.Add(self.coot, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        grid_sizer_1.Add(self.wmolbutton, 0, wx.TOP | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)
        grid_sizer_1.Add(gridsize, 2, wx.EXPAND | wx.ADJUST_MINSIZE, 0)
        grid_sizer_1.Add(self.restoins, 0, wx.TOP | wx.RIGHT | wx.ALIGN_CENTER | wx.ADJUST_MINSIZE, 1)

        sizer_2.Add(grid_sizer_1, 0, wx.EXPAND, 0)
        self.notebook_1.AddPage(self.text, "->")
        self.notebook_1.AddPage(self.text2, "LST")
        self.notebook_1.AddPage(self.text3, "CIF")
        self.notebook_1.AddPage(self.text4, "PCIF")
        self.num = self.notebook_1.GetSelection()

        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_1.Add(self.notebook_1, 3, wx.EXPAND, 0)  # remtabs
        # sizer_3.Add(self.webify, 1, wx.EXPAND, 0)  # remtabs
        # sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)  # remtabs

        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        self.CenterOnScreen()
        ############################################CENTER####################################################################
        #        displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        #        sizes = [display.GetGeometry().GetSize() for display in displays]
        #        displaySize=sizes[0].Get()
        #        self.SetPosition((displaySize[0]/2-displaySize[0]/2.4, displaySize[1]/2-displaySize[0]/4))
        self.SetMinSize((700, 400))
        if len(self.inputfile) == 1:
            if not self.filehistory.GetCount() == 0:
                if len(self.filehistory.GetHistoryFile(0)) > 3:
                    if os.path.exists(self.filehistory.GetHistoryFile(0)) == True:
                        self.fnamefull = self.filehistory.GetHistoryFile(0)
                        self.dirname = os.path.dirname(self.fnamefull)
                        self.filename = os.path.split(self.fnamefull)[1]
                        self.SetTitle("Linxtl Editing ... " + self.fnamefull)
                        self.Load(event)
                else:
                    self.fnamefull = None
        else:
            self.fnamefull = self.inputfile[1]
            self.dirname = os.path.dirname(inputfile[1])
            self.filename = os.path.split(self.fnamefull)[1]
            self.SetTitle("Linxtl Editing ... " + self.fnamefull)
            self.Load(event)
        # end wxGlade

    #        self.Bind(wx.stc.EVT_STC_STYLENEEDED, self.onColor1)
    def OnMouseMiddleDown(self, event):
        pass

    def OnMouseRightDown(self, event):

        popup = wx.Menu()
        popup.Append(wx.ID_UNDO, "Undu\tctrl-z", "", wx.ITEM_NORMAL)
        popup.Append(wx.ID_REDO, "Redo\tctrl-y", "", wx.ITEM_NORMAL)
        popup.Append(wx.ID_CUT, "Cut\tctrl-x", "", wx.ITEM_NORMAL)
        popup.Append(wx.ID_COPY, "Copy\tctrl-c", "", wx.ITEM_NORMAL)
        popup.Append(wx.ID_PASTE, "Paste\tctrl-v", "", wx.ITEM_NORMAL)
        popup.AppendSeparator()
        popup.Append(ID_RESI_DIALOG, "Go to Residue\tctrl-g", "", wx.ITEM_NORMAL)
        popup.AppendSeparator()
        popup.Append(ID_EditOc, "Set atomic occupancy factor\tctrl-e", "", wx.ITEM_NORMAL)
        popup.Append(ID_editisotr, "Change U(iso)", "", wx.ITEM_NORMAL)
        imp = wx.Menu()
        imp.Append(ID_THF, 'THF: full disorder')
        imp.Append(ID_THF2, 'THF: only carbons')
        imp.Append(ID_Phenyl, 'Phenyl: 6 atoms')
        imp.Append(ID_Phenylb, 'Phenyl: rotational 5 atoms')
        imp.Append(ID_tbu, 'tBu/CF3 rotational disorder')
        popup.Append(ID_PART, "Split into parts", "", wx.ITEM_NORMAL)
        popup.Append(wx.ID_ANY, 'restraints for', imp)
        popup.Append(ID_ISOTR, "Isotropic\tctrl-i", "", wx.ITEM_NORMAL)
        popup.Append(ID_onRefW, "Weight refinement", "", wx.ITEM_NORMAL)
        popup.AppendSeparator()
        popup.Append(ID_Delq, "Kill Q peaks\tctrl-k", "", wx.ITEM_NORMAL)
        popup.Append(ID_HDEL, "Kill H atoms\tctrl-shift-k", "", wx.ITEM_NORMAL)
        popup.Append(ID_Invers, "Inversion of the structure", "", wx.ITEM_NORMAL)
        popup.Append(ID_Sort, "Sort Atoms", "", wx.ITEM_NORMAL)
        popup.Append(ID_HTAB, "Add HTAB parameters", "", wx.ITEM_NORMAL)
        popup.Append(ID_OMIT, "OMIT all bad reflections", "", wx.ITEM_NORMAL)
        popup.AppendSeparator()
        popup.Append(ID_Copyitr, "Copy ins to res\tctrl-shift-i", "", wx.ITEM_NORMAL)
        popup.Append(ID_Copyrti, "Copy res to ins\tctrl-shift-r", "", wx.ITEM_NORMAL)
        popup.AppendSeparator()
        self.text.PopupMenu(popup)
        self.text2.PopupMenu(popup)
        self.text3.PopupMenu(popup)
        self.text4.PopupMenu(popup)

        popup.Destroy()

    def preference(self):
        if os.path.exists(os.path.join(self.path, "user", "preference")) == True:
            preference_var = open(os.path.join(self.path, "user", "preference"), 'r')
            self.preference_var = preference_var.readlines()
            self.getpreference()
            preference_var.close()
        else:
            preference = open(os.path.join(self.path, "user", "preference"), 'w')
            lines = "FONT_SIZE 14\nFONT_MAIN Courier New\n"
            preference.writelines(lines + "\n" * 50)
            preference.close()
            preference = open(os.path.join(self.path, "user", "preference"), 'r')
            self.preference_var = preference.readlines()
            self.getpreference()

    def exdeclare_vars(self):
        json_file = os.path.join(self.path, "user", "external.json")
        json_file_obj = open(json_file, 'r')
        self.external_config = json.load(json_file_obj)
        json_file_obj.close()
        self.phtoxl = self.external_config['shelxl']
        self.phtoxs = self.external_config['shelxs']
        self.phtoxt = self.external_config['shelxt']
        self.phtoxm = self.external_config['shelxd']
        self.phtoxc = self.external_config['shelxc']
        self.phtoxh = self.external_config['shelxh']
        self.phtoxe = self.external_config['shelxe']
        self.phtoxprep = self.external_config['xprep']
        self.phtoplaton = self.external_config['platon']
        self.phtosir = self.external_config['sir']
        self.phtoxpro = self.external_config['xpro']
        self.phtopublcif = self.external_config['publcif']
        self.phtoxp = self.external_config['xp']
        self.phtoxshell = self.external_config['xshell5']
        self.phtoxshell6 = self.external_config['xshell5']
        self.phtoshelxle = self.external_config['shelxle']
        self.phtocoot = self.external_config['coot']
        self.phtoolex = self.external_config['olex']
        self.phtosadabs = self.external_config['sadabs']
        self.phtoxcif = self.external_config['sadabs']
        self.phtocellnow = self.external_config['cellnow']
        self.phtoxabs = self.external_config['xabs']
        self.phtoaimless = self.external_config['aimless']
        self.phtopointless = self.external_config['pointless']
        self.phtoxds = self.external_config['xds']
        self.phtomercury = self.external_config['mercury']
        self.phtopovray = self.external_config['povray']
        self.phtosfconvert = self.external_config['sfconvert']
        self.phtoxseed = self.external_config['xseed']
        self.phtosxgraph = self.external_config['sxgraph']
        self.phtodiamond = self.external_config['diamond']
        self.phtoencifer = self.external_config['encifer']
        self.phtodirdif = self.external_config['dirdif']
        self.phtopymol = self.external_config['pymol']
        self.phtojmol = self.external_config['jmol']
        self.phtoavogadro = self.external_config['avogadro']
        self.phtochimera = self.external_config['chimera']
        self.phtowine = self.external_config['wine']
        # self.phtosaint = self.external_config['saint']
        self.phtoanode = self.external_config['anode']
        self.phtodrawxtl = self.external_config['drawxtl']
        self.phtorasmol = self.external_config['rasmol']
        self.phtoanycif = self.external_config['anycif']
        self.phtoxds2sad = self.external_config['xds2sad']
        self.phtotwinabs = self.external_config['twinabs']
        self.phtoortep3 = self.external_config['ortep3']

    def extdeclare(self):

        if os.path.exists(os.path.join(self.path, "user", "external.json")) == True:
            self.exdeclare_vars()
        else:
            self.phtoxl = ""
            self.phtoxs = ""
            self.phtoxt = ""
            self.phtoxm = ""
            self.phtoxc = ""
            self.phtoxh = ""
            self.phtoxe = ""
            self.phtoxprep = ""
            self.phtoplaton = ""
            self.phtosir = ""
            self.phtoxpro = ""
            self.phtopublcif = ""
            self.phtoxp = ""
            self.phtoxshell = ""
            self.phtoxshell6 = ""
            self.phtoshelxle = ""
            self.phtocoot = ""
            self.phtoolex = ""
            self.phtosadabs = ""
            self.phtoxcif = ""
            self.phtocellnow = ""
            self.phtoxabs = ""
            self.phtoaimless = ""
            self.phtopointless = ""
            self.phtoxds = ""
            self.phtomercury = ""
            self.phtopovray = ""
            self.phtosfconvert = ""
            self.phtoxseed = ""
            self.phtosxgraph = ""
            self.phtodiamond = ""
            self.phtoencifer = ""
            self.phtodirdif = ""
            self.phtopymol = ""
            self.phtojmol = ""
            self.phtoavogadro = ""
            self.phtochimera = ""
            self.phtowine = ""
            # self.phtosaint = ""
            self.phtoanode = ""
            self.phtodrawxtl = ""
            self.phtorasmol = ""
            self.phtoanycif = ""
            self.phtoxds2sad = ""
            self.phtotwinabs = ""
            self.phtoortep3 = ""
            exobj = {
                'shelxl': self.phtoxl,
                'shelxh': self.phtoxh,
                'shelxs': self.phtoxs,
                'shelxt': self.phtoxt,
                'shelxd': self.phtoxm,
                'shelxc': self.phtoxc,
                'shelxe': self.phtoxe,
                'xprep': self.phtoxprep,
                'platon': self.phtoplaton,
                'sir': self.phtosir,
                'xpro': self.phtoxpro,
                'publcif': self.phtopublcif,
                'xp': self.phtoxp,
                'xshell5': self.phtoxshell,
                'xshell6': self.phtoxshell6,
                'shelxle': self.phtoshelxle,
                'coot': self.phtocoot,
                'olex': self.phtoolex,
                'sadabs': self.phtosadabs,
                'xcif': self.phtoxcif,
                'cellnow': self.phtocellnow,
                'xabs': self.phtoxabs,
                'aimless': self.phtoaimless,
                'pointless': self.phtopointless,
                'xds': self.phtoxds,
                'mercury': self.phtomercury,
                'povray': self.phtopovray,
                'sfconvert': self.phtosfconvert,
                'xseed': self.phtoxseed,
                'sxgraph': self.phtosxgraph,
                'diamond': self.phtodiamond,
                'encifer': self.phtoencifer,
                'dirdif': self.phtodirdif,
                'pymol': self.phtopymol,
                'jmol': self.phtojmol,
                'avogadro': self.phtoavogadro,
                'chimera': self.phtochimera,
                'wine': self.phtowine,
                # 'saint': self.phtosaint,
                'anode': self.phtoanode,
                'drawxtl': self.phtodrawxtl,
                'rasmol': self.phtorasmol,
                'anycif': self.phtoanycif,
                'xds2sad': self.phtoxds2sad,
                'twinabs': self.phtotwinabs,
                'ortep3': self.phtoortep3
            }
            json_file = os.path.join(self.path, "user", "external.json")
            json_file_obj = open(json_file, 'w')
            json.dump(exobj, json_file_obj)
            json_file_obj.close()
        if os.path.exists(self.phtowine) == True:
            self.phtowine = self.phtowine
        elif os.path.exists("/usr/bin/wine") == True:
            self.phtowine = "/usr/bin/wine"

    def getpreference(self):
        self.fsg = self.preference_var[0].replace("\n", "").replace('FONT_SIZE', "").replace(" ", "")
        self.main_font = self.preference_var[1].replace("\n", "").replace('FONT_MAIN ', "")

    def CODBASE(self, event):
        #        subprocess.call(os.path.join(self.path,"external.py"))
        from codbasegui import crystalbase_main
        displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        sizes = [display.GetGeometry().GetSize() for display in displays]
        displaySize = sizes[0].Get()
        paths = {"path":os.path.join(self.path, "Modules")}
        cod = crystalbase_main(None, -1, "", paths, size=(displaySize[0] / 1.5, displaySize[1] / 2))
        cod.Show()

    #        cod.Destroy()
    #         exec(open(os.path.join(self.path, "Modules", "codbasegui.py")).read())
    def external(self, event):
        from external import cexternal
        external = cexternal()
        external.Show()

    def on_file_history(self, event):
        if self.Modified(event):
            fileNum = event.GetId() - wx.ID_FILE1
            # # printfileNum
            self.fnamefull = self.filehistory.GetHistoryFile(fileNum)

            # # printself.fnamefull
            self.dirname = os.path.dirname(self.fnamefull)
            # self.filehistory.AddFileToHistory(path)
            if os.path.exists(self.fnamefull) == False:
                dlg = wx.MessageDialog(self, "Error File " + self.fnamefull + " does not exist",
                                       'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                self.filename = os.path.basename(self.fnamefull)
                self.SetTitle("Linxtl Editing ... " + self.fnamefull)
                self.fmtime = int(os.stat(self.fnamefull).st_mtime)
                # # print"fname", self.filename
                self.Load(event)

    def onUpdate(self, event):
        from urllib.request import urlopen
        import http.client
        dialog = wx.MessageDialog(self,
                                  "This will update Linxtl. Would you like to proceed? It might take some time, depending on the speed of your internet connection.",
                                  "Update?", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
        dialog.Centre()
        result = dialog.ShowModal()
        dialog.Destroy()
        if result == wx.ID_YES:
            try:
                request = urlopen('http://sourceforge.net/projects/linxtl/')
                response = request.readlines()
                #           # # printresponse

                for line in response:
                    found = line.find("Download /Linxtl v.")
                    #               # # printfound
                    if not found == -1:
                        # # printfound
                        # print line[found+20:found+25]
                        # # printself.version.strip()
                        if line[found + 20:found + 25] == self.version.strip():
                            # # print"linxtl is up to date"
                            dlg = wx.MessageBox("Linxtl is up to date", "Info", wx.OK)
                        else:
                            if not os.path.exists(os.path.join(self.path, "tmp")):
                                os.makedirs(os.path.join(self.path, "tmp"))
                            shutil.copy2(os.path.join(self.path, 'update.py'), os.path.join(self.path, 'tmp', 'pu.py'))
                            os.chmod(os.path.join(self.path, "tmp", 'pu.py'), 0o755)
                            sys.path.append(os.path.join(self.path, "tmp"))
                            import pu
                            #                            up()
                            sys.exit(2)
            #                        Popen(os.path.join(self.path,'update.py'), shell=True)
            # # print"done"
            #                        self.close()
            except urllib2.HTTPError:
                # print'Unable to get latest version info - HTTPError = ' + str(e.reason)
                sys.exit(2)

            except urllib2.URLError:
                print('Unable to get latest version info - URLError')
                sys.exit(2)

            except http.client.HTTPException:
                # print'Unable to get latest version info - HTTPException'
                sys.exit(2)

            except Exception:
                import traceback
                # print'Unable to get latest version info - Exception = ' + traceback.format_exc()

    def onOpen(self, event):  # wxGlade: MyFrame.<event_handler>
        self.notebook_1.SetSelection(0)
        if self.Modified(event):
            dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, wx.FD_OPEN)
            if dlg.ShowModal() == wx.ID_OK:
                self.dirname = dlg.GetDirectory()
                self.filename = dlg.GetFilename()
                self.fnamefull = os.path.join(self.dirname, self.filename)
                self.Load(event)
                self.SetStatusText('You selected: %s' % self.filename)
                self.fmtime = int(os.stat(self.fnamefull).st_mtime)
                self.SetTitle("Linxtl Editing ... " + self.fnamefull)

            # # print"added to history",os.path.join(self.dirname,self.filename)

            dlg.Destroy()

    def activated(self, event):

        if os.path.exists(self.fnamefull):
            f = open(self.fnamefull).read()
            text = str(self.text.GetText())
            loaded = sys.getsizeof(text)
            saved = sys.getsizeof(f)
            if event.GetActive() == True:
                if loaded != saved:
                    self.restoins.SetBackgroundColour(wx.Colour(244, 154, 154))
                else:
                    self.restoins.SetBackgroundColour(wx.Colour(172, 248, 181))

    def toobig(self, event, file):
        size = os.path.getsize(file)
        return size

    def Load(self, event):

        self.text.ClearAll()
        self.text2.ClearAll()
        self.text3.ClearAll()
        self.text4.ClearAll()
        self.text.LoadFile(self.fnamefull)
        self.filenamenoext = os.path.splitext(self.filename)[0]
        self.fnoe = os.path.splitext(self.fnamefull)[0]
        if os.path.exists(self.fnoe + ".lst"):
            self.text2.LoadFile(self.fnoe + ".lst")
        if os.path.exists(self.fnoe + ".cif"):
            self.text3.LoadFile(self.fnoe + ".cif")
            self.onCifColor(event)
        if os.path.exists(os.path.join(self.dirname, "publish.cif")):
            self.text4.LoadFile(os.path.join(self.dirname, "publish.cif"))
            self.onPCifColor(event)
        self.onColor1(event)
        out = self.getrf()
        self.filehistory.AddFileToHistory(os.path.join(self.dirname, self.filename))
        self.filehistory.Save(self.config)
        self.SetTitle("Linxtl Editing ... " + self.fnamefull)
        if not out == None:
            self.SetStatusText('The file ' + self.fnamefull + ' has been loaded' + " " + out)
        else:
            self.SetStatusText('The file ' + self.fnamefull + ' has been loaded')
        self.timemod(event)

    def timemod(self, event):
        self.modtime = os.path.getmtime(self.fnamefull)

    def caretpos(self, event):

        num = self.notebook_1.GetSelection()
        # print num
        if num == 0:
            x = self.text.GetCurrentLine()
            self.SetStatusText(str(x + 1), 1)
        elif num == 2:
            if os.path.exists(self.fnoe + ".cif"):
                x = self.text3.GetCurrentLine()
                self.SetStatusText(str(x + 1), 1)
        elif num == 3:
            if os.path.exists(os.path.join(self.dirname, "publish.cif")):
                x = self.text4.GetCurrentLine()
                self.SetStatusText(str(x + 1), 1)
        self.num = num

    def onpage(self, event):
        num = self.notebook_1.GetSelection()
        if num == 0:
            self.SetTitle("Linxtl Editing ... " + self.fnamefull)
            self.text.ScrollToLine(self.linenum_t1)
            self.linenum_t2 = self.text2.GetFirstVisibleLine()
            self.linenum_t3 = self.text3.GetFirstVisibleLine()
            self.linenum_t4 = self.text4.GetFirstVisibleLine()
        if num == 1:
            if os.path.exists(self.fnoe + ".lst"):
                self.onReloadlst(event)
                self.text2.ScrollToLine(self.linenum_t2)
                self.linenum_t1 = self.text.GetFirstVisibleLine()
                self.linenum_t3 = self.text3.GetFirstVisibleLine()
                self.linenum_t4 = self.text4.GetFirstVisibleLine()
        elif num == 2:
            if os.path.exists(self.fnoe + ".cif"):
                self.onReloadcif(event)
                self.text3.ScrollToLine(self.linenum_t3)
                self.linenum_t1 = self.text.GetFirstVisibleLine()
                self.linenum_t2 = self.text2.GetFirstVisibleLine()
                self.linenum_t4 = self.text4.GetFirstVisibleLine()
        elif num == 3:
            if os.path.exists(os.path.join(self.dirname, "publish.cif")):
                self.onReloadpcif(event)
                self.text4.ScrollToLine(self.linenum_t4)
                self.linenum_t1 = self.text.GetFirstVisibleLine()
                self.linenum_t2 = self.text2.GetFirstVisibleLine()
                self.linenum_t3 = self.text3.GetCurrentLine()
        self.num = num

    def onReloadRes(self, event):  # wxGlade: MyFrame.<event_handler>
        self.topline = self.text.GetFirstVisibleLine()
        self.fnoe = os.path.splitext(self.fnamefull)[0]
        self.fnamefull = self.fnoe + ".res"
        self.fin = open(self.fnamefull)
        self.text.SetText(self.fin.read())
        self.fin.close()
        self.onColor1(event)
        out = self.getrf()
        self.filehistory.AddFileToHistory(os.path.join(self.dirname, self.fnamefull))
        self.filehistory.Save(self.config)
        if not out == None:
            self.SetStatusText('The file ' + self.fnamefull + ' has been loaded' + " " + out)
        else:
            self.SetStatusText('The file ' + self.fnamefull + ' has been loaded')
        self.text.ScrollToLine(self.topline)
        self.SetTitle("Linxtl Editing ... " + self.fnamefull)
        out = self.getrf()
        self.timemod(event)
        #            self.text.SetSavePoint()
        #            self.onSave(event)
        self.SetStatusText("reloaded " + self.fnamefull + " " + str(out))

    def onReloadafterXT(self, event):
        if os.path.exists(self.fnoe + "_a.res"):
            self.fnoe = self.fnoe + "_a"
            self.fnamefull = self.fnoe + ".res"
            self.filename = os.path.basename(self.fnamefull)
            self.filenamenoext = os.path.splitext(self.filename)[0]
            self.onReload(event)
        else:
            dlg = wx.MessageDialog(self, "Error!!! File does not exist",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onReload(self, event):  # wxGlade: MyFrame.<event_handler>
        self.topline = self.text.GetFirstVisibleLine()
        self.fnoe = os.path.splitext(self.fnamefull)[0]
        self.fin = open(self.fnamefull)
        self.text.SetText(self.fin.read())
        self.fin.close()
        self.onColor1(event)
        out = self.getrf()
        self.filehistory.AddFileToHistory(os.path.join(self.dirname, self.fnamefull))
        self.filehistory.Save(self.config)
        if not out == None:
            self.SetStatusText('The file ' + self.fnamefull + ' has been loaded' + " " + out)
        else:
            self.SetStatusText('The file ' + self.fnamefull + ' has been loaded')
        self.text.ScrollToLine(self.topline)
        self.SetTitle("Linxtl Editing ... " + self.fnamefull)
        out = self.getrf()
        self.timemod(event)
        self.SetStatusText("reloaded " + self.fnamefull + " " + str(out))

    def onReloadcif(self, event):  # wxGlade: MyFrame.<event_handler>
        self.fnoe = os.path.splitext(self.fnamefull)[0]
        self.fin = open(self.fnoe + ".cif")
        self.text3.SetText(self.fin.read())
        self.fin.close()
        self.onCifColor(event)
        self.SetTitle("Linxtl Editing ... " + self.fnoe + ".cif")
        self.text3.SetSavePoint()
        self.SetStatusText("reloaded " + self.fnoe + ".cif")

    def onReloadpcif(self, event):  # wxGlade: MyFrame.<event_handler>
        self.fin = open(os.path.join(self.dirname, "publish.cif"))
        self.text4.SetText(self.fin.read())
        self.fin.close()
        self.onPCifColor(event)
        self.SetTitle("Linxtl Editing ... " + os.path.join(self.dirname, "publish.cif"))
        self.text4.SetSavePoint()
        self.SetStatusText("reloaded " + os.path.join(self.dirname, "publish.cif"))

    def onReloadlst(self, event):  # wxGlade: MyFrame.<event_handler>
        #         self.fin.close()
        self.fin = open(self.fnoe + ".lst")
        self.text2.SetText(self.fin.read())
        self.fin.close()
        self.SetTitle("Linxtl Editing ... " + self.fnoe + ".lst")
        self.text2.SetSavePoint()
        self.SetStatusText("reloaded " + self.fnoe + ".lst")

    def onSearch(self, event):
        num = self.notebook_1.GetSelection()
        from find_replace import find_r
        if num == 0:
            col = self.onColor1
            fd = find_r(event, self.text, self.main_font, int(self.fsg), col)
            fd.Show()
        elif num == 1:
            col = self.onColor1
            fd = find_r(event, self.text2, self.main_font, int(self.fsg), col)
            fd.Show()
        elif num == 2:
            col = self.onCifColor
            fd = find_r(event, self.text3, self.main_font, int(self.fsg), col)
            fd.Show()
        elif num == 3:
            col = self.onPCifColor
            fd = find_r(event, self.text4, self.main_font, int(self.fsg), col)
            fd.Show()

    def replacetext(self, event, findstring, replacestring):
        num = self.notebook_1.GetSelection()
        if num == 0:
            for i in range(4):
                text = self.text.GetText()
                if text.find(findstring) != -1:
                    pos = text.find(findstring)
                    while pos != -1:
                        text = self.text.GetText()
                        pos = text.find(findstring, pos)
                        self.text.BeginUndoAction()
                        self.text.SetTargetStart(pos)
                        self.text.SetTargetEnd(pos + len(findstring))
                        self.text.ReplaceTarget(replacestring)
                        #            self.text.SetText(text)
                        self.text.EndUndoAction()
                        pos = text.find(findstring, pos + 1)

    def onSave(self, event):
        num = self.notebook_1.GetSelection()
        self.topline = self.text.GetFirstVisibleLine()
        self.capital(event)
        if self.fnamefull is None:
            return self.onSaveAs()
        self.text.SaveFile(self.fnamefull)
        if os.path.exists(self.fnoe + ".cif"):
            if len(self.text3.GetText()) > 20:
                if self.num == 2:
                    self.text3.SaveFile(self.fnoe + ".cif")
        if os.path.exists(os.path.join(self.dirname, "publish.cif")):
            print(self.num)
            if self.num == 3:
                if len(self.text4.GetText()) > 20:
                    self.text4.SaveFile(os.path.join(self.dirname, "publish.cif"))
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)
        out = self.getrf()
        #        if  self.ossystem.startswith("lin"):
        #           self.restoins.SetBackgroundColour(wx.Colour(172,248,181))
        self.SetStatusText('The file has been saved' + " " + str(out))
        #        self.text.SetSavePoint()
        self.timemod(event)
        return True

    def onfSave(self, event):  # wxGlade: MyFrame.<event_handler>
        self.topline = self.text.GetFirstVisibleLine()
        self.capital(event)
        if self.fnamefull is None:
            return self.onSaveAs()
        self.text.SaveFile(self.fnamefull)
        self.onColor1(event)

        self.text.ScrollToLine(self.topline)
        return True

    def onSaveAs(self, event):  # wxGlade: MyFrame.<event_handler>
        self.notebook_1.SetSelection(0)
        self.topline = self.text.GetFirstVisibleLine()
        dlg = wx.FileDialog(self, "Save a file", self.dirname, "", "*.*", \
                            wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            # Grab the content to be saved
            itcontains = self.text.GetText()
            # Open the file for write, write, close
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            filehandle = open(os.path.join(self.dirname, self.filename), 'w')
            filehandle.write(itcontains)
            filehandle.close()
            out = self.getrf()
            self.SetStatusText('The file has been saved' + " " + str(out))
        # Get rid of the dialog to keep things tidy
        self.timemod(event)
        dlg.Destroy()
        self.text.ScrollToLine(self.topline)

    def onGetHTML(self, event):
        txt = open(self.fnamefull, 'r')
        listt = []
        text = txt.readlines()
        txt.close()
        for line in text:
            html = line.replace(' ', ' &nbsp ')
            listt.append(html)
        html_text = "<br />".join(listt)
        return html_text

    def onPrint(self, event):
        self.notebook_1.SetSelection(0)
        from wx.html import HtmlEasyPrinting
        html_text = self.onGetHTML(event)
        printout = HtmlEasyPrinting()
        printout.SetFonts("", "", [8, 8, 9, 10, 10, 10, 40])
        printData = wx.PrintData()
        printDialogData = wx.PrintDialogData()
        printDialogData.SetPrintData(printData)
        printDialogData.SetAllPages(False)
        printDialogData.SetNoCopies(1)
        printer = wx.Printer(printDialogData)
        printout.PrintText(html_text)

    def OnPrintPreview(self, event):
        self.notebook_1.SetSelection(0)
        from wx.html import HtmlEasyPrinting
        html_text = self.onGetHTML(event)
        printout = HtmlEasyPrinting()
        printout.SetHeader(self.fnamefull)
        printout.SetFonts("", "", [8, 8, 9, 10, 10, 10, 40])
        printData = wx.PrintData()
        printDialogData = wx.PrintDialogData()
        printDialogData.SetPrintData(printData)
        printDialogData.SetAllPages(True)
        printDialogData.SetNoCopies(1)
        printer = wx.Printer(printDialogData)
        printout.PreviewText(str(html_text))

    def onINS(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, self.filenamenoext + ".ins")):
            try:
                if self.ossystem.startswith("win"):

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".ins"])
                else:

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".ins"])

            except OSError:
                pass

    def onRes(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, self.filenamenoext + ".res")):
            try:
                if self.ossystem.startswith("win"):

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".res"])
                else:

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".res"])

            except OSError:
                pass

    def onINP(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, self.filenamenoext + ".inp")):
            try:
                if self.ossystem.startswith("win"):

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".inp"])
                else:

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".inp"])

            except OSError:
                pass

    def onLST(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, self.filenamenoext + ".lst")):
            try:
                if self.ossystem.startswith("win"):

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".lst"])
                else:

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".lst"])

            except OSError:
                pass

    def onEReport(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, self.filenamenoext + ".tex")):
            try:
                if self.ossystem.startswith("win"):

                    webbrowser.open('file://%s' % os.path.join(self.dirname, self.filenamenoext + ".tex"))

                else:

                    webbrowser.open('file://%s' % os.path.join(self.dirname, self.filenamenoext + ".tex"))

            except OSError:
                pass
        else:
            dlg = wx.MessageDialog(self, "Error!!! File does not exist",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onHTMLReport(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, "publish_" + self.filenamenoext + ".html")):
            try:
                if self.ossystem.startswith("win"):
                    os.chdir(self.dirname)
                    webbrowser.open('file://%s' % os.path.join(self.dirname, "publish_" + self.filenamenoext + ".html"))
                elif self.ossystem.startswith("darwin"):
                    os.chdir(self.dirname)
                    webbrowser.open('file://%s' % os.path.join(self.dirname, "publish_" + self.filenamenoext + ".html"))

                else:
                    os.chdir(self.dirname)
                    webbrowser.open('file://%s' % os.path.join(self.dirname, "publish_" + self.filenamenoext + ".html"))
                    # webbrowser.open('publish.html')

            except OSError:
                pass
        else:
            dlg = wx.MessageDialog(self, "Error! " + "publish_" + self.filenamenoext + ".html" + "does not exist",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onHTMLBOND(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, "bonds_angles_" + self.filenamenoext + ".htm")):
            try:
                if self.ossystem.startswith("win"):
                    os.chdir(self.dirname)
                    webbrowser.open(
                        'file://%s' % os.path.join(self.dirname, "bonds_angles_" + self.filenamenoext + ".htm"))
                elif self.ossystem.startswith("darwin"):
                    os.chdir(self.dirname)
                    webbrowser.open(
                        'file://%s' % os.path.join(self.dirname, "bonds_angles_" + self.filenamenoext + ".htm"))
                else:
                    os.chdir(self.dirname)
                    webbrowser.open(
                        'file://%s' % os.path.join(self.dirname, "bonds_angles_" + self.filenamenoext + ".htm"))

            except OSError:
                pass
        else:
            dlg = wx.MessageDialog(self, "Error! " + os.path.join(self.dirname,
                                                                  "bonds_angles_" + self.filenamenoext + ".htm") + " does not exist",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onPCF(self, event):  # wxGlade: MyFrame.<event_handler>

        if os.path.exists(os.path.join(self.dirname, self.filenamenoext + ".pcf")):
            try:
                if self.ossystem.startswith("win"):

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".pcf"])
                else:

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".pcf"])

            except OSError:
                pass
        else:
            dlg = wx.MessageDialog(self, "Error!!! File does not exist",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def reftable(self, event):
        if self.ossystem.startswith("win"):
            os.chdir(self.dirname)
            webbrowser.open(
                os.path.join('file://%s' % os.path.join(self.dirname, self.filenamenoext + "_table" + ".rtf")))
        else:
            os.chdir(self.dirname)
            webbrowser.open(
                os.path.join('file://%s' % os.path.join(self.dirname, self.filenamenoext + "_table" + ".rtf")))

    def onCif(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, self.filenamenoext + ".cif")):
            try:
                if self.ossystem.startswith("win"):

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".cif"])
                else:

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'), self.fnoe + ".cif"])

            except OSError:
                pass
        else:
            dlg = wx.MessageDialog(self, "Error!!! File does not exist",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onTable(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, "publish.cif")):
            try:
                if self.ossystem.startswith("win"):
                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'),
                                      os.path.join(self.dirname, 'publish.cif')])

                else:

                    subprocess.Popen([sys.executable, os.path.join(self.path, 'linxtl.py'),
                                      os.path.join(self.dirname, 'publish.cif')])
            except OSError:
                pass
        else:
            dlg = wx.MessageDialog(self, "Error!!! File does not exist",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onSetwd(self, event):  # wxGlade: MyFrame.<event_handler>
        dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText('You selected: %s' % dlg.GetPath())
            # # printdlg.GetPath()
            tmpf = open(os.path.join(os.path.join(self.path, 'workdir')), 'w')
            # print tmpf
            tmpf.write(dlg.GetPath())
            tmpf.close()
            self.dirname = dlg.GetPath()
        dlg.Destroy()

    def onOpenwd(self, event):  # wxGlade: MyFrame.<event_handler>
        try:
            if self.ossystem.startswith("win"):
                webbrowser.open(self.dirname)
            elif self.ossystem.startswith('darwin'):
                subprocess.Popen(['open', self.dirname])
            elif self.ossystem.startswith('linux'):
                # webbrowser.open("file://"+self.dirname)
                subprocess.check_call(['xdg-open', self.dirname])
        except OSError:
            pass

    def onFntolc(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        if len(sys.argv) == 1:
            filenames = os.listdir(self.dirname)
        else:
            filenames = sys.argv[1:]
        for filename in filenames:
            if filename.upper():
                newfilename = filename.lower()
                # # print"Renaming", filename, "to", newfilename, "..."
                os.rename(filename, newfilename)

    def onliststructues(self, event):  # wxGlade: MyFrame.<event_handler>
        proc = ['Database of CIF files', 'Database of PDB files', 'Database of P4P files', 'Database of SCA files']
        dlg = wx.SingleChoiceDialog(self, 'Select the file extension', 'File extension?', proc, wx.CHOICEDLG_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText('You chose: %s\n' % dlg.GetStringSelection())
            dlg.Destroy()
            if dlg.GetSelection() == 0:
                self.getinfocif(event)
            elif dlg.GetSelection() == 1:
                self.getinfopdb(event)
            elif dlg.GetSelection() == 2:
                self.getinfop4p(event)
            elif dlg.GetSelection() == 3:
                self.getinfosca(event)

    def getinfopdb(self, event):
        pdb, dir = self.getpdb(event)
        ciffull = []
        for filename in pdb:
            briefs = []
            if len(filename) > 100:
                briefs.append("<a href=" + filename + ">" + filename[0:25] + "~" + filename[75:] + "</a>")
            else:
                briefs.append("<a href=" + filename + ">" + filename + "</a>")
            temp = open(filename, 'r').readlines()
            try:
                temp = temp[0:4]
                for i, pdbline in enumerate(temp):
                    if pdbline.startswith("CRYST1"):
                        crystlist = pdbline.split()
                        a = crystlist[1]
                        b = crystlist[2]
                        c = crystlist[3]
                        alpha = crystlist[4]
                        beta = crystlist[5]
                        gamma = crystlist[6]
                        vol = float(a) * float(b) * float(c)
                        briefs.extend((a, b, c, alpha, beta, gamma, str(round(vol, 3))))
                if len(briefs) > 2:
                    ciffull.append(briefs)
            except IndexError:
                pass
        ciffull.insert(0, ["PDB File", "a", "b", "c", "&#945", "&#946", "&#947", "Volume"])
        import HTML
        htmlcif = HTML.table(ciffull)
        fc = open(os.path.join(dir, "List_of_X_ray_structures_PDB.html"), 'w')
        fc.write(htmlcif)
        fc.close()
        self.openweb(event, os.path.join(dir, "List_of_X_ray_structures_PDB.html"))
        self.SetStatusText(
            os.path.join(dir, "List_of_X_ray_structures_PDB.html") + " has been saved in " + dir + " directory")

    def getinfosca(self, event):
        sca, dir = self.getsca(event)
        ciffull = []
        for filename in sca:
            briefs = []
            if len(filename) > 100:
                briefs.append("<a href=" + filename + ">" + filename[0:25] + "~" + filename[75:] + "</a>")
            else:
                briefs.append("<a href=" + filename + ">" + filename + "</a>")
            try:
                temp = open(filename, 'r').readlines()
                temp = temp[2]
                crystlist = temp.split()
                a = crystlist[0]
                b = crystlist[1]
                c = crystlist[2]
                alpha = crystlist[3]
                beta = crystlist[4]
                gamma = crystlist[5]
                space = crystlist[6]
                vol = float(a) * float(b) * float(c)
                briefs.extend((a, b, c, alpha, beta, gamma, str(round(vol, 3)), space))
                if len(briefs) > 2:
                    ciffull.append(briefs)
            except IndexError:
                pass
        ciffull.insert(0, ["PDB File", "a", "b", "c", "&#945", "&#946", "&#947", "Volume", "Space Group"])
        import HTML
        htmlcif = HTML.table(ciffull)
        fc = open(os.path.join(dir, "List_of_X_ray_structures_SCA.html"), 'w')
        fc.write(htmlcif)
        fc.close()
        self.openweb(event, os.path.join(dir, "List_of_X_ray_structures_SCA.html"))
        self.SetStatusText(
            os.path.join(dir, "List_of_X_ray_structures_SCA.html") + " has been saved in " + dir + " directory")

    def getinfop4p(self, event):
        p4p, dir = self.getp4p(event)
        ciffull = []
        for filename in p4p:
            briefs = []
            if len(filename) > 100:
                briefs.append("<a href=" + filename + ">" + filename[0:25] + "~" + filename[75:] + "</a>")
            else:
                briefs.append("<a href=" + filename + ">" + filename + "</a>")
            try:
                temp = open(filename, 'r').readlines()
                temp = temp[0:10]
                for i, p4pline in enumerate(temp):
                    if p4pline.startswith("CHEM"):
                        briefs.append((p4pline.split()[1]).replace("\r", "").replace("\n", ""))
                    elif p4pline.startswith("CELL "):
                        crystlist = p4pline.split()
                        a = crystlist[1]
                        b = crystlist[2]
                        c = crystlist[3]
                        alpha = crystlist[4]
                        beta = crystlist[5]
                        gamma = crystlist[6]
                        vol = crystlist[7]

                        briefs.extend((a, b, c, alpha, beta, gamma, vol))
                if len(briefs) > 2:
                    ciffull.append(briefs)
            except IndexError:
                pass
        ciffull.insert(0, ["P4P File", "Formula", "a", "b", "c", "&#945", "&#946", "&#947", "Volume"])
        import HTML
        htmlcif = HTML.table(ciffull)
        fc = open(os.path.join(dir, "List_of_X_ray_structures_P4P.html"), 'w')
        fc.write(htmlcif)
        fc.close()
        self.openweb(event, os.path.join(dir, "List_of_X_ray_structures_P4P.html"))
        self.SetStatusText(
            os.path.join(dir, "List_of_X_ray_structures_P4P.html") + " has been saved in " + dir + " directory")

    def getinfocif(self, event):

        cifs, dir = self.getcifs(event)
        # print dir
        ciffull = []
        for filename in cifs:
            briefs = []
            briefs.append("<a href=" + filename + ">" + filename + "</a>")
            temp = open(filename, 'r').readlines()
            for i, cifline in enumerate(temp):
                cifline = cifline.replace("\r", "").replace("\n", "")
                #                if cifline.startswith("data_"):
                #                    briefs.append(("Data_Name="+cifline).replace("data_","").replace(" ",""))
                if cifline.startswith("_chemical_formula_sum"):
                    briefs.append((temp[i + 1]).replace("\r", "").replace("\n", ""))
                elif cifline.startswith("_cell_length_a"):
                    briefs.append((("a=" + cifline).replace("_cell_length_a", "")).replace(" ", ""))
                elif cifline.startswith("_cell_length_b"):
                    briefs.append((("b=" + cifline).replace("_cell_length_b", "")).replace(" ", ""))
                elif cifline.startswith("_cell_length_c"):
                    briefs.append((("c=" + cifline).replace("_cell_length_c", "")).replace(" ", ""))
                elif cifline.startswith("_cell_angle_alpha"):
                    briefs.append((("&#945=" + cifline).replace("_cell_angle_alpha", "")).replace(" ", ""))
                elif cifline.startswith("_cell_angle_beta"):
                    briefs.append((("&#946=" + cifline).replace("_cell_angle_beta", "")).replace(" ", ""))
                elif cifline.startswith("_cell_angle_gamma"):
                    briefs.append((("&#947=" + cifline).replace("_cell_angle_gamma", "")).replace(" ", ""))
                elif cifline.startswith("_cell_volume"):
                    briefs.append((("V=" + cifline).replace("_cell_volume", "")).replace(" ", ""))
                elif cifline.startswith("_diffrn_measured_fraction_theta_full"):
                    briefs.append(((cifline).replace("_diffrn_measured_fraction_theta_full", "")).replace(" ", ""))
            if len(briefs) > 2:
                ciffull.append(briefs)

        ciffull.insert(0, ["Cif File", "Formula", "a", "b", "c", "&#945", "&#946", "&#947", "Volume", "Completness"])
        import HTML
        htmlcif = HTML.table(ciffull)
        fc = open(os.path.join(dir, "List_of_X_ray_structures_CIF.html"), 'w')
        fc.write(htmlcif)
        fc.close()
        self.openweb(event, os.path.join(dir, "List_of_X_ray_structures_CIF.html"))
        self.SetStatusText(
            os.path.join(dir, "List_of_X_ray_structures_CIF.html") + " has been saved in " + dir + " directory")

    def openweb(self, event, htmfile):
        webbrowser.open(htmfile)

    def getcifs(self, event):
        ciflist = []
        try:
            dlg = wx.DirDialog(self, "Choose a directory with all structures:",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                scandir = str(dlg.GetPath())
                try:
                    for dirpath, dirnames, filenames in os.walk(str(dlg.GetPath())):
                        for filename in filenames:
                            if (filename.lower()).endswith(".cif"):
                                ciflist.append(os.path.join(dirpath, filename))
                except UnicodeEncodeError:
                    pass
            return ciflist, scandir
        except OSError:
            pass

    def getpdb(self, event):
        ciflist = []
        try:
            dlg = wx.DirDialog(self, "Choose a directory with all structures:",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                try:
                    scandir = str(dlg.GetPath())
                    for dirpath, dirnames, filenames in os.walk(str(dlg.GetPath())):
                        for filename in filenames:
                            if (filename.lower()).endswith(".pdb"):
                                ciflist.append(os.path.join(dirpath, filename))
                except UnicodeEncodeError:
                    pass

            return ciflist, scandir
        except OSError:
            pass

    def getsca(self, event):
        ciflist = []
        try:
            dlg = wx.DirDialog(self, "Choose a directory with all structures:",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                try:
                    scandir = str(dlg.GetPath())
                    for dirpath, dirnames, filenames in os.walk(str(dlg.GetPath())):
                        for filename in filenames:
                            if (filename.lower()).endswith(".sca"):
                                ciflist.append(os.path.join(dirpath, filename))
                except UnicodeEncodeError:
                    pass

            return ciflist, scandir
        except OSError:
            pass

    def getp4p(self, event):
        try:
            dlg = wx.DirDialog(self, "Choose a directory with all structures:",
                               style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
            if dlg.ShowModal() == wx.ID_OK:
                try:
                    ciflist = []
                    scandir = str(dlg.GetPath())
                    for dirpath, dirnames, filenames in os.walk(str(dlg.GetPath())):
                        for filename in filenames:
                            if (filename.lower()).endswith(".p4p"):
                                ciflist.append(os.path.join(dirpath, filename))
                except UnicodeEncodeError:
                    pass

            return ciflist, scandir
        except OSError:
            pass

    def onTar(self, event):  # wxGlade: MyFrame.<event_handler>
        list = []
        listext = ['.res', '.ins', "lin.tmp", '.hkl', '.ps', 'pdf', '.png', '.eps', '.tif', '.html', '.sqf', '.sqz',
                   'htm', '.jpg', '.p4p', '.hkp', '.tex', '.rtf', '.res.bk', '.tbl', '.cif', '.lst', '.sqf', '.sqz',
                   'pcf', 'fab']
        os.chdir(self.dirname)
        try:
            for file in os.listdir(self.dirname):
                for i in listext:
                    if file.endswith(i):
                        list1 = list.append(file)
                        x = 0

            while os.path.exists(os.path.join(self.filenamenoext + str(x)) + ".zip"):
                x += 1

            t = zipfile.ZipFile(os.path.join(self.filenamenoext + str(x)) + ".zip", 'w',
                                compression=zipfile.ZIP_DEFLATED)
            for i in list:
                t.write(i)
            t.close()
            self.SetStatusText(
                "files with extentions res, ins, hkl, hkp, res.bk, tbl, cif, lst, sqf and sqz were added to archive")
        except OSError:
            pass

    def onQuit(self, event):  # wxGlade: MyFrame.<event_handler>
        if self.Modified(event):
            self.Destroy()

    def Modified(self, event):
        # check if file has been modified

        if self.text.GetModify():
            #            if self.onSave(event)!=True:
            dialog = wx.MessageDialog(self, "File was modified! Do you want to save it?", "Save changes?",
                                      wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
            dialog.Centre()
            result = dialog.ShowModal()
            dialog.Destroy()
            if result == wx.ID_YES:
                self.onSave(event)
                return True
            elif result == wx.ID_NO:
                return True
            else:
                return False

        return True

    def onCloselin(self, event):
        if self.Modified(event):
            # # print"quit"
            self.Destroy()

    def stats(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(os.path.join(self.dirname, 'stats.txt')) == True:
            st = open(os.path.join(self.dirname, 'stats.txt'), 'r')
            stats = st.read()
            st.close()

            dlg = wx.lib.dialogs.ScrolledMessageDialog(self, stats,
                                                       'Stats', size=(650, 600))
            dlg.ShowModal()
            dlg.Destroy()
        else:
            wx.MessageBox('No statistics available for this structure.', 'Error',
                          wx.OK | wx.ICON_INFORMATION)

    def ziprestore(self, event):  # wxGlade: MyFrame.<event_handler>
        zips = []
        for file in os.listdir(self.dirname):
            if file.endswith(".zip"):
                zips.append(file)
        if len(zips) == 0:
            wx.MessageBox('No backup', 'Error',
                          wx.OK | wx.ICON_INFORMATION)
        else:
            zips = sorted(zips, key=self.onsortkeys)
            dlg = wx.lib.dialogs.MultipleChoiceDialog(self, "Select backup to restore",
                                                      "Backups", zips, size=(500, 600))
            if (dlg.ShowModal() == wx.ID_OK):
                zippath = os.path.join(self.dirname, "".join(dlg.GetValueString()))
                t = zipfile.ZipFile(zippath, compression=zipfile.ZIP_DEFLATED)
                dlg.Destroy()
                for name in t.namelist():
                    t.extract(name, self.dirname)
                self.onReload(event)

    def onstats(self, event):
        stats = open(os.path.join(self.dirname, "stats.txt"), 'a')
        out = self.getrf()
        if len(out) <= 10:
            out = "Refinement Error"
            stats.writelines(out + '\n')
        else:
            stats.writelines(out + '\n')
        stats.close()

    def getrf(self):
        if os.path.exists(self.fnoe + ".lst") == True:
            if os.path.getsize(self.fnoe + ".lst") != 0:
                lst = open(self.fnoe + ".lst", 'r')
                lstread = lst.read()
                lst.close()
                num = lstread.find("Final Structure Factor")
                rlnum = lstread.find("R1 =", num)
                wrnum = lstread.find("wR2 =", num)
                goofnum = lstread.find("GooF = S =", num)
                rl = (lstread[rlnum:rlnum + 13]).replace(" ", "") + "  "
                wr = (lstread[wrnum:wrnum + 13]).replace(" ", "") + "  "
                goof = (lstread[goofnum:goofnum + 20]).replace(" ", "") + "  "
                out = rl + wr + goof
                return out

    def prdevices(self, event):
        try:
            if self.ossystem.startswith("win"):
                webbrowser.open(os.path.join(self.path, "user", "device"))
            elif self.ossystem.startswith('darwin'):
                subprocess.Popen(['open', os.path.join(self.path, "user", "device")])
            else:
                webbrowser.open(os.path.join(self.path, "user", "device"))
        #              subprocess.Popen("xdg-open"' ' +  os.path.join(self.path, "user", "device"), shell=True)
        except OSError:
            pass

    def pruser(self, event):
        try:
            if self.ossystem.startswith("win"):
                webbrowser.open(os.path.join(self.path, "user"))
            elif self.ossystem.startswith('darwin'):
                subprocess.Popen(['open', os.path.join(self.path, "user")])
            else:
                webbrowser.open(os.path.join(self.path, "user"))
        #              subprocess.Popen("xdg-open"' ' +  os.path.join(self.path, "user", "device"), shell=True)
        except OSError:
            pass

    def prtable(self, event):
        if self.ossystem.startswith("win"):
            webbrowser.open('file://%s' % os.path.join(self.path, "user", "FullTable_2013.rtf"))
        else:
            webbrowser.open('file://%s' % os.path.join(self.path, "user", "FullTable_2013.rtf"))

    def onOlex(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoolex, "'" + self.fnoe + ".res" + "'"])
        elif self.ossystem.startswith("darwin"):
            subprocess.call(['open', '-a', self.phtoolex, self.fnoe + ".res"])
        else:
            if self.phtoolex.endswith("start"):
                f = open(os.path.join(self.path, "bin", "somescripts", "olex"), 'r')
                fr = f.read()
                f.close()
                fi = open(self.phtoolex, 'w')
                fi.write(fr)
                fi.close()
            subprocess.Popen([self.phtoolex, self.fnoe + ".res"])

    def onCoot(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtocoot, '--coord', self.fnoe + ".res", '--data', self.fnoe + ".fcf"])
        elif self.ossystem.startswith("darwin"):
            subprocess.call(['open', '-a', self.phtocoot, '--coord', self.fnoe + ".res", '--data', self.fnoe + ".fcf"])
        else:
            subprocess.Popen([self.phtocoot, '--coord', self.fnoe + ".res", '--data', self.fnoe + ".fcf"])

    def onelix(self, event):  # wxGlade: MyFrame.<event_handler>
        if os.path.exists(self.fnoe + ".pdb"):
            try:
                if self.ossystem.startswith("win"):
                    subprocess.Popen(
                        [sys.executable, os.path.join(self.path, 'vtkelix', 'elix.py'), self.fnoe + ".pdb"])
                else:
                    subprocess.Popen(
                        [sys.executable, os.path.join(self.path, 'vtkelix', 'elix.py'), self.fnoe + ".pdb"])
            except OSError:
                pass
        else:
            dlg = wx.MessageDialog(self, self.fnoe + ".pdb file was not found",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onAvogadro(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoavogadro, self.fnoe + ".cif"])
        elif self.ossystem.startswith("darwin"):
            subprocess.call(['open', '-a', self.phtoavogadro, self.fnoe + ".cif"])
        else:
            subprocess.Popen([self.phtoavogadro, self.fnoe + ".cif"])

    def anycif(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoanycif, self.fnoe + ".cif"])
        elif self.ossystem.startswith("darwin"):
            subprocess.call(['open', '-a', self.phtoanycif, self.fnoe + ".cif"])
        else:
            subprocess.Popen([self.phtoanycif, self.fnoe + ".cif"])

    def onPyMol(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtopymol, self.fnoe + ".pdb"])
        elif self.ossystem.startswith("darwin"):
            subprocess.call(['open', '-a', self.phtopymol, self.fnoe + ".pdb"])
        else:
            subprocess.Popen([self.phtopymol, self.fnoe + ".pdb"])

    def onMercury(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtomercury, self.fnoe + ".cif"])
        elif self.ossystem.startswith("darwin"):
            subprocess.call(['open', '-a', self.phtomercury, self.fnoe + ".cif"])
        else:
            subprocess.Popen([self.phtomercury, self.filenamenoext + ".cif"])

    def ontwinabs(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtotwinabs, self.fnoe + ".p4p"])
        else:
            subprocess.Popen([self.phtotwinabs, self.fnoe + ".p4p"])

    def ondrawxtl(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtodrawxtl, self.fnoe + ".cif"])
        else:
            subprocess.Popen([self.phtodrawxtl, self.fnoe + ".cif"])

    def onjmol(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtojmol, self.fnoe + ".pdb"])
        else:
            subprocess.Popen([self.phtojmol, self.fnoe + ".pdb"])

    def onortep3(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoortep3, self.fnoe + ".cif"])
        else:
            dir = (os.path.dirname(self.phtoortep3)).replace(' ', '\ ')
            if os.path.exists("/opt/cxoffice/bin/wine") == True:
                script = '#!/bin/bash' + '\n' + 'export ORTEP3DIR=' + dir + '\n' + '/opt/cxoffice/bin/wine' + ' ' + self.phtoortep3.replace(
                    ' ', '\ ') + ' ' + self.fnoe + ".cif"
                subprocess.Popen(script, shell=True)
            elif os.path.exists(self.phtowine) == True:
                script = '#!/bin/bash' + '\n' + 'export ORTEP3DIR=' + dir + '\n' + self.phtowine + ' ' + self.phtoortep3.replace(
                    ' ', '\ ') + ' ' + self.fnoe + ".cif"
                subprocess.Popen(script, shell=True)
            elif os.path.exists("/usr/bin/wine") == True:
                script = '#!/bin/bash' + '\n' + 'export ORTEP3DIR=' + dir + '\n' + '/usr/bin/wine' + ' ' + self.phtoortep3.replace(
                    ' ', '\ ') + ' ' + self.fnoe + ".cif"
                subprocess.Popen(script, shell=True)
            else:
                dlg = wx.MessageDialog(self,
                                       "Error!!! Wine or Crossover Office was not found on this computer. To install wine type in terminal: su -c yum install wine (Fedora) or: sudo apt-get install wine (Ubuntu)",
                                       'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

    def ondiamond(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen(self.phtodiamond + ' ' + self.fnoe + ".cif")
        else:
            if os.path.exists("/opt/cxoffice/bin/wine") == True:
                subprocess.Popen(["/opt/cxoffice/bin/wine", self.phtodiamond, self.fnoe + ".cif"])
            elif os.path.exists(self.phtowine) == True:
                subprocess.Popen([self.phtowine, self.phtodiamond, self.fnoe + ".cif"])
            else:
                dlg = wx.MessageDialog(self,
                                       "Error!!! Wine or Crossover Office was not found on this computer. To install wine type in terminal: su -c yum install wine (Fedora) or: sudo apt-get install wine (Ubuntu)",
                                       'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

    def onChimera(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtochimera, self.fnoe + ".cif"])
        elif self.ossystem.startswith("darwin"):
            subprocess.call(['open', '-a', self.phtochimera, self.fnoe + ".cif"])
        else:
            subprocess.Popen([self.phtochimera, self.fnoe + ".cif"])

    def onsupersadabs(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtosupersadabs, self.fnoe + ".p4p"])
        else:
            if os.path.exists("/opt/cxoffice/bin/wine") == True:
                subprocess.Popen(["/opt/cxoffice/bin/wine", self.phtosupersadabs, self.fnoe + ".p4p"])
            elif os.path.exists(self.phtowine) == True:
                subprocess.Popen([self.phtowine, self.phtosupersadabs, self.fnoe + ".p4p"])
            else:
                dlg = wx.MessageDialog(self,
                                       "Error!!! Wine or Crossover Office was not found on this computer. To install wine type in terminal: su -c yum install wine (Fedora) or: sudo apt-get install wine (Ubuntu)",
                                       'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

    def ondirdif(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtodirdif, self.fnoe + ".res"])
        else:
            if os.path.exists("/opt/cxoffice/bin/wine") == True:
                subprocess.Popen(["/opt/cxoffice/bin/wine ", self.phtodirdif, self.fnoe + ".res"])
            elif os.path.exists(self.phtowine) == True:
                subprocess.Popen([self.phtowine, self.phtodirdif, self.fnoe + ".res"])
            else:
                dlg = wx.MessageDialog(self,
                                       "Error!!! Wine or Crossover Office was not found on this computer. To install wine type in terminal: su -c yum install wine (Fedora) or: sudo apt-get install wine (Ubuntu)",
                                       'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

    def onenCifer(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoencifer, self.fnoe])
        else:
            subprocess.Popen([self.phtoencifer, self.fnoe + ".cif"])

    def onsxgraph(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtosxgraph, self.fnoe + ".res"])
        else:
            if os.path.exists("/opt/cxoffice/bin/wine") == True:
                subprocess.Popen(["/opt/cxoffice/bin/wine", self.phtosxgraph, self.fnoe + ".res"])
            elif os.path.exists(self.phtowine) == True:
                # print self.phtosxgraph
                subprocess.call([self.phtowine, self.phtosxgraph, self.fnoe + '.res'])
            else:
                dlg = wx.MessageDialog(self,
                                       "Error!!! Wine or Crossover Office was not found on this computer. To install wine type in terminal: su -c yum install wine (Fedora) or: sudo apt-get install wine (Ubuntu)",
                                       'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

    #            subprocess.Popen([self.phtosxgraph, self.fnoe+".cif"])
    def onxseed(self, event):
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoxseed, self.fnoe + ".res"])
        else:
            if os.path.exists("/opt/cxoffice/bin/wine") == True:
                subprocess.Popen(["/opt/cxoffice/bin/wine", self.phtoxseed, self.fnoe + ".res"])
            elif os.path.exists(self.phtowine) == True:
                # print self.phtosxgraph
                subprocess.call([self.phtowine, self.phtoxseed, self.fnoe + '.res'])
            else:
                dlg = wx.MessageDialog(self,
                                       "Error!!! Wine or Crossover Office was not found on this computer. To install wine type in terminal: su -c yum install wine (Fedora) or: sudo apt-get install wine (Ubuntu)",
                                       'Error', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()

    def onUndo(self, event):
        print('undo in action')
        num = self.notebook_1.GetSelection()
        if num == 0:
            self.topline = self.text.GetFirstVisibleLine()
            if self.text.CanUndo():
                self.text.Undo()
                self.text.ScrollToLine(self.topline)

        if num == 1:
            self.topline = self.text2.GetFirstVisibleLine()
            if self.text2.CanUndo():
                self.text2.Undo()
                self.text2.ScrollToLine(self.topline)
        if num == 2:
            self.topline = self.text3.GetFirstVisibleLine()
            if self.text3.CanUndo():
                self.text3.Undo()
                self.onColor1(event)
                self.text3.ScrollToLine(self.topline)
        if num == 3:
            self.topline = self.text4.GetFirstVisibleLine()
            if self.text4.CanUndo():
                self.text4.Undo()
                self.onColor1(event)
                self.text4.ScrollToLine(self.topline)
        self.onColor1(event)

    def onRedu(self, event):

        num = self.notebook_1.GetSelection()
        if num == 0:
            self.topline = self.text.GetFirstVisibleLine()
            if self.text.CanRedo():
                self.text.Redo()
                self.onColor1(event)
                self.text.ScrollToLine(self.topline)

        if num == 1:
            self.topline = self.text2.GetFirstVisibleLine()
            if self.text2.CanRedo():
                self.text2.Redo()
                self.onColor1(event)
                self.text2.ScrollToLine(self.topline)

        if num == 2:
            self.topline = self.text3.GetFirstVisibleLine()
            if self.text3.CanRedo():
                self.text3.Redo()
                self.onColor1(event)
                self.text3.ScrollToLine(self.topline)
        if num == 3:
            self.topline = self.text4.GetFirstVisibleLine()
            if self.text4.CanRedo():
                self.text4.Redo()
                self.onColor1(event)
                self.text4.ScrollToLine(self.topline)

    def onCut(self, event):  # wxGlade: MyFrame.<event_handler>
        self.num = self.notebook_1.GetSelection()
        self.text.BeginUndoAction()
        self.topline = self.text.GetFirstVisibleLine()
        self.text.ScrollToLine(self.topline)
        self.text.EndUndoAction()
        if self.num == 1:
            self.text2.Cut()
        elif self.num == 2:
            self.text3.Cut()
        elif self.num == 3:
            self.text4.Cut()
        elif self.num == 0:
            self.text.Cut()

    def ClearClipboard(self, event):
        print(wx.TheClipboard.IsOpened())
        if wx.TheClipboard.IsOpened():
            wx.TheClipboard.Clear()
        else:
            wx.TheClipboard.Open()
            wx.TheClipboard.Clear()
        wx.TheClipboard.Close()


    def CopyClipboard(self, event, ctext):
        self.clipborddata = ""
        self.dataObj = wx.TextDataObject()
        text = ctext.GetSelectedText()
        self.clipborddata = text
        self.dataObj.SetText(text)
        self.ClearClipboard(event)
        if wx.TheClipboard.IsOpened():
            wx.TheClipboard.SetData(self.dataObj)
            print("opennn", text, self.dataObj)
            # wx.TheClipboard.Flush()
            wx.TheClipboard.Close()
        else:
            wx.TheClipboard.Open()
            wx.TheClipboard.SetData(self.dataObj)
            print("opennn", text, self.dataObj)
            # wx.TheClipboard.Flush()
            wx.TheClipboard.Close()


    def pastefunction(self, ctext):

        clipdata = wx.TextDataObject()
        wx.TheClipboard.GetData(clipdata)
        if clipdata.GetText():
            ctext.AddText(clipdata.GetText())
            wx.TheClipboard.Close()
        else:

            clipdata.SetText(self.clipborddata)
            ctext.AddText(self.clipborddata)
            wx.TheClipboard.Close()

    def PasteClipboard(self, event, ctext):
            if wx.TheClipboard.IsOpened():
                self.pastefunction(ctext)
            else:
                wx.TheClipboard.Open()
                self.pastefunction(ctext)


    def onCopy(self, event):  # wxGlade: MyFrame.<event_handler>
        self.num = self.notebook_1.GetSelection()
        print(self.num)
        if self.num == 2:
            self.CopyClipboard(event, self.text3)
        elif self.num == 1:
            self.CopyClipboard(event, self.text2)
        elif self.num == 3:
            self.CopyClipboard(event, self.text4)
        elif self.num == 0:
            self.CopyClipboard(event, self.text)

            # self.text.Copy()
            # self.text.Copy()
            # self.text.Copy()
            # self.Copy()


    def onPaste(self, event):  # wxGlade: MyFrame.<event_handler>
        print("paste")
        self.text.BeginUndoAction()
        self.topline = self.text.GetFirstVisibleLine()
        self.num = self.notebook_1.GetSelection()
        self.text.ScrollToLine(self.topline)
        self.text.EndUndoAction()
        if self.num == 1:
            self.PasteClipboard(event, self.text2)
        if self.num == 2:
            self.PasteClipboard(event, self.text3)
        if self.num == 3:
            self.PasteClipboard(event, self.text4)
        if self.num == 0:
            # self.text.Paste()
            self.PasteClipboard(event, self.text)

    def onSELECT(self, event):  # wxGlade: MyFrame.<event_handler>
        self.text.SelectAll()

    def onDelete(self, event):  # wxGlade: MyFrame.<event_handler>
        self.num = self.notebook_1.GetSelection()
        self.text.BeginUndoAction()
        self.topline = self.text.GetFirstVisibleLine()
        self.text.ScrollToLine(self.topline)
        self.text.EndUndoAction()
        if self.num == 2:
            self.text3.Clear()
        elif self.num == 1:
            self.text2.Clear()
        elif self.num == 3:
            self.text4.Clear()
        elif self.num == 0:
            self.text.Clear()

    def onfonts(self, event):
        dialog = wx.FontDialog(None, wx.FontData())
        if dialog.ShowModal() == wx.ID_OK:
            data = dialog.GetFontData()
            font = data.GetChosenFont()
            colour = data.GetColour()
            # print 'You selected: "%s", %d points\n' % (font.GetFaceName(), font.GetPointSize())
            textfont = font.GetFaceName()
            fulltext = self.text.GetText()
            self.text.StyleSetSpec(0, 'fore:#000000, back:#FFFFFF, face:' + textfont + ', size:13')
            for item in fulltext:
                self.text.StartStyling(0, 0)
                self.text.SetStyling(len(item), 0)

    def onCopyrti(self, event):  # wxGlade: MyFrame.<event_handler>
        #          self.onSave(event)
        shutil.copy2(self.fnoe + '.res', self.fnoe + '.ins')
        self.onReload(event)
        #          if  self.ossystem.startswith("lin"):
        #             self.restoins.SetBackgroundColour(wx.Colour(172,248,181))
        self.SetStatusText(self.fnoe + ".res" + " was copied to " + self.fnoe + ".ins")

    def onCopyitr(self, event):  # wxGlade: MyFrame.<event_handler>
        shutil.copy2(self.fnoe + '.ins', self.fnoe + '.res')
        self.onReload(event)
        # self.getpcf(event)

    ################# pcf file######################################
    # def getpcf(self, event):
    #     if os.path.exists(self.fnoe+'.p4p'.lower())==True:
    #         if os.path.exists(self.fnoe+'.pcf'.lower())==True:
    #            event.Skip()
    #         else:
    #           self.descriptp4p(event)
    #
    # def descriptp4p(self,event):
    #        # # print"pcf"
    #         listnumber=[]
    #         phpopen=open(self.fnoe+'.p4p','r')
    #         phpopen.close()
    #         pcfsyn=["_symmetry_cell_setting", "_chemical_formula_moiety", "_cell_formula_units_Z",
    #         "_symmetry_space_group_name_H-M", "_cell_measurement_temperature",
    #         "_cell_measurement_reflns_used", "_refine_ls_hydrogen_treatment",
    #         "_exptl_absorpt_process_details", "_cell_measurement_theta_min",
    #         "_cell_measurement_theta_max", "_exptl_crystal_description",
    #         "_exptl_crystal_colour", "_exptl_crystal_size_min",
    #         "_exptl_crystal_size_mid", "_exptl_crystal_size_max", "_exptl_crystal_density_meas",
    #         "_exptl_crystal_density_method", "_exptl_absorpt_correction_type",
    #         "_exptl_absorpt_correction_T_min", "_exptl_absorpt_correction_T_max",
    #         "_diffrn_ambient_temperature", "_diffrn_radiation_type",
    #         "_diffrn_radiation_source", "_diffrn_radiation_monochromator",
    #         "_diffrn_measurement_device_type", "_diffrn_measurement_method",
    #         "_diffrn_detector_area_resol_mean", "_diffrn_standards_number",
    #         "_diffrn_standards_interval_count", "_diffrn_standards_decay_%",
    #         "_computing_data_collection", "_computing_cell_refinement",
    #         "_computing_data_reduction", "_computing_structure_solution",
    #         "_computing_structure_refinement", "_computing_molecular_graphics",
    #         "_computing_publication_material"]

    def capital(self, event):
        if self.filename.lower().endswith(".res") or self.filename.lower().endswith(".ins"):
            text = self.text.GetText()
            for word in definitions.shelx_commands:
                if text.find(word.lower()) != -1:
                    self.replacetext(event, word.lower(), word)

    def onFinal(self, event):  # wxGlade: MyFrame.<event_handler>
        self.capital(event)
        self.onDelq(event)
        self.topline = self.text.GetFirstVisibleLine()
        text = self.text.GetText()
        tx = text.split("\n")
        list = []
        key = ["BOND", "PLAN", "RIGU", "ACTA", "CONF", "WPDB", "HTAB"]
        key1 = ["WPDB -1", "RIGU", "BOND $H", "PLAN 0", "ACTA", "CONF", "HTAB"]
        loc1 = 7
        try:
            self.getunitlst(event)
        except IndexError:
            pass

        if "L.S." not in text:
            dlg = wx.MessageDialog(self, "No L.S. statement in the res file found",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

        if "TEMP" in text:
            for line in tx:
                if "TEMP" in line:
                    x = line.replace("TEMP", "").replace(" ", "")
                    x = float(x)
                    if x > 0:
                        doit = wx.MessageDialog(self, "Temperature is higer than 0. Is temperature correct?", "Check!",
                                                wx.YES_NO)
                        igot = doit.ShowModal()  # Shows it
                        if igot == wx.ID_YES:
                            for line in tx:
                                if line.startswith("L.S."):
                                    loc1 = tx.index(line)
                                    tx.remove(line)
                                    tx.insert(loc1, "L.S. 20")
                            for k in key:
                                for line in tx:
                                    if line.startswith(k):
                                        tx.remove(line)
                            for k1 in key1:
                                tx.insert(loc1 + 1, k1)

                                #            self.onRefW(event)
                        else:
                            break
                    else:

                        for line in tx:
                            if line.startswith("L.S."):
                                loc1 = tx.index(line)
                                tx.remove(line)
                                tx.insert(loc1, "L.S. 20")
                        for k in key:
                            for line in tx:
                                if line.startswith(k):
                                    tx.remove(line)
                        for k1 in key1:
                            tx.insert(loc1 + 1, k1)

        else:
            dlg = wx.MessageDialog(self, "No TEMP statement in the res file found", 'Error',
                                   wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
        ready = '\n'.join(tx)
        self.text.BeginUndoAction()
        self.text.SetText(ready)

        self.text.EndUndoAction()
        self.onColor1(event)
        self.text.ScrollToLine(0)
        self.SetStatusText('Final setting  completed')
        doit = wx.MessageDialog(self, "Do you want to proceed to refinement? ", "Refine ???", wx.YES_NO)
        igot = doit.ShowModal()  # Shows it
        if igot == wx.ID_YES:
            self.onSave(event)
            self.onCopyrti(event)
            self.onXL(event)
        self.onColor1(event)
        self.text.ScrollToLine(0)

    def onInvers(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        text = self.text.GetText()
        tx = text.split("\n")
        ## print tx
        for line in tx:
            if line.startswith("UNIT"):
                loc1 = tx.index(line)
                tx.insert(loc1 + 2, "MOVE 1 1 1 -1")
        ready = '\n'.join(tx)
        self.text.SetText(ready)
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

    #    def striplist(self, l):
    #       # # print"stripped", ([x.strip(' ') for x in l])
    #        return([x.strip(' ') for x in l])
    def ISOTR(self, event):
        text = self.text.GetText()
        listd = ["AFIX", "H"]
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        foundh = seltext.find("AFIX")
        pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
        if len(seltext) == 0:
            doit = wx.MessageDialog(self,
                                    "Do you want to delete the anisotropic displacement parameters for all atoms?\n",
                                    "Remove?", wx.YES_NO)
            igot = doit.ShowModal()  # Shows it
            if igot == wx.ID_YES:
                foundh = text.find("AFIX")
                tx = text.split("\n")
                goodlist = {}
                length = len(tx)
                for index, item in reversed(
                        list(enumerate(tx))):  ################### Removing items from list starting from the end
                    if not item.upper().startswith('SFAC'):
                        if '=' in item:
                            tx.pop(index + 1)
                        if "created by" in item:
                            tx.pop(index)
                for line in tx:
                    if pattern.match(line):
                        loc2 = tx.index(line)
                        getgoodone = ((line.strip()).split())[0:7]
                        getready = '   '.join(getgoodone)
                        tx.remove(line)
                        tx.insert(loc2, getready)
                if foundh != -1:
                    doit = wx.MessageDialog(self, "Do you want to delete hydrogen atoms as well?\n", "Remove?",
                                            wx.YES_NO)
                    igot = doit.ShowModal()  # Shows it
                    if igot == wx.ID_YES:
                        i = 0
                        while (i < 10):
                            for line in tx:
                                for item in listd:
                                    if "HKLF" not in line:
                                        if line.startswith(item):
                                            tx.remove(line)
                            i = i + 1
                        ready = '\n'.join(tx)
                        self.text.BeginUndoAction()
                        self.text.ClearAll()
                        # # printself.topline
                        self.text.SetText(ready)
                        self.text.EndUndoAction()


                    else:
                        ready = '\n'.join(tx)
                        self.text.BeginUndoAction()
                        self.text.ClearAll()
                        # # printself.topline
                        self.text.SetText(ready)
                        self.text.EndUndoAction()
                        self.onColor1(event)

                else:
                    ready = '\n'.join(tx)
                    self.text.BeginUndoAction()
                    self.text.ClearAll()
                    self.text.SetText(ready)
                    self.text.EndUndoAction()


        else:

            frm, to = self.text.GetSelection()
            tx = seltext.split("\n")
            for index, item in reversed(
                    list(enumerate(tx))):  ################### Removing items from list starting from the end
                if not item.upper().startswith('SFAC'):
                    if '=' in item:
                        tx.pop(index + 1)

            for line in tx:
                if not line.startswith(
                        ("CELL", "FVAR", "SADI", "SIMU", "DELU", "EADP", "TITL", "HKLF", "ZERR", "SFAC", "UNIT")):
                    loc2 = tx.index(line)
                    getgoodone = ((line.strip()).split())[0:7]
                    getready = '   '.join(getgoodone)
                    tx.remove(line)
                    tx.insert(loc2, getready)
            if foundh != -1:
                doit = wx.MessageDialog(self, "Do you want to delete hydrogen atoms as well?\n", "Reload file ...",
                                        wx.YES_NO)
                igot = doit.ShowModal()  # Shows it
                if igot == wx.ID_YES:
                    i = 0
                    while (i < 10):
                        for line in tx:
                            for item in listd:
                                if "HKLF" not in line:
                                    if line.startswith(item):
                                        tx.remove(line)
                        i = i + 1
                    self.text.BeginUndoAction()
                    ready = '\n'.join(tx)
                    b, e = self.text.GetSelection()
                    lb = self.textsize(seltext)
                    self.text.ReplaceSelection(ready)
                    self.text.EndUndoAction()
                    le = self.textsize(ready)
                    diff = int(lb) - int(le)
                    self.text.SetSelection(b, e - diff)
                else:
                    ready = '\n'.join(tx)
                    self.text.BeginUndoAction()
                    b, e = self.text.GetSelection()
                    lb = self.textsize(seltext)
                    self.text.ReplaceSelection(ready)
                    self.text.EndUndoAction()
                    le = self.textsize(ready)
                    diff = int(lb) - int(le)
                    self.text.SetSelection(b, e - diff)
            else:
                ready = '\n'.join(tx)
                self.text.BeginUndoAction()
                b, e = self.text.GetSelection()
                lb = self.textsize(seltext)
                self.text.ReplaceSelection(ready)
                self.text.EndUndoAction()
                le = self.textsize(ready)
                diff = int(lb) - int(le)
                self.text.SetSelection(b, e - diff)

        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

    def HDEL(self, event):
        listd = ['AFIX']
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        if len(seltext) < 10:
            doit = wx.MessageDialog(self, "Do you want to delete all hydrogen atoms ?\n", "Reload file ...", wx.YES_NO)
            igot = doit.ShowModal()  # Shows it
            if igot == wx.ID_YES:
                text = self.text.GetText()
                tx = text.split("\n")
                # print "gooooooo"
                i = 0
                while (i < 6):
                    for line in tx:
                        #                                for number in range(1,10):
                        if line.startswith("H"):
                            if line[1].isdigit():
                                tx.remove(line)
                    i = i + 1
                i = 0
                while (i < 4):
                    for line in tx:
                        for item in listd:
                            if line.startswith(item):
                                tx.remove(line)
                    i = i + 1

                ready = '\n'.join(tx)
                # # printready
                self.text.BeginUndoAction()
                self.text.ClearAll()
                self.text.SetText(ready)
                self.text.EndUndoAction()


        else:
            text = self.text.GetSelectedText()
            tx = text.split("\n")
            ## print
            i = 0
            while (i < 4):
                for line in tx:
                    if line.startswith("H"):
                        if line[1].isdigit():
                            tx.remove(line)
                i = i + 1
            i = 0
            while (i < 4):
                for line in tx:
                    for item in listd:
                        if line.startswith(item):
                            tx.remove(line)
                i = i + 1
            ready = '\n'.join(tx)
            self.text.BeginUndoAction()
            self.text.ReplaceSelection(ready)
            self.text.EndUndoAction()

        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

    def splitcif(self, event):
        filters = 'Cif files (*.cif)|*.cif|All files (*.*)|*.*'
        dlg = wx.FileDialog(self, "Choose a 2013+ cif file", self.dirname, "", filters, wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dirname = self.dirname = dlg.GetDirectory()
            fname = self.filename = dlg.GetFilename()
            self.fnamefull = os.path.join(self.dirname, self.filename)
            self.fnoe = os.path.splitext(self.fnamefull)[0]
            self.filenamenoext = os.path.splitext(self.filename)[0]
            fcif = open(self.fnamefull, 'r')
            fcifread = fcif.readlines()

            #            resfileb=fcifread.find("_shelx_res_file")
            #            resfileend=fcifread.find("_shelx_res_checksum")
            #            hklfileb=fcifread.find("_shelx_hkl_file")
            for num, lines in enumerate(fcifread):

                if "_shelx_res_file" in lines:
                    resfileb = num + 2
                if "_shelx_res_checksum" in lines:
                    resfileend = num - 1
                if "_shelx_hkl_file" in lines:
                    hklfileb = num + 2
                if "_shelx_hkl_checksum" in lines:
                    hklend = num - 2
            #            hklend=fcifread.find("_shelx_hkl_checksum")-3
            resfileout = fcifread[resfileb:resfileend]  # .replace(";","")
            hklfileout = fcifread[hklfileb:(int(hklend))]  # .replace(";","")
            hkloutlist = self.striplist(hklfileout)
            res = open(os.path.join(dirname, self.filenamenoext + ".res"), 'w')
            res.writelines(resfileout)
            hkl = open(os.path.join(dirname, self.filenamenoext + ".hkl"), 'w')
            hkl.writelines(hkloutlist)
            res.close()
            hkl.close()
            fcif.close()
            view = wx.MessageDialog(self, 'The cif file has been split to hkl and res. Load res?', "Load res file?",
                                    wx.YES_NO)
            igot = view.ShowModal()  # Shows it
            if igot == wx.ID_YES:
                self.fnamefull = self.fnoe + ".res"
                self.Load(event)

    def simplecif(self, event):
        self.makeTMP()
        tmp = open(os.path.join(self.dirname, 'publish.tmp'), 'r')
        read = tmp.read()
        tmp.close()
        simple = open(os.path.join(self.dirname, 'simple.cif'), 'w')
        simple.write(read)
        simple.close()
        self.SetStatusText(" the file " + os.path.join(self.dirname, 'simple.cif') + "  has been created")

    ##################Cif file edditing#####################################
    def makeTMP(self):

        if os.path.exists(os.path.join(self.dirname, 'publish.cif')) == True:
            last = open(os.path.join(self.dirname, 'publish.tmp'), 'w')  # changed to w
            firstf = open(os.path.join(self.dirname, 'publish.cif'), 'r')
            first = firstf.readlines()
            end = len(first)
            number = 0
            for num, line in enumerate(first):
                if line.startswith("data_"):
                    number = num
                elif line.startswith("_refine_diff_density_rms"):
                    end = num
                elif line.startswith("_space_group_crystal_system"):
                    l = line.replace('_space_group_crystal_system', '_symmetry_cell_setting')
                    first.pop(num)
                    first.insert(num, l)
                elif line.startswith("_space_group_name_Hall"):
                    l = line.replace('_space_group_name_Hall', '_symmetry_space_group_name_Hall')
                    first.pop(num)
                    first.insert(num, l)
                elif line.startswith("_space_group_name_H-M_alt"):
                    l = line.replace('_space_group_name_H-M_alt', '_symmetry_space_group_name_H-M')
                    first.pop(num)
                    first.insert(num, l)

            first = first[number:end + 2]

            list = []
            keys = ['_platon_squeeze_void_nr', '_platon_squeeze_details']
            for line in first:
                for key in keys:
                    if key in line.lower():
                        list.append(first.index(line))
            firstf.close()
            first.insert(0, "\n")
            if len(list) != 0:
                first = first[0:list[0] - 2] + first[list[1] + 4:]
            else:
                first = first
            last.writelines(first)
            last.close()
        elif os.path.exists(self.fnoe + '.cif') == True:
            # print"got normal cif "
            listnumber = []
            last = open(os.path.join(self.dirname, 'publish.tmp'), 'w')
            firstf = open(self.fnoe + '.cif', 'r')
            first = firstf.readlines()
            end = len(first)
            number = 0
            for num, line in enumerate(first):
                if line.startswith("data_"):
                    number = num
                elif line.startswith("_refine_diff_density_rms"):
                    end = num
                elif line.startswith("_space_group_crystal_system"):
                    l = line.replace('_space_group_crystal_system', '_symmetry_cell_setting')
                    first.pop(num)
                    first.insert(num, l)
                elif line.startswith("_space_group_name_Hall"):
                    l = line.replace('_space_group_name_Hall', '_symmetry_space_group_name_Hall')
                    first.pop(num)
                    first.insert(num, l)
                elif line.startswith("_space_group_name_H-M_alt"):
                    l = line.replace('_space_group_name_H-M_alt', '_symmetry_space_group_name_H-M')
                    first.pop(num)
                    first.insert(num, l)

            first = first[number:end + 2]
            list = []
            keys = ['_platon_squeeze_void_nr', '_platon_squeeze_details']
            for line in first:
                for key in keys:
                    if key in line.lower():
                        list.append(first.index(line))

            firstf.close()
            first.insert(0, "\n")
            if len(list) != 0:
                first = first[0:list[0] - 2] + first[list[1] + 4:]
            else:
                first = first
            last.writelines(first)
            last.close()

    # def readciffile(self):
    #     self.makeTMP()
    #     # print 'reading cif'
    #     if os.path.exists(os.path.join(self.dirname, 'publish.tmp')) == True:
    #         self.ciffile = libcif.LoadCIF(os.path.join(self.dirname, 'publish.tmp'))
    #     #             os.remove(os.path.join(self.dirname,'publish.tmp'))
    #     elif os.path.exists(self.fnoe + '.cif') == True:
    #         self.ciffile = libcif.LoadCIF(self.fnoe + '.cif')
    #     else:
    #         dlg = wx.MessageDialog(self, "Error!!! The CIF file was not found",
    #                                'Error', wx.OK | wx.ICON_INFORMATION)
    #         dlg.ShowModal()
    #         dlg.Destroy()

    def createdirreport(self, event):
        if not os.path.exists(os.path.join(self.dirname, "report")):
            os.makedirs(os.path.join(self.dirname, "report"))

    def reportcopy(self, event):
        self.createdirreport(event)
        if os.path.exists(os.path.join(self.dirname, 'publish_' + self.filenamenoext + ".html")):
            shutil.copy(os.path.join(self.dirname, 'publish_' + self.filenamenoext + ".html"),
                        os.path.join(self.dirname, 'report', 'publish_' + self.filenamenoext + ".html"))
        if os.path.exists(os.path.join(self.dirname, "bonds_angles_" + self.filenamenoext + ".htm")):
            shutil.copy(os.path.join(self.dirname, "bonds_angles_" + self.filenamenoext + ".htm"),
                        os.path.join(self.dirname, 'report', "bonds_angles_" + self.filenamenoext + ".htm"))
        if os.path.exists(os.path.join(self.dirname, self.filenamenoext + "_table.rtf")):
            shutil.copy(os.path.join(self.dirname, self.filenamenoext + "_table.rtf"),
                        os.path.join(self.dirname, 'report', self.filenamenoext + "_table.rtf"))
        if os.path.exists(os.path.join(self.dirname, "publish.cif")):
            shutil.copy(os.path.join(self.dirname, "publish.cif"), os.path.join(self.dirname, 'report', "publish.cif"))
        if os.path.exists(os.path.join(self.dirname, "simple.cif")):
            shutil.copy(os.path.join(self.dirname, "simple.cif"), os.path.join(self.dirname, 'report', "simple.cif"))

    def Fullreport(self, event):
        view = wx.MessageDialog(self,
                                'This option will guide you through creating a full report in html format, table of refinement parameters and table of bonds and angles. Do you want to proceed?',
                                "Continue?", wx.YES_NO)
        igot = view.ShowModal()  # Shows it
        if igot == wx.ID_YES:
            #self.Appendix(event)
            self.onBonAng(event)
            self.onHtmlTable(event)
            self.simplecif(event)
            self.reportcopy(event)

    # def Appendix(self, event):
    #     self.readciffile()
    #     x = libcif.Appendix(os.path.join(self.dirname, "publish_" + self.filenamenoext + ".html"), self.ciffile,
    #                         Lang='En')
    #     view = wx.MessageDialog(self, 'Do you want to view the report ?', "View report?", wx.YES_NO)
    #     igot = view.ShowModal()  # Shows it
    #     if igot == wx.ID_YES:
    #         webbrowser.open('file://%s' % os.path.join(self.dirname, "publish_" + self.filenamenoext + ".html"))
    #     self.SetStatusText("File " + "publish_" + self.filenamenoext + ".html" + "was created in the work directory")

    def Fullcif(self, event):
        #self.readciffile()
        x = libcif.WriteReport(os.path.join(self.dirname, "publish_" + self.filenamenoext + ".html"), self.ciffile,
                               Lang='En')

    def molformula(self, event):
        #self.readciffile()
        self.zformula()
        mw = libcif.MolForm(self.ciffile, self.zasym)

        dlg = wx.MessageDialog(self, 'Molecular formula = ' + mw, 'Molecular Formula', wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def zformula(self):
        #self.readciffile()
        self.zasym = libcif.Zprime(self.ciffile)

    def onRename(self, event):
        #        listext=['.res', '.ins', '.hkl', '.p4p', '.raw', '.ls', '.lst', '.cif']
        filters = 'All files (*.*)|*.*'
        table = []
        dialog = wx.FileDialog(self, "Choose a file", self.dirname, wildcard=filters, style=wx.FD_OPEN | wx.FD_MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            filenames = dialog.GetPaths()
            dir = dialog.GetDirectory()
            dialog.Destroy()
            if filenames:
                textentry = wx.TextEntryDialog(None, "How do you want to rename your files?", "File name?", "",
                                               style=wx.OK | wx.CANCEL)
                if textentry.ShowModal() == wx.ID_OK:
                    newfilename = os.path.join(dir, textentry.GetValue())
                    for f in filenames:
                        name = f.split(".")[-1]
                        try:
                            if os.path.exists(newfilename + "." + name) == False:
                                os.rename(f, newfilename + "." + name)
                                print("renaming", f, " to ", newfilename + "." + name)
                                if len(dir) < 40:
                                    table.append([f, newfilename + "." + name])
                                else:
                                    table.append([f.split(dir[0:len(dir) / 3])[1],
                                                  (newfilename + "." + name).split(dir[0:len(dir) / 3])[1]])

                            else:
                                print("file exists!")
                                table.append(["File " + newfilename + "." + name + " exists"])
                        except OSError:
                            pass
                textentry.Destroy()
        header = ["Old File Name", "New File Name"]
        self.tablelist(event, table, header)

    def onXL(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        # t=os.path.getmtime(self.fnamefull)
        # if self.modtime==t:
        #     self.onXLmain(event)
        # else:
        #     doreload = wx.MessageDialog(self, "File was modified by external sources. Do you want to reload the res file?", "Reload file?", wx.YES_NO)
        #     igot = doreload.ShowModal() # Shows it
        #     if igot == wx.ID_YES:
        #         self.onReload(event)
        #         self.onXLmain(event)
        #     else:
        #         self.onSave(event)
        #         self.onXLmain(event)
        self.onXLmain(event)
        self.text.ScrollToLine(self.topline)

    def onXLR2I(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        t = os.path.getmtime(self.fnamefull)
        if self.modtime == t:
            self.onDelq(event)
            self.onSave(event)
            self.onCopyrti(event)
            self.onXLmain(event)
        else:
            doreload = wx.MessageDialog(self,
                                        "File was modified by external sources. Do you want to reload the res file?",
                                        "Reload file?", wx.YES_NO)
            igot = doreload.ShowModal()  # Shows it
            if igot == wx.ID_YES:
                self.onReload(event)
                self.onDelq(event)
                self.onSave(event)
                self.onCopyrti(event)
                self.onXLmain(event)
            else:
                self.onDelq(event)
                self.onSave(event)
                self.onSave(event)
                self.onCopyrti(event)
                self.onXLmain(event)
        self.text.ScrollToLine(self.topline)

    def onXLmain(self, event):  # wxGlade: MyFrame.<event_handler>
        self.notebook_1.SetSelection(0)
        try:
            if os.path.exists(os.path.join(self.dirname, self.filenamenoext + ".hkl")) == False:
                dlg = wx.MessageDialog(self,
                                       "hkl file was not found. The hkl file might be absent or have a different base name from the res file",
                                       'hkl file was not found', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
            if self.ossystem.startswith("win"):
                os.chdir(self.dirname)

                xl = subprocess.Popen([self.phtoxl, self.filenamenoext], stdout=subprocess.PIPE, shell=True)
                self.onterminal(event, xl, False)

                stdout_value = xl.communicate()
                failed = xl.returncode
                if failed == 0:
                    sizeres = os.path.getsize(self.fnoe + ".res")
                    if sizeres < 70:

                        #                           dooad = wx.MessageDialog(self, "Res file is empty! Do you want to copy ins file to res?\n", "Reload file ...", wx.YES_NO)
                        #                           igot = doreload.ShowModal() # Shows it
                        #                           if igot == wx.ID_YES:
                        self.onSave(event)
                    #                                 self.onCopyitr(event)
                    else:

                        self.onReload(event)
            elif self.ossystem.startswith("darwin"):
                os.chdir(self.dirname)

                xl = subprocess.Popen([self.phtoxl, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xl, False)

                stdout_value, stderr_value = xl.communicate()
                failed = xl.returncode
                if failed == 0:
                    sizeres = os.path.getsize(self.fnoe + ".res")
                    if sizeres < 70:
                        #                            doreload = wx.MessageDialog(self, "Res file is empty! Do you want to copy ins file to res?\n", "Reload file ...", wx.YES_NO)
                        #                           igot = doreload.ShowModal() # Shows it
                        #                           if igot == wx.ID_YES:
                        self.onSave(event)
                    #                                 self.onCopyitr(event)
                    else:
                        self.onReload(event)
            else:

                os.chdir(self.dirname)
                xl = subprocess.Popen([self.phtoxl, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xl, False)
                stdout_value, stderr_value = xl.communicate()
                failed = xl.returncode
                # print failed
                if failed == 0:
                    sizeres = os.path.getsize(self.fnoe + ".res")
                    print(sizeres)
                    if sizeres < 70:
                        #                            doreload = wx.MessageDialog(self, "Res file is empty! Do you want to copy ins file to res?\n", "Reload file ...", wx.YES_NO)
                        #                           igot = doreload.ShowModal() # Shows it
                        #                           if igot == wx.ID_YES:
                        self.onSave(event)
                    #                                 self.onCopyitr(event)
                    else:
                        self.onReload(event)
            self.onstats(event)
        except OSError:
            pass

    #         else:
    #            dlg = wx.MessageDialog(self, "Dublicated labels found",
    #                                'Dublicated labels', wx.OK | wx.ICON_INFORMATION)
    #            dlg.ShowModal()
    #            dlg.Destroy()

    def XLforWR(self, event):  # wxGlade: MyFrame.<event_handler>
        self.notebook_1.SetSelection(0)
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                xl = subprocess.Popen([self.phtoxl, self.filenamenoext])
                stdout_value = xl.communicate()
                failed = xl.returncode
                # # printfailed
                if failed == 0:
                    self.onReload(event)
            elif self.ossystem.startswith("darwin"):
                xl = subprocess.Popen([self.phtoxl, self.filenamenoext])
                stdout_value = xl.communicate()
                failed = xl.returncode
                # # printfailed
                if failed == 0:
                    self.onReload(event)
            else:
                xl = subprocess.Popen([self.phtoxl, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xl, True)
                stdout_value, stderr_value = xl.communicate()
                failed = xl.returncode
                if failed == 0:
                    self.onReload(event)
        except OSError:
            pass

    ##################################################################### autosolve ###########################################################################

    def atomnum(self, event, textlist, a):  # returns the last number plus 1 for the atom a
        sfac = self.getsfac(textlist)
        num = 0
        for i, atoms in enumerate(sfac):
            if len(atoms) == 1:
                if a in atoms:
                    num = i + 1
        return num

    def getR(self, event, textlist):
        for line in textlist:
            if line.startswith("REM R1 ="):
                l = line.split()
                self.striplist(l)
                # print l[3]
                return l[3]

    def settext(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        l = self.striplist(self.textlist)
        ready = '\n'.join(l)
        self.text.SetText(ready)
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

        ########################find max number for c######################################################

    def findmax(self, event, textlist, atom):  #
        lastcarb = []
        for line in textlist:
            for n in range(10):
                if line.startswith(atom + str(n)):
                    cnum = re.findall('\\d', line.split()[0])
                    lastcarb.append(int("".join(cnum)))
        if not lastcarb:
            cmax = 0
        else:
            cmax = max(lastcarb)
        return cmax

    #    def ongetatoms(self, event):
    #        text = self.text.GetText()
    #        gtext=text.split("\n")
    #        sfac=self.getsfac(gtext)

    def relabel(self, event, gtext, sfac):
        pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
        cnt = 1
        ra = wx.TextEntryDialog(None, "Starting atom number?",  "Atom number?", "1", style=wx.OK | wx.CANCEL)
        if ra.ShowModal() == wx.ID_OK:
            cnt = int(ra.GetValue())
        atoms = []
        for num, line in enumerate(gtext):
            if pattern.match(line.upper()):
                if "=" in line:
                    gtext[num] = line.upper() + gtext[num + 1]
                    gtext[num + 1] = ""
        for s in sfac:
            count = cnt
            s = s.upper()
            pat = re.compile(r"(([%s]{%d}[\d\s]{1,3}[\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5}))" % (s, len(s)))
            for num, line in enumerate(gtext):
                if pat.match(line):
                    if not line.upper().startswith("Q"):
                        if not line.upper().startswith("ZERR"):
                            if not line.upper().startswith("FVAR"):
                                l = line.split()
                                #                                    print (line)
                                l[0] = s + str(count)  # split line and replace label
                                ldone = "   ".join(l)
                                if "=" in line:
                                    leq = ldone.replace('=', '= \n     ')
                                    gtext[num] = leq
                                else:
                                    gtext[num] = ldone
                                count = count + 1
        gtext = self.striplist(gtext)
        return gtext

    def renamecarbons(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        text = self.text.GetText()
        gtext = text.split("\n")
        sfac = self.getsfac(gtext)
        if len(seltext) == 0:
            if "RESI" in text:
                resi = wx.MessageDialog(self,
                                        "RESI instruction found in file. This will relabel atoms independent of residue. Do you want to continue?",
                                        "", wx.YES_NO)
                igot = resi.ShowModal()  # Shows it
                if igot == wx.ID_YES:
                    gtext = self.relabel(event, gtext, sfac)
                    self.text.BeginUndoAction()
                    self.text.ClearAll()
                    self.text.SetText("\n".join(gtext))
                    self.onColor1(event)
                    self.text.ScrollToLine(self.topline)
                    self.text.EndUndoAction()
            else:
                gtext = self.relabel(event, gtext, sfac)
                self.text.BeginUndoAction()
                self.text.ClearAll()
                self.text.SetText("\n".join(gtext))
                self.onColor1(event)
                self.text.ScrollToLine(self.topline)
                self.text.EndUndoAction()
        else:
            sel = seltext.split("\n")
            gtext = self.relabel(event, sel, sfac)
            self.text.BeginUndoAction()
            self.text.ReplaceSelection("\n".join(gtext))
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)
            self.text.EndUndoAction()

    ###Sets Qs as carbons ###################################################

    def qstoc(self, event):
        ra = wx.TextEntryDialog(None, "Select range of Q peaks height", "1-100", "1-10", style=wx.OK | wx.CANCEL)
        if ra.ShowModal() == wx.ID_OK:
            r = ra.GetValue()
        text = self.text.GetText()
        textlist = text.split("\n")
        cchange = []
        lastcarb = []
        for line in textlist:
            for n in range(10):
                if line.startswith("C" + str(n)):
                    cnum = re.findall('\\d', line.split()[0])
                    lastcarb.append(int("".join(cnum)))
        cmax = self.findmax(event, textlist, "C")
        # print cmax

        indexline = []
        for i, line in enumerate(textlist):
            if not line.startswith("CELL"):
                if not line.startswith("ZERR"):
                    if len(line) > 50:
                        indexline.append(i)
        fmol = indexline[0]
        i = 1
        for line in textlist:

            #                # print fmol
            for n in range(10):
                if line.startswith("Q" + str(n)):
                    try:
                        l = line.split()
                        self.striplist(l)

                        if int(l[0].upper().replace("Q", "")) in range(int(r.split("-")[0]), int(r.split("-")[1])):
                            num = self.atomnum(event, textlist, "C")
                            cchange.append(
                                "C" + str(int(cmax) + int(i)) + "     " + str(num) + "     " + "     ".join(l[2:7]))
                            # print "C"+str(int(cmax)+int(i))+"     "+str(num)+"     "+"     ".join(l[2:7])
                    #                            textlist.remove(line)

                    except ValueError:
                        continue
                    i = i + 1
        textlist.insert(fmol + 2, '\n'.join(cchange))
        ready = '\n'.join(textlist)
        self.text.BeginUndoAction()
        self.topline = self.text.GetFirstVisibleLine()
        self.text.SetText(ready)
        self.onDelq(event)
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)
        self.text.EndUndoAction()

    def onRefW(self, event):
        listw3 = []
        listw = []
        listw1 = []
        listw2 = []

        cicles = wx.TextEntryDialog(None, "Choose a number of weight refinement cicles", "Number of cicles", "3",
                                    style=wx.OK | wx.CANCEL)
        if cicles.ShowModal() == wx.ID_OK:
            # # print"You entered: %s" % cicles.GetValue()
            times = int(cicles.GetValue())
            # # printtimes
            self.XLforWR(event)
            count = 1
            while count <= times:
                text = self.text.GetText()
                textlist = text.split("\n")
                for line1 in textlist:
                    if line1.startswith("WGHT"):
                        loc1 = textlist.index(line1)
                        listw1.append(line1)
                        listw2.append(loc1)
                        listw.append('R' + str(count) + ': ' + line1)
                textlist.pop(listw2[0])
                textlist.insert(listw2[0], listw1[1])
                textout = '\n'.join(textlist)
                self.text.SetText(textout)
                self.onSave(event)
                self.onCopyrti(event)
                self.XLforWR(event)
                count = 1 + count
            # # printlistw
            for index in range(1, (len(listw)), 2):
                # # printindex
                listw3.append(listw[index])
            dlg = wx.MessageDialog(self, "" + '\n'.join(listw3),
                                   'Results of refinement:', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def Activate(self, event):
        event = wx.ActivateEvent(wx.wxEVT_ACTIVATE, False, self.GetId())
        event.SetEventObject(self)

    # # printevent

    def onXH(self, event):  # wxGlade: MyFrame.<event_handler>
        try:
            if self.ossystem == 'win32':
                os.chdir(self.dirname)
                xl = subprocess.Popen([self.phtoxh, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xl, False)
                stderr_value = xl.communicate()
                failed = xl.returncode
                if failed == 0:
                    sizeres = os.path.getsize(self.fnoe + ".res")
                    if sizeres == 0:
                        doreload = wx.MessageDialog(self, "Res file is empty! Do you want to copy ins file to res?\n",
                                                    "Reload file ...", wx.YES_NO)
                        igot = doreload.ShowModal()  # Shows it
                        if igot == wx.ID_YES:
                            self.onCopyitr(event)
                    else:
                        self.onReload(event)
            elif self.ossystem.startswith("darwin"):
                # print "starting XL"
                os.chdir(self.dirname)
                xh = subprocess.Popen([self.phtoxh, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xh, False)
                stdout_value, stderr_value = xh.communicate()
                # print  stdout_value, stderr_value
                failed = xh.returncode
                if failed == 0:
                    sizeres = os.path.getsize(self.fnoe + ".res")
                    if sizeres == 0:
                        doreload = wx.MessageDialog(self, "Res file is empty! Do you want to copy ins file to res?\n",
                                                    "Reload file ...", wx.YES_NO)
                        igot = doreload.ShowModal()  # Shows it
                        if igot == wx.ID_YES:
                            self.onCopyitr(event)
                    else:
                        self.onReload(event)
            else:
                os.chdir(self.dirname)
                xl = subprocess.Popen([self.phtoxh, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xl, False)
                stdout_value, stderr_value = xl.communicate()
                failed = xl.returncode
                if failed == 0:
                    sizeres = os.path.getsize(self.fnoe + ".res")
                    if sizeres == 0:
                        doreload = wx.MessageDialog(self, "Res file is empty! Do you want to copy ins file to res?\n",
                                                    "Reload file ...", wx.YES_NO)
                        igot = doreload.ShowModal()  # Shows it
                        if igot == wx.ID_YES:
                            self.onCopyitr(event)
                    else:
                        self.onReload(event)
        except OSError:
            pass

    def onXS(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                xs = subprocess.Popen([self.phtoxs, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                self.onterminal(event, xs, False)
            #                   xs=subprocess.Popen([self.phtoxs, self.filenamenoext])
            elif self.ossystem.startswith("darwin"):
                xs = subprocess.Popen([self.phtoxs, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xs, False)
            else:
                xs = subprocess.Popen([self.phtoxs, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xs, False)
            self.onReloadRes(event)
        except OSError:
            pass

    def onPubl(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        if os.path.exists('publish.cif') == True:
            fcif = os.path.join(self.dirname, "publish")
        else:
            fcif = self.fnoe
        try:
            if self.ossystem.startswith("win"):
                xs = subprocess.Popen([self.phtopublcif, fcif + '.cif'])
            elif self.ossystem.startswith("darwin"):
                # print fcif
                xs = subprocess.Popen(
                    ['open', '-a', self.phtopublcif, '"' + self.dirname + self.filenamenoext + '.cif' + '"'])
            else:
                subprocess.Popen([self.phtopublcif, fcif + ".cif"])
        except OSError:
            pass

    def onRasmol(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                rs = subprocess.Popen([self.phtorasmol, self.filenamenoext + ".cif"])
            elif self.ossystem.startswith("darwin"):
                subprocess.call([self.phtorasmol, self.filenamenoext + ".cif"])
            else:
                subprocess.Popen([self.phtorasmol, self.filenamenoext + ".cif"])
        except OSError:
            pass

    def onXP(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                subprocess.Popen([self.phtoxp, self.filenamenoext + ".res"])
            elif self.ossystem.startswith("darwin"):
                subprocess.Popen([self.phtoxp, self.filenamenoext + ".res"])
            else:
                xp = subprocess.Popen(
                    ['xterm', '-hold', '-e', self.phtoxp, '-u %s', '-p %s', self.filenamenoext + ".res"])
        except OSError:
            pass

    def onXPREP(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                if os.path.exists(self.fnoe + ".p4p") == True:
                    subprocess.Popen([self.phtoxprep, self.filenamenoext])
                else:
                    askyesno = wx.MessageDialog(self,
                                                "It appeares that you do not have p4p file with the same base name. Do you want to use cell setting from the res or (XDS)hkl file?",
                                                "Cell from res, hkl?", wx.YES_NO)
                    igot = askyesno.ShowModal()  # Shows it
                    if not (self.onGetCell(event) is None):
                        if igot == wx.ID_YES:
                            p4pfromres = open(self.fnoe + ".p4p", 'w')
                            p4pfromres.writelines("CELL " + " ".join(self.onGetCell(event)))
                            p4pfromres.close()
                            subprocess.Popen([self.phtoxprep, self.filenamenoext])
                        else:
                            subprocess.Popen([self.phtoxprep, self.filenamenoext])

            elif self.ossystem.startswith("darwin"):
                if self.phtoxprep.endswith(".exe"):
                    if os.path.exists(self.phtowine) == True:
                        if os.path.exists(self.fnoe + ".p4p") == True:
                            subprocess.call([self.phtowine, self.phtoxprep, self.filenamenoext])
                        else:
                            askyesno = wx.MessageDialog(self,
                                                        "It appeares that you do not have p4p file with the same base name. Do you want to use cell setting from the res file?",
                                                        "Cell from res?", wx.YES_NO)
                            igot = askyesno.ShowModal()  # Shows it
                            if not (self.onGetCell(event) is None):
                                if igot == wx.ID_YES:
                                    p4pfromres = open(self.fnoe + ".p4p", 'w')
                                    p4pfromres.writelines("CELL " + " ".join(self.onGetCell(event)))
                                    p4pfromres.close()
                                    subprocess.call([self.phtowine, self.phtoxprep, self.filenamenoext])
                                else:
                                    subprocess.call([self.phtowine, self.phtoxprep, self.filenamenoext])
                    else:
                        dlg = wx.MessageDialog(self,
                                               "Error!!! Wine or Crossover Office was not found on this computer. Please install wine",
                                               'Error', wx.OK | wx.ICON_INFORMATION)
                        dlg.ShowModal()
                        dlg.Destroy()
                else:
                    if os.path.exists(self.fnoe + ".p4p") == True:

                        subprocess.Popen(['xterm', '-bg', 'white', '-fs 55', '-e', self.phtoxprep, self.filenamenoext])
                    else:
                        askyesno = wx.MessageDialog(self,
                                                    "It appeares that you do not have p4p file with the same base name. Do you want to use cell setting from the res file?",
                                                    "Cell from res?", wx.YES_NO)
                        igot = askyesno.ShowModal()  # Shows it
                        if not (self.onGetCell(event) is None):
                            print("nooo")
                            if igot == wx.ID_YES:
                                p4pfromres = open(self.fnoe + ".p4p", 'w')
                                p4pfromres.writelines("CELL " + " ".join(self.onGetCell(event)))
                                p4pfromres.close()
                                subprocess.Popen(['xterm', '-bg', 'white', '-e', self.phtoxprep, self.filenamenoext])
                            else:
                                subprocess.Popen(['xterm', '-bg', 'white', '-e', self.phtoxprep, self.filenamenoext])
            else:
                if self.phtoxprep.endswith(".exe"):
                    if os.path.exists(self.phtowine) == True:
                        subprocess.call([self.phtowine, self.phtoxprep, self.filenamenoext])
                    else:
                        dlg = wx.MessageDialog(self,
                                               "Error!!! Wine or Crossover Office was not found on this computer. Please install wine",
                                               'Error', wx.OK | wx.ICON_INFORMATION)
                        dlg.ShowModal()
                        dlg.Destroy()
                else:
                    if os.path.exists(self.fnoe + ".p4p") == True:
                        subprocess.Popen(['xterm', '-bg', 'white', '-e', self.phtoxprep, self.filenamenoext])
                    else:
                        askyesno = wx.MessageDialog(self,
                                                    "It appeares that you do not have p4p file with the same base name. Do you want to use cell setting from the res file?",
                                                    "Cell from res?", wx.YES_NO)
                        igot = askyesno.ShowModal()  # Shows it
                        print("p4p no")
                        if igot == wx.ID_YES:
                            if not (self.onGetCell(event) is None):
                                p4pfromres = open(self.fnoe + ".p4p", 'w')
                                p4pfromres.writelines("CELL " + " ".join(self.onGetCell(event)))
                                p4pfromres.close()
                                subprocess.Popen(['xterm', '-bg', 'white', '-e', self.phtoxprep, self.filenamenoext])
                        else:
                            subprocess.Popen(['xterm', '-bg', 'white', '-e', self.phtoxprep])


        except OSError:
            pass

    def onXT(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        import shlex
        com = self.phtoxt + ' ' + self.filenamenoext
        try:
            if self.ossystem.startswith("win"):
                if os.path.exists(self.fnoe + ".ins") == True:
                    xt = subprocess.Popen(com, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                          stderr=subprocess.STDOUT, shell=True)
                    self.onterminal(event, xt, False)
                else:
                    dlg = wx.MessageDialog(self,
                                           "Error! " + self.filenamenoext + ".ins does not exist. The ins file must contain at least TITL, CELL, ZERR, SFAC, and UNIT instruction for shelxt to work",
                                           'Error', wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
            elif self.ossystem.startswith("darwin"):
                if os.path.exists(self.fnoe + ".ins") == True:
                    xt = subprocess.Popen(com, bufsize=0, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                          stderr=subprocess.STDOUT, shell=True)
                    self.onterminal(event, xt, False)
                else:
                    dlg = wx.MessageDialog(self,
                                           "Error! " + self.filenamenoext + ".ins does not exist. The ins file must contain at least TITL, CELL, ZERR, SFAC, and UNIT instruction for shelxt to work",
                                           'Error', wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
            else:
                if os.path.exists(self.fnoe + ".ins") == True:
                    xt = subprocess.Popen(com, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                          shell=True)
                    self.onterminal(event, xt, False)
                else:
                    dlg = wx.MessageDialog(self,
                                           "Error! " + self.filenamenoext + ".ins does not exist. The ins file must contain at least TITL, CELL, ZERR, SFAC, and UNIT instruction for shelxt to work",
                                           'Error', wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
            askyesno = wx.MessageDialog(self, "Res file will be changed by the first available XT solution. Proceed?",
                                        "Change res file ...", wx.YES_NO)
            igot = askyesno.ShowModal()  # Shows it
            if igot == wx.ID_YES:
                askyesno = wx.MessageDialog(self, "Relable atoms?", "Relable ...", wx.YES_NO)
                igot = askyesno.ShowModal()  # Shows it
                if igot == wx.ID_YES:
                    askyesno.Destroy()
                    self.onReloadafterXT(event)
                    self.renamecarbons(event)
                    self.onSave(event)


        except OSError:
            pass

    def onGetCell(self, event):
        if os.path.exists(self.fnoe + ".res") == True:
            gtext = (self.text.GetText()).split("\n")
            for lines in gtext:
                if "CELL" in lines:
                    cell = lines.split(' ')
                    cellline = self.striplist(cell)[2:8]
                    self.wavelength = self.striplist(cell)[1]
            return cellline
        #        elif os.path.exists(self.fnoe+".hkl")==True or os.path.exists(self.fnoe+".HKL")==True:
        #            print('UNIT_CELL_CONSTANTS')
        else:
            dlg = wx.MessageDialog(self,
                                   "Error! " + self.filenamenoext + ".res does not exist, empty or not open. Please open res or ins file",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onsir(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                xs = subprocess.Popen(self.phtosir + '  ' + self.filenamenoext + ".ins")
            elif self.ossystem.startswith("darwin"):
                subprocess.Popen([self.phtosir, self.filenamenoext + ".ins"])
            else:
                xs = subprocess.Popen([self.phtosir, self.filenamenoext + ".ins"])
        except OSError:
            pass

    def onanode(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                anode = subprocess.Popen([self.phtoanode, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            elif self.ossystem.startswith("darwin"):
                anode = subprocess.Popen([self.phtoanode, self.filenamenoext], bufsize=0, stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            else:
                anode = subprocess.Popen(['xterm', '-hold', '-e', self.phtoanode, self.filenamenoext], bufsize=0,
                                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        except OSError:
            pass

    def onxm(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                xm = subprocess.Popen([self.phtoxm, self.filenamenoext], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)
                self.onterminal(event, xm, False)
            elif self.ossystem.startswith("darwin"):
                xm = subprocess.Popen([self.phtoxm, self.filenamenoext], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)
                self.onterminal(event, xm, False)
            else:
                xm = subprocess.Popen([self.phtoxm, self.filenamenoext], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)
                self.onterminal(event, xm, False)
        except OSError:
            pass

    def onxe(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                xe = subprocess.Popen([self.phtoxe, self.filenamenoext, self.filenamenoext, '-a -h'], bufsize=0,
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xe, False)
            elif self.ossystem.startswith("darwin"):
                xe = subprocess.Popen([self.phtoxe, self.filenamenoext, self.filenamenoext, '-a -h'], bufsize=0,
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xe, False)
            else:
                xe = subprocess.Popen([self.phtoxe, self.filenamenoext, self.filenamenoext, '-a -h'], bufsize=0,
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                self.onterminal(event, xe, False)

        except OSError:
            pass

    def onxc(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                xc = subprocess.Popen(
                    self.phtoxc + " " + self.filenamenoext + " " + " < " + self.filenamenoext + ".inp",
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                self.onterminal(event, xc, False)
            elif self.ossystem.startswith("darwin"):
                xc = subprocess.Popen(
                    self.phtoxc + " " + self.filenamenoext + " " + " < " + self.filenamenoext + ".inp",
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                self.onterminal(event, xc, False)
            else:

                xc = subprocess.Popen(
                    self.phtoxc + " " + self.filenamenoext + " " + " < " + self.filenamenoext + ".inp",
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                self.onterminal(event, xc, False)

        except OSError:
            pass

    def onSADABS(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtosadabs, self.filenamenoext])
        elif self.ossystem.startswith("darwin"):
            subprocess.Popen([self.phtosadabs, self.filenamenoext])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', self.phtosadabs, '-u %s', '-p %s', self.filenamenoext])

    def onXABS2(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoxabs, self.filenamenoext])
        elif self.ossystem.startswith("darwin"):
            subprocess.Popen([self.phtoxabs, self.filenamenoext])
        else:
            subprocess.Popen(['xterm', '-hold', '-e', self.phtoxabs, self.filenamenoext])

    def onCELLNOW(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                subprocess.Popen([self.phtocellnow, self.filenamenoext + ".p4p"])
            elif self.ossystem.startswith("darwin"):
                subprocess.Popen([self.phtocellnow, self.filenamenoext + ".p4p"])
            else:
                subprocess.Popen(['xterm', '-hold', '-e', self.phtocellnow, self.filenamenoext + ".p4p"])
        except OSError:
            pass

    def onXCIF(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                proc = subprocess.Popen([self.phtoxcif, self.filenamenoext])
            elif self.ossystem.startswith("darwin"):
                subprocess.Popen([self.phtoxcif, self.filenamenoext])
            else:
                proc = subprocess.Popen('xterm', '-hold', '-e', self.phtoxcif, self.filenamenoext)
        except OSError:
            pass

    def onup(self, prog, f):
        info = open(os.path.join(prog, "Contents", "Info.plist"), 'r')
        inf = info.readlines()
        for n, i in enumerate(inf):
            if "WineProgramArguments" in i:
                inf[n + 1] = "    <string>" + f + "</string>" + "\n"
        open(os.path.join(prog, "Contents", "Info.plist"), 'w').writelines(inf)
        info.close()
        return True

    def onXSHELL(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                subprocess.Popen([self.phtoxshell, self.filenamenoext + '.res'])
            elif self.ossystem.startswith("darwin"):
                if os.path.exists(self.phtowine) == True:
                    subprocess.call([self.phtowine, self.phtoxshell, self.filenamenoext + ".res"])
                elif self.phtoxshell.endswith('.app'):
                    wait = self.onup(self.phtoxshell, os.path.join(self.dirname, self.filenamenoext + ".res"))
                    if wait == True:
                        # print wait
                        subprocess.call([os.path.join(self.phtoxshell, "Contents", "MacOS", "startwine")])
                else:
                    dlg = wx.MessageDialog(self,
                                           "Error!!! Wine or Crossover Office was not found on this computer. Please install wine",
                                           'Error', wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
            else:
                if os.path.exists("/opt/cxoffice/bin/wine") == True:
                    subprocess.Popen(["/opt/cxoffice/bin/wine", self.phtoxshell, self.filenamenoext + ".res"])
                elif os.path.exists(self.phtowine) == True:
                    subprocess.Popen([self.phtowine, self.phtoxshell, self.filenamenoext + ".res"])
                else:
                    dlg = wx.MessageDialog(self,
                                           "Error!!! Wine or Crossover Office was not found on this computer. To install wine type in terminal: su -c yum install wine (Fedora) or: sudo apt-get install wine (Ubuntu)",
                                           'Error', wx.OK | wx.ICON_INFORMATION)
                    dlg.ShowModal()
                    dlg.Destroy()
        except OSError:
            pass

    def wmol_run(self, event):
        from wmol import wmol
        # displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        # sizes = [display.GetGeometry().GetSize() for display in displays]
        # displaySize = sizes[0].Get()
        # paths = {"file": self.fnoe+".res", "path":os.path.join(self.path, "Modules")}
        # wc = webchem(None, -1, paths, size=(displaySize[0] / 3, displaySize[1] / 1.5))
        # wc.Show()
        wmol(self.fnamefull)


    def onXSHELL6(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoxshell6, self.filenamenoext + ".res"], shell=True)
        elif self.ossystem.startswith("darwin"):
            subprocess.call([self.phtoxshell6, self.filenamenoext + ".res"])
        else:
            subprocess.Popen([self.phtoxshell6, self.filenamenoext + ".res"])

    def shelxle(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        if self.ossystem.startswith("win"):
            subprocess.Popen([self.phtoshelxle, self.filenamenoext + ".res"])
        elif self.ossystem.startswith("darwin"):
            subprocess.Popen([self.phtoshelxle + '/Contents/MacOS/shelxle', self.filenamenoext + ".res"])
        else:
            subprocess.Popen([self.phtoshelxle, self.filenamenoext + ".res"])

    def onXPRO(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        try:
            if self.ossystem.startswith("win"):
                subprocess.Popen([self.phtoxpro, self.filenamenoext])
            elif self.ossystem.startswith("darwin"):
                subprocess.Popen([self.phtoxpro, self.filenamenoext])
            else:
                subprocess.Popen(['xterm', '-hold', '-e', self.phtoxpro, '-u %s', '-p %s', self.filenamenoext])
        except OSError:
            pass

    def onCleanfolder(self, event):
        clean = wx.MessageDialog(self,
                                 "The files with extentions .par .out .ome .trm  .bin .pjn \n .sup .sum .sar .dge .eld .prf .tmp .r3d .chk will be deleted. \n\n\t\t\t   Do you want to proceed? ",
                                 "Delete files ...", wx.YES_NO)
        igot = clean.ShowModal()  # Shows it
        if igot == wx.ID_YES:
            for file in os.listdir(self.dirname):
                listext = ['par', 'out', 'ome', 'trm', 'bin', '.pjn', '.sup', '.lis', '.sum', '.sar', '.dge', '.eld',
                           '.prf', '.tmp', '.chk', '.r3d']
                for i in listext:
                    if file.endswith(i):
                        os.remove(os.path.join(self.dirname, file))
            self.SetStatusText(
                "Files with extention .par .out .ome .trm  .bin .pjn .sup .sum .sar .dge .eld .prf .tmp .r3d .chk were deleted")

    def oncleang(self, event):
        for file in os.listdir(self.dirname):
            listext = ['.pjn', '.def', '.sup', '.lis', '.sum', '.sar', '.dge', '.eld', '.prf', '.tmp', '.chk', '.r3d',
                       '.new']
            for i in listext:
                if file.endswith(i):
                    os.remove(os.path.join(self.dirname, file))

    def garbage(self, event):
        clean = wx.MessageDialog(self,
                                 "The files, other than currently loaded ones, will be moved into subderictory 'notused'. Do you want to proceed? ",
                                 "Move files ", wx.YES_NO)
        igot = clean.ShowModal()  # Shows it
        if igot == wx.ID_YES:
            if os.path.exists(os.path.join(self.dirname, "notused")) == True:
                for file in os.listdir(self.dirname):
                    if not self.filenamenoext + "." in file:
                        if not file.endswith("others"):
                            if not file.endswith("lin.tmp"):
                                if not file.endswith("stats.txt"):
                                    if not file.endswith("checkcif.pdf"):
                                        if not file.endswith("publish.cif"):
                                            if not file.endswith("bonds_angles_" + self.filenamenoext + "htm"):
                                                if not file.endswith("publish_" + self.filenamenoext + "html"):
                                                    if not file.endswith(".rtf"):
                                                        try:
                                                            shutil.copy(os.path.join(self.dirname, file),
                                                                        os.path.join(self.dirname, "notused"))
                                                            os.remove(os.path.join(self.dirname, file))
                                                        except (OSError, IOError):
                                                            pass
            else:
                os.mkdir(os.path.join(self.dirname, "notused"))
                for file in os.listdir(self.dirname):
                    if not file.endswith("notused"):
                        if not self.filenamenoext + "." in file:
                            if not file.endswith("lin.tmp"):
                                if not file.endswith("stats.txt"):
                                    if not file.endswith("checkcif.pdf"):
                                        if not file.endswith("publish.cif"):
                                            if not file.endswith("bonds_angles_" + self.filenamenoext + "htm"):
                                                if not file.endswith("publish_" + self.filenamenoext + "html"):
                                                    if not file.endswith(".rtf"):
                                                        try:
                                                            shutil.copy(os.path.join(self.dirname, file),
                                                                        os.path.join(self.dirname, "notused"))
                                                            os.remove(os.path.join(self.dirname, file))
                                                        except (OSError, IOError):
                                                            pass

        self.SetStatusText("The files, other than currently loaded ones, have been moved into subderictory 'notused'")

    def getZERR(self, gtext):
        return ([line for line in gtext if line.lower().startswith('zerr')])

    def getunitlst(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        lofl = self.getlistsfac(event)
        if lofl is not None:
            sfac = []
            unit = []
            for i in lofl:
                sfac.append(i[0])
                unit.append(i[2].replace(".00", ""))
                # print sfac
            # print unit
            txt = self.text.GetText()
            gtext = txt.split("\n")
            for line in gtext:
                if line.startswith("SFAC"):
                    loc1 = gtext.index(line)
                    gtext.remove(line)
                    gtext.insert(loc1, "SFAC " + " ".join(sfac))
                elif line.startswith("UNIT"):
                    loc2 = gtext.index(line)
                    gtext.remove(line)
                    gtext.insert(loc2, "UNIT " + " ".join(unit))
            ready = "\n".join(gtext)
            self.text.BeginUndoAction()

            self.text.SetText(ready)
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)
            self.text.EndUndoAction()

    def getlistsfac(self, event):

        listtab = []
        if os.path.exists(self.fnoe + ".lst") == True:
            lstread = open(self.fnoe + ".lst", 'r').readlines()
            for numbers, lines in enumerate(lstread):
                if "Unit-cell contents from UNIT" in lines:
                    #                   # # printlines, numbers
                    listtab.append(numbers)
                elif "Least-squares cycle   1" in lines:
                    #                   # # printlines, numbers
                    listtab.append(numbers)
            #            # print len(listtab), listtab
            if len(listtab) == 1:
                dlg3 = wx.MessageDialog(self, 'The molecular formula is correct',
                                        'Info', wx.OK | wx.ICON_INFORMATION)
                dlg3.ShowModal()

            else:
                gettex = lstread[int(listtab[0]) + 1:listtab[1]]
                # print "gettex", gettex
                listlines = []
                for line in gettex:
                    if not line.strip():
                        continue
                    listlines.append(line.split())
                #                # print listlines
                return listlines

    def getMolForm(self, event):
        gtext = (self.text.GetText()).split("\n")
        for lines in gtext:
            if "CELL" in lines:
                cell = lines.split(' ')
                a, b, c, alpha, beta, gamma = self.striplist(cell)[2:8]
                a = float(a)
                b = float(b)
                c = float(c)
                alpha = float(alpha)
                beta = float(beta)
                gamma = float(gamma)
        sfac = self.getsfac(gtext)
        # print sfac
        zerr = self.getZERR(gtext)
        z = (" ".join(zerr)).split()[1]
        z = abs(float(z))
        # bond length ((x2-x1)*a)**2+((y2-y1)*b)**2+((z2-z1)*c)**2+2*b*c(y2-y1)*(z2-z1)*cos(alpha)+2*a*c(z2-z1)*(x2-x1)*cos(beta)+2*a*c(y2-y1)*(x2-x1)*cos(gamma)
        allatoms = []
        for num in range(10):
            for label in sfac:
                for lines in gtext:
                    if lines.upper().startswith(label.upper() + str(num)):
                        #                          if lines.upper().split()[5].startswith("11.0"):
                        allatoms.append(' '.join(lines.upper().split()[0:1]))
        #                          elif lines.upper().split()[5].startswith("10.5"):
        #                              allatoms.append(' '.join(lines.upper().split()[0:1])+str("_0.5_"))

        atomname = []
        for num in range(10):
            for label in sfac:
                for atoms in allatoms:
                    if atoms.upper().startswith(label.upper() + str(num)):
                        atomname.append(label)

        formula = []
        unit = []
        for l in sfac:
            formula.append(l + str(atomname.count(l)))
            unit.append(str(int(z) * int(atomname.count(l))))
        self.dataObj = wx.TextDataObject()
        self.dataObj.SetText("Mol formula: " + " ".join(formula) + "\n" + "UNIT " + " ".join(unit))
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.dataObj)
            wx.TheClipboard.Close()
            dlg = wx.MessageDialog(self,
                                   'The following data was copied to clipboard:  ' + "\n" + "Mol formula: " + " ".join(
                                       formula) + "\n" + "UNIT " + " ".join(unit),
                                   'Data was copied to clipboard', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def ondublicates(self, event):
        dub = self.testfordubs(event)
        if not dub == True:
            dlg = wx.MessageDialog(self, "No dublicates",
                                   'Info', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def get_text_as_list(self):
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        return gtext

    def find_stuff(self, event, searchstring):
        position = []
        start = 0
        end = self.text.GetTextLength()
        length = len(searchstring)
        while True:
            start = self.text.FindText(start, end, searchstring)
            if not start == -1:
                line = (self.text.GetLine(self.text.LineFromPosition(start))).replace("\n", "").replace("\r", "")
                position.append([start, line])
            if start == -1:
                break
            start += length
        return position

    def split_residue(self, event):
        searchstring = "resi"
        resi_position = self.find_stuff(event, searchstring)
        residues = {}
        resi_name = False
        resi_number = False
        for num, line in enumerate(resi_position):
            start, lines = line
            line_lst = lines.split()
            if len(line_lst) >= 2:
                resi_number = line_lst[1]
            if len(line_lst) == 3:
                resi_name = line_lst[2]
            try:
                end = resi_position[num + 1][0]
            except IndexError:
                end = self.text.GetTextLength()
            residues[resi_number] = [start, end, resi_name]
        return residues

    def goto_residue(self, event):
        residue = self.split_residue(event)
        keysdict = residue.keys()
        reslist = ["RESI " + str(k) + " " + str(residue[k][2]) for k in keysdict]
        reslist = sorted(reslist, key=self.onsortkeys)
        if reslist:
            dlg = wx.SingleChoiceDialog(self, 'Select residue to go to', 'Residue?', reslist, wx.CHOICEDLG_STYLE)
            dlg.SetSize((80, 500))
            if dlg.ShowModal() == wx.ID_OK:
                self.SetStatusText('Residue: %s\n' % dlg.GetStringSelection())
                start = residue[(dlg.GetStringSelection()).split()[1]][0]
                end = residue[(dlg.GetStringSelection()).split()[1]][1]
                self.text.GotoPos(start + 1000)
                self.text.SetSelection(start, end)
        else:
            dlg3 = wx.MessageDialog(self, 'There are no residues in this file!',
                                    'Info', wx.OK | wx.ICON_INFORMATION)
            dlg3.ShowModal()
            #######################################################################HERE

    def find_restraints(self, event):
        restraints_dict = {}
        restraints_list = []
        for restraints in ["DFIX", "SADI", "SIMU", "DANG", "SAME", "FLAT", "DELU", "EADP"]:
            restraints_dict[restraints] = self.find_stuff(event, restraints)
            restraints_list = restraints_list + self.find_stuff(event, restraints)
        restraints_list = self.delete_empty_list(event, restraints_list)
        return restraints_dict, restraints_list
        #    for num in range(len(residues)):

    def delete_empty_list(self, event, listoflists):
        list_good = [x for x in listoflists if x != []]
        return list_good

    # def get_atoms_inres(self, event):
    #     pattern = re.compile(r'^([A-Za-z][\d]{1,2}.?)')
    #     restraints_dict, restraints_list = self.find_restraints(event)
    #     residues = self.find_residue(event, self.text.GetText())
    #     inverst_res = dict((v[2], k) for k, v in  residues.iteritems())
    #     print(inverst_res)
    #     for items in restraints_list:
    #         rest=items[1]
    #         lines=rest.split()
    #         for i in lines:
    #             if pattern.match(i):
    #                 try:
    #                    print(restraints_dict[lines[0].split("_")[1]])
    #                    print(i+lines[0].split("_")[1]) # need to include restraints without _
    #                 except IndexError:
    #                     print(i)
    def missmatch(self, event):
        # self.get_atoms_inres(event)
        txt = self.text.GetText()
        ltab = self.getlst(event)  # atoms
        start = 0
        theend = self.text.GetTextLength()
        residues = self.find_residue(event, txt)
        if ltab:  # missmatched atoms
            for searchstring in ltab:
                length = len(searchstring)
                self.finditem(event, searchstring, start, theend, length)
                if "_" in searchstring:
                    if residues:
                        string, residue_number = searchstring.split("_")
                        start = residues[residue_number][0]  # name not used
                        end = residues[residue_number][1]
                        length = len(string)
                        # print(searchstring, residue_number, start, end)
                        starts = self.finditem(event, string, start, end, length)
                        # #starts=self.finditem(event, string, mode, 0, residues[str(0)][0], length)
                        # print(starts)
            restraints_dict, restraints_list = self.find_restraints(event)
            part = 0
            for atoms in ltab:
                if "_" in atoms:
                    atom, part = atoms.split("_")
                for rest in restraints_list:
                    findatom = rest[1].find(atom)
                    if findatom != -1:
                        try:
                            # O5A_2 [2203, u'SADI_LIG 0.01 O5A C11A C9A C12A C10A C13A C11A C14A C12A C15A C13A C16A']
                            if residues[part][2] == rest[1].split()[0].split("_")[1]:
                                # print(atoms, rest, findatom)
                                self.add_color(event, atom, int(rest[0]) + findatom)
                        except KeyError:
                            pass

    def add_color(self, event, label, start):
        length = len(label)
        mode = wx.stc.STC_FIND_MATCHCASE
        self.text.StartStyling(start, wx.stc.STC_INDICS_MASK)
        self.text.SetStyling(length, wx.stc.STC_INDIC1_MASK)

    def finditem(self, event, searchstring, start, end, length):
        starts = []
        mode = wx.stc.STC_FIND_MATCHCASE
        while True:
            start = int(self.text.FindText(start, end, searchstring))
            starts.append(start)
            if start == -1:
                break
            self.text.StartStyling(start, wx.stc.STC_INDICS_MASK)
            self.text.SetStyling(length, wx.stc.STC_INDIC1_MASK)
            start += length
        return starts

    def getlst(self, event):
        listtab = []
        if os.path.exists(self.fnoe + ".lst") == True:
            ls = open(self.fnoe + ".lst", 'r')
            lstread = ls.readlines()
            ls.close()
            for numbers, lines in enumerate(lstread):
                if "type mismatch for" in lines:
                    listtab.append(numbers)
            if len(listtab) == 0:
                dlg3 = wx.MessageDialog(self, 'There are no mismatched atoms in restraints',
                                        'Info', wx.OK | wx.ICON_INFORMATION)
                dlg3.ShowModal()
            else:
                atomslist = []
                gettex = lstread[int(listtab[0]):listtab[-1]]
                gettex = self.striplist(gettex)
                for lines in gettex:
                    atoms = lines.split()[6:10]
                    atomslist = atomslist + atoms
                return atomslist

    def testfordubs(self, event):
        labels = []
        atoms = []
        mode = wx.stc.STC_FIND_MATCHCASE
        pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
        for linum in range(self.text.GetLineCount()):
            line = self.text.GetLineRaw(linum).decode("utf-8")
            if pattern.match(line):
                if not line.upper().startswith("ZERR"):
                    if not line.upper().startswith("Q"):
                        searchval = line.split()[0]
                        labels.append(searchval)
                        atoms.append(line)
        seen = set()
        seen_add = seen.add
        seen_twice = list(set(x for x in labels if x in seen or seen_add(x)))
        #        print(labels, seen_twice)
        self.seen_twice = seen_twice
        if len(seen_twice) != 0:
            for atom in atoms:
                for label in seen_twice:
                    start = 0
                    end = self.text.GetTextLength()

                    if label + " " in atom:
                        length = len(atom)
                        while True:
                            start = int(self.text.FindText(start, end, atom))
                            if start == -1: break
                            self.text.StartStyling(start, wx.stc.STC_INDICS_MASK)
                            self.text.SetStyling(length, wx.stc.STC_INDIC1_MASK)
                            self.text.GotoPos(start + 50)
                            start += length
            return True
        else:
            return False

    def oncalcbonds(self, event, allatoms, oxiline, r):
        proc = []
        a, b, c, alpha, beta, gamma = [float(list_item) for list_item in
                                       self.onGetCell(event)]  # list of strings to float
        for line in allatoms:
            xc = float(oxiline.split()[2])
            yc = float(oxiline.split()[3])
            zc = float(oxiline.split()[4])
            xa = float(line.split()[2])
            ya = float(line.split()[3])
            za = float(line.split()[4])
            xcom = ((xc - xa) * a) ** 2
            ycom = ((yc - ya) * b) ** 2
            zcom = ((zc - za) * c) ** 2

            bc = 2 * b * c * math.cos(math.radians(alpha)) * (yc - ya) * (zc - za)
            ac = 2 * a * c * math.cos(math.radians(beta)) * (zc - za) * (xc - xa)
            ab = 2 * a * b * math.cos(math.radians(gamma)) * (yc - ya) * (xc - xa)
            calcbond = math.sqrt(xcom + ycom + zcom + bc + ac + ab)
            if float(r[0]) > calcbond > float(r[1]):
                proc.append(str(line) + " = " + str(round(calcbond, 3)))
        return proc

    def water(self, event):
        textentry = wx.TextEntryDialog(None, "Please provide oxygen label for hydrogen bond discovery", "Oxygen label?",
                                       "", style=wx.OK | wx.CANCEL)
        if textentry.ShowModal() == wx.ID_OK:
            # # print"You entered: %s" % textentry.GetValue()
            oxy = textentry.GetValue()
            textentry.Destroy()

        gtext = (self.text.GetText()).split("\n")
        sfac = self.getsfac(gtext)
        sfac.insert(0, 'Q')
        allatoms = []
        for num in range(10):
            for label in sfac:
                for lines in gtext:
                    if lines.upper().startswith(label.upper() + str(num)):
                        allatoms.append(' '.join(lines.upper().split()[0:6]))
                    elif lines.upper().startswith(label.upper() + " "):
                        allatoms.append(' '.join(lines.upper().split()[0:6]))
                    elif lines.upper().startswith(oxy.upper() + " "):
                        oxiline = ' '.join(lines.upper().split()[0:6])

        allatoms = list(set(allatoms))
        r = ['1.6', '0.5']
        selected = []
        selfull = []
        hydro = []
        proc = self.oncalcbonds(event, allatoms, oxiline, r)
        dlg = wx.MultiChoiceDialog(self, oxy + ' connectivity to neighboring atoms', 'Bonds', proc, wx.CHOICEDLG_STYLE)
        dlg.SetSize((900, 600))
        if dlg.ShowModal() == wx.ID_OK:
            for items in dlg.GetSelections():
                selected.append(proc[items])
        dlg.Destroy()
        print(selected)
        #####    now calculate bonds to EWG atoms
        if len(selected) >= 1:
            rd = ['5', '1.7']
            contacts = {}
            for i in selected:
                sel = self.oncalcbonds(event, allatoms, i, rd)
                contacts[i.split()[0]] = sel
            rescon = []
            for items in contacts:
                fst = contacts[items]
                for ix in fst:
                    if "O" in (ix.split()[0]).upper():
                        rescon.append(
                            (str(items) + " contact with " + str(ix.split()[0]) + " length=" + str(ix.split()[-1])))
                    elif "F" in (ix.split()[0]).upper():
                        rescon.append(
                            (str(items) + " contact with " + str(ix.split()[0]) + " length=" + str(ix.split()[-1])))
                    elif "N" in (ix.split()[0]).upper():
                        rescon.append(
                            (str(items) + " contact with " + str(ix.split()[0]) + " length=" + str(ix.split()[-1])))
                    elif "CL" in (ix.split()[0]).upper():
                        rescon.append(
                            (str(items) + " contact with " + str(ix.split()[0]) + " length=" + str(ix.split()[-1])))
                    elif "BR" in (ix.split()[0]).upper():
                        rescon.append(
                            (str(items) + " contact with " + str(ix.split()[0]) + " length=" + str(ix.split()[-1])))
            if not len(rescon) == 0:
                result = []
                dlg = wx.MultiChoiceDialog(self, 'Connectivity to EWG atoms', 'Potential hydrogens', rescon,
                                           wx.CHOICEDLG_STYLE)
                dlg.SetSize((900, 600))
                if dlg.ShowModal() == wx.ID_OK:
                    for items in dlg.GetSelections():
                        result.append(rescon[items].split()[0])
                dlg.Destroy()

                if len(result) >= 1:
                    n = 1
                    for qs in result:
                        for li in gtext:
                            if li.startswith(qs.split()[0] + " "):
                                h = 'H' + str(n) + 'O'
                                xh = li.split()
                                xh[0] = h
                                xh[1] = "2"
                                hydro.append("     ".join(xh[0:6]) + "    -1.5000")
                        n = n + 1
                if len(hydro) >= 1:
                    askyesno = wx.MessageDialog(self, "Do you want to add hydrogen atoms to " + str(oxy) + "  atom?",
                                                "Add hydrogens?", wx.YES_NO)
                    igot = askyesno.ShowModal()  # Shows it
                    if igot == wx.ID_YES:
                        self.insertatoms(event, gtext, oxy, hydro)
                    askyesno.Destroy()
            else:

                askyesno = wx.MessageDialog(self,
                                            "No EWG atoms were found in local surrounding. Do you want to add H atoms anyway?",
                                            "Addd Hatoms?", wx.YES_NO)
                igot = askyesno.ShowModal()  # Shows it
                if igot == wx.ID_YES:
                    n = 1
                    for qs in selected:
                        for li in gtext:
                            if li.startswith(qs.split()[0] + " "):
                                print(li)
                                h = 'H' + str(n) + 'O'
                                xh = li.split()
                                xh[0] = h
                                xh[1] = "2"
                                hydro.append("     ".join(xh[0:6]) + "    -1.5000")
                        n = n + 1
                askyesno.Destroy()
                self.insertatoms(event, gtext, oxy, hydro)

    def insertatoms(self, event, gtext, atom, hydro):
        self.topline = self.text.GetFirstVisibleLine()
        for line in gtext:
            if line.startswith(atom + "  "):
                loc1 = gtext.index(line)
                if "=" in line:
                    loc1 = int(gtext.index(line)) + 1
        for h in hydro:
            gtext.insert(loc1 + 1, h)
        ready = '\n'.join(gtext)
        self.text.BeginUndoAction()
        self.text.ClearAll()
        # # printself.topline
        self.text.SetText(ready)
        self.text.EndUndoAction()
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

    def getsfac(self, gtext):
        sfac = ([line for line in gtext if line.lower().startswith('sfac')])
        longsfac = []
        if len(sfac) > 1:

            for atoms in sfac:
                try:
                    longsfac.append(atoms.upper().replace('\r', '').replace('\n', '').split()[1])
                except IndexError:
                    pass
            return longsfac
        else:
            sfacstring = ' '.join(sfac).upper().replace('\r', '').replace('\n', '')
            shortsfac = sfacstring.split()[1:]
            return shortsfac

    def oncalcallbonds(self, event, allatoms, carbons):
        atombonds = []
        a, b, c, alpha, beta, gamma = [float(list_item) for list_item in
                                       self.onGetCell(event)]  # list of strings to float
        for line in carbons:
            for atom in allatoms:
                xc = float(atom.split()[2])
                yc = float(atom.split()[3])
                zc = float(atom.split()[4])
                xa = float(line.split()[2])
                ya = float(line.split()[3])
                za = float(line.split()[4])
                xcom = ((xc - xa) * a) ** 2
                ycom = ((yc - ya) * b) ** 2
                zcom = ((zc - za) * c) ** 2
                bc = 2 * b * c * math.cos(math.radians(alpha)) * (yc - ya) * (zc - za)
                ac = 2 * a * c * math.cos(math.radians(beta)) * (zc - za) * (xc - xa)
                ab = 2 * a * b * math.cos(math.radians(gamma)) * (yc - ya) * (xc - xa)
                calcbond = math.sqrt(xcom + ycom + zcom + bc + ac + ab)
                if calcbond <= 10:
                    atombonds.append([atom.split()[0], line.split()[0], calcbond])
        return atombonds

    def getallcarbons(self, gtext):
        carbons = []
        for numb in range(10):
            for lines in gtext:
                if lines.upper().startswith('C' + str(numb)):
                    carbons.append(' '.join(lines.upper().split()[0:5]))
        return carbons

    # def searchnext(self,event, calcbonds, bond):
    #     for atom in calcbonds:
    #         if
    # def analyse_bonds(self,event, calcbonds):
    #     for bond in calcbonds:
    #        if bond[1]<=2.54:
    #            link

    def find_residue_split(self, event):
        # gtext = self.get_text_as_list(event)
        syms = [[0, 0, 0]]
        allatoms = []
        if len(syms) > 0:
            symsi = 1
            for sym in syms:
                atoms = list(set(self.getallatoms(event, sym, "_" + str(symsi))))
                allatoms = allatoms + atoms
                symsi = symsi + 1
        calcbonds = self.oncalcallbonds(event, allatoms, allatoms)
        print(calcbonds)

    def onGetSymm(self, event, gtext):
        symlist = []
        fisyms = []
        for line in gtext:
            line = line.upper()
            if "SYMM" in line:
                symm = line.replace(',', '').split(' ')
                symlist.append(symm[1:])
        if len(symlist) > 0:
            for syms in symlist:
                for index, sy in enumerate(syms):
                    if len(sy) == 2:
                        syms[index] = str(0) + sy
                for i, item in enumerate(syms):
                    if "+" in item:
                        item = item.split("+")[0]
                        syms[i] = item.replace("1/2", "0.5").replace("1/3", "0.333333333").replace("1/4", "0.25")
                    if "-" in item:
                        item = item.split("-")[0]
                        syms[i] = "-" + str(
                            item.replace("1/2", "0.5").replace("1/3", "0.333333333").replace("1/4", "0.25"))
                fisyms.append(syms)
        return fisyms

    def get_selected_column(self, col):
        column = []
        seltext = self.text.GetSelectedText()
        seltextlist = seltext.split("\n")
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, 'No text selected!',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:
            pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
            for num, lines in enumerate(seltextlist):
                listline = lines.upper().split()
                if pattern.match(lines):
                    try:
                        column.append(str((listline[col])))
                    except IndexError:
                        print("No Item in List")
        return column


    def on_insert_command(self, command):
        self.topline = self.text.GetFirstVisibleLine()

        tx = self.get_text_as_list()
        for line in tx:
            if line.startswith("UNIT"):
                loc1 = tx.index(line)
        tx.insert(loc1+2, command)
        ready = '\n'.join(tx)
        self.text.BeginUndoAction()
        self.text.SetText(ready)
        self.text.EndUndoAction()

    def onHFIX_selected(self):
        atoms = self.get_selected_column(0)
        defvalue = ''
        textentry = wx.TextEntryDialog(None, "Please type the occupancy factor you want to apply!", "Text Entry",
                                           defvalue, style=wx.OK | wx.CANCEL)
        if textentry.ShowModal() == wx.ID_OK:
            defvalue = textentry.GetValue()
            textentry.Destroy()
            for n,a in enumerate(atoms):
                atoms[n] = "HFIX "+defvalue+"  "+a
            comm = "\n".join(atoms)
        self.on_insert_command(comm)



    def onHFIX2(self, event):
        seltext = self.text.GetSelectedText()
        if len(seltext)>0:
            self.onHFIX_selected()
        else:
            self.onDelq(event)
            gtext = (self.text.GetText()).split("\n")
            carbons = self.getallcarbons(gtext)
            hfix = []
            # syms=self.onGetSymm(event, gtext)
            syms = [[0, 0, 0]]
            allatoms = []
            if len(syms) > 0:
                symsi = 1
                for sym in syms:
                    atoms = list(set(self.getallatoms(event, sym, "_" + str(symsi))))
                    allatoms = allatoms + atoms
                    symsi = symsi + 1
            calcbonds = self.oncalcallbonds(event, allatoms, carbons)
            for atom, carb, calcbond in calcbonds:
                # print(carb, atom, calcbond)
                if 1.0 < calcbond < 1.28:
                    if 'C' in atom:
                        hfix.append('t ' + carb.split()[0])
                    elif 'O' in atom:
                        if 1.2 < calcbond < 1.28:
                            hfix.append('d ' + carb.split()[0])
                        elif 1.0 < calcbond < 1.20:
                            hfix.append('t ' + carb.split()[0])
                    elif 'N' in atom:
                        if 1.21 < calcbond < 1.35:
                            hfix.append('d ' + carb.split()[0])
                        elif 1.0 < calcbond < 1.20:
                            hfix.append('t ' + carb.split()[0])

                elif 1.31 < calcbond < 1.45:
                    if 'C' in atom:
                        hfix.append('d ' + carb.split()[0])
                    elif 1.35 < calcbond < 1.44:

                        if 'N' in atom:
                            hfix.append('s ' + carb.split()[0])
                        elif 'O' in atom:
                            hfix.append('s ' + carb.split()[0])
                    elif 'F' in atom:
                        hfix.append('s ' + carb.split()[0])
                    else:
                        if 1.31 < calcbond < 1.40:
                            if 'N' in atom:
                                hfix.append('d ' + carb.split()[0])
                            elif 'O' in atom:
                                hfix.append('d ' + carb.split()[0])
                        else:
                            if not 'N' in atom:
                                if not 'O' in atom:
                                    hfix.append('d ' + carb.split()[0])
                if 1.44 < calcbond < 2.1:
                    hfix.append('s ' + carb.split()[0])
            afix = []
            for c in carbons:
                tmp = []
                for i in hfix:
                    # print(c.split()[0], i.split()[1])
                    if (c.split()[0]).find(i.split()[1]) != -1:
                        #                    print len(c.split()[0]), i.split()[1]
                        if len(c.split()[0]) == len(i.split()[1]):
                            tmp.append(i)
                l = len(tmp)
                #            print c, l
                if l == 1:
                    if tmp[0].split()[0] == 's':
                        afix.append("HFIX 137 " + c.split()[0])
                    elif tmp[0].split()[0] == 'd':
                        afix.append("HFIX 93 " + c.split()[0])
                    elif tmp[0].split()[0] == 't':
                        afix.append("HFIX 163 " + c.split()[0])
                if l == 2:

                    if tmp[0].split()[0] == 's' and tmp[1].split()[0] == 's':
                        afix.append("HFIX 23 " + c.split()[0])
                    if tmp[0].split()[0] == 'd' and tmp[1].split()[0] == 'd':
                        afix.append("HFIX 43 " + c.split()[0])
                    if tmp[0].split()[0] == 'd' and tmp[1].split()[0] == 's':
                        afix.append("HFIX 43 " + c.split()[0])
                    if tmp[0].split()[0] == 's' and tmp[1].split()[0] == 'd':
                        afix.append("HFIX 43 " + c.split()[0])
                if l == 3:
                    if tmp[0].split()[0] == 's' and tmp[1].split()[0] == 's' and tmp[2].split()[0] == 's':
                        afix.append("HFIX 13 " + c.split()[0])

            #        print afix, hfix

            tores = []
            text = self.text.GetText()
            tx = text.split("\n")
            # print tx
            for line in tx:
                if line.startswith("UNIT"):
                    loc1 = tx.index(line)
            for i in afix:
                tx.insert(loc1 + 2, i)
            ready = '\n'.join(tx)
            self.topline = self.text.GetFirstVisibleLine()
            # printself.topline
            self.text.BeginUndoAction()
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)

    def onHFIX(self, event):  # wxGlade: MyFrame.<event_handler>
        self.onDelq(event)
        self.oncleang(event)
        os.chdir(self.dirname)
        askyesno = wx.MessageDialog(self, "Do you want to use the new res \n" "file for the refinement?",
                                    "Change Res file ...", wx.YES_NO)
        igot = askyesno.ShowModal()  # Shows it
        if igot == wx.ID_YES:
            try:
                xcif = subprocess.Popen(self.phtoplaton + ' -f ' + self.filenamenoext + ".res")
                xcif.wait()
                code = xcif.returncode
                if code == 0:
                    if os.path.exists(self.fnoe + ".new") == True:
                        sizenew = os.path.getsize(self.fnoe + ".new")
                        shutil.copy(self.filenamenoext + ".res", self.filenamenoext + ".res" + ".bk")
                        if sizenew == 0:
                            dlg = wx.MessageDialog(self,
                                                   "\t Error File " + self.filenamenoext + ".new" + "  is empty  ",
                                                   'Error', wx.OK | wx.ICON_INFORMATION)
                            dlg.ShowModal()
                            dlg.Destroy()
                        else:
                            shutil.copy(self.filenamenoext + ".new", self.filenamenoext + ".res")
                            self.onReload(event)
                    elif os.path.exists(self.fnoe + "_pl.res") == True:
                        sizenew = os.path.getsize(self.fnoe + "_pl.res")
                        shutil.copy(self.filenamenoext + ".res", self.filenamenoext + ".res" + ".bk")
                        if sizenew == 0:
                            dlg = wx.MessageDialog(self,
                                                   "\t Error File " + self.filenamenoext + "_pl.res" + "  is empty  ",
                                                   'Error', wx.OK | wx.ICON_INFORMATION)
                            dlg.ShowModal()
                            dlg.Destroy()
                        else:
                            shutil.copy(self.filenamenoext + "_pl.res", self.filenamenoext + ".res")
                            self.onReload(event)
                    else:
                        dlg = wx.MessageDialog(self,
                                               "\t Error File " + self.filenamenoext + ".new" + "  does not exist. \n\t You might have a problem with the refinement \n\t or you already have hydrogen atoms ",
                                               'Error', wx.OK | wx.ICON_INFORMATION)
                        dlg.ShowModal()
                        dlg.Destroy()

            except OSError:
                pass
        else:
            subprocess.Popen([self.phtoplaton, ' -u %s', '-p %s', '-f', self.filenamenoext + ".res"])
        askyesno.Destroy()

    def killplaton(self, event):
        if self.ossystem.startswith("win"):
            os.system("taskkill /f /im platon.exe")
            print("kill platon")

    def lastfile(self, event, dirname, extension):
        return max([f for f in os.listdir(dirname) if f.lower().endswith(extension)], key=os.path.getctime)

    def onAddSym(self, event):
        os.chdir(self.dirname)
        askyesno = wx.MessageDialog(self, "Res file will be changed do you want to continue?", "Change res file ...",
                                    wx.YES_NO)
        igot = askyesno.ShowModal()  # Shows it
        if igot == wx.ID_YES:
            askyesno.Destroy()
            shutil.copy(self.fnoe + ".res", self.fnoe + ".sym" + ".bk")
            try:
                print(self.phtoplaton + ' -u -p -n ' + self.fnoe + '.res')
                addsym = subprocess.Popen(self.phtoplaton + ' -u -p -n ' + self.fnoe + '.res',
                                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                          shell=True)
                if not self.ossystem.startswith("win"):
                    self.onterminal(event, addsym, False)
                stdout_value = addsym.communicate()
                code = addsym.returncode
                if code == 0:
                    if os.path.exists(self.fnoe + "_pl.res"):
                        try:
                            shutil.copy(self.fnoe + "_pl.res", self.fnoe + ".res")
                        except shutil.Error:
                            pass
                    self.onReload(event)

            except OSError:
                pass

    def onORTEP(self, event):  # wxGlade: MyFrame.<event_handler>
        print("ORTEP")
        self.killplaton(event)
        try:
            print(self.phtoplaton + " -a " + self.fnoe + '.cif')
            if os.path.exists(self.fnoe + ".cif"):
                try:
                    ort = subprocess.call(self.phtoplaton + " -a  " + self.fnoe + '.cif', stdin=subprocess.PIPE,
                                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                except subprocess.CalledProcessError as e:
                    output = e.output
                    retcode = e.returncode
                    print(retcode)
            else:
                askyesno = wx.MessageDialog(self, "File not found", "file not found", wx.OK)

        except OSError:
            pass

    def oncifcheck(self, event):
        if sys.platform == 'darwin':
            subprocess.Popen(['open', "http://journals.iucr.org/services/cif/checkcif.html"])
        else:
            webbrowser.open("http://journals.iucr.org/services/cif/checkcif.html")

    def onPlaton(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        self.killplaton(event)
        if os.path.exists(self.fnoe + ".cif") == True:
            try:
                if self.ossystem.startswith("win"):
                    subprocess.Popen([self.phtoplaton, self.filenamenoext + ".cif"])
                elif self.ossystem.startswith("darwin"):
                    subprocess.Popen([self.phtoplaton, self.filenamenoext + ".cif"])
                else:
                    subprocess.Popen([self.phtoplaton, self.filenamenoext + ".cif"])
            except OSError:
                pass
        else:
            dlg = wx.MessageDialog(self, "\t Error File " + self.fnoe + ".cif" + "  does not exist. \n\t",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onplatonpxrd(self, event):  # wxGlade: MyFrame.<event_handler>
        print("Running Pluton", self.phtoplaton + " -P " + self.fnoe + ".res")
        try:
            ort = subprocess.Popen(self.phtoplaton + " -P " + self.fnoe + ".res", shell=True)
        except OSError:
            pass

    def onFCFVALIDATE(self, event):  # wxGlade: MyFrame.<event_handler>
        self.killplaton(event)
        print("Running Pluton", self.phtoplaton + " -p " + self.fnoe + ".res")
        try:
            plot = subprocess.Popen(self.phtoplaton + " -u -p  -V " + self.fnoe + ".cif", stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            if not self.ossystem.startswith("win"):
                self.onterminal(event, plot, False)
            out = plot.communicate()[0]
            code = plot.returncode
            if code == 0:
                webbrowser.open(self.fnoe + '.ckf')
        except OSError:
            pass

    def TWIN_1(self, event):
        command = "TWIN 0 1 0 1 0 0 0 0 -1"
        self.add_command(event, command)

    def TWIN_2(self, event):
        command = "TWIN 1 0 0 0 -1 0 0 0 -1"
        self.add_command(event, command)

    def TWIN_3(self, event):
        command = "TWIN 0 0 1 0 1 0 -1 0 -1 3"
        self.add_command(event, command)

    def TWIN_4(self, event):
        command = "TWIN -1 0 0 0 -1 0 0 0 1"
        self.add_command(event, command)

    def MOVE_1(self, event):
        command = "MOVE .25 .25 1 -1"
        self.add_command(event, command)

    def MOVE_2(self, event):
        command = "MOVE 1 .5 1 -1"
        self.add_command(event, command)

    def MOVE_3(self, event):
        command = "MOVE 1 .5 1 -1"
        self.add_command(event, command)

    def MOVE_4(self, event):
        command = "MOVE 1 .5 .25 -1"
        self.add_command(event, command)

    def MOVE_5(self, event):
        command = "MOVE 1 .5 .25 -1"
        self.add_command(event, command)

    def MOVE_6(self, event):
        command = "MOVE .25 .25 .25 -1"
        self.add_command(event, command)

    def MOVE_7(self, event):
        command = "MOVE 1 .5 1 -1"
        self.add_command(event, command)

    def add_command(self, event, command):
        gtext = self.text.GetText().split("\n")
        self.ongetunit(event, gtext)
        gtext.insert(int(self.unitposition) + 2, command)
        ready = '\n'.join(gtext)
        self.text.BeginUndoAction()
        self.text.SetText(ready)
        self.text.EndUndoAction()
        self.onColor1(event)
        self.text.ScrollToLine(0)

    def insert_chunk(self, event, chunk):
        gtext = self.text.GetText().split("\n")
        self.ongetunit(event, gtext)
        chunk_line = '\n'.join(chunk)
        gtext.insert(int(self.unitposition) + 2, chunk_line)
        ready = '\n'.join(gtext)
        self.text.BeginUndoAction()
        self.text.SetText(ready)
        self.text.EndUndoAction()
        self.onColor1(event)
        self.text.ScrollToLine(0)

    def onSqueeze(self, event):  # wxGlade: MyFrame.<event_handler>
        os.chdir(self.dirname)
        askyesno = wx.MessageDialog(self, " Do you want to use the new hkl \n" "file for refinement?",
                                    "Change hkl file ...", wx.YES_NO)
        igot = askyesno.ShowModal()  # Shows it
        if igot == wx.ID_YES:
            try:
                sq = subprocess.Popen([self.phtoplaton, "-q", self.filenamenoext + ".res"], stdout=subprocess.PIPE)
                if not self.ossystem.startswith("win"):
                    self.onterminal(event, sq, False)
                stdout_value = sq.communicate()
                sq.wait()
                code = sq.returncode
                if code == 0:
                    if os.path.exists(self.filenamenoext + "_sq.hkl") == True:
                        sizenew = os.path.getsize(self.filenamenoext + "_sq.hkl")
                        shutil.copy(self.filenamenoext + ".hkl", self.filenamenoext + ".hkl" + ".nosq")
                        shutil.copy(self.filenamenoext + ".res", self.filenamenoext + ".res" + ".nosq")
                        if sizenew == 0:
                            dlg = wx.MessageDialog(self,
                                                   "\t Error File " + self.filenamenoext + ".hkp" + "  is empty  ",
                                                   'Error', wx.OK | wx.ICON_INFORMATION)
                            dlg.ShowModal()
                            dlg.Destroy()
                        else:
                            shutil.copy(self.filenamenoext + "_sq.hkl", self.filenamenoext + ".hkl")
                            shutil.copy(self.filenamenoext + "_sq.ins", self.filenamenoext + ".res")
                            shutil.copy(self.filenamenoext + "_sq.ins", self.filenamenoext + ".ins")
                            shutil.copy(self.filenamenoext + "_sq.fab", self.filenamenoext + ".fab")
                            self.onReloadRes(event)
                    #                            self.addabin(event)

                    else:
                        dlg = wx.MessageDialog(self,
                                               "\t Error File " + self.filenamenoext + "._sq.hkl" + "  does not exist. \n\t You might have a problem with the refinement ",
                                               'Error', wx.OK | wx.ICON_INFORMATION)
                        dlg.ShowModal()
                        dlg.Destroy()


            except OSError:

                pass
        else:
            if self.ossystem.startswith("win"):
                sq = subprocess.Popen([self.phtoplaton, "-u %s", "-p %s", "-q", self.filenamenoext + ".res"])
            elif self.ossystem.startswith("darwin"):
                sq = subprocess.Popen([self.phtoplaton, "-u %s", "-p %s", "-q", self.filenamenoext + ".res"])
            else:
                sq = subprocess.Popen(
                    ['xterm', '-hold', '-e', self.phtoplaton, " -u %s", "-p %s", "-q", self.filenamenoext + ".res"])

    def onCifVal(self, event):

        try:
            if self.ossystem.startswith("win"):
                subprocess.Popen(self.phtoplaton + " -U " + self.filenamenoext + ".cif")
            elif self.ossystem.startswith("darwin"):
                subprocess.Popen(self.phtoplaton + " -U " + self.filenamenoext + ".cif")
            else:
                print(self.phtoplaton + " -u " + self.fnoe + ".cif")
                cif = subprocess.Popen(self.phtoplaton + " -u " + self.fnoe + ".cif", stdout=subprocess.PIPE,
                                       shell=True)
                if not self.ossystem.startswith("win"):
                    self.onterminal(event, cif, False)
        except OSError:
            pass

    def HTMLCombine(self, event):
        beg = r"<html><head /><body><center><h2>Appendix" + "\n" + r"</h2><hr> </hr>"
        end = r"</center></body></html>"
        filters = 'HTML files (*.html)|*.html|All files (*.*)|*.*'
        dialog = wx.FileDialog(self, "Choose a file", self.dirname, wildcard=filters, style=wx.FD_OPEN | wx.FD_MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            selected = dialog.GetPaths()
            dirnameall = dialog.GetDirectory()
            if os.path.exists(os.path.join(dirnameall, 'allhtml.html')) == True:
                os.remove(os.path.join(dirnameall, 'allhtml.html'))
            last = open(os.path.join(dirnameall, 'allhtml.tmp'), 'wa')
            for fileitem in selected:
                firstf = open(fileitem, 'r')
                first = firstf.read()
                first = "".join([first, "<p>&nbsp</p> <p>&nbsp </p>"])
                first2 = first.replace(beg, "").replace(end, "")
                firstf.close()
                last.writelines(first2)
            last.close()
            last = open(os.path.join(dirnameall, 'allhtml.tmp'), 'ra')
            fullfile1 = last.read()
            fullfile2 = fullfile1.split(" ")
            fullfile2.insert(0, beg)
            fullfile2.append(end)
            x = 1
            for line in fullfile2:
                if "Table" in line:
                    ind = fullfile2.index(line)
                    fullfile2.remove(line)
                    y = fullfile2.pop(ind)
                    line = line.replace("Table", "Table " + str(x) + r":")
                    fullfile2.insert(ind, line)
                    x = x + 1
            fullfile3 = ' '.join(fullfile2)
            last.close()
            os.remove(os.path.join(dirnameall, 'allhtml.tmp'))
            final = open(os.path.join(dirnameall, 'allhtml.html'), 'wa')
            final.writelines(fullfile3)
            final.close()
            self.SetStatusText('File allhtml.html has been created in ' + dirnameall)
            publ = wx.MessageDialog(self, "Do you want to view allhtml.html", "allhtml.html ...", wx.YES_NO)
            igot = publ.ShowModal()  # Shows it
            if igot == wx.ID_YES:
                webbrowser.open(os.path.join(dirnameall, 'allhtml.html'))

        dialog.Destroy()

    def Combine(self, event):
        listnumber = []
        list = []
        filters = 'Cif files (*.cif)|*.cif|All files (*.*)|*.*'
        dialog = wx.FileDialog(self, "Choose a file", self.dirname, wildcard=filters, style=wx.FD_OPEN | wx.FD_MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            selected = dialog.GetPaths()
            dirnameall = dialog.GetDirectory()
            if os.path.exists(os.path.join(dirnameall, 'allcifs.cif')) == True:
                os.remove(os.path.join(dirnameall, 'allcifs.cif'))
            last = open(os.path.join(dirnameall, 'allcifs.cif'), 'a')
            first = selected[0]
            firstfile = open(first, 'r')
            firstext = firstfile.readlines()
            firstfile.close()
            head = []
            for number, line in enumerate(firstext):
                if line.startswith("data_global"):
                    head.append(number)
                if not line.startswith("data_global"):
                    if line.startswith("data_"):
                        head.append(number)
            if len(head) == 2:
                header = firstext[head[0]:head[1]]
                last.writelines(header)
            else:
                header = "\n"
                last.writelines(header)
            for fileitem in selected:
                f = open(fileitem, 'r')
                fread = f.readlines()
                f.close()
                for number, line in enumerate(fread):
                    if not line.startswith("data_global"):
                        if line.startswith("data_"):
                            num = number
                            texta = fread[number:]
                            last.writelines(texta)
            last.close()

            self.SetStatusText('File allcifs.cif has been created in ' + dirnameall)
            publ = wx.MessageDialog(self, "Do you want to perform checkCIF for allcif.cif file?", "CheckCIF?",
                                    wx.YES_NO)
            igot = publ.ShowModal()  # Shows it
            if igot == wx.ID_YES:
                webbrowser.open("http://journals.iucr.org/services/cif/checkcif.html")

        dialog.Destroy()

    def GETLISTV(self, event, seltable):
        listTT = seltable[0]
        text1 = open(os.path.join(self.path, "user", listTT), 'r')
        text = text1.read()
        text1.close()
        if os.path.exists(os.path.join(self.dirname, 'publish.cif')) == True:
            fline = open(os.path.join(self.dirname, 'publish.cif'), 'r')
        # # print"opening file:  ",  os.path.join(self.dirname,'publish.cif')
        else:
            fline = open(self.fnoe + ".cif", 'r')

        pos1 = ['_audit_creation_method', '_chemical_name_systematic', '_space_group_crystal_system',
                '_space_group_IT_number',
                '_space_group_name_H-M_alt', '_space_group_name_Hall',
                '_chemical_name_common', '_chemical_formula_moiety',
                '_chemical_formula_sum', '_chemical_formula_weight', '_symmetry_cell_setting'
            , '_symmetry_space_group_name_H-M', '_symmetry_space_group_name_Hall',
                '_symmetry_equiv_pos_as_xyz', '_cell_length_a', '_cell_length_b', '_cell_length_c',
                '_cell_angle_alpha', '_cell_angle_beta', '_cell_angle_gamma', '_cell_volume',
                '_cell_formula_units_Z', '_cell_measurement_temperature', '_cell_measurement_reflns_used',
                '_cell_measurement_theta_min', '_cell_measurement_theta_max', '_exptl_crystal_description',
                '_exptl_crystal_colour', '_exptl_crystal_size_max', '_exptl_crystal_size_mid',
                '_exptl_crystal_size_min', '_exptl_crystal_density_meas', '_exptl_crystal_density_diffrn',
                '_exptl_crystal_density_method', '_exptl_crystal_F_000', '_exptl_absorpt_coefficient_mu',
                '_exptl_absorpt_correction_type', '_exptl_absorpt_correction_T_min',
                '_exptl_absorpt_correction_T_max', '_exptl_absorpt_process_details', '_exptl_special_details',
                '_diffrn_ambient_temperature', '_diffrn_radiation_wavelength', '_diffrn_radiation_type',
                '_diffrn_radiation_source', '_diffrn_radiation_monochromator', '_diffrn_measurement_device_type',
                '_diffrn_measurement_method', '_diffrn_detector_area_resol_mean', '_diffrn_reflns_number',
                '_diffrn_reflns_av_R_equivalents', '_diffrn_reflns_av_sigmaI/netI', '_diffrn_reflns_limit_h_min',
                '_diffrn_reflns_limit_h_max', '_diffrn_reflns_limit_k_min', '_diffrn_reflns_limit_k_max',
                '_diffrn_reflns_limit_l_min', '_diffrn_reflns_limit_l_max', '_diffrn_reflns_theta_min',
                "_exptl_transmission_factor_min", "_exptl_transmission_factor_max",
                '_diffrn_reflns_theta_max', '_reflns_number_total', '_reflns_number_gt',
                '_reflns_threshold_expression', '_refine_special_details', "_diffrn_standards_number",
                "_diffrn_standards_interval_count",
                "_diffrn_standards_decay_%", '_refine_ls_structure_factor_coef', '_refine_ls_matrix_type',
                '_refine_ls_weighting_scheme',
                '_refine_ls_weighting_details', '_atom_sites_solution_primary', '_atom_sites_solution_secondary',
                '_atom_sites_solution_hydrogens', '_refine_ls_hydrogen_treatment', '_refine_ls_extinction_method',
                '_refine_ls_extinction_coef', '_refine_ls_number_reflns', '_refine_ls_number_parameters',
                '_refine_ls_number_restraints', "_diffrn_reflns_av_unetI/netI", '_refine_ls_R_factor_all',
                '_refine_ls_R_factor_gt',
                '_refine_ls_wR_factor_ref', '_refine_ls_wR_factor_gt', '_refine_ls_goodness_of_fit_ref',
                '_refine_ls_restrained_S_all', '_refine_ls_shift/su_max', '_refine_ls_shift/su_mean',
                '_atom_site_label', '_atom_site_type_symbol', '_atom_site_fract_x', '_atom_site_fract_y',
                '_atom_site_fract_z', '_atom_site_U_iso_or_equiv', '_atom_site_adp_type', '_atom_site_occupancy',
                '_platon_squeeze_void_nr', '_platon_squeeze_void_average_x', '_platon_squeeze_void_average_y',
                '_platon_squeeze_void_average_z', '_platon_squeeze_void_volume',
                '_platon_squeeze_void_count_electrons', '_platon_squeeze_void_content', '_platon_squeeze_details',
                '_diffrn_measured_fraction_theta_max', '_diffrn_reflns_theta_full',
                '_diffrn_measured_fraction_theta_full', '_refine_diff_density_max',
                '_refine_diff_density_min', '_refine_diff_density_rms', '_geom_hbond_atom_site_label_D',
                '_geom_hbond_atom_site_label_H', '_geom_hbond_atom_site_label_A',
                '_geom_hbond_distance_DH', '_geom_hbond_distance_HA', '_geom_hbond_distance_DA',
                '_geom_hbond_angle_DHA', '_geom_hbond_site_symmetry_A']
        lines = fline.readlines()

        for num, line in enumerate(lines):
            for i in pos1:
                #                      x=0
                #                      while x<3:
                if (line.lower()[:40].find(i.lower()) != -1):
                    if "_chemical_formula_sum" in line:
                        result = lines[num + 1]
                        nospaceresult = result.replace(" ", "").replace("'", "")
                        text = text.replace(i, nospaceresult)
                    else:
                        result = line[len(i):-1]
                        nospaceresult = result.replace(" ", "").replace("'", "")
                        text = text.replace(i, nospaceresult)
        #                      x=x+1
        text2 = open(self.fnoe + "_table" + ".rtf", 'w')
        text2.write(text)
        text2.close()
        fline.close()
        #        self.SetStatusText("Resulting table was saved as "+ self.dirnameslash+"tableforpub.rtf")
        publ = wx.MessageDialog(self, "Do you want to view the resulting table", "Table...", wx.YES_NO)
        igot = publ.ShowModal()  # shows it
        if igot == wx.ID_YES:
            os.chdir(self.dirname)
            webbrowser.open('file://%s' % os.path.join(self.dirname, self.filenamenoext + "_table" + ".rtf"))

    def usertable(self, event):
        userdir = os.path.join(self.path, "user")
        list_user_tables = []
        for file in os.listdir(userdir):
            if file.endswith(".rtf"):
                list_user_tables.append(file)
        print(list_user_tables)
        return list_user_tables

    def onHtmlTable(self, event):
        list_user_tables = self.usertable(event)
        list_user_tables = sorted(list_user_tables, key=self.onsortkeys)
        if os.path.exists(self.fnoe + '.cif') or os.path.exists(os.path.join(self.path, 'publish.cif')) == True:
            dlg = wx.lib.dialogs.MultipleChoiceDialog(self, "Please select the table", "Table?", list_user_tables,
                                                      size=(500, 600))
            if (dlg.ShowModal() == wx.ID_OK):
                self.GETLISTV(event, dlg.GetValueString())
                dlg.Destroy()
        else:
            dlg = wx.MessageDialog(self, "No cif file found!",
                                   'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    def onRXCIF(self, event):  # wxGlade: MyFrame.<event_handler>
        tex = self.fnoe + ".tex"
        fcif = self.fnoe + ".cif"
        try:
            if self.ossystem.startswith("win"):
                os.chdir(self.phtoxcif.replace("xcif", ""))
                proc = subprocess.Popen([self.phtoxcif, self.fnoe], stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, env={'xcif': self.phtoxcif.replace(r'\xcif', '')})
                inside = "S\n" + self.fnoe + "\n" + "T\n" + fcif + "\n" + "Y\n" + tex + "\n" + "def\nY\nY\nN\nY\nN\nN\nN\nY\nN\nQ\n"
                # # printinside
                proc.stdin.write(inside)
                stdin_value, stdout_value = proc.communicate()
                self.SetStatusText("Resulting table was saved as " + self.fnoe + ".tex")
            elif self.ossystem.startswith("darwin"):
                os.chdir(self.phtoxcif.replace("xcif", ""))
                # # printself.phtoxcif.replace("xcif", "")
                # # print"kjhkhkjh", os.path.split(self.phtoxcif)[1]
                proc = subprocess.Popen([self.phtoxcif, self.fnoe], stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, env={'xcif': self.phtoxcif.replace("/xcif", "")})
                inside = "S\n" + self.fnoe + "\n" + "T\n" + fcif + "\n" + "Y\n" + tex + "\n" + "def\nY\nY\nN\nY\nN\nN\nN\nY\nN\nQ\n"
                # # printinside
                proc.stdin.write(inside)
                stdin_value, stdout_value = proc.communicate()
                self.SetStatusText("Resulting table was saved as " + self.fnoe + ".tex")
            else:
                os.chdir(self.phtoxcif.replace("xcif", ""))
                # # printself.phtoxcif.replace("xcif", "")
                # # print"kjhkhkjh", os.path.split(self.phtoxcif)[1]
                proc = subprocess.Popen([self.phtoxcif, self.fnoe], stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, env={'xcif': self.phtoxcif.replace("/xcif", "")})
                inside = "S\n" + self.fnoe + "\n" + "T\n" + fcif + "\n" + "Y\n" + tex + "\n" + "def\nY\nY\nN\nY\nN\nN\nN\nY\nN\nQ\n"
                # # printinside
                proc.stdin.write(inside)
                stdin_value, stdout_value = proc.communicate()
                self.SetStatusText("Resulting table was saved as " + self.fnoe + ".tex")
        except OSError:
            pass

    def updatepcf(self, event):
        pcfopen = open(self.filenamenoext + ".pcf")
        tex = pcfopen.readlines()
        pcfopen.close()
        lit1 = "_refine_ls_hydrogen_treatment"
        lit2 = "_exptl_absorpt_process_details"
        lit3 = "_exptl_absorpt_correction_type"
        lita = "_chemical_formula_moiety"
        litb = "_cell_formula_units_Z"
        litc = "_exptl_crystal_description"
        litd = "_symmetry_space_group_name_H-M"
        lite = "_exptl_crystal_density_meas"
        litf = "_symmetry_space_group_name_Hall"
        x = []
        y = []
        z = []
        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        for line in tex:
            if line.startswith(lit1):
                x.append(line)
        if not x:
            tex.insert(5, "_refine_ls_hydrogen_treatment     constr \r\n")
        else:
            for bx in x:
                if bx in tex:
                    break
                else:
                    tex.insert(5, "_refine_ls_hydrogen_treatment     constr \r\n")

        for line in tex:
            if line.startswith(lit2):
                y.append(line)
        if not y:
            tex.insert(6, "_exptl_absorpt_process_details    'Sadabs (Sheldrick, 1996)'\r\n")
        else:
            for by in y:
                if by in tex:
                    break
                else:
                    tex.insert(6, "_exptl_absorpt_process_details    'Sadabs (Sheldrick, 1996)'\r\n")
        for line in tex:
            if line.startswith(lit3):
                z.append(line)
        if not z:
            tex.insert(7, "_exptl_absorpt_correction_type    multi-scan\r\n")
        else:
            for bz in z:
                if bz in tex:
                    lbz = tex.index(bz)
                    tex.remove(bz)
                    tex.insert(lbz, "_exptl_absorpt_correction_type    multi-scan\r\n")
                else:
                    tex.insert(7, "_exptl_absorpt_correction_type    multi-scan\r\n")
                    ###################################################################################3
        for line in tex:
            if line.startswith(lita):
                a.append(line)
        if not a:
            tex.insert(2, "_chemical_formula_moiety          ? \r\n")
        else:
            for ba in a:
                if ba in tex:
                    break
                else:
                    tex.insert(2, "_chemical_formula_moiety       ? \r\n")
                    ###################################################################################
        for line in tex:
            if line.startswith(litd):
                d.append(line)
        if not d:
            tex.insert(2, "_symmetry_space_group_name_H-M              ? \r\n")
        else:
            for bd in d:
                if bd in tex:
                    break
                else:
                    tex.insert(2, "_symmetry_space_group_name_H-M             ? \r\n")
                    ###########################################################################
        for line in tex:
            if line.startswith(litc):
                c.append(line)
        if not c:
            tex.insert(9, "_exptl_crystal_description          ? \r\n")
        else:
            for bc in c:
                if bc in tex:
                    break
                else:
                    tex.insert(9, "_exptl_crystal_description          ? \r\n")
                    ################################################################################
        for line in tex:
            if line.startswith(litb):
                b.append(line)
        if not b:
            tex.insert(3, "_cell_formula_units_Z          ? \r\n")
        else:
            for bb in b:
                if bb in tex:
                    break
                else:
                    tex.insert(3, "_cell_formula_units_Z          ? \r\n")
                    #################################################################################
        for line in tex:
            if line.startswith(lite):
                e.append(line)
        if not e:
            tex.insert(10, "_exptl_crystal_density_meas      '?'\r\n")
        else:
            for be in e:
                if be in tex:
                    item = tex.index(be)
                    tex.remove(be)
                    tex.insert(item, "_exptl_crystal_density_meas      '?'\r\n")
                else:
                    tex.insert(10, "_exptl_crystal_density_meas      '?'\r\n")

        pcfopen = open(self.filenamenoext + ".pcf", 'w')
        pcfopen.writelines(tex)
        pcfopen.close()

    def editPcf(self, event):
        os.chdir(self.dirname)
        if os.path.exists(self.filenamenoext + ".pcf") == True:
            self.updatepcf(event)
        else:
            self.color = self.min = self.mid = self.max = self.zval = self.mformula = "?"
            publ = wx.MessageDialog(self,
                                    " A *.pcf file was not found in the current directory! Do you want to create it? Alternatively, you can generate it with XPREP program.",
                                    "Error! no PCF file", wx.YES_NO)
            igot = publ.ShowModal()  # shows it
            if igot == wx.ID_YES:
                pcfopen = open(self.filenamenoext + ".pcf", 'w')

                pcf = '''
_symmetry_cell_setting             '?'
_chemical_formula_moiety            ? 
_cell_formula_units_Z               ? 
_symmetry_space_group_name_H-M     '?'
_cell_measurement_temperature      100
_cell_measurement_reflns_used      '?'
_refine_ls_hydrogen_treatment      constr 
_exptl_absorpt_process_details     '?'
_cell_measurement_theta_min         ?
_cell_measurement_theta_max         ?
_exptl_crystal_description         '?'
_exptl_crystal_colour              '?'
_exptl_crystal_size_min             ?
_exptl_crystal_size_mid             ?
_exptl_crystal_size_max             ?
_exptl_crystal_density_meas         'not measured'
_exptl_crystal_density_method       '?'
_exptl_absorpt_correction_type       multi-scan
_exptl_absorpt_correction_T_min      ?
_exptl_absorpt_correction_T_max      ?
_diffrn_ambient_temperature          ?
_diffrn_radiation_type              '?'
_diffrn_radiation_source            '?'
_diffrn_radiation_monochromator     '?'
_diffrn_measurement_device_type     '?'
_diffrn_measurement_method          '?'
_diffrn_detector_area_resol_mean    '?'
_diffrn_standards_number            '?'
_diffrn_standards_interval_count     ?
_diffrn_standards_decay_%            ?
_computing_data_collection          '?'
_computing_cell_refinement          '?'
_computing_data_reduction           '?'
_computing_structure_solution       '?' 
_computing_structure_refinement     '?'
_computing_molecular_graphics       '?'
_computing_publication_material     'Linxtl'
                '''
                pcfopen.write(pcf)
                pcfopen.close()
                self.updatepcf(event)

    def onPrpare(self, event):  # thanks to Jice from daniweb to help me out with this code!!!!

        ##########################################################################################
        from checkcif import Options
        self.editPcf(event)
        self.opt = Options(self, self.version, self.fnoe, self.dirname, self.path, self.text)
        print("checkcif")

        # from checkcifgui import checkcifgui
        # checkcifgui(self, self.version, self.fnoe, self.dirname, self.path, self.text)


    ##########################################################################################

    def onMShellx(self, event):  # wxGlade: MyFrame.<event_handler>
        try:
            manual = 'http://shelx.uni-ac.gwdg.de/SHELX/shelx97.pdf'
            # os.path.join(path,'about','shelx.pdf')
            if self.ossystem.startswith("win"):
                webbrowser.open(manual)
            elif self.ossystem.startswith('darwin'):
                subprocess.Popen(['open', manual])
            else:
                webbrowser.open(manual)
        except OSError:
            pass

    def onDelq(self, event):

        gtext = self.text.GetText()
        tx = gtext.split("\n")
        i = 0
        while (i < 10):
            for line in tx:
                if line.startswith("Q"):
                    tx.remove(line)

            i = i + 1
        ready = '\n'.join(tx)
        self.topline = self.text.GetFirstVisibleLine()
        # # printself.topline
        self.text.SetText(ready)
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

    def DelHtab(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        gtext = self.text.GetText()
        tx = gtext.split("\n")
        i = 0
        while (i < 10):
            for line in tx:
                if line.startswith("HTAB"):
                    tx.remove(line)
                elif line.startswith("EQIV"):
                    tx.remove(line)
            i = i + 1
        ready = '\n'.join(tx)
        self.text.SetText(ready)
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

    def delresi(self, event):
        todel = "RESI"
        self.del_function(event, todel)

    def Delmol(self, event):
        todel = "MOLE"
        self.del_function(event, todel)

    def del_function(self, event, todel):
        self.topline = self.text.GetFirstVisibleLine()
        gtext = self.text.GetText()
        tx = gtext.split("\n")
        i = 0
        while (i < 10):
            for line in tx:
                if line.startswith(todel):
                    tx.remove(line)
            i = i + 1
        ready = '\n'.join(tx)
        self.text.SetText(ready)
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

    def textsize(self, text):
        length = len(text)
        return length

    def editisotr(self, event):
        col = 6
        defvalue = "0.05"
        self.valuedit(event, col, defvalue)

    def onEditOc(self, event):  # replace the column instead of value
        col = 5
        defvalue = "10.50000"
        self.valuedit(event, col, defvalue)

    def PERTURB(self, event):  # replace the column instead of value
        col = 2
        value = 0.015
        self.xyz_edit(event, col, value)

    def add_trailer(self, event):
        col = 0
        textentry = wx.TextEntryDialog(None, "Please provide a trailer for the atomic label", "Trailer", "A",
                                       style=wx.OK | wx.CANCEL)
        if textentry.ShowModal() == wx.ID_OK:
            newlabel = textentry.GetValue()
        textentry.Destroy()
        value = str(newlabel)
        self.label_edit(event, col, value)

    def label_edit(self, event, col, value):
        seltextresult = []
        gtl = self.text.GetText()
        sfac = self.getsfac(gtl.split('\n'))
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        seltextlist = seltext.split("\n")
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, 'No text selected!',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:
            pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
            for num, lines in enumerate(seltextlist):
                listline = lines.upper().split()
                if pattern.match(lines):
                    try:
                        listline[col] = str((listline[col]) + value)
                        seltextlist[num] = '   '.join(listline)
                    except IndexError:
                        print("No Item in List")
            lb = self.textsize(seltext)
            sel = "\n".join(seltextlist)
            b, e = self.text.GetSelection()
            self.text.BeginUndoAction()
            self.text.ReplaceSelection(sel)
            self.text.EndUndoAction()
            self.onColor1(event)
            le = self.textsize(sel)
            diff = int(lb) - int(le)
            self.text.ScrollToLine(self.topline)
            self.text.SetSelection(b, e - diff)

    def xyz_edit(self, event, col, value):
        seltextresult = []
        gtl = self.text.GetText()
        sfac = self.getsfac(gtl.split('\n'))
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        seltextlist = seltext.split("\n")
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, 'No text selected!',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:
            pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
            for num, lines in enumerate(seltextlist):
                listline = lines.upper().split()
                if pattern.match(lines):
                    try:
                        listline[col] = str(float(listline[col]) + value)
                        seltextlist[num] = '   '.join(listline)
                    except IndexError:
                        print("No Item in List")
            lb = self.textsize(seltext)
            sel = "\n".join(seltextlist)
            b, e = self.text.GetSelection()
            self.text.BeginUndoAction()
            self.text.ReplaceSelection(sel)
            self.text.EndUndoAction()
            self.onColor1(event)
            le = self.textsize(sel)
            diff = int(lb) - int(le)
            self.text.ScrollToLine(self.topline)
            self.text.SetSelection(b, e - diff)

    def valuedit(self, event, col, defvalue):
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        seltextlist = seltext.split("\n")
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, 'No text selected!',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:

            textentry = wx.TextEntryDialog(None, "Please type the occupancy factor you want to apply!", "Text Entry",
                                           defvalue, style=wx.OK | wx.CANCEL)
            if textentry.ShowModal() == wx.ID_OK:
                defvalue = textentry.GetValue()
            textentry.Destroy()
            pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')

            for num, lines in enumerate(seltextlist):
                listline = lines.upper().split()
                if pattern.match(lines):
                    try:
                        listline[col] = defvalue
                        print(listline)
                        seltextlist[num] = '   '.join(listline)
                    except IndexError:
                        print("No Item in List")

            lb = self.textsize(seltext)
            sel = "\n".join(seltextlist)
            b, e = self.text.GetSelection()
            self.text.BeginUndoAction()
            self.text.ReplaceSelection(sel)
            self.text.EndUndoAction()
            self.onColor1(event)
            le = self.textsize(sel)
            diff = int(lb) - int(le)
            self.text.ScrollToLine(self.topline)
            self.text.SetSelection(b, e - diff)

    def ondublicate(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            linenumber = self.text.GetCurrentLine()
            line_text = self.text.GetCurLine()
            pos = self.text.GetCurrentPos()
            beg = pos - int(line_text[1])
            end = pos - int(line_text[1]) + len(line_text[0])
            self.text.SetSelection(beg, end)
            line = line_text[0]
            print(line)
            self.text.ReplaceSelection(line + line)
        else:
            listrem = []
            #            self.onSplit(event)
            seltext1 = seltext.split('\n')
            for item in seltext1:
                if not item.strip():
                    continue
            self.text.BeginUndoAction()
            self.text.ReplaceSelection(seltext + "\n" + seltext)
            self.text.EndUndoAction()
            frm, to = self.text.GetSelection()
        self.onColor1(event)
        self.text.ScrollToLine(self.topline)

    def onRem(self, event):

        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            linenumber = self.text.GetCurrentLine()
            line_text = self.text.GetCurLine()
            pos = self.text.GetCurrentPos()
            beg = pos - int(line_text[1])
            end = pos - int(line_text[1]) + len(line_text[0])
            self.text.SetSelection(beg, end)
            line = "REM " + line_text[0]
            self.text.ReplaceSelection(line)
        else:
            listrem = []
            #            self.onSplit(event)
            seltext1 = seltext.split('\n')
            for item in seltext1:
                if not item.strip():
                    continue

                seltext = seltext.replace(item, "REM " + item)
            self.text.BeginUndoAction()

            self.text.ReplaceSelection(seltext)
            self.text.EndUndoAction()
            frm, to = self.text.GetSelection()
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)

    def onUNRem(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            linenumber = self.text.GetCurrentLine()
            line_text = self.text.GetCurLine()
            if "REM" in line_text[0]:
                pos = self.text.GetCurrentPos()
                beg = pos - int(line_text[1])
                end = pos - int(line_text[1]) + len(line_text[0])
                self.text.SetSelection(beg, end)
                line = line_text[0].replace("REM ", "")
                self.text.BeginUndoAction()
                self.text.ReplaceSelection(line)
                self.text.EndUndoAction()
        else:
            seltext1 = seltext.split("\n")
            for item in seltext1:
                seltext = seltext.replace("REM ", "")
            self.text.BeginUndoAction()
            self.text.ReplaceSelection(seltext)
            self.text.EndUndoAction()
            # self.text.EnsureCaretVisible()
            frm, to = self.text.GetSelection()
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)

    def striplist(self, lines):
        return ([line for line in lines if line.strip()])

    def onParts(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        partA = []
        partB = []
        #        partC=[]
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self,
                                    'No text selected! Please label your carbon atoms with a trailer, for example C1A, C1B, and then select the disordered atoms and repeat this action ',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:

            self.ISOTR(event)
            seltext = self.text.GetSelectedText()
            tx = seltext.split("\n")
            tex = self.striplist(tx)
            # # printtex
            for line in tex:
                l = line.strip()  # len((line.strip())[0])
                if len((l.split())[0]) >= 3:
                    if 'A' in line.upper():
                        partA.append(line)
                    elif 'B' in line.upper():
                        partB.append(line)
            partA = sorted(partA, key=self.onsortkeys)
            partB = sorted(partB, key=self.onsortkeys)
            ready = 'PART  1' + '\n' + '\n'.join(partA) + '\n' + 'PART  2' + '\n' + '\n'.join(partB) + '\n' + 'PART  0'
            self.text.ReplaceSelection(ready)
            self.text.EnsureCaretVisible()
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)

    def onOMIT(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        lst_file = self.get_lst_file(event)
        ltab = self.find_omit(event, lst_file)
        if ltab:
            tores = []
            for x in ltab:
                tores.append("OMIT  " + ' '.join(x.split()[0:3]))
            self.insert_chunk(event, tores)
        else:
            dlg3 = wx.MessageDialog(self, 'Nothing to OMIT', 'info', wx.OK | wx.ICON_INFORMATION)
            dlg3.ShowModal()

    def get_lst_file(self, event):
        if os.path.exists(self.fnoe + ".lst") == True:
            lstread = open(self.fnoe + ".lst", 'r').readlines()
            return lstread
        else:
            dlg3 = wx.MessageDialog(self, 'Lst file does not exist', 'Error', wx.OK | wx.ICON_ERROR)
            dlg3.ShowModal()

    def find_omit(self, event, lst_file):
        list_omit = []
        reg = r"[\-?\d\s]{1,4}[\-?\d\s]{1,4}[\-?\d\s]{1,}(?:\s+-?\d+\.\d+){5}"
        pattern = re.compile(reg)
        for line in lst_file:
            if pattern.match(line):
                l = line.split()
                if float(l[5]) >= 9:
                    list_omit.append(line)
        return list_omit

    def onHTAB(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        ltab = self.listtab(event)
        tores = []
        i = 1
        for x in ltab:
            if len(x) > 7:
                tores.append(
                    "EQIV " + '$' + str(i) + ' ' + ' '.join(x[7:10]) + '\n' + "HTAB " + ((x[0]).split('-'))[0] + ' ' +
                    x[5] + '_$' + str(i))
                i = i + 1
            else:
                tores.append("HTAB " + ((x[0]).split('-'))[0] + ' ' + x[5])

        # # printtores

        text = self.text.GetText()
        tx = text.split("\n")
        for line in tx:
            if line.startswith("UNIT"):
                loc1 = tx.index(line)
            elif line.startswith("HTAB"):
                loc2 = tx.index(line)
                tx.pop(loc2)
        for i in tores:
            tx.insert(loc1 + 1, i)
        ready = '\n'.join(tx)

        # # printself.topline
        self.text.SetText(ready)
        self.onColor1(event)

        self.text.ScrollToLine(self.topline)

    def listtab(self, event):
        #       # # printself.fnoe
        listtab = []
        self.onFinal(event)
        if os.path.exists(self.fnoe + ".lst") == True:
            lstread = open(self.fnoe + ".lst", 'r').readlines()
            for numbers, lines in enumerate(lstread):
                if "Hydrogen bonds" in lines:
                    #                   # # printlines, numbers
                    listtab.append(numbers)
                elif "FMAP and GRID set by" in lines:
                    #                   # # printlines, numbers
                    listtab.append(numbers)
            # # printlen(listtab), listtab
            if len(listtab) == 1:
                dlg3 = wx.MessageDialog(self, 'There are no hydrogen bonds to add',
                                        'Info', wx.OK | wx.ICON_INFORMATION)
                dlg3.ShowModal()
            else:
                # # print"# print gettext              "
                gettex = lstread[int(listtab[0]) + 4:listtab[1]]
                listlines = []
                for line in gettex:
                    if not line.strip():
                        continue
                    listlines.append(line.split())
                htabl = []

                return listlines

    def cifdicttoshelx(self, event):
        filters = 'Cif files (*.cif)|*.cif|All files (*.*)|*.*'
        dialog = wx.FileDialog(self, "Choose a file", self.dirname, wildcard=filters, style=wx.FD_OPEN | wx.FD_MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            selected = dialog.GetPath()
            dirnameall = dialog.GetDirectory()
            from dict_to_shelx import mxtosm
            dict = mxtosm(event, selected)
            dfix, dang = dict.constraints(event)
            text = self.text.GetText()
            gtext = text.split("\n")
            self.topline = self.text.GetFirstVisibleLine()
            self.ongetunit(event, gtext)
            gtext.insert(self.unitposition + 1, '\n'.join(dfix))
            gtext.insert(self.unitposition + 1, '\n'.join(dang))
            ready = '\n'.join(gtext)
            self.text.BeginUndoAction()
            self.text.ClearAll()
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)
        dialog.Destroy()

    def oncollide(self, event):
        dlg = wx.TextEntryDialog(self,
                                 'Please provide shelx collision message', 'Shelx collision message?', '',
                                 style=wx.TE_MULTILINE | wx.OK | wx.CANCEL)
        if dlg.ShowModal() == wx.ID_OK:
            col_text = str(dlg.GetValue().encode("latin1"))
            from colided import collision
            col = collision(col_text)
            out_free = col.parseinput(col_text)
            text = self.text.GetText()
            gtext = text.split("\n")
            self.topline = self.text.GetFirstVisibleLine()
            self.ongetunit(event, gtext)
            gtext.insert(self.unitposition + 1, '\n'.join(out_free))
            ready = '\n'.join(gtext)
            self.text.BeginUndoAction()
            self.text.ClearAll()
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)
        dlg.Destroy()

    def ontBu(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        partA = []
        partB = []
        #        partC=[]
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, '''            No atoms selected! 
            Please rename the disordered atoms 
            with an additional trailer, for example, C1A, C1B.
            Then select all the disordered atoms and apply restraints''',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:

            tx = seltext.split("\n")
            tex = self.striplist(tx)
            # # printtex
            for line in tex:
                l = line.strip()  # len((line.strip())[0])
                if len((l.split())[0]) >= 3:
                    if (l.split()[0]).endswith('A'):
                        # # print"splittt", l.split()[0]
                        partA.append(line.split()[0])
                    elif (l.split()[0]).endswith('B'):
                        partB.append(line.split()[0])

            partA = list(set(partA))
            partB = list(set(partB))
            partA = self.sortkey(partA)
            partB = self.sortkey(partB)
            # partC=sorted(partB, key=self.sortkey)
            # # printpartA, partB #partC
            # # print"need to get a base atom"
            atm = wx.TextEntryDialog(None, "Please provide a quotarnary carbon of the tBu group", "Base atom?", "C1",
                                     style=wx.OK | wx.CANCEL)
            if atm.ShowModal() == wx.ID_OK:
                # # print"You entered: %s" % atm.GetValue()
                base = atm.GetValue()
                # # printbase

                sadi2 = "SADI 0.02 " + partA[0] + ' ' + partA[1] + ' ' + partA[1] + ' ' + partA[2] + ' ' + partA[
                    2] + ' ' + partA[0] + ' ' + partB[0] + ' ' + partB[1] + ' ' + partB[1] + ' ' + partB[2] + ' ' + \
                        partB[2] + ' ' + partB[0]
                sadi4 = "SADI 0.02 " + partA[0] + ' ' + partB[0] + ' ' + partB[0] + ' ' + partA[1] + ' ' + partA[
                    1] + ' ' + partB[1] + ' ' + partB[1] + ' ' + partA[2] + ' ' + partA[2] + ' ' + partB[2] + ' ' + \
                        partB[2] + ' ' + partA[0]
                # F7A F7B F7B F8A F8A F8B F8B F9A F9A F9B F9B F7A

                simu3 = "SIMU 0.008 " + partA[0] + ' ' + partB[0] + ' ' + partA[1] + ' ' + partB[1] + ' ' + partA[
                    2] + ' ' + partB[2] + ' ' + partB[2] + ' ' + partA[0]
                delu3 = "ISOR 0.008 " + partA[0] + ' ' + partB[0] + ' ' + partA[1] + ' ' + partB[1] + ' ' + partA[
                    2] + ' ' + partB[2] + ' ' + partB[2] + ' ' + partA[0]
                rest = sadi2 + '\n' + sadi4 + '\n' + simu3 + '\n' + delu3

                text = self.text.GetText()
                gtext = text.split("\n")
                insertpos = self.text.LineFromPosition(int(self.text.GetSelectionStart()))
                gtext.insert(insertpos, rest)
                ready = '\n'.join(gtext)
                self.text.BeginUndoAction()
                self.text.ClearAll()
                # # printself.topline
                self.text.SetText(ready)
                self.text.EndUndoAction()
                self.onColor1(event)
                self.text.ScrollToLine(self.topline)

                # self.text.EnsureCaretVisible()

    def gen_flat(self, event, rest):
        self.topline = self.text.GetFirstVisibleLine()
        partA = []
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        sfac = self.getsfac(gtext)
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, '''            No atoms selected! 
            Please rename the disordered atoms 
            with an additional trailer, for example, C1A, C1B.
            Then select all disordered atoms and apply restraints''',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:
            tx = seltext.split("\n")
            tex = self.striplist(tx)
            for label in sfac:
                for lines in tex:
                    for num in range(10):
                        if lines.upper().startswith(label.upper() + str(num)):
                            partA.append(''.join(lines.upper().split()[0]))
            partA = list(set(partA))
            partA = self.sortkey(partA)
            flat1 = rest + ' 0.008 ' + ' '.join(partA)
            insertpos = self.text.LineFromPosition(int(self.text.GetSelectionStart()))
            gtext.insert(insertpos, flat1)
            ready = '\n'.join(gtext)
            self.text.BeginUndoAction()
            b, e = self.text.GetSelection()
            lb = self.textsize(gtl)
            self.text.ClearAll()
            # # printself.topline
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)
            le = self.textsize(ready)
            diff = int(lb) - int(le)
            self.text.SetSelection(b - diff, e - diff)
            self.text.ScrollToLine(self.topline)

    def FLAT(self, event):
        self.gen_flat(event, "FLAT")

    def SIMU(self, event):
        self.gen_flat(event, "SIMU")

    def onISOR(self, event):
        self.gen_flat(event, "ISOR")

    def SADIa(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        partA = []
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        sfac = self.getsfac(gtext)
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, '''            No atoms selected! 
            Please rename the disordered atoms 
            with an additional trailer, for example, C1A, C1B.
            Then select all the disordered atoms and apply restraints''',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:
            tx = seltext.split("\n")
            tex = self.striplist(tx)
            for num in range(10):
                for label in sfac:
                    for lines in tex:
                        if lines.upper().startswith(label.upper() + str(num)):
                            partA.append(''.join(lines.upper().split()[0]))
            partA = list(set(partA))
            partA = self.sortkey(partA)
            get_list1 = [0, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12, 11, 13,
                         12, 14, 13, 15, 14, 16, 15, 17, 16, 18]
            flat1 = ''

            if len(partA) > 2:
                for nums in get_list1[0:2 * int(len(partA)) - 4]:
                    flat1 = flat1 + partA[nums] + " "
            else:
                dlg2 = wx.MessageDialog(self, '''Please make sure that you selected more than 2 atoms''',
                                        'Error', wx.OK | wx.ICON_INFORMATION)
                dlg2.ShowModal()
            insertpos = self.text.LineFromPosition(int(self.text.GetSelectionStart()))
            gtext.insert(insertpos, "SADI 0.04 " + flat1)
            ready = '\n'.join(gtext)
            self.text.BeginUndoAction()

            b, e = self.text.GetSelection()
            lb = self.textsize(gtl)
            self.text.ClearAll()
            # # printself.topline
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)
            le = self.textsize(ready)
            diff = int(lb) - int(le)
            self.text.SetSelection(b - diff, e - diff)

    def gen_restraints(self, event, rest):
        self.topline = self.text.GetFirstVisibleLine()
        partA = []
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        sfac = self.getsfac(gtext)

        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, '''            No atoms selected!
                    Please rename the disordered atoms
                    with an additional trailer, for example, C1A, C1B.
                    Then select all the disordered atoms and apply restraints''',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:
            tx = seltext.split("\n")
            tex = self.striplist(tx)
            for num in range(10):
                for label in sfac:
                    for lines in tex:
                        if lines.upper().startswith(label.upper() + str(num)):
                            partA.append(''.join(lines.upper().split()[0]))
            partA = list(set(partA))
            partA = self.sortkey(partA)
            # print partA
            if len(partA) > 1:
                get_list1 = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10,
                             10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18]
                flat1 = ''
                if 18 > len(partA) > 2:
                    for nums in get_list1[0:2 * int(len(partA)) - 2]:
                        flat1 = flat1 + partA[nums] + " "
            else:
                dlg2 = wx.MessageDialog(self,
                                        '''Please make sure that you selected more than 1 and less than 18 atoms for this restraint/contraint''',
                                        'Error', wx.OK | wx.ICON_INFORMATION)
                dlg2.ShowModal()
            insertpos = self.text.LineFromPosition(int(self.text.GetSelectionStart()))
            gtext.insert(insertpos, rest + " 0.02 " + flat1)
            ready = '\n'.join(gtext)
            self.text.BeginUndoAction()
            b, e = self.text.GetSelection()
            lb = self.textsize(gtl)
            self.text.ClearAll()
            # # printself.topline
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)
            self.text.ScrollToLine(self.topline)
            le = self.textsize(ready)
            diff = int(lb) - int(le)
            self.text.SetSelection(b - diff, e - diff)

    def SADIb(self, event):
        self.gen_restraints(event, "SADI")

    def DFIX(self, event):
        self.gen_restraints(event, "DFIX")

    def DELU(self, event):
        self.gen_flat(event, "DELU")

    def EADP(self, event):
        self.gen_flat(event, "EADP")

    def ISOR(self, event):
        self.gen_flat(event, "ISOR")

    def onTHF(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        partA = []
        partB = []
        #        partC=[]
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, '''            No atoms selected! 
            Please rename the disordered atoms 
            with an additional trailer, for example, C1A, C1B.
            Then select all the disordered atoms and apply restraints''',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:

            tx = seltext.split("\n")
            tex = self.striplist(tx)
            # # printtex
            for line in tex:
                l = line.strip()  # len((line.strip())[0])
                if len((l.split())[0]) >= 3:
                    if (l.split()[0]).endswith('A'):
                        # # print"splittt", l.split()[0]
                        partA.append(line.split()[0])
                    elif (l.split()[0]).endswith('B'):
                        partB.append(line.split()[0])
            #                    elif 'C' in line:
            #                        partC.append(line.split()[0])
            # # print"before sorting", partA, partB, #partC
            partA = list(set(partA))
            partB = list(set(partB))
            partA = self.sortkey(partA)
            partB = self.sortkey(partB)
            # partC=sorted(partB, key=self.sortkey)
            # # printpartA, partB #partC
            sadi1 = 'SADI ' + ' '.join(partA[0:4]) + ' ' + ' '.join(partB[0:4])
            sadi2 = 'SADI ' + partA[4] + ' ' + partA[0] + ' ' + partA[4] + ' ' + partA[3] + ' ' + partB[4] + ' ' + \
                    partB[0] + ' ' + partB[4] + ' ' + partB[3]
            sadi3 = 'SADI 0.02 ' + partA[4] + ' ' + partA[1] + ' ' + partA[4] + ' ' + partA[2] + ' ' + partB[4] + ' ' + \
                    partB[1] + ' ' + partB[4] + ' ' + partB[2]
            sadi4 = 'SADI 0.02 ' + partA[0] + ' ' + partA[2] + ' ' + partA[1] + ' ' + partA[3] + ' ' + partB[0] + ' ' + \
                    partB[2] + ' ' + partB[1] + ' ' + partB[3]
            sadi5 = 'SADI 0.02 ' + partA[0] + ' ' + partA[3] + ' ' + partB[0] + ' ' + partB[3]
            simu1 = "SIMU 0.008 " + ' '.join(partA[0:4])
            simu2 = "SIMU 0.008 " + ' '.join(partB[0:4])
            delu1 = "DELU 0.008 " + ' '.join(partA[0:4])
            delu2 = "DELU 0.008 " + ' '.join(partB[0:4])
            rest = sadi1 + '\n' + sadi2 + '\n' + sadi3 + '\n' + sadi4 + '\n' + sadi5 + '\n' + simu1 + '\n' + simu2 + '\n' + delu1 + '\n' + delu2
            #            else:
            #                ready = 'PART  1'+'\n'+'\n'.join(partA)+'\n'+'PART  2'+'\n'+'\n'.join(partB)+'\n'+'PART  0'
            #           # # print
            text = self.text.GetText()
            gtext = text.split("\n")
            insertpos = self.text.LineFromPosition(int(self.text.GetSelectionStart()))
            gtext.insert(insertpos, rest)
            ready = '\n'.join(gtext)
            self.text.BeginUndoAction()

            self.text.ClearAll()
            # # printself.topline
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)

            self.text.ScrollToLine(self.topline)

    def onTHF2(self, event):
        partA = []
        partB = []
        #        partC=[]
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, '''            No atoms selected! 
            Please rename the disordered atoms 
            with an additional trailer, for example, C1A, C1B.
            Then select all the disordered atoms and apply restraints''',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:
            atm = wx.TextEntryDialog(None, "Please provide the label for non disordered atom", "Base atom?", "O1",
                                     style=wx.OK | wx.CANCEL)
            if atm.ShowModal() == wx.ID_OK:
                # # print"You entered: %s" % atm.GetValue()
                base = atm.GetValue()
                # # printbase
                tx = seltext.split("\n")
                tex = self.striplist(tx)
                # # printtex
                for line in tex:
                    l = line.strip()  # len((line.strip())[0])
                    if len((l.split())[0]) >= 3:
                        if (l.split()[0]).endswith('A'):
                            # # print"splittt", l.split()[0]
                            partA.append(line.split()[0])
                        elif (l.split()[0]).endswith('B'):
                            partB.append(line.split()[0])
                #                    elif 'C' in line:
                #                        partC.append(line.split()[0])
                # # print"before sorting", partA, partB, #partC
                partA = list(set(partA))
                partB = list(set(partB))
                partA = self.sortkey(partA)
                partB = self.sortkey(partB)
                # partC=sortedhttps://mail.google.com/mail/u/0/#inbox(partB, key=self.sortkey)
                # # printpartA, partB #partC
                #                sadi1='SADI ' + ' '.join(partA[0:4])+' '+' '.join(partB[0:4])
                sadi2 = 'SADI ' + base + ' ' + partA[0] + ' ' + base + ' ' + partA[3] + ' ' + base + ' ' + partB[
                    0] + ' ' + base + ' ' + partB[3]
                sadi3 = 'SADI ' + base + ' ' + partA[1] + ' ' + base + ' ' + partA[3] + ' ' + base + ' ' + partB[
                    1] + ' ' + base + ' ' + partB[3]
                sadi4 = 'SADI 0.02 ' + partA[0] + ' ' + partA[2] + ' ' + partA[1] + ' ' + partA[3] + ' ' + partB[
                    0] + ' ' + partB[2] + ' ' + partB[1] + ' ' + partB[3]
                sadi5 = 'SADI 0.02 ' + partA[0] + ' ' + partA[3] + ' ' + partB[0] + ' ' + partB[3]
                simu1 = "SIMU 0.008 " + ' ' + base + ' ' + ' '.join(partA[0:4])
                simu2 = "SIMU 0.008 " + ' ' + base + ' ' + ' '.join(partB[0:4])
                delu1 = "DELU " + ' ' + base + ' ' + ' '.join(partA[0:4])
                delu2 = "DELU " + ' ' + base + ' ' + ' '.join(partB[0:4])
                rest = sadi2 + '\n' + sadi3 + '\n' + sadi4 + '\n' + sadi5 + '\n' + simu1 + '\n' + simu2 + '\n' + delu1 + '\n' + delu2
                #            else:
                #                ready = 'PART  1'+'\n'+'\n'.join(partA)+'\n'+'PART  2'+'\n'+'\n'.join(partB)+'\n'+'PART  0'
                #           # # print
                text = self.text.GetText()
                gtext = text.split("\n")
                insertpos = self.text.LineFromPosition(int(self.text.GetSelectionStart()))
                gtext.insert(insertpos, rest)
                ready = '\n'.join(gtext)
                self.text.BeginUndoAction()

                self.text.ClearAll()
                # # printself.topline
                self.text.SetText(ready)
                self.text.EndUndoAction()
                self.onColor1(event)

                self.text.ScrollToLine(self.topline)

    def onPhenylb(self, event):
        partA = []
        partB = []
        self.topline = self.text.GetFirstVisibleLine()
        #        partC=[]
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, '''            No atoms selected! 
            Please rename the disordered atoms 
            with an additional trailer, for example, C1A, C1B.
            Then select all the disordered atoms and apply restraints''',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:
            atm = wx.TextEntryDialog(None, "Please provide the label for non disordered atom", "Base atom?", "C1",
                                     style=wx.OK | wx.CANCEL)
            if atm.ShowModal() == wx.ID_OK:
                base = atm.GetValue()
            tx = seltext.split("\n")
            tex = self.striplist(tx)
            for line in tex:
                l = line.strip()  # len((line.strip())[0])
                if len((l.split())[0]) >= 3:
                    if (l.split()[0]).endswith('A'):
                        partA.append(line.split()[0])
                    elif (l.split()[0]).endswith('B'):
                        partB.append(line.split()[0])

            partA = list(set(partA))
            partB = list(set(partB))
            partA = self.sortkey(partA)
            partB = self.sortkey(partB)
            sadi2 = 'SADI ' + base + ' ' + partA[0] + ' ' + partA[0] + ' ' + partA[1] + ' ' + partA[1] + ' ' + partA[
                2] + ' ' + partA[2] + ' ' + partA[3] + ' ' + partA[3] + ' ' + partA[4] + ' ' + partA[
                        4] + ' ' + ' ' + base
            sadi3 = 'SADI ' + base + ' ' + partB[0] + ' ' + partB[0] + ' ' + partB[1] + ' ' + partB[1] + ' ' + partB[
                2] + ' ' + partB[2] + ' ' + partB[3] + ' ' + partB[3] + ' ' + partB[4] + ' ' + partB[
                        4] + ' ' + ' ' + base
            sadi4 = 'SADI 0.02 ' + base + ' ' + partA[1] + ' ' + partA[1] + ' ' + partA[3] + ' ' + partA[
                3] + ' ' + base + ' ' + base + ' ' + partB[1] + ' ' + partB[1] + ' ' + partB[3] + ' ' + partB[
                        3] + ' ' + base
            simu3 = "SIMU 0.008 " + base + ' ' + partB[0] + " " + base + ' ' + partA[0] + " " + partB[0] + ' ' + partA[
                0] + ' ' + partB[1] + ' ' + partA[1] + ' ' + partB[2] + ' ' + partA[2] + ' ' + partB[3] + ' ' + partA[
                        3] + ' ' + partB[4] + ' ' + partA[4]
            delu1 = "DELU 0.008 " + base + ' ' + ' '.join(partA[0:5])
            delu2 = "DELU 0.008 " + base + ' ' + ' '.join(partB[0:5])
            flat1 = 'FLAT 0.01 ' + base + ' ' + ' '.join(partA[0:5])
            flat2 = 'FLAT 0.01 ' + base + ' ' + ' '.join(partB[0:5])
            rest = sadi2 + '\n' + sadi3 + '\n' + sadi4 + '\n' + simu3 + '\n' + delu1 + '\n' + delu2 + '\n' + flat1 + '\n' + flat2
            #            else:
            #                ready = 'PART  1'+'\n'+'\n'.join(partA)+'\n'+'PART  2'+'\n'+'\n'.join(partB)+'\n'+'PART  0'
            #           # # print
            text = self.text.GetText()
            gtext = text.split("\n")
            insertpos = self.text.LineFromPosition(int(self.text.GetSelectionStart()))
            gtext.insert(insertpos, rest)
            ready = '\n'.join(gtext)

            self.text.BeginUndoAction()
            self.text.ClearAll()
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)

            self.text.ScrollToLine(self.topline)

    def onPhenyl(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        partA = []
        partB = []
        #        partC=[]
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            dlg2 = wx.MessageDialog(self, '''            No atoms selected! 
            Please rename the disordered atoms 
            with an additional trailer, for example, C1A, C1B.
            Then select all the disordered atoms and apply restraints''',
                                    'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
        else:

            tx = seltext.split("\n")
            tex = self.striplist(tx)
            for line in tex:
                l = line.strip()  # len((line.strip())[0])
                if len((l.split())[0]) >= 3:
                    if (l.split()[0]).endswith('A'):
                        partA.append(line.split()[0])
                    elif (l.split()[0]).endswith('B'):
                        partB.append(line.split()[0])
            partA = list(set(partA))
            partB = list(set(partB))
            partA = self.sortkey(partA)
            partB = self.sortkey(partB)
            sadi2 = 'SADI ' + partA[0] + ' ' + partA[1] + ' ' + partA[1] + ' ' + partA[2] + ' ' + partA[2] + ' ' + \
                    partA[3] + ' ' + partA[3] + ' ' + partA[4] + ' ' + partA[4] + ' ' + partA[5] + ' ' + partA[
                        5] + ' ' + partA[0]
            sadi3 = 'SADI ' + partB[0] + ' ' + partB[1] + ' ' + partB[1] + ' ' + partB[2] + ' ' + partB[2] + ' ' + \
                    partB[3] + ' ' + partB[3] + ' ' + partB[4] + ' ' + partB[4] + ' ' + partB[5] + ' ' + partB[
                        5] + ' ' + partB[0]
            sadi4 = 'SADI 0.02 ' + partA[0] + ' ' + partA[2] + ' ' + partA[2] + ' ' + partA[4] + ' ' + partB[0] + ' ' + \
                    partB[2] + ' ' + partB[2] + ' ' + partB[4]
            sadi5 = 'SADI 0.02 ' + partA[0] + ' ' + partA[2] + ' ' + partA[1] + ' ' + partA[3] + ' ' + partB[0] + ' ' + \
                    partB[2] + ' ' + partB[1] + ' ' + partB[3]
            simu1 = "SIMU 0.008 " + ' '.join(partA[0:6])
            simu2 = "SIMU 0.008 " + ' '.join(partB[0:6])
            simu3 = "SIMU 0.008 " + partB[0] + ' ' + partA[0] + ' ' + partB[1] + ' ' + partA[1] + ' ' + partB[2] + ' ' + \
                    partA[2] + ' ' + partB[3] + ' ' + partA[3] + ' ' + partB[4] + ' ' + partA[4] + ' ' + partB[
                        5] + ' ' + partA[5]
            delu1 = "DELU 0.008 " + ' '.join(partA[0:6])
            delu2 = "DELU 0.008 " + ' '.join(partB[0:6])
            flat1 = 'FLAT 0.01 ' + ' '.join(partA[0:6])
            flat2 = 'FLAT 0.01 ' + ' '.join(partB[0:6])
            rest = sadi2 + '\n' + sadi3 + '\n' + sadi4 + '\n' + sadi5 + '\n' + simu1 + '\n' + simu2 + '\n' + simu3 + '\n' + delu1 + '\n' + delu2 + '\n' + flat1 + '\n' + flat2
            text = self.text.GetText()
            gtext = text.split("\n")
            insertpos = self.text.LineFromPosition(int(self.text.GetSelectionStart()))
            gtext.insert(insertpos, rest)
            ready = '\n'.join(gtext)
            self.text.BeginUndoAction()

            self.text.ClearAll()
            self.text.SetText(ready)
            self.text.EndUndoAction()
            self.onColor1(event)

            self.text.ScrollToLine(self.topline)

    def onDFIXASIS(self, event):
        cell = self.onGetCell(event)
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        sfac = self.getsfac(gtext)
        from auto_dfix import calcrest
        seltext = self.text.GetSelectedText()
        seltext = seltext.split("\n")
        cell = self.onGetCell(event)
        if len(seltext) > 1:
            dfix = calcrest(event, seltext, cell, sfac)
            #           print (dfix.calcbonds(event))
            self.dataObj = wx.TextDataObject()
            self.dataObj.SetText(dfix.calcbonds(event))
            if wx.TheClipboard.Open():
                wx.TheClipboard.SetData(self.dataObj)
                wx.TheClipboard.Close()
                dlg = wx.MessageDialog(self, 'The following data was copied to clipboard: \n' + dfix.calcbonds(event),
                                       'Data was copied to clipboard', wx.OK | wx.ICON_INFORMATION)
                dlg.ShowModal()
                dlg.Destroy()
        else:
            dlg2 = wx.MessageDialog(self, 'No atoms selected!', 'Error', wx.OK | wx.ICON_INFORMATION)
            dlg2.ShowModal()
            dlg2.Destroy()

    def getenergy(self, event):
        self.onGetCell(event)
        plank = 6.626e-34
        speedlight = 299792458
        hztokev = 6.241509e18
        energy = plank * speedlight * hztokev / (float(self.wavelength) * 1e-10 * 1000)
        return round(energy, 6)

    def dispcalc(self, event):
        from disp import GetXsectionCoeff
        from disp import FPcalc
        gtext = self.text.GetText().split("\n")
        sfac = self.getsfac(gtext)
        energy = self.getenergy(event)
        displist = []
        for element in sfac:
            orb = GetXsectionCoeff(element)
            fp, fpp, mu = FPcalc(orb, float(energy))
            displist.append(" ".join(["DISP", str(element), str(fp), str(fpp), str(mu)]))
        return displist, gtext

    def onDISP(self, event):
        displist, gtext = self.dispcalc(event)
        self.ongetunit(event, gtext)
        gtext.insert(self.unitposition, '\n'.join(displist))
        ready = '\n'.join(gtext)
        self.text.BeginUndoAction()
        self.text.SetText(ready)
        self.text.EndUndoAction()
        self.onColor1(event)
        self.text.ScrollToLine(0)

    def onhkllat(self, event):
        import hkllatmain
        #        from hkllatmain import hkllat
        hkllat = hkllatmain.create(None, "HKLLAT")
        if os.path.exists(self.fnoe + ".hkl"):
            lo = hkllat.load(event, self.fnoe + ".hkl")
        elif os.path.exists(self.fnoe + ".sca"):
            lo = hkllat.load(event, self.fnoe + ".sca")
        elif os.path.exists(self.fnoe + ".p4p"):
            lo = hkllat.load(event, self.fnoe + ".p4p")
        hkllat.Show()

    def onBonAng(self, event):
        from bonds import Bang
        bangshow = Bang(self.path, self.dirname, self.fnoe, self.filenamenoext)
        igot = bangshow.ShowModal()
        bangshow.Destroy()

    def onsfconvert(self, event):
        print('''set CCP4 environment variables in /etc/environment file, run: source ccp4.setup-sh''')
        from convert import convertsf
        sf = convertsf(self.dirname, self.phtosfconvert)
        igot = sf.ShowModal()
        sf.Destroy()

    def onpovray(self, event):
        from povray import povrayclass
        pov = povrayclass(self.path, self.dirname, self.fnoe, self.filenamenoext, self.phtopovray)
        igot = pov.ShowModal()
        pov.Destroy()

    def onSimpleSadabs(self, event):
        from sadabs import SimpleSadabs
        sad = SimpleSadabs(None, -1, self.path, self.dirname, self.fnoe, self.filenamenoext, self.phtosadabs)
        sad.Show()

    def checkifatom(self, event, text):
        text = text.split("\n")
        #        pattern = re.compile(r'^([A-Za-z0-9]{1,4}\s+\d{1,3}(?:\s+-?\d+\.\d+){5})', re.MULTILINE)
        atoms = []
        other = []
        pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
        patternanis = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5}\s=)')
        for num, line in enumerate(text):
            if pattern.match(line):
                if '=' in line:
                    atoms.append(text[num] + "\n" + text[num + 1])
                else:
                    atoms.append(line)
            else:
                if not line.startswith("   "):
                    other.append(line)
        return atoms, other

    def onsortkeys(self, string):
        return tuple(int(num) if num else alpha for num, alpha in (re.compile(r'(\d+)|(\D+)').findall)(string))

    def sortkey(self, l):
        convert = lambda text: int(text) if text.isdigit() else text.lower()
        alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
        return sorted(l, key=alphanum_key)

    def sortbylabel(self, atomgrid):
        return sorted(atomgrid, key=lambda x: x.split()[0][-1])

    def onSort(self, event):
        self.topline = self.text.GetFirstVisibleLine()
        seltext = self.text.GetSelectedText()
        if len(seltext) == 0:
            self.topline = self.text.GetFirstVisibleLine()
            from sort import onSortc
            sortshow = onSortc(self.path, self.dirname, self.fnoe, self.filenamenoext, self.text)
            igot = sortshow.ShowModal()
            self.onColor1(event)
            sortshow.Destroy()
        else:
            lb = self.textsize(seltext)
            atomgrid, othergrid = self.checkifatom(event, seltext)
            atom = []
            atomgrid = sorted(atomgrid, key=self.onsortkeys)
            # atomgrid=self.sortbylabel(atomgrid)
            others = "\n".join(othergrid)
            result = others + "\n".join(atomgrid)
            b, e = self.text.GetSelection()
            self.text.BeginUndoAction()
            self.text.ReplaceSelection(result)
            self.text.EndUndoAction()
            self.onColor1(event)
            le = self.textsize(result)
            diff = int(lb) - int(le)
            self.text.ScrollToLine(self.topline)
            self.text.SetSelection(b, e - diff)

    # def onSaint(self, event):
    #     from mainsaint import MainSaint
    #     saint = MainSaint(self.path, self.dirname, self.fnoe, self.filenamenoext, self.phtosaint)
    #     saint.ShowModal()
    #     saint.Destroy()

    def onmxmap(self, event):
        from mxmap import mxmain
        mx = mxmain(None, -1, self.path, self.dirname, self.phtocoot, self.phtoxc, self.phtoxm, self.phtoxe)
        mx.Show()

    def onterminal(self, event, shell, cond):
        from terminal import terminal
        ter = terminal(event, shell, cond)
        ter.ShowModal()
        ter.Destroy()

    def onSolvD(self, event):  # wxGlade: MyFrame.<event_handler>
        try:

            if self.ossystem.startswith("win"):
                webbrowser.open('http://shelx.uni-ac.gwdg.de/SHELX/pm_disorder.pdf')
            elif self.ossystem.startswith('darwin'):
                subprocess.Popen(['open', 'http://shelx.uni-ac.gwdg.de/SHELX/pm_disorder.pdf'])
            else:
                webbrowser.open('http://shelx.uni-ac.gwdg.de/SHELX/pm_disorder.pdf')
        except OSError:
            pass

    def onAbout(self, event):
        info = wx.adv.AboutDialogInfo()
        info.Name = "LinXTL"
        info.Version = self.version
        info.Copyright = "Copyright (C) 2009-2019 Denis Spasyuk, Canadian Light Source"
        info.Description = '''LinXTL is a crystallographic toolbox for structural refinement.'''
        info.WebSite = ("http://sourceforge.net/projects/linxtl/")  # , "Home page")
        wx.adv.AboutBox(info)

    def aforcalc(self, event, mask):
        try:
            atoms = wx.TextEntryDialog(None, "         Define atoms for calculations          ", "Atoms?", mask,
                                       style=wx.OK | wx.CANCEL)
            if atoms.ShowModal() == wx.ID_OK:
                ats = atoms.GetValue()
            atoms.Destroy()
            return ats
        except UnboundLocalError:
            pass

    def getlines(self, event, mask):
        coordinates = []
        atom = self.aforcalc(event, mask)
        atoms = atom.split()
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        for a in atoms:
            for lines in gtext:
                if len(lines) >= 20:
                    if lines.upper().startswith(a.upper() + " "):
                        coordinates.append(" ".join(lines.split()[2:5]))
        return coordinates, atom

    def getspecs(self, event, mask):
        coordinates = []
        atoms = mask.split()
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        for a in atoms:
            for lines in gtext:
                if len(lines) >= 20:
                    if lines.upper().startswith(a.upper() + " "):
                        coordinates.append(" ".join(lines.split()[0:5]))
        return coordinates

    def ongetunit(self, event, tx):
        for num, line in enumerate(tx):
            if line.startswith("UNIT"):
                self.unitposition = num
                unl = len(line.replace("UNIT", "").split())
                return unl, line.replace("UNIT", "").split()

    def distanceortho(self, event, atoma, atomb):
        import math
        x1 = atoma[0]
        x2 = atomb[0]
        y1 = atoma[1]
        y2 = atomb[1]
        z1 = atoma[2]
        z2 = atomb[2]
        distance = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) + (z2 - z1) * (z2 - z1))
        print("slippage:  ", x2 - x1, y2 - y1)
        print("Distance from centroid of the plane A to the centroid of plane B:", distance)
        return distance

    def calcplane(self, event, one, two, At, Bt):
        acentr = self.calccentroids(event, one, At)
        bcentr = self.calccentroids(event, two, Bt)
        distance = self.distanceortho(event, acentr, bcentr)
        import math
        # ABv=x2-x1, y2-y1, z2-z1 ACv=x3-x1, y3-y1, z3-z1; cross cx=Ay*Bz-Az-By cy=Az*Bx-Ax*Bz cz=Ax*By-AyBx
        A = one[0]
        B = one[2]
        C = one[4]
        ABv = [float(B[2]) - float(A[2]), float(B[3]) - float(A[3]), float(B[4]) - float(A[4])]
        ACv = [float(C[2]) - float(A[2]), float(C[3]) - float(A[3]), float(C[4]) - float(A[4])]
        i = ABv
        j = ACv
        cx = i[1] * j[2] - i[2] * j[1]
        cy = i[2] * j[0] - i[0] * j[2]
        cz = i[0] * j[1] - i[1] * j[0]
        plane = [cx, cy, cz]
        Dp = cx * (-1 * float(A[2])) + cy * (-1 * float(A[3])) + cz * (-1 * float(A[4]))
        top = abs(plane[0] * bcentr[0] + plane[1] * bcentr[1] + plane[2] * bcentr[2] + Dp)
        bottom = math.sqrt(plane[0] * plane[0] + plane[1] * plane[1] + plane[2] * plane[2])  #
        dis = top / bottom
        xy = math.sqrt(distance * distance - dis * dis)
        ttop = -float(plane[0]) * float(bcentr[0]) - float(plane[1]) * float(bcentr[1]) - float(plane[2]) * float(
            bcentr[2]) - Dp
        tbottom = float(plane[0]) * float(plane[0]) + float(plane[1]) * float(plane[1]) + float(plane[2]) * float(
            plane[2])
        t = abs(ttop / tbottom)
        xp = plane[0] * t + bcentr[0]
        yp = plane[1] * t + bcentr[1]
        zp = plane[2] * t + bcentr[2]
        projbcentr = [round(xp, 5), round(yp, 5), round(zp, 5)]
        xslip = ["X slippage: ", round(abs(float(projbcentr[0]) - float(acentr[0])), 4)]
        yslip = ["Y slippage: ", round(abs(float(projbcentr[1]) - float(acentr[1])), 4)]
        zslip = ["Z slippage: ", round(abs(float(projbcentr[2]) - float(acentr[2])), 4)]
        # projection
        #        print("plane",plane, Dp)
        #        print("Vectors: ",ABv, ACv)
        #        print("Cross Product of two vectors", cx, cy, cz)
        #        print("centroids: ",acentr, bcentr)
        #        print("Projection of B centroid: ", projbcentr)
        #        print("Normal distance from point to plane=", dis)
        #        print("XY slippage: ", xy, zslip)
        #        print("t=", t)
        pout = ["Plane A: ", str(round(plane[0], 5)) + "&#215;X " + str(round(plane[1], 5)) + "&#215;Y " + str(
            round(plane[2], 5)) + "&#215;Z " + "=" + str(round(Dp, 2))]
        xyout = ["XY slippage: ", round(xy, 5)]
        proj = ["Projection of centroid B into plane A: ", projbcentr]
        outlist = []
        outlist.append(["Centroid A: ", acentr])
        outlist.append(["Centroid B: ", bcentr])
        outlist.append(["Distance between centroids A-B:  ", str(round(distance, 5))])
        outlist.append(["Normal of centroid B to plane A:", round(dis, 5)])
        outlist.append(pout)
        outlist.append(xslip)
        outlist.append(yslip)
        outlist.append(xyout)
        outlist.append(proj)

        self.listhtml(event, outlist)

    def results(self, event, symone, symtwo, A, B):  # returns orthocoordinates
        from calcslip import slippage
        coordA = self.getspecs(event, A)
        coordB = self.getspecs(event, B)
        slipr = slippage(self.text, self.onGetCell(event), self.dirname)
        one = slipr.calcortho(event, self.onGetCell(event), coordA, symone)
        two = slipr.calcortho(event, self.onGetCell(event), coordB, symtwo)
        self.calcplane(event, one, two, A, B)
        slipr.Destroy()

    def calccentroids(self, event, one, A):
        lcoord = []
        for l in one:
            l = l[2:5]
            lcoord.append(l)
        fl = (len(lcoord))
        lcoord = [[float(j) for j in i] for i in lcoord]  # convert to a list of listed floats
        sumxyz = ([sum(i) for i in zip(*lcoord)])
        frx = round(sumxyz[0] / fl, 6)
        fry = round(sumxyz[1] / fl, 6)
        frz = round(sumxyz[2] / fl, 6)
        return [frx, fry, frz]

    def calctmp(self, event, symone, symtwo, A, B):
        result = [symone, symtwo, A, B]
        fcalc = open(os.path.join(self.dirname, "linxtl_calc.tmp"), 'w')
        fcalc.writelines(["%s\n" % item for item in result])
        fcalc.close()

    def calcslip(self, event):
        from calcslip import slippage
        slip = slippage(self.text, self.onGetCell(event), self.dirname)
        result = slip.ShowModal()
        if result == wx.ID_OK:
            X = slip.text_ctrl_X.GetValue()
            Y = slip.text_ctrl_Y.GetValue()
            Z = slip.text_ctrl_Z.GetValue()
            XA = slip.text_ctrl_XA.GetValue()
            YA = slip.text_ctrl_YA.GetValue()
            ZA = slip.text_ctrl_ZA.GetValue()
            A = slip.text_ctrl_A.GetValue()
            B = slip.text_ctrl_B.GetValue()
            symone = [X, Y, Z]
            symtwo = [XA, YA, ZA]
            self.results(event, symone, symtwo, A, B)
            self.calctmp(event, ",".join(symone), ",".join(symtwo), A, B)
        slip.Destroy()

    def getallatoms(self, event, sym, symsi):
        print(sym)
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        allatoms = []
        sfac = self.getsfac(gtext)
        for a in sfac:
            for lines in gtext:
                for n in range(10):
                    if len(lines) >= 20:
                        if lines.upper().startswith(a.upper() + str(n)):
                            # allatoms.append(" ".join([lines.split()[0]+str(symsi)]+[lines.split()[1]]+[float(lines.split()[2])+float(sym[0])]+[float(lines.split()[3])+float(sym[1])]+[float(lines.split()[4])+float(sym[2])]))
                            allatoms.append(lines.split()[0] + str(symsi) + " " + str(lines.split()[1]) + " " + str(
                                float(lines.split()[2]) + float(sym[0])) + " " + str(
                                float(lines.split()[3]) + float(sym[1])) + " " + str(
                                float(lines.split()[4]) + float(sym[2])))
        return allatoms

    def output_writer(self, event, out):
        fileout = open(self.fnoe + "_linxtl_log.html", 'a')
        fileout.write(out)
        fileout.close()

    def listhtml(self, event, table):
        import HTML
        orthoc = HTML.table(table)
        from webify import webb
        title = "This table was saved as " + self.fnoe + "_log.html"
        w = webb(event, '<center>' + orthoc + '</center>', title)
        w.ShowModal()
        w.Destroy()
        start = '<center>' + "&nbsp" * 50
        end = "&nbsp" * 50 + '</center>'
        self.output_writer(event, start + orthoc + end)

    def tablelist(self, event, table, header):
        import HTML
        table.insert(0, header)
        orthoc = HTML.table(table)
        from webify import webb
        title = "This table was saved as " + self.fnoe + "_log.html"
        w = webb(event, '<center>' + orthoc + '</center>', title)
        w.ShowModal()
        w.Destroy()
        self.output_writer(event, '<center>' + orthoc + '</center>')

    def nicecols(self, event, table):
        import HTML
        table.insert(0, ["Atom", "SFAC N", "a (orth)", "b (ortho)", "c (ortho)"])
        orthoc = HTML.table(table)
        from webify import webb
        title = "This table was saved as " + self.fnoe + "_log.html"
        w = webb(event, '<center>' + orthoc + '</center>', title)
        w.ShowModal()
        w.Destroy()
        self.output_writer(event, '<center>' + orthoc + '</center>')

    def calcorttho(self, event):
        sym = [0, 0, 0]
        symsi = ''
        atoms = self.getallatoms(event, sym, symsi)
        from calcslip import slippage
        centr = slippage(self.text, self.onGetCell(event), self.dirname)
        cb = centr.calcortho(event, self.onGetCell(event), atoms, ["0 +x", "0 +y", "0 +z"])
        centr.Destroy()
        self.nicecols(event, cb)

    def calccentr(self, event):
        from calcslip import slippage
        mask = "C1 C2 C3 C4 C5 C6"
        atoms, ats = self.getlines(event, mask)
        atoms = "\n".join(atoms)
        centr = slippage(self.text, self.onGetCell(event), self.dirname)
        c = centr.centroid(event, atoms, self.onGetCell(event))
        centr.Destroy()
        gtl = self.text.GetText()
        gtext = gtl.split("\n")
        length, unit = self.ongetunit(event, gtext)
        sfac = "SFAC Cg 0 0 0 0 0 0 0 0 0 0 0 0 0 0.1"
        cg = "Cg1   " + str(int(length) + 1) + "   " + str(c[0]) + "   " + str(c[1]) + "   " + str(
            c[2]) + "     10.00000    0.00100"
        self.dataObj = wx.TextDataObject()
        self.dataObj.SetText(sfac + "\n" + "UNIT " + " ".join(unit) + " 1" + "\n" + cg)
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.dataObj)
            wx.TheClipboard.Close()
            dlg = wx.MessageDialog(self,
                                   'The following data was copied to clipboard:  ' + "\n" + sfac + "\n" + "UNIT " + " ".join(
                                       unit) + " 1" + "\n" + cg,
                                   'Data was copied to clipboard', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()

    ##################################Colours############################################################
    def onCifColor(self, event):
        Colorify = colorify(event, self.text3, self.fnamefull, self.filename, self.ossystem, self.fsg, self.main_font)
        Colorify.oncolorcif(event, self.text3)

    def onPCifColor(self, event):
        Colorify = colorify(event, self.text4, self.fnamefull, self.filename, self.ossystem, self.fsg, self.main_font)
        Colorify.oncolorcif(event, self.text4)

    def onColor1(self, event):
        Colorify = colorify(event, self.text, self.fnamefull, self.filename, self.ossystem, self.fsg, self.main_font)
        size = self.toobig(event, self.fnamefull)
        self.text.ClearDocumentStyle()
        if self.fnamefull.endswith('.res'):
            if not size >= 1000000:
                Colorify.onColorprime(event)
        elif self.fnamefull.endswith('.ins'):
            if not size >= 1000000:
                Colorify.onColorprime(event)
        else:
            if not size >= 100000:
                Colorify.onColorprime(event)

    ##################################Colours############################################################

    def Batch(self, event):
        proc = ['Table of refinement parameters', 'HTML report', 'Bonds and Angles']
        dlg = wx.SingleChoiceDialog(self, 'Select a batch process', 'Choose a batch process.', proc, wx.CHOICEDLG_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.SetStatusText('You chose: %s\n' % dlg.GetStringSelection())
            if dlg.GetSelection() == 0:
                # print dlg.GetSelection()
                dlg.Destroy()
                listnumber = []
                list = []

                filters = 'Cif files (*.cif)|*.cif|All files (*.*)|*.*'
                dialog = wx.FileDialog(self, "Choose a file", self.dirname, wildcard=filters,
                                       style=wx.FD_OPEN | wx.FD_MULTIPLE)
                if dialog.ShowModal() == wx.ID_OK:
                    selected = dialog.GetPaths()
                    dirnameall = dialog.GetDirectory()
                    # print selected, dirnameall

                    for fileitem in selected:
                        self.filename = os.path.split(fileitem)[1]
                        self.filenamenoext = os.path.splitext(self.filename)[0]
                        self.SetStatusText(self.filenamenoext)
                        self.fnoe = os.path.splitext(fileitem)[0]
                        self.onHtmlTable(event)
            elif dlg.GetSelection() == 1:
                # print dlg.GetSelection()
                dlg.Destroy()
                listnumber = []
                list = []
                filters = 'Cif files (*.cif)|*.cif|All files (*.*)|*.*'
                dialog = wx.FileDialog(self, "Choose a file", self.dirname, wildcard=filters,
                                       style=wx.FD_OPEN | wx.FD_MULTIPLE)
                if dialog.ShowModal() == wx.ID_OK:
                    selected = dialog.GetPaths()
                    dirnameall = dialog.GetDirectory()
                    # print selected, dirnameall
                    for fileitem in selected:
                        self.dirname = dirnameall
                        self.filename = os.path.split(fileitem)[1]
                        self.filenamenoext = os.path.splitext(self.filename)[0]
                        self.SetStatusText(self.filenamenoext)
                        self.fnoe = os.path.splitext(fileitem)[0]
                        self.Appendix(event)
            elif dlg.GetSelection() == 2:
                # print dlg.GetSelection()
                dlg.Destroy()
                listnumber = []
                list = []
                filters = 'Cif files (*.cif)|*.cif|All files (*.*)|*.*'
                dialog = wx.FileDialog(self, "Choose a file", self.dirname, wildcard=filters,
                                       style=wx.FD_OPEN | wx.FD_MULTIPLE)
                if dialog.ShowModal() == wx.ID_OK:
                    selected = dialog.GetPaths()
                    dirnameall = dialog.GetDirectory()
                    # print selected
                    for fileitem in selected:
                        # print fileitem
                        self.dirname = dirnameall
                        self.filename = os.path.split(fileitem)[1]
                        self.filenamenoext = os.path.splitext(self.filename)[0]
                        self.SetStatusText(self.filenamenoext)
                        self.fnoe = os.path.splitext(fileitem)[0]
                        self.onBonAng(event)


class MyApp(wx.App):
    def OnInit(self):
        displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        sizes = [display.GetGeometry().GetSize() for display in displays]
        displaySize = sizes[0].Get()
        frame_1 = MyFrame(None, -1, "", size=(displaySize[0] / 1.2, displaySize[1] / 1.2))
        self.SetTopWindow(frame_1)
        frame_1.Show(True)
        return 1
