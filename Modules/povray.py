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
import subprocess
import webbrowser
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
class povrayclass(wx.Dialog):
    def __init__(self, path, dirname, fnoe, filenamenoext, phtopovray):
        xres,yres= wx.DisplaySize()
        size=(xres/5*xres/yres, yres/2.5)
        wx.Dialog.__init__(self, None, -1, 'Povray', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER  ,  size=size)
        self.dirname=dirname
        self.fnoe=fnoe
        self.phtopovray=phtopovray
        self.filenamenoext=filenamenoext
        self.path=path    
        self.__do_layout()   
        if os.path.exists(os.path.join(self.dirname, filenamenoext+".pov")):
           self.fileinput.SetValue(os.path.join(self.dirname, filenamenoext+".pov"))
        else:
           self.fileinput.SetValue(" ")
        self.fileoutput.SetValue(os.path.join(self.dirname, filenamenoext+".png"))

    def __do_layout(self):
           # begin wxGlade: MyFrame.__set_properties
        xres,yres= wx.DisplaySize()
        self.SetTitle("Render povray")
        self.SetMinSize((xres/6*xres/yres, yres/3))
        # end wxGlade
        self.fileinput = wx.TextCtrl(self, wx.ID_ANY, "")
        self.OPEN = wx.Button(self, wx.ID_ANY, ("Open"))
        self.sizer_3_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Povray input file"))
        self.fileoutput = wx.TextCtrl(self, wx.ID_ANY, "")
        self.OPEN2 = wx.Button(self, wx.ID_ANY, ("Open"))
        self.sizer_3_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Povray output file"))
        self.width = wx.TextCtrl(self, wx.ID_ANY, "2000")
        self.sizer_5_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Width"))
        self.height = wx.TextCtrl(self, wx.ID_ANY, "2000")
        self.sizer_6_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Height"))
        self.OPENpng = wx.Button(self, wx.ID_ANY, ("Open Image"))
        self.render = wx.Button(self, wx.ID_ANY, ("Render"))
        self.close = wx.Button(self, wx.ID_ANY, ("Close"))
        self.Bind(wx.EVT_BUTTON, self.openimage, self.OPENpng)
        self.Bind(wx.EVT_BUTTON, self.povload, self.OPEN)
        self.Bind(wx.EVT_BUTTON, self.povoutput, self.OPEN2)
        self.Bind(wx.EVT_BUTTON, self.onclose, self.close)
        self.Bind(wx.EVT_BUTTON, self.onrender, self.render)
        
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_6_staticbox.Lower()
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.HORIZONTAL)
        self.sizer_5_staticbox.Lower()
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.HORIZONTAL)
        self.sizer_3_copy_staticbox.Lower()
        sizer_3_copy = wx.StaticBoxSizer(self.sizer_3_copy_staticbox, wx.HORIZONTAL)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        sizer_3.Add(self.fileinput, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.OPEN, 0, wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_2.Add(sizer_3, 1, wx.LEFT | wx.EXPAND, 5)
        sizer_3_copy.Add(self.fileoutput, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3_copy.Add(self.OPEN2, 0, wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_2.Add(sizer_3_copy, 1, wx.LEFT | wx.EXPAND, 5)
        sizer_5.Add(self.width, 1, 0, 0)
        sizer_4.Add(sizer_5, 1, wx.LEFT | wx.EXPAND, 5)
        sizer_6.Add(self.height, 1, 0, 0)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_4.Add(self.OPENpng, 0, wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_7.Add(self.render, 1, wx.LEFT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 15)
        sizer_7.Add((50, 20), 2, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_7.Add(self.close, 1, wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 15)
        sizer_2.Add(sizer_7, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Center()
        self.CenterOnScreen()
        self.SetSizerAndFit(sizer_1)
        
      
    
        
    def povload(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.pov",  wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            dir=dlg.GetDirectory()
            name=dlg.GetFilename()
            fnamefull=os.path.join(dir,name)
            self.fileinput.SetValue(fnamefull)  
    def povoutput(self, event):
        dlg = wx.FileDialog(self, "Set a file name [png]", self.dirname, "", "*.png", wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            dir=dlg.GetDirectory()
            name=dlg.GetFilename()
            fnamefull=os.path.join(dir,name)
            self.fileoutput.SetValue(fnamefull) 
    def status(self, event):
         print("I'm alive")
    def onrender(self, event):
        import distutils.spawn 
        input=self.fileinput.GetValue()
        output=self.fileoutput.GetValue()
        width=self.width.GetValue()
        height=self.height.GetValue()
        os.chdir(self.dirname)
        
        timer = RepeatingTimer(1.0, self.status(event))
        timer.daemon = True # Allows program to exit if only the thread is alive
        timer.start()   
        proc=subprocess.Popen([self.phtopovray, input, "-H"+height, "-W"+width])
        proc.wait()

        timer.cancel()
    def openimage(self, event):
        out=self.fileoutput.GetValue()
        # print out
        if os.path.exists(self.fnoe+".png"):
            try:
                if ossystem.startswith("win"):
                    os.chdir(self.dirname)
                   
                    webbrowser.open(out)
                elif ossystem.startswith("darwin"):
                    os.chdir(self.dirname)
                    webbrowser.open('file://%s' % out)            
                else:
                    os.chdir(self.dirname)
                    webbrowser.open('file://%s' % out)
                    #webbrowser.open('publish.html')
             
            except OSError:
                   pass
        else: 
            dlg = wx.MessageDialog(self, "Error! "+out+" does not exist",
                                'Error', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
          
    def onclose(self, event):
        self.Close()
