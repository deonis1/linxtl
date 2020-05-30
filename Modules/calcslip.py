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
import os
import wx
import math
class slippage(wx.Dialog):
    def __init__(self, text, cell, dirname):
        self.text=text
        self.dirname=dirname
        self.cell=cell
        self.calctmp()
        # begin wxGlade: MyFrame1.__init__
        wx.Dialog.__init__(self, None, -1, 'SimpleSadabs', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER  )
#        self.title = wx.StaticText(self, wx.ID_ANY, ("Define planes"))
        if os.path.exists(os.path.join(self.dirname, "linxtl_calc.tmp")):
            print(self.symoner, self.symtwor, self.Ar, self.Br)
            self.text_ctrl_A = wx.TextCtrl(self, wx.ID_ANY, self.Ar)
            self.sizer_7_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Atoms for ring A:"))
            self.text_ctrl_B = wx.TextCtrl(self, wx.ID_ANY, self.Br)
            self.sizer_8_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Atoms for ring B:"))
            self.text_ctrl_X = wx.TextCtrl(self, wx.ID_ANY, self.symoner.split(',')[0], style=wx.TE_RIGHT)
            self.x = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_Y = wx.TextCtrl(self, wx.ID_ANY, self.symoner.split(',')[1], style=wx.TE_RIGHT)
            self.y = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_Z = wx.TextCtrl(self, wx.ID_ANY, self.symoner.split(',')[2], style=wx.TE_RIGHT)
            self.z = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_XA = wx.TextCtrl(self, wx.ID_ANY, self.symtwor.split(',')[0], style=wx.TE_RIGHT)
            self.xa = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_YA = wx.TextCtrl(self, wx.ID_ANY, self.symtwor.split(',')[1], style=wx.TE_RIGHT)
            self.ya = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_ZA = wx.TextCtrl(self, wx.ID_ANY, self.symtwor.split(',')[2], style=wx.TE_RIGHT)
            self.za = wx.StaticText(self, wx.ID_ANY, (""))
        else:
            self.text_ctrl_A = wx.TextCtrl(self, wx.ID_ANY, "C1 C2 C3 C4 C5 C6")
            self.sizer_7_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Atoms for ring A:"))
            self.text_ctrl_B = wx.TextCtrl(self, wx.ID_ANY, "C1 C2 C3 C4 C5 C6")
            self.sizer_8_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Atoms for ring B:"))
            self.text_ctrl_X = wx.TextCtrl(self, wx.ID_ANY, "0 +x", style=wx.TE_RIGHT)
            self.x = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_Y = wx.TextCtrl(self, wx.ID_ANY, "0 +y", style=wx.TE_RIGHT)
            self.y = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_Z = wx.TextCtrl(self, wx.ID_ANY, "0 +z", style=wx.TE_RIGHT)
            self.z = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_XA = wx.TextCtrl(self, wx.ID_ANY, "1 -x", style=wx.TE_RIGHT)
            self.xa = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_YA = wx.TextCtrl(self, wx.ID_ANY, "1 -y", style=wx.TE_RIGHT)
            self.ya = wx.StaticText(self, wx.ID_ANY, (""))
            self.text_ctrl_ZA = wx.TextCtrl(self, wx.ID_ANY, "1 -z", style=wx.TE_RIGHT)
            self.za = wx.StaticText(self, wx.ID_ANY, (""))
        
        self.sizer_11_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Symmetry Operator for ring B:"))
        self.sizer_9_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Symmetry Operator for ring A:"))
        self.ok = wx.Button(self, wx.ID_OK)
        self.cancel = wx.Button(self, wx.ID_ANY, ("Cancel"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle(("Slippage. Please define two planes:"))
        
        self.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.SetForegroundColour(wx.Colour(0, 0, 0))

        self.text_ctrl_A.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_A.SetForegroundColour(wx.Colour(0, 0, 0))

        self.text_ctrl_B.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_B.SetForegroundColour(wx.Colour(0, 0, 0))

        self.text_ctrl_X.SetMinSize((80, -1))
        self.text_ctrl_X.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_X.SetForegroundColour(wx.Colour(0, 0, 0))
        self.x.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.x.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_ctrl_Y.SetMinSize((80, -1))
        self.text_ctrl_Y.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_Y.SetForegroundColour(wx.Colour(0, 0, 0))
        self.y.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.y.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_ctrl_Z.SetMinSize((80, -1))
        self.text_ctrl_Z.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_Z.SetForegroundColour(wx.Colour(0, 0, 0))
        self.z.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.z.SetForegroundColour(wx.Colour(0, 0, 0))
        
        self.text_ctrl_XA.SetMinSize((80, -1))
        self.text_ctrl_XA.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_XA.SetForegroundColour(wx.Colour(0, 0, 0))
        self.xa.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.xa.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_ctrl_YA.SetMinSize((80, -1))
        self.text_ctrl_YA.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_YA.SetForegroundColour(wx.Colour(0, 0, 0))
        self.ya.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.ya.SetForegroundColour(wx.Colour(0, 0, 0))
        self.text_ctrl_ZA.SetMinSize((80, -1))
        self.text_ctrl_ZA.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.text_ctrl_ZA.SetForegroundColour(wx.Colour(0, 0, 0))
        self.za.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.za.SetForegroundColour(wx.Colour(0, 0, 0))
        
        self.ok.SetMinSize((-1, -1))
        self.cancel.SetMinSize((-1, -1))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_9_staticbox.Lower()
        sizer_9 = wx.StaticBoxSizer(self.sizer_9_staticbox, wx.HORIZONTAL)
        self.sizer_11_staticbox.Lower()
        sizer_11 = wx.StaticBoxSizer(self.sizer_11_staticbox, wx.HORIZONTAL)
        self.sizer_8_staticbox.Lower()
        sizer_8 = wx.StaticBoxSizer(self.sizer_8_staticbox, wx.VERTICAL)
        self.sizer_7_staticbox.Lower()
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.VERTICAL)
#        sizer_6.Add(self.title, 0, wx.LEFT, 10)
        sizer_7.Add(self.text_ctrl_A, 0, wx.LEFT | wx.EXPAND, 10)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add(self.text_ctrl_B, 0, wx.LEFT | wx.EXPAND, 10)
        sizer_6.Add(sizer_8, 1, wx.EXPAND, 0)
        
        sizer_9.Add(self.text_ctrl_X, 0, wx.LEFT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_9.Add(self.x, 0, wx.LEFT  | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.text_ctrl_Y, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.y, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.text_ctrl_Z, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(self.z, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_11.Add(self.text_ctrl_XA, 0, wx.LEFT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_11.Add(self.xa, 0, wx.LEFT  | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add(self.text_ctrl_YA, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add(self.ya, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add(self.text_ctrl_ZA, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_11.Add(self.za, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 0)
        
        sizer_6.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_10.Add(self.ok, 0, wx.LEFT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 20)
        sizer_10.Add((50, 20), 1, 0, 0)
        sizer_10.Add(self.cancel, 0, wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 20)
        sizer_6.Add(sizer_10, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_6)
       #self.SetSizerAndFit(sizer_6)
        sizer_6.SetSizeHints(self)
        
        self.Bind(wx.EVT_BUTTON, self.OnOk, self.ok)       
        self.Bind(wx.EVT_BUTTON, self.onclose, self.cancel)
        self.Layout()
        self.SetSize((400, 300))
        self.SetMinSize((400, 300))
     
    def calctmp(self):
        if os.path.exists(os.path.join(self.dirname, "linxtl_calc.tmp")):
            if os.path.getsize(os.path.join(self.dirname, "linxtl_calc.tmp"))>60:
#                print(os.path.getsize(os.path.join(self.dirname, "linxtl_calc.tmp")))
                fcalc=open(os.path.join(self.dirname, "linxtl_calc.tmp"), 'r')
                pars=fcalc.readlines()
                self.symoner=pars[0].replace("\n","").replace("\r","")
                self.symtwor=pars[1].replace("\n","").replace("\r","")
                self.Ar=pars[2].replace("\n","").replace("\r","") 
                self.Br=pars[3].replace("\n","").replace("\r","")
                fcalc.close()
        # end wxGlade
    def getlines(self, event):
        coordinates=[]
        atoms=atom.split()
        gtl=self.text.GetText()
        gtext=gtl.split("\n")
        for a in atoms:
            for lines in gtext:
                if len(lines)>=20:
                   if lines.upper().startswith(a.upper()+" "):
                      coordinates.append(" ".join(lines.split()[0:5]))
        return coordinates

    def centroid(self, event, coord, cell):
        clist=[]
        
        fracl=[]
        a=float(cell[0])
        b=float(cell[1])
        c=float(cell[2])
        alpha=float(cell[3])
        beta=float(cell[4])
        gamma=float(cell[5])

#        for line in coord.split("\n"):    
#            line=line.split(' ')
#            xcor=a*float(line[2])+(b*math.cos(math.radians(gamma)))*float(line[3]) ########### correct formula to include z
#            ycor=(b*math.sin(math.radians(gamma)))*float(line[3])
#            zcor=(b*math.sin(math.radians(gamma)))*float(line[3])
#            res=(xcor, ycor, zcor)
#            clist.append(res)

        fra=coord.split("\n")
        for li in fra:
            fracl.append(li.split())
        fl=(len(fracl))
        fracl = [[float(j) for j in i] for i in fracl] #convert to a list of listed floats
        sumxyz=([sum(i) for i in zip(*fracl)])
        frx=round(sumxyz[0]/fl, 6)
        fry=round(sumxyz[1]/fl, 6)
        frz=round(sumxyz[2]/fl, 6)
        #SFAC Cg 0 0 0 0 0 0 0 0 0 0 0 0 0 0.
        #Cg1   7    0.537361    0.369170    0.193034    10.00000    0.00100
        return frx, fry, frz
    
    def calcortho(self, event, cell, coord, sym):
        clist=[]
        clistortho=[]
        a=float(cell[0])
        b=float(cell[1])
        c=float(cell[2])
        alpha=float(cell[3])
        beta=float(cell[4])
        gamma=float(cell[5])
        count=1
        for line in coord:
            line=line.split()
            print(line)
            xa=float(sym[0].split()[0])
            ya=float(sym[1].split()[0])
            za=float(sym[2].split()[0]) 
            xb=sym[0].split()[1][0]
            yb=sym[1].split()[1][0]
            zb=sym[2].split()[1][0]
            if xb=="+":
               x=float(line[2])
            if yb=="+":
               y=float(line[3])
            if zb=="+":
               z=float(line[4])
            if xb=="-":
               x=-float(line[2])
            if yb=="-":
               y=-float(line[3])
            if zb=="-":
               z=-float(line[4])
          
            cosstar=((math.cos(math.radians(beta))*math.cos(math.radians(gamma))-math.cos(math.radians(alpha)))/(math.sin(math.radians(gamma))*math.sin(math.radians(beta))))
            xcor=a*(xa+x)+(b*math.cos(math.radians(gamma)))*(ya+y)+c*math.cos(math.radians(beta))*(za+z)*math.sin(math.radians(beta))
            ycor=(b*math.sin(math.radians(gamma)))*(ya+y)-c*cosstar*(za+z)
            zcor=(c*math.sin(math.radians(beta)))*(za+z)*math.sqrt(1-(math.cos(math.radians(alpha)))*(math.cos(math.radians(alpha))))
            clistortho.append([str(line[0]), str(line[1]), str(round(xcor, 4)), str(round(ycor, 4)), str(round(zcor, 4))])
                
        result=clistortho   
            
        return result    
    
    
    
#    def calcslip(self, event, coord, cell, symone, symtwo):
#        clist=[]
#        a=float(cell[0])
#        b=float(cell[1])
#        c=float(cell[2])
#        alpha=float(cell[3])
#        beta=float(cell[4])
#        gamma=float(cell[5])
#        calcone=self.calcortho(event, cell, coord, symone)
#        calctwo=self.calcortho(event, cell, coord, symtwo)
#        return calcone+calctwo
##        return ("Slippage x="+str(dx)+"; y="+str(dy)+"\n") 
   
    def clippboard(self, event, out):
        self.dataObj = wx.TextDataObject()
        self.dataObj.SetText(out)
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.dataObj)
            wx.TheClipboard.Close()
            dlg = wx.MessageDialog(self, 'The following data was copied to clipboard:  '+"\n"+out,
                                'Data was copied to clipboard', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            
    def OnOk(self, event):
        print("Exit")
        event.Skip()
       
       

#        self.clippboard(event, out)
    def onclose(self, event):
        self.Close()