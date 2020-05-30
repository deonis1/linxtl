#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import os
import wx
import wx.stc
import re


class colorify():
    def __init__(self, event, text, fnamefull, filename, ossystem, fsg, main_font):
        self.text = text
        self.fnamefull = fnamefull
        self.filename = filename
        self.ossystem = ossystem
        self.fsg = fsg
        self.main_font = main_font

    def onColorprime(self, event):
        if self.fnamefull.lower().endswith(".res") or self.fnamefull.lower().endswith(".ins"):
            self.Colbadoc(event)
            self.colmain(event)
            self.markpartsresi(event)
        elif self.filename.lower().endswith(".cif"):
            self.oncolorcif(event, self.text)

    def finditem(self, event, searchstring, mode, start, end, length):
        while True:
            start = int(self.text.FindText(start, end, searchstring))
            if start == -1:
                break
            self.text.StartStyling(start, wx.stc.STC_INDICS_MASK)
            self.text.SetStyling(length, wx.stc.STC_INDIC2_MASK)
            start += length

    def colmain(self, event):
        self.text.Colourise(0, -1)
        mode = wx.stc.STC_FIND_MATCHCASE
        start = 0
        end = self.text.GetTextLength()
        for searchstring in ["11.000000", "21.000000", "31.000000", "10.500000"]:
            length = len(searchstring)
            self.finditem(event, searchstring, mode, start, end, length)

    def markpartsresi(self, event):
        for linum in range(self.text.GetLineCount()):
            line = self.text.GetLineRaw(linum)
            line = line.decode('utf-8')
            if "PART" in line and not "PART 0" in line:
                self.text.MarkerDefine(1, wx.stc.STC_MARK_BACKGROUND, background="#E0E6F8")
                self.text.MarkerAdd(linum, 1)
            if "RESI" in line:
                self.text.MarkerDefine(2, wx.stc.STC_MARK_BACKGROUND, background="#E0F8E0")
                self.text.MarkerAdd(linum, 2)

    def stext(self, event):
        text = self.text.GetText()
        textlist = text.split("\n")
        self.textlist = textlist

        #################################colour uis#############################################################

    def Colbadoc(self, event):
        values = []
        mode = wx.stc.STC_FIND_MATCHCASE
        pattern = re.compile(r'^([A-Za-z][\w\s]{1,2}.?\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
        for linum in range(self.text.GetLineCount()):
            line = self.text.GetLineRaw(linum)
            line = line.decode('utf-8')
            if pattern.match(line):
                if not line.upper().startswith("ZERR"):
                    if not line.upper().startswith("Q"):
                        searchval = line.split()[6]
                        end = self.text.GetLineEndPosition(linum)
                        begline = end - len(line)
                        beg = int(self.text.FindText(end - len(line), end, searchval))
                        if 0.0141 <= float(searchval) <= 0.100:
                            self.text.StartStyling(beg, wx.stc.STC_INDICS_MASK)
                            self.text.SetStyling(len(searchval), wx.stc.STC_INDIC2_MASK)
                        elif 0.1 <= float(searchval) <= 5.0:
                            self.text.StartStyling(beg, wx.stc.STC_INDICS_MASK)
                            self.text.SetStyling(len(searchval), wx.stc.STC_INDIC1_MASK)
                        elif -1.00 <= float(searchval) <= 0.014:
                            self.text.StartStyling(beg, wx.stc.STC_INDICS_MASK)
                            self.text.SetStyling(len(searchval), wx.stc.STC_INDIC0_MASK)

    def oncolorcif(self, event, t):
        t.Colourise(0, -1)
