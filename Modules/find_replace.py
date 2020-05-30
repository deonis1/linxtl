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
import re
class find_r(wx.Dialog):
    def __init__(self, event, text_class, main_font,  fsg, color):
       
        wx.Dialog.__init__(self, None, -1, 'Find and Replace', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER  )
        # begin wxGlade: MyFrame.__init__
        self.text=text_class
        self.oncolor=color
        self.pos=0
        self.flist=[]
        self.main_font=main_font
        self.fsg=fsg
        self.Find_label = wx.StaticText(self, wx.ID_ANY, ("Find"),  style=0)
        self.text_find = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_NO_VSCROLL)
        self.text_find.SetFocus() 
        self.replace_label = wx.StaticText(self, wx.ID_ANY, ("Replace"),   style=wx.ALIGN_BOTTOM)
        self.text_replace = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_NO_VSCROLL)
#        self.match_case = wx.CheckBox(self, wx.ID_ANY, ("Match Case"))
#        self.match_word = wx.CheckBox(self, wx.ID_ANY, ("Match Word"))
#        self.wrap_around = wx.CheckBox(self, wx.ID_ANY, ("Wrap Around"))
#        self.search_back = wx.CheckBox(self, wx.ID_ANY, ("Search Back"))
        self.find_b = wx.Button(self, wx.ID_ANY, ("Find"))
        self.find_next = wx.Button(self, wx.ID_ANY, ("Find Next"))
        self.replace_b = wx.Button(self, wx.ID_ANY, ("Replace"))
        self.replaceall_b = wx.Button(self, wx.ID_ANY, ("Replace All"))
        self.close_b = wx.Button(self, wx.ID_CLOSE, ("Close"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Find and Replace ")
        self.SetSize((1500, 600))
        self.SetBackgroundColour(wx.Colour(249, 249, 248))
        self.Find_label.SetMinSize((120, 34))
        self.replace_label.SetMinSize((120, 34))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.Find_label,0, wx.ALIGN_BOTTOM|wx.LEFT|wx.TOP, 10)
        sizer_3.Add(self.text_find,1,  wx.ALIGN_TOP|wx.ALL, 10)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_4.Add(self.replace_label, 0, wx.ALIGN_CENTER|wx.LEFT|wx.TOP, 10)
        sizer_4.Add(self.text_replace, 1, wx.ALIGN_TOP|wx.ALL, 10)
        sizer_2.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_6.Add((150, 100), 0, wx.ALIGN_CENTER, 0)
        sizer_6.Add(sizer_6_copy, 1, 0, 0)
        sizer_2.Add(sizer_6, 1, 0, 0)
        sizer_5.Add(self.find_b, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 20)
        sizer_5.Add(self.find_next, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 20)
        sizer_5.Add(self.replace_b, 0, wx.ALIGN_CENTER  | wx.LEFT | wx.RIGHT, 20)
        sizer_5.Add(self.replaceall_b, 0, wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, 20)
        sizer_5.Add(self.close_b, 0, wx.ALIGN_CENTER | wx.ALL, 20)
        sizer_2.Add(sizer_5, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.SetSizerAndFit(sizer_2)
   
        self.Layout()
        self.Center()
        self.CenterOnScreen()
        self.binding()
        
    def binding(self):
        self.Bind(wx.EVT_BUTTON, self.on_find, self.find_b)
        self.Bind(wx.EVT_BUTTON, self.on_find_next, self.find_next)
        self.Bind(wx.EVT_BUTTON, self.on_replace, self.replace_b)
        self.Bind(wx.EVT_BUTTON, self.on_replaceall, self.replaceall_b)
        self.Bind(wx.EVT_BUTTON, self.on_close, self.close_b)
        self.Bind(wx.EVT_CLOSE,  self.on_close)
        self.text_find.Bind(wx.EVT_KEY_UP,  self.on_find_key)
        
    def clearcolor(self, event):
        self.text.ClearDocumentStyle()
        self.text.SetLexer(wx.stc.STC_LEX_NULL)
    def on_replace(self, event):
        searchstring=self.text_find.GetValue()
        lensearch=len(searchstring)
        self.on_find(event)
        lflist=len(self.flist)
        pos=self.text.GetCurrentPos()
        replacestring=self.text_replace.GetValue()
        lenreplace=len(replacestring)
        diff=lenreplace-lensearch
        if lflist>0:
            if not pos>=int(self.flist[-1][0]): #check if position of the cursor is close to the end
                    self.text.GotoPos(int(self.flist[self.lastitem][0])+diff-lensearch-1) 
#                    self.text.SetSelection(int(self.flist[self.lastitem][0]), int(self.flist[self.lastitem][0])+int(self.flist[self.lastitem][1]))
                    self.text.BeginUndoAction()
                    self.text.SetTargetStart(self.flist[self.lastitem][0])
                    self.text.SetTargetEnd(int(self.flist[self.lastitem][0])+int(self.flist[self.lastitem][1]))
                    self.text.ReplaceTarget(replacestring)
                    self.text.EndUndoAction()
                    self.lastitem=self.lastitem+1 #go to next find

    def on_find_next(self, event):
        searchstring = self.text_find.GetValue()
        if not len(searchstring) == 0:
            self.clearcolor(event)
            self.flist = []
            end = self.text.GetTextLength()
            start = self.text.GetCurrentPos()
            mode = wx.stc.STC_FIND_MATCHCASE
            length = len(searchstring)
            self.finditem(event, searchstring, mode, start, end, length)
            lensearch = len(searchstring)
            lenreplace = len(self.text_replace.GetValue())
            diff = lenreplace - lensearch
            lflist = len(self.flist)
            pos = self.text.GetCurrentPos()
            if lflist > 0:
                if not pos >= int(self.flist[-1][0]):  # check if position of the cursor is close to the end
                    try:
                        for i in self.flist:
                            if pos<=i[0]:
                                print(i[0])
                                self.text.GotoPos(i[0])
                                self.text.SetSelection(i[0], int(i[0]) + int(i[1]))
                                break
                    except IndexError:
                        print("list index out of range in on_find")


    def on_replaceall(self, event):
        self.on_find(event)
        lflist=len(self.flist)
        replacestring=self.text_replace.GetValue()
        findstring = self.text_find.GetValue()
        self.text.BeginUndoAction()
        if lflist>0:
                for items in reversed(self.flist):
                    self.text.SetSelection(items[0], int(items[0])+int(items[1])) 
                    
                    self.text.SetTargetStart(items[0])
                    self.text.SetTargetEnd(int(items[0])+int(items[1]))
                    self.text.ReplaceTarget(replacestring)
        self.text.EndUndoAction()

    def finditem(self, event, searchstring, mode, start, end, length):  
                self.text.StyleSetSpec(15, "fore:#000000,back:#FFFF00,face:%s,size:%d" % (self.main_font,int(self.fsg))) #yellow for find
                while True:
                    start= int(self.text.FindText(start, end,  searchstring))
                    if start==-1: break
                    self.flist.append((start, len(searchstring)))
                    self.text.StartStyling(start, wx.stc.STC_INDICS_MASK)
                    self.text.SetStyling(length, wx.stc.STC_INDIC1_MASK) 
                    start+=  length
    def on_find_key(self,event):
        if len(self.text_find.GetValue())>=2:
            self.on_find(event)
        elif len(self.text_find.GetValue())==0:
            self.clearcolor(event)
    def on_find(self, event):
                searchstring=self.text_find.GetValue()
                if not len(searchstring)==0:
                    self.clearcolor(event)
                    self.flist=[]
                    end=self.text.GetTextLength()
                    start=self.text.GetCurrentPos()
                    mode=wx.stc.STC_FIND_MATCHCASE
                    self.lastitem=0
                    length=len(searchstring)
                    self.finditem(event, searchstring, mode, start, end, length)   
                    lensearch=len(searchstring)
                    lenreplace=len(self.text_replace.GetValue())
                    diff=lenreplace-lensearch
                    try:
                       self.text.GotoPos(int(self.flist[self.lastitem][0])+diff-lensearch-1) 
                    except IndexError: 
                      print("list index out of range in on_find")
    def stclex(self):
        from shelxlexer import lexer_class
        lexc=lexer_class(self.text, self.fsg, self.main_font)
        
    
    def on_close(self, event):
        self.clearcolor(event)
        self.stclex()
        self.oncolor(event)
        self.Destroy()
