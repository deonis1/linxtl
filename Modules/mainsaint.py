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
import subprocess
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

        

class MainSaint(wx.Dialog):
    def __init__(self, path, dirname, fnoe, filenamenoext, phtosaint):
        wx.Dialog.__init__(self, None, -1, 'SaintGui 1.03', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER  )
        self.path=path
        self.phtosaint=phtosaint
        self.fnoe=fnoe
        self.dirnameall=dirname
        self.SetBackgroundColour(wx.Colour(241, 241, 241))
        self.SetForegroundColour(wx.Colour(20, 19, 81))
        if not os.path.exists(self.phtosaint):
                 askyesno = wx.MessageDialog( self, "Saint was not found. Please install saint. \n See Preference > External Programs for more details",  "file not found", wx.OK)
        self.list_box_1 = wx.CheckListBox(self, wx.ID_ANY, choices=[])
        
        self.p4p = wx.TextCtrl(self, wx.ID_ANY, "")
        self.p4p.SetValue(self.fnoe+".p4p")
        self.browsep4p = wx.Button(self, wx.ID_ANY, ("browse"))
        self.sizer_1_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Input P4P file; Define project directory"))
        self.x = wx.TextCtrl(self, wx.ID_ANY, ("1"))
        self.y = wx.TextCtrl(self, wx.ID_ANY, ("1"))
        self.z = wx.TextCtrl(self, wx.ID_ANY, ("1"))
        self.sizer_2_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Box Size (X,Y,Z)"))
        self.spatial = wx.TextCtrl(self, wx.ID_ANY, ("$P4P"))
        self.browsespatial = wx.Button(self, wx.ID_ANY, ("browse"))
        self.sizer_1_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Spatial Cal filename"))
        self.checkbox_1 = wx.CheckBox(self, wx.ID_ANY, ("Enable Box Size Refinement"))
        self.crystal = wx.ComboBox(self, wx.ID_ANY, choices = ['Triclinic:-1', 'Monoclinic:2/m', 'Orthorhombic:mmm','Tetragonal:4/m','Tetragonal:4/mmm','Trigonal:-3','Trigonal:-3m','Hexagonal:6/m','Hexagonal:6/mmm','Cubic:m-3','Cubicm:-3m'], style=wx.CB_DROPDOWN)
        # choices=[("Triclinic:1-:P"), ("Monoclinic:2/m:P"), ("Monoclinic:2/m:C"), ("Orthorhombic:mmm:P"), ("Orthorhombic:mmm:C"),("Orthorhombic:mmm:I"), ("Orthorhombic:mmm:F"), ("Tetragonal:4/m"), ("Tetragonal:4/mmm:P"), ("Tetragonal:4/mmm:I"), ("Trigonal:3-:P"), ("Trigonal:m3-:P"), ("Hexagonal:6/m:"), ("Hexagonal:6/mmm:P"), ("Cubic:3-m:P"), ("Cubic:3-m:I"),  ("Cubic:m3-m")], style=wx.CB_DROPDOWN)
#        saintcrystalsystems = {1: 'Triclinic',3: 'Monoclinic',5: 'Orthorhombic', 6: 'Tetragonal',7: 'Hexagonal', 8: 'Rhombohedral', 9: 'Cubic'}
#        saintl = ['-1', '2/m', 'mmm','4/m','4/mmm','-3H','-3R','-3m','-3m1','-31m','6/m','6/mmm','m-3','m-3m']
#        saintlatticetypes = {0: 'P', 1: 'A', 2: 'B', 3: 'C', 4: 'F',  5: 'I', 6: 'R'}
        
        self.sizer_3_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Crystal System"))
        self.res = wx.TextCtrl(self, wx.ID_ANY, ("0.840"))
        self.sizer_5_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Resolution "))
        self.lsfit = wx.TextCtrl(self, wx.ID_ANY, ("8.00"))
        self.sizer_4_staticbox = wx.StaticBox(self, wx.ID_ANY, ("LS Fit:  Max I/sigma "))
        self.strong = wx.TextCtrl(self, wx.ID_ANY, ("10.0"))
        self.sizer_10_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Strong thresh (I/sigma) "))
        self.twin = wx.TextCtrl(self, wx.ID_ANY, ("1.000 "))
        self.sizer_4_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Twin overlaps: Separation factor "))
        self.boxvol = wx.TextCtrl(self, wx.ID_ANY, ("1.000"))
        self.sizer_11_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Box volume target "))
        self.advanceinput = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.HSCROLL | wx.TE_LINEWRAP)
        self.sizer_15_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Saint Input Command (Advanced)"))
        self.findruns = wx.Button(self, wx.ID_ANY, ("Find Runs"))
        self.stop = wx.Button(self, wx.ID_ANY, ("Stop"))
        self.Integrate = wx.Button(self, wx.ID_ANY, ("Integrate"))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        
        self.stop.SetBackgroundColour(wx.Colour(237,0,1))
        self.__set_properties()
        self.__do_layout()

#        self.Bind(wx.EVT_TEXT, self.onp4p, self.p4p)
        self.Bind(wx.EVT_BUTTON, self.onBrowse, self.browsep4p)
        self.Bind(wx.EVT_BUTTON, self.onBrowse2, self.browsespatial)
        self.Bind(wx.EVT_BUTTON, self.onfindruns, self.findruns)
        self.Bind(wx.EVT_BUTTON, self.onintegrate, self.Integrate)
        self.Bind(wx.EVT_BUTTON, self.onstop, self.stop)
        # end wxGlade
        

    def __set_properties(self):
        xres,yres= wx.DisplaySize()
        textsize=(xres/10, -1)
        # begin wxGlade: MainSaint.__set_properties
        buttonsize=wx.Button.GetDefaultSize()    
        size=(self.SetSize((xres/2.5*xres/yres, yres/1.5)))
        self.SetSize(size)
#        self.SetBackgroundColour(wx.Colour(249, 249, 248))
#        self.SetForegroundColour(wx.Colour(76, 76, 76))
        self.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Arial"))
        self.list_box_1.SetMinSize((210, 350))
        self.p4p.SetMinSize(textsize)
        self.x.SetMinSize(buttonsize)
        self.y.SetMinSize(buttonsize)
        self.z.SetMinSize(buttonsize)
        self.spatial.SetMinSize(textsize)
        self.checkbox_1.SetValue(1)
        self.crystal.SetMinSize(textsize)
        self.crystal.SetSelection(-1)
        self.res.SetMinSize(textsize)
        self.lsfit.SetMinSize(textsize)
        self.strong.SetMinSize(textsize)
        self.twin.SetMinSize(textsize)
        self.boxvol.SetMinSize(textsize)
        self.advanceinput.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.advanceinput.SetForegroundColour(wx.Colour(76, 76, 76))
        
        self.advanceinput.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Arial"))
      
 
        
        self.findruns.SetBackgroundColour(wx.Colour(249, 249, 248))
        self.findruns.SetForegroundColour(wx.Colour(76, 76, 76))
        self.findruns.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Arial"))
        
        self.Integrate.SetBackgroundColour(wx.Colour(249, 249, 248))
        self.Integrate.SetForegroundColour(wx.Colour(76, 76, 76))
        self.Integrate.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Arial"))
        
        self.stop.SetBackgroundColour(wx.Colour(249, 249, 248))
        self.stop.SetForegroundColour(wx.Colour(76, 76, 76))
        self.stop.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Arial"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainSaint.__do_layout
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_15_staticbox.Lower()
        sizer_15 = wx.StaticBoxSizer(self.sizer_15_staticbox, wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(5, 2, 0, 0)             #changed from 10 to 5 for macosx
        self.sizer_11_staticbox.Lower()
        sizer_11 = wx.StaticBoxSizer(self.sizer_11_staticbox, wx.HORIZONTAL)
        self.sizer_4_copy_staticbox.Lower()
        sizer_4_copy = wx.StaticBoxSizer(self.sizer_4_copy_staticbox, wx.HORIZONTAL)
        self.sizer_10_staticbox.Lower()
        sizer_10 = wx.StaticBoxSizer(self.sizer_10_staticbox, wx.HORIZONTAL)
        self.sizer_4_staticbox.Lower()
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.HORIZONTAL)
        self.sizer_5_staticbox.Lower()
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.HORIZONTAL)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        self.sizer_1_copy_staticbox.Lower()
        sizer_1_copy = wx.StaticBoxSizer(self.sizer_1_copy_staticbox, wx.HORIZONTAL)
        self.sizer_2_staticbox.Lower()
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        self.sizer_1_staticbox.Lower()
        sizer_1 = wx.StaticBoxSizer(self.sizer_1_staticbox, wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9.Add(self.list_box_1, 1, wx.EXPAND, 0)
        sizer_8.Add(sizer_9, 0, wx.EXPAND, 0)
        sizer_1.Add(self.p4p, 0, 0, 0)
        sizer_1.Add(self.browsep4p, 1, 0, 0)
        grid_sizer_1.Add(sizer_1, 2, 0, 0)
        sizer_2.Add(self.x, 0, wx.RIGHT, 7)
        sizer_2.Add(self.y, 0, wx.RIGHT, 7)
        sizer_2.Add(self.z, 0, 0, 7)
        grid_sizer_1.Add(sizer_2, 1, 0, 0)
        sizer_1_copy.Add(self.spatial, 1, 0, 0)
        sizer_1_copy.Add(self.browsespatial, 0, 0, 0)
        grid_sizer_1.Add(sizer_1_copy, 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_1, 0, wx.RIGHT | wx.TOP, 12)
        sizer_3.Add(self.crystal, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_3, 0, 0, 0)
        sizer_5.Add(self.res, 0, 0, 0)
        grid_sizer_1.Add(sizer_5, 1, 0, 0)
        sizer_4.Add(self.lsfit, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_4, 1, 0, 0)
        sizer_10.Add(self.strong, 0, 0, 0)
        grid_sizer_1.Add(sizer_10, 1, 0, 0)
        sizer_4_copy.Add(self.twin, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(sizer_4_copy, 0, 0, 0)
        sizer_11.Add(self.boxvol, 0, 0, 0)
        grid_sizer_1.Add(sizer_11, 1, 0, 0)
        sizer_13.Add(grid_sizer_1, 7, wx.EXPAND, 0)
        sizer_15.Add(self.advanceinput, 1, wx.EXPAND, 0)
        sizer_13.Add(sizer_15, 2, wx.EXPAND, 0)
        sizer_14.Add(self.findruns, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_14.Add(self.Integrate, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_14.Add(self.stop, 0, wx.LEFT | wx.RIGHT | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 10)
        sizer_13.Add(sizer_14, 1, wx.EXPAND, 0)
        sizer_12.Add(sizer_13, 1, wx.EXPAND, 0)
        sizer_8.Add(sizer_12, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_8, 2, wx.EXPAND, 0)
        sizer_7.Add(self.text_ctrl_1, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_6)
        self.SetSizerAndFit(sizer_6)

        self.Layout()
        self.Center()
        self.CenterOnScreen()


        

    def onBrowse2(self, event):  # wxGlade: MainSaint.<event_handler>
        filters = 'All files (*.*)|*.*'
        dialog = wx.FileDialog( self, "Choose a file",  self.dirnameall, wildcard = filters, style = wx.FD_OPEN | wx.MULTIPLE )
        if dialog.ShowModal() == wx.ID_OK:
            selected = dialog.GetFilename()
            # print selected
            dirnameall=dialog.GetDirectory()
            if os.path.exists(os.path.join(dirnameall,selected))==True: 
                self.spatial.SetValue(os.path.join(dirnameall,selected))
    def gensaintini(self):
        saintini=open(os.path.join(self.dirnameall,"saintinput.ini"), 'w')
        p4pfile=self.p4p.GetValue()
        x=self.x.GetValue()
        y=self.y.GetValue()
        z=self.z.GetValue()
        spatial=self.spatial.GetValue()
        boxref=self.checkbox_1.GetValue() 
        crystalsys=self.crystal.GetValue()
        resol=self.res.GetValue()
        lsfitv=self.lsfit.GetValue()
        stronv=self.strong.GetValue()
        twinv=self.twin.GetValue()
        boxvolv=self.boxvol.GetValue()
        advance=self.advanceinput.GetValue()
        runs=self.list_box_1.GetCheckedStrings()
        run=",".join(runs)
        saintini.writelines(str(p4pfile+'\n'+x+'\n'+y+'\n'+z+'\n'+spatial+'\n'+str(boxref)+'\n'+crystalsys+'\n'+resol+'\n'+lsfitv+'\n'+stronv+'\n'+twinv+'\n'+boxvolv+'\n'+advance+'\n'+str(run)+'\n'))
        saintini.close()
    def stripzero(self, l):
        return [x for x in l if x]
    def onBrowse(self, event):  # wxGlade: MainSaint.<event_handler> 
        filters = 'P4P file (*.p4p)|*.p4p| All files (*.*)|*.*'
        dialog = wx.FileDialog( self, "Choose a file",  self.dirnameall, wildcard = filters, style = wx.FD_OPEN | wx.MULTIPLE )
        if dialog.ShowModal() == wx.ID_OK:
            selected = dialog.GetFilename()            
            dirnameall=dialog.GetDirectory()
            self.dirnameall=dirnameall
            if os.path.exists(os.path.join(dirnameall,selected))==True: 
                self.p4p.SetValue(os.path.join(dirnameall,selected))
                pforp=open(os.path.join(dirnameall,selected), 'r').readlines()
                for line in pforp:
                    if "BRAVAIS" in line:
                        brav=self.stripzero(line.split(" "))
                        self.spcg=brav[1]
                        self.brl=brav[2]
                saintl = {'P':0, 'A':1, 'B':2, 'C':3, 'F':4,  'I':5, 'R':6}
                crystalsystem={'Triclinic':'-1', 'Monoclinic':'2/m', 'Orthorhombic':'mmm','Tetragonal':'4/m','Tetragonal':'4/mmm','Trigonal':'-3','Trigonal':'-3m','Hexagonal':'6/m','Hexagonal':'6/mmm','Cubic':'m-3','Cubicm':'-3m'}
                self.latice=saintl[self.brl]
#                crystalsys=crystalsystem[self.spcg]
                if os.path.exists(os.path.join(dirnameall,"saintinput.ini")):
                    # print os.path.join(dirnameall,"saintinput.ini")
                    saint=open(os.path.join(dirnameall,'saintinput.ini'), 'r')
                    saintini=saint.readlines()
                    p4pfile=saintini[0].replace('\n','')
                    x=saintini[1].replace('\n','')
                    y=saintini[2].replace('\n','')
                    z=saintini[3].replace('\n','')
                    spatial=saintini[4].replace('\n','')
                    boxref=str(saintini[5].replace('\n',''))
#                    crystalsys=saintini[6].replace('\n','')
                    resol=saintini[7].replace('\n','')
                    lsfitv=saintini[8].replace('\n','')
                    stronv=saintini[9].replace('\n','')
                    twinv=saintini[10].replace('\n','')
                    boxvolv=saintini[11].replace('\n','')
                    advance=saintini[12].replace('\n','')
                    self.old=advance
                    self.dirname=saintini[13].replace('\n','')
                    runs=saintini[14].replace('\n','')
                    self.x.SetValue(x)
                    self.y.SetValue(y)
                    self.z.SetValue(z)
                    self.spatial.SetValue(spatial)
                    self.checkbox_1.SetValue(bool(boxref))
#                    self.crystal.SetStringSelection(crystalsys)
                    self.res.SetValue(resol)
                    if boxref=="True":
                       self.checkbox_1.SetValue(1)
                       boxref="N"
                    else:
                       self.checkbox_1.SetValue(2)
                       boxref="Y"
                    self.lsfit.SetValue(lsfitv)
                    self.strong.SetValue(stronv)
                    self.twin.SetValue(twinv)
                    self.boxvol.SetValue(boxvolv)
                    self.advanceinput.SetValue(advance)
                    run=runs.split(",")
                    self.list_box_1.Clear()
                    # print run
                    for i in run:
                         self.list_box_1.Append(i)
                                        
                    self.list_box_1.SetChecked(range(len(run)))
                    start=run[0].split("_")[1]
                    end=run[-1].split("_")[1]
                    # print run[0]
                    # print run[-1]
                    run=",".join(run)
                    framesc=self.countruns(event)
                    framesc=",".join(framesc)
                    sfrm=os.path.join(self.dirname, runs[0].split("_")[0]+"_"+"["+start+"-"+end+"]"+"_"+"0001.sfrm")
                    raw=os.path.join(self.dirnameall,runs[0].split("_")[0]+"_"+"["+start+"-"+end+"]"+".raw")
                    outputma=os.path.join(self.dirnameall,runs[0].split("_")[0]+"_0m._ma")
                    outputpar=os.path.join(self.dirnameall, runs[0].split("_")[0]+"_g.p4p")
                    outputls=os.path.join(self.dirnameall,runs[0].split("_")[0]+"_0m._ls")
                    inside="G\n"+"I\n"+outputma+"\n"+"O\n"+outputpar+"\n"+"L\n"+outputls+"\n"+"Q\n"+"I\n"+"I\n"+sfrm+"\n"+"M\n"+p4pfile+"\n"+"#\n"+"-3\n"+"N\n"+framesc+"\n"+"U\n"+resol+"\n"+"C\n"+spatial+"\n"+"P\n"+"-1\n"+"0\n"+"R\n"+raw+"\n"+"S\n"+x+"\n"+y+"\n"+z+"\n"+"H\n"+stronv+"\n"+"A\n"+"V\n"+boxvolv+"\n"+"\n"+"S\n"+"2\n"+twinv+"\n"+"\n"+"L\n"+lsfitv+"\n"+"\n"+"Q\n"+"!\n"+"\n"+"E\n"+"Y\n"+"Y\n"+"Y\n"
                    advance=inside.replace("\n","Enter")
                    self.advanceinput.SetValue(advance)
                else: 
                    self.gensaintini()
                   
    def countruns(self,event):
        get=self.list_box_1.GetCheckedStrings()
        # print get 
        count=[]
        for items in get:
            x=0
            i=items.split("_")[0]+"_"+items.split("_")[1]
            for files in os.listdir(self.dirname):
                   if i in files:
                      x+=1
            # print x
            count.append(str(x))    
        return count
    def sortkey(self, string):    
        return tuple(int(num) if num else alpha for num, alpha in (re.compile(r'(\d+)|(\D+)').findall)(string))
    def onfindruns(self, event):  # wxGlade: MainSaint.<event_handler>
        runs=[]
#        wx.FileDialog( self, "Choose a file",  self.dirnameall, wildcard = filters, style = wx.FD_OPEN | wx.MULTIPLE )
        dialog = wx.DirDialog(self, "Choose sfrm directory:",  self.dirnameall, style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.list_box_1.Clear()
            selected = dialog.GetPath()
            self.dirname=selected
            for files in os.listdir(selected):
                if files.endswith("0001.sfrm"):
                   runs.append(files)
        sorrun=sorted(runs, key=self.sortkey)
#        # print sorrun
        for i in sorrun:
             self.list_box_1.Append(i)
        self.list_box_1.SetChecked(range(len(runs)))
    def onstop(self, event):  # wxGlade: MainSaint.<event_handler>
        self.shell.kill()
    def check(self, event, old): 
        advance=self.advanceinput.GetValue()
        if not len(advance)==len(old):
            return True
        else:
            return False
        
    def onintegrate(self, event):  # wxGlade: MainSaint.<event_handler>  
        p4pfile=self.p4p.GetValue()
        x=self.x.GetValue()
        y=self.y.GetValue()
        z=self.z.GetValue()
        spatial=self.spatial.GetValue()
        boxref=self.checkbox_1.GetValue() 
        crystalsys=self.crystal.GetValue()
        resol=self.res.GetValue()
        lsfitv=self.lsfit.GetValue()
        stronv=self.strong.GetValue()
        twinv=self.twin.GetValue()
        boxvolv=self.boxvol.GetValue()
        advance=self.advanceinput.GetValue()
        runs=self.list_box_1.GetCheckedStrings()
        start=runs[0].split("_")[1]
        end=runs[-1].split("_")[1]
        run=",".join(runs)
        framesc=self.countruns(event)  
        if os.path.exists(p4pfile)==True: 
                pforp=open(p4pfile, 'r').readlines()
                for line in pforp:
                    if "BRAVAIS" in line:
                        brav=self.stripzero(line.split(" "))
                        self.spcg=brav[1]
                        self.brl=brav[2]
        saintl = {'P':0, 'A':1, 'B':2, 'C':3, 'F':4,  'I':5, 'R':6}
        crystalsystem={'Triclinic':'-1', 'Monoclinic':'2/m', 'Orthorhombic':'mmm','Tetragonal':'4/m','Tetragonal':'4/mmm','Trigonal':'-3','Trigonal':'-3m','Hexagonal':'6/m','Hexagonal':'6/mmm','Cubic':'m-3','Cubicm':'-3m'}
        self.latice=saintl[self.brl]
        framesc=",".join(framesc)
        sfrm=os.path.join(self.dirname, runs[0].split("_")[0]+"_"+"["+start+"-"+end+"]"+"_"+"0001.sfrm")
        raw=os.path.join(self.dirnameall,runs[0].split("_")[0]+"_"+"["+start+"-"+end+"]"+".raw")
        outputma=os.path.join(self.dirnameall,runs[0].split("_")[0]+"_0001._ma")
        outputpar=os.path.join(self.dirnameall, runs[0].split("_")[0]+"_000g.p4p")
        outputls=os.path.join(self.dirnameall,runs[0].split("_")[0]+"_0001._ls")
        # print outputma, outputpar, outputls, sfrm, p4pfile, crystalsys.split, str(self.latice), framesc, resol, spatial, raw, stronv, twinv, lsfitv
        #inside="G\n"+"I\n"+outputma+"\n"+"O\n"+outputpar+"\n"+"L\n"+outputls+"\n"+"Q\n"+"I\n"+"I\n"+sfrm+"\n"+"M\n"+p4pfile+"\n"+"P\n"+crystalsys.split(":")[1]+"\n"+str(self.latice)+"\n"+"#\n"+"-3\n"+"N\n"+framesc+"\n"+"U\n"+resol+"\n"+"C\n"+spatial+"\n"+"R\n"+raw+"\n"+"S\n"+x+"\n"+y+"\n"+z+"\n"+"H\n"+stronv+"\n"+"A\n"+"V\n"+boxvolv+"\n"+"\n"+"S\n"+"2\n"+twinv+"\n"+"\n"+"L\n"+lsfitv+"\n"+"\n"+"Q\n"+"!\n"+"\n"+"E\n"+"Y\n"+"Y\n"+"Y\n"
        inside="G\n"+"I\n"+outputma+"\n"+"O\n"+outputpar+"\n"+"L\n"+outputls+"\n"+"Q\n"+"I\n"+"I\n"+sfrm+"\n"+"M\n"+p4pfile+"\n"+"#\n"+"-3\n"+"N\n"+framesc+"\n"+"U\n"+resol+"\n"+"C\n"+spatial+"\n"+"P\n"+"-1\n"+"0\n"+"R\n"+raw+"\n"+"S\n"+x+"\n"+y+"\n"+z+"\n"+"H\n"+stronv+"\n"+"A\n"+"V\n"+boxvolv+"\n"+"\n"+"S\n"+"2\n"+twinv+"\n"+"\n"+"L\n"+lsfitv+"\n"+"\n"+"Q\n"+"!\n"+"\n"+"E\n"+"Y\n"+"Y\n"+"Y\n"
        advance=inside.replace("\n","Enter")
        if os.path.exists(os.path.join(self.dirnameall,"saintinput.ini"))==True:
            saintini=open(os.path.join(self.dirnameall,"saintinput.ini"), 'r').readlines()
            old=saintini[12].replace('\n','')
            cheched=self.check(event,old)
            if cheched==True:
                inside=advance.replace("Enter", "\n")
            elif cheched==False:
                inside=inside
            
        saintini=open(os.path.join(self.dirnameall,"saintinput.ini"), 'w')
        saintini.writelines(str(p4pfile+'\n'+x+'\n'+y+'\n'+z+'\n'+spatial+'\n'+str(boxref)+'\n'+crystalsys+'\n'+resol+'\n'+lsfitv+'\n'+stronv+'\n'+twinv+'\n'+boxvolv+'\n'+advance+'\n'+self.dirname+'\n'+run+'\n'))
        saintini.close()
        os.chdir(self.dirnameall)
        self.shell = subprocess.Popen([self.phtosaint], bufsize=0,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        self.shell_thread = threading.Thread(target=self.read_shell_output)
        self.shell_thread.start()
        self.Connect(-1, -1, EVT_CHARACTER_ID, self.on_result)
        self.shell.stdin.write(inside)
        self.advanceinput.SetValue(advance)
  
 
    def read_shell_output(self):
      while True:
         output = self.shell.stdout.readline()
         if not len(output)==3:
            if not len(output)==2:
                if output == '':
                    break
                wx.PostEvent(self, CharacterEvent(output))

    def on_result(self, event):
        self.text_ctrl_1.AppendText(event.character)
