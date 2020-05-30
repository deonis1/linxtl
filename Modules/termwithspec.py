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
import sys, os
global ossystem
ossystem=sys.platform
import threading
EVT_CHARACTER_ID = wx.NewId()
class RepeatingTimer(threading._Timer):
    def run(self):
        while True:
            self.finished.wait(self.interval)
            if self.finished.is_set():
                return
            else:
                self.function(*self.args, **self.kwargs)
class CharacterEvent(wx.PyEvent):
    def __init__(self, character):
      wx.PyEvent.__init__(self)
      self.SetEventType(EVT_CHARACTER_ID)
      self.character = character

        
class terminal(wx.Dialog):
    def __init__(self,  event, ter):
        displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        sizes = [display.GetGeometry().GetSize() for display in displays]
        displaySize=sizes[0].Get()
        xres,yres= displaySize                                  
        si=(xres/3*xres/yres,yres/2)
        wx.Dialog.__init__(self, None, -1, 'Results of refinement',  style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER  , size=si)
        self.shell=ter
        self.text_ctrl_1=wx.stc.StyledTextCtrl(self, -1, style=wx.TE_MULTILINE|wx.RESIZE_BORDER|wx.NO_BORDER|wx.WANTS_CHARS|wx.HSCROLL)
#        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.HSCROLL)
        self.SetMinSize((800, 450))
        if ossystem.startswith("darwin"):
           self.fs=12
        elif ossystem.startswith("win"):
           self.fs=11
        elif ossystem.startswith("lin"):
           self.fs=12
        self.text_ctrl_1.SetLexer(wx.stc.STC_LEX_LUA)
        
        styled_text=["R1 = ", "Maximum", "wR2","GooF", "S", "Restrained"]
        self.text_ctrl_1.SetKeyWords(0, " ".join(styled_text))
        if ossystem.startswith("darwin"):
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,'fore:#CCCFFF,back:#000000,face:Courier,size:'+str(self.fs))
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_DEFAULT,'fore:#CCCFFF,back:#000000,face:Courier,size:'+str(self.fs))
               self.text_ctrl_1.StyleClearAll()
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_WORD,'fore:#FFFFFF,back:#000000,bold,face:Courier,size:'+str(self.fs)) 
#               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_NUMBER,'fore:#FFFFFF,back:#000000,bold,face:Courier,size:'+str(self.fs))        
        elif ossystem.startswith("win"):
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,'fore:#CCCCCC,back:#000000,face:Lucida Console,size:'+str(self.fs))
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_DEFAULT,'fore:#CCCCCC,back:#000000,face:Lucida Console,size:'+str(self.fs))
               self.text_ctrl_1.StyleClearAll()
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_WORD,'fore:#FFFFFF,back:#000000,bold,face:Courier,size:'+str(self.fs)) 
#               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_NUMBER,'fore:#FFFFFF,back:#000000,bold,face:Courier,size:'+str(self.fs))        
        elif ossystem.startswith("lin"):
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,'fore:#CCCFFF,back:#000000,face:Courier,size:'+str(self.fs)) 
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_DEFAULT,'fore:#CCCFFF,back:#000000,face:Courier,size:'+str(self.fs)) 
               self.text_ctrl_1.StyleClearAll()
               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_WORD,'fore:#FFFFFF,back:#000000,bold,face:Courier,size:'+str(self.fs))     
#               self.text_ctrl_1.StyleSetSpec(wx.stc.STC_LUA_NUMBER,'fore:#FFFFFF,back:#000000,bold,face:Courier,size:'+str(self.fs))     
        
        self.text_ctrl_1.SetMarginWidth(2, 0)
        self.text_ctrl_1.SetMarginWidth(1, 0)
        self.text_ctrl_1.SetMarginWidth(0, 0)
        self.text_ctrl_1.SetMarginLeft(2)
        self.text_ctrl_1.SetSelBackground(True, wx.Colour(0,0,66))
       
        self.ter(event)
        self.__set_properties()
        self.__do_layout()


        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Terminal")
        
        
#        self.Fit()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.text_ctrl_1, 1, wx.EXPAND, 3)
        self.SetSizer(sizer_1)
        
        self.Layout()
        # end wxGlade
 
    def read_shell_output(self):
      while True:
         output = self.shell.stdout.readline()
         wx.Yield()
         if not len(output)==3:
            if not len(output)==2:
                if output == '':
                    break
                wx.PostEvent(self, CharacterEvent(output))

    def ter(self, event):

        self.shell_thread = threading.Thread(target=self.read_shell_output)
        self.shell_thread.start()
        self.Connect(-1, -1, EVT_CHARACTER_ID, self.on_result)

    def onCol(self, event): 
            print("p")
            self.text_ctrl_1.Colourise(0, -1) 
    
    def on_result(self, event):
        x=event.character
        self.text_ctrl_1.AppendText(x)
        self.text_ctrl_1.LineScrollDown()
        self.onCol(event)
