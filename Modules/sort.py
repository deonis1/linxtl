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
import re
global ossystem
ossystem=sys.platform

class onSortc(wx.Dialog):
    def __init__(self, path, dirname, fnoe, filenamenoext, text):
       
        wx.Dialog.__init__(self, None, -1, 'Sort', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        
        self.dirname=dirname
        self.fnoe=fnoe
        self.text=text
        self.filenamenoext=filenamenoext
        self.path=path
        self.GetAL()
        self.sortlist=[]
        self.list1 = wx.ListBox(self, -1, choices=self.sortlist, style=0|wx.LB_EXTENDED)
        self.sizer_7_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Sort List"))
        self.b3 = wx.Button(self, wx.ID_ANY, ("All -->"))
        self.b4 = wx.Button(self, wx.ID_ANY, ("Sort A1B2C3"))
        self.b11 = wx.Button(self, wx.ID_ANY, ("Sort by trailer"))
        self.b7 = wx.Button(self, wx.ID_ANY, ("OK"), style=wx.BU_BOTTOM)
        self.b1 = wx.Button(self, wx.ID_ANY, ("<--"))
        self.b2 = wx.Button(self, wx.ID_ANY, ("-->"))
        self.list2 = wx.ListBox(self, -1, choices=self.mainlist, style=0|wx.LB_EXTENDED) # style =wx.LB_MULTIPLE
        self.sizer_8_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Atom List"))
        self.b8 = wx.Button(self, wx.ID_ANY, ("<--All"))
        self.b9 = wx.Button(self, wx.ID_ANY, ("Sort A1B2C3"))
        self.b10 = wx.Button(self, wx.ID_CANCEL, ("Cancel"))
       
        self.Bind(wx.EVT_BUTTON, self.onleft, self.b1)
        self.Bind(wx.EVT_BUTTON, self.onright, self.b2)
#        self.Bind(wx.EVT_BUTTON, self.atommass, self.b5)
        self.Bind(wx.EVT_BUTTON, self.leftsortNUM, self.b4)
        self.Bind(wx.EVT_BUTTON, self.rightsortNUM, self.b9)
        self.Bind(wx.EVT_BUTTON, self.sortlabel, self.b11)
        self.Bind(wx.EVT_BUTTON, self.ONOK, self.b7)
        self.Bind(wx.EVT_BUTTON, self.allright, self.b3)
        self.Bind(wx.EVT_BUTTON, self.allleft, self.b8)
        self.SetBackgroundColour(wx.Colour(249, 249, 248))
        self.SetForegroundColour(wx.Colour(76, 76, 76))
        self.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Arial"))
        self.__set_properties()
        self.__do_layout()


        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: sort.__set_properties
        self.SetTitle("Sort")
        xres,yres= wx.DisplaySize()
        size=(xres/8*xres/yres, yres/3)
        self.SetSize(size)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.SetForegroundColour(wx.Colour(100, 100, 100))
  
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: sort.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_8_staticbox.Lower()
        sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_7_staticbox.Lower()
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.HORIZONTAL)
        sizer_7.Add(self.list1, 1, wx.EXPAND, 0)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_5.Add(self.b3, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5)
        sizer_5.Add(self.b4, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 0)
        sizer_5.Add((20, 20), 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.b7, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_4.Add((50, 50), 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.b1, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 45)
        sizer_4.Add(self.b2, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 40)
        sizer_4.Add((50, 50), 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_8.Add(self.list2, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_6.Add(self.b8, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 0)
        sizer_6.Add(self.b9, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 0)
        sizer_6.Add(self.b11, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 0)
        sizer_6.Add((20, 20), 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(self.b10, 0, wx.BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.SetMinSize((400,500))
        self.SetSizerAndFit(sizer_1)
        self.Layout()
        # end wxGlade      
    def allright(self,event):
        num=self.list1.GetCount() 
        for i in range(0,num):
           self.list2.Append(self.list1.GetString(i))
        self.list1.Clear()  
    def allleft(self,event):
        num=self.list2.GetCount() 
        for i in range(0,num):
           self.list1.Append(self.list2.GetString(i))
        self.list2.Clear() 
        
    def onleft(self, event):
        temp=[]
        sel=self.list2.GetSelections() 
        for i in sel:
           self.list1.Append(self.list2.GetString(i))
        ad=0
        for i in sel:
            self.list2.Delete(i+ad)
            ad=ad-1
    def onright (self, event):
        temp=[]
        sel=self.list1.GetSelections() 
       # # print"GetSelection", sel
        for i in sel:
           self.list2.Append(self.list1.GetString(i))
        ad=0
        for i in sel:
            self.list1.Delete(i+ad)
            ad=ad-1
    
    def sortbylabel(self, atomgrid):
        return sorted(atomgrid, key=lambda x: x.split()[0][-1])
           
    def sortkey(self, string):    
        return tuple(int(num) if num else alpha for num, alpha in (re.compile(r'(\d+)|(\D+)').findall)(string))
    def rightsortNUM(self, event):
        temp=[]
        num=self.list2.GetCount() 
        for i in range(0,num):
           temp.append(self.list2.GetString(i))
        good=sorted(temp, key=self.sortkey)
        self.list2.Clear() 
        self.list2.Set(good)
    def sortlabel(self, event):
        temp=[]
        num=self.list2.GetCount() 
        for i in range(0,num):
           temp.append(self.list2.GetString(i))
        print("DSSSSSSSSSSSSSS", temp)
        good=self.sortbylabel(temp)
        print(good)
        self.list2.Clear() 
        self.list2.Set(good)
    

    def leftsortNUM(self, event):
        temp=[]
        num=self.list1.GetCount() 
        for i in range(0,num):
           temp.append(self.list1.GetString(i))
        good=sorted(temp, key=self.sortkey)
        self.list1.Clear() 
        self.list1.Set(good)
    
    def striplist(self, lines): 
        return([line for line in lines if line.strip()]) 

    def getsfac(self,gtext):
            return([line.replace('SFAC', '').replace('\r','').replace('\n','') for line in gtext if line.lower().startswith('sfac')]) 
    def GetAL(self):
        sortlist=[]
        text=self.text.GetText()
        gtext=text.split("\n")
        Atoms=self.getsfac(gtext)
        self.sfac=(''.join(Atoms)).split()
        atomindex=[]
        listallatoms=[]
        for i, line in enumerate(gtext):
            line=line.upper()
            for atom in self.sfac:
                atom=atom.upper()
                for ind in range(10):
                    if not line.startswith("CELL"):
                        if not line.startswith("ZERR"):
                            if len(line)>50:
                               if line.startswith(atom+str(ind)):
                                    atomindex.append(i)
                                    if not line.startswith("H"+str(ind)):
                                        sortlist.append(line.split()[0])
                                        if '=' in line:
                                            atomindex.append(i+1)
                                            line=line+'\n'+gtext[i+1]
                                            if 'AFIX' in gtext[i+2]:
                                                for ix, linex in enumerate(gtext[i+2:i+6]):
                                                     if 'AFIX   0' in linex:
                                                        line=line+'\n'+'\n'.join(gtext[i+2:i+2+ix+1])
                                                        
    #                                                    line=line+'\n'+('\n'.join(gtext[i+1:i+3+ix+1])+'\n')
                                            
                                        else:  
                                            line=line
                                        listallatoms.append(line)
        self.mainlist=sortlist                            
        self.latext=listallatoms
        closestatom=min(atomindex)
        furthestatom=max(atomindex)
        self.closest=closestatom
        self.furthest=furthestatom   

    def ONOK(self, event):
        temp=[]
        final=[]
        text=self.text.GetText()
        gtext=text.split("\n")
        num=self.list2.GetCount() 
        for i in range(0,num):
           temp.append(self.list2.GetString(i))
        for sorted in temp:
            for i, unsort in enumerate(self.latext):
                if sorted==unsort.split()[0]:
                        final.append(self.latext[i])
       
#        writetxt="".join(final)
        thetext=gtext[0:self.closest]+final+gtext[self.furthest+1:-1]
        self.text.SetText('\n'.join(thetext)+'\n')
        self.Close(True)

class webhtml(wx.Dialog):
    def __init__(self, path, dirname, webpage, fnoe, filenamenoext, text):
        wx.Dialog.__init__(self, None, -1, 'Webbrowser')
        self.dirname=dirname
        self.fnoe=fnoe
        self.webpage=webpage
        self.text=text
        self.filenamenoext=filenamenoext
        self.path=path    
        html = wx.html.HtmlWindow(self) 
        #if "gtk2" in wx.Platformlnfo:
        html.SetStandardFonts()
        wx.CallAfter(html.LoadPage, self.webpage)
