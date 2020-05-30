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
import _thread
import subprocess
class SimpleSadabs(wx.Frame):
    def __init__(self,  event, parent,  path, dirname, fnoe, filenamenoext, phtosadabs):
#      self.path,  self.dirname, self.webpage, self.fnoe, self.filenamenoext
        xres,yres= wx.DisplaySize()
        si=(xres/4*xres/yres, yres/2)
        wx.Frame.__init__(self,  event, parent,  'SimpleSadabs', size=si)
        self.dirname=dirname
        self.fnoe=fnoe
        self.phtosadabs=phtosadabs
        self.filenamenoext=filenamenoext
        self.path=path   
        if not os.path.exists(self.phtosadabs):
                 askyesno = wx.MessageDialog( self, "Sadabs was not found. Please install sadabs. \n See Preference > External Programs for more details",  "file not found", wx.OK)
        self.InitUI()
        self.Center()
        self.CenterOnScreen()    
    def InitUI(self):
#        panel = wx.Panel(self, -1)
        
        self.fileinput = wx.TextCtrl(self, wx.ID_ANY, "")
        self.OPEN = wx.Button(self, wx.ID_ANY, ("Open"))
        self.sizer_3_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Input raw files"))
        self.hklfile = wx.TextCtrl(self, wx.ID_ANY, "")
        self.sizer_11_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Output"))
        self.num = wx.TextCtrl(self, wx.ID_ANY, "50")
        self.sizer_11_copy_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Number of Refinement Cycles"))
        self.list_box = wx.CheckListBox(self, choices=[], size=(160,200))  
        self.sizer_11_copy_1_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Batches"))
        self.r1 = wx.RadioButton(self, wx.ID_ANY, ("-1"))
        self.r2 = wx.RadioButton(self, wx.ID_ANY, ("2/m"))
        self.r3 = wx.RadioButton(self, wx.ID_ANY, ("mmm"))
        self.r4 = wx.RadioButton(self, wx.ID_ANY, ("4/m (Z unique)"))
        self.r5 = wx.RadioButton(self, wx.ID_ANY, ("4/mmm (Z unique)"))
        self.r6 = wx.RadioButton(self, wx.ID_ANY, ("-3 (Rhombohedral axes)"))
        self.r7 = wx.RadioButton(self, wx.ID_ANY, ("-3 (Z unique)"))
        self.r8 = wx.RadioButton(self, wx.ID_ANY, ("-3m (Rhombohedral axes)"))
        self.r9 = wx.RadioButton(self, wx.ID_ANY, ("-31m (Z unique)"))
        self.r10 = wx.RadioButton(self, wx.ID_ANY, ("-3m1 (Z unique)"))
        self.r11 = wx.RadioButton(self, wx.ID_ANY, ("6/m (Z unique)"))
        self.r12 = wx.RadioButton(self, wx.ID_ANY, ("6/mmm (Z unique)"))
        self.r13 = wx.RadioButton(self, wx.ID_ANY, ("m3"))
        self.r14 = wx.RadioButton(self, wx.ID_ANY, ("m3m"))
        self.r15 = wx.CheckBox(self, wx.ID_ANY, ("Graphite Monochromator"))
        self.r16 = wx.CheckBox(self, wx.ID_ANY, ("Silicon Monochromator"))
        self.muofrlabel =wx.StaticText(self, wx.ID_ANY, ("Spherical absorption correction Mu*r"))
        self.muofr = wx.TextCtrl(self, wx.ID_ANY, ("0.2"))
        self.r15.SetValue(True)
        self.r1.SetValue(True)
        self.run = wx.Button(self, wx.ID_ANY, ("Run"))
        self.close = wx.Button(self, wx.ID_ANY, ("Close"))
        self.sizer_9_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Laue Group"))
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer_9_staticbox.Lower()
        sizer_9 = wx.StaticBoxSizer(self.sizer_9_staticbox, wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(10, 2, 0, 0)
        sizer_10 = wx.BoxSizer(wx.VERTICAL)
        self.sizer_11_copy_1_staticbox.Lower()
        sizer_11_copy_1 = wx.StaticBoxSizer(self.sizer_11_copy_1_staticbox, wx.HORIZONTAL)
        self.sizer_11_copy_staticbox.Lower()
        sizer_11_copy = wx.StaticBoxSizer(self.sizer_11_copy_staticbox, wx.HORIZONTAL)
        self.sizer_11_staticbox.Lower()
        sizer_11 = wx.StaticBoxSizer(self.sizer_11_staticbox, wx.HORIZONTAL)
        self.sizer_3_staticbox.Lower()
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        sizer_3.Add(self.fileinput, 5, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.OPEN, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(sizer_3, 1,  wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10)
        sizer_11.Add(self.hklfile, 1, 0, 0)
        sizer_10.Add(sizer_11, 1, wx.EXPAND, 0)
        sizer_11_copy.Add(self.num, 1, 0, 0)
        sizer_10.Add(sizer_11_copy, 1, wx.EXPAND, 0)
        sizer_11_copy_1.Add(self.list_box, 1, wx.EXPAND, 0)
        sizer_10.Add(sizer_11_copy_1, 5, wx.EXPAND, 0)
        sizer_4.Add(sizer_10, 2, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 15)
        grid_sizer_1.Add(self.r1, 0, 0, 0)
        grid_sizer_1.Add(self.r2, 0, 0, 0)
        grid_sizer_1.Add(self.r3, 0, 0, 0)
        grid_sizer_1.Add(self.r4, 0, 0, 0)
        grid_sizer_1.Add(self.r5, 0, 0, 0)
        grid_sizer_1.Add(self.r6, 0, 0, 0)
        grid_sizer_1.Add(self.r7, 0, 0, 0)
        grid_sizer_1.Add(self.r8, 0, 0, 0)
        grid_sizer_1.Add(self.r9, 0, 0, 0)
        grid_sizer_1.Add(self.r10, 0, 0, 0)
        grid_sizer_1.Add(self.r11, 0, 0, 0)
        grid_sizer_1.Add(self.r12, 0, 0, 0)
        grid_sizer_1.Add(self.r13, 0, 0, 0)
        grid_sizer_1.Add(self.r14, 0, 0, 0)
        grid_sizer_1.Add(self.r15, 0, 0, 0)
        grid_sizer_1.Add(self.r16, 0, 0, 0)
        grid_sizer_1.Add(self.muofrlabel, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.muofr, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.run, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.close, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_9.Add(grid_sizer_1, 1,  wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10)
        sizer_4.Add(sizer_9, 3, wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 5, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.SetSizerAndFit(sizer_1)
        self.SetBackgroundColour(wx.Colour(245,245,245))
        self.Layout()
        self.Bind(wx.EVT_BUTTON, self.onrun, self.run)       
        self.Bind(wx.EVT_BUTTON, self.pforp, self.OPEN)
        self.Bind(wx.EVT_BUTTON, self.onclose, self.close)
    def onrun(self, event):
        rawfiles=self.list_box.GetChecked()
       
        if not len(rawfiles)<1:
           self.tst(event)
        else: 
            error = wx.MessageDialog(self, "No raw files found!",
                                   'Error', wx.OK | wx.ICON_ERROR)
            error.ShowModal()
            error.Destroy()

 
        
    def getvalues(self, event):
        buton=[self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8, self.r9, self.r10, self.r11, self.r12, self.r13, self.r14 ]
        monochromator=[self.r15, self.r16]
        scan=self.num.GetValue()
        raws=[]
        rawfiles=self.list_box.GetSelections()
        hklfile=self.hklfile.GetValue()
        muofr=self.muofr.GetValue()
        muofr=muofr.replace(' ', '')
        monoc=2
        for m, c in enumerate(monochromator):
#            print ("monocccccc", m, c.GetValue())
            if c.GetValue():
               monoc=m+2
        for n, b in enumerate(buton):
            if b.GetValue()==True:
               group=n+1
        for i in self.rawfiles:
            raws.append(os.path.join(self.choosen_dir,i)) 
        return hklfile, group, raws, monoc, muofr
           
     
    def sortkey(self, string):    
        return tuple(int(num) if num else alpha for num, alpha in (re.compile(r'(\d+)|(\D+)').findall)(string))   
        
    def pforp(self, event):
        filters = 'Bruker raw (*.raw)|*.raw|Sadabs file (*.sad)|*.sad'
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", filters, style = wx.FD_OPEN | wx.FD_MULTIPLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.choosen_dir=dlg.GetDirectory()
            fir=dlg.GetFilenames()
            name=fir[0]
            self.rawfiles=sorted(fir, key=self.sortkey) 
            self.list_box.Clear()
            self.fnoe=os.path.splitext(os.path.join(self.choosen_dir, name))[0]
            for i in self.rawfiles:
                self.list_box.Append(i)
            self.fileinput.SetValue(" ".join(self.rawfiles))  
            self.list_box.SetChecked(range(len(self.rawfiles)))
            self.hklfile.SetValue(self.fnoe+".hkl")
    def instruct(self, event):
        hklfile, laue, raw_files, monoc, muofr=self.getvalues(event)
        monoc=str(monoc)
        os.chdir(self.dirname)
        outabs=hklfile.replace(".hkl",".abs")
        laue=str(laue).replace(" ","")
        ps_files=hklfile.replace(".hkl","_sad.ps") 
        input = [('Expert mode \s\[.+\]:\s','Y'),
        ('Maximum number of reflections allowed (2000000):',''),
        ('Enter listing filename \s\[.+\]:\s',outabs),
        ('Enter Laue group number:\s',laue),
        ('Treat Friedel opposites as equivalent for parameter refinement (Y or N)','Y'),
        ('Use a centrosymmetric point group for error model and statistics','Y'),
        (' Enter name of HKLF 4 format file containing reference or native data to which',''),
        ('Enter filename ','\n'.join(["%s" % v for v in raw_files])),
        ('Select option\s\[.+\]:\s',"/"),
        ('Enter mean(I/sigma) threshold (must be positive)',""),
        ('Highest resolution for parameter refinement',"0.1"),
        ('Factor g for initial weighting scheme 0.04',""),
        ('Restraint esd for equal consecutive scale\s\[.+\]:\s',''),
        ('Apply angle of incidence correction N:\s',''),
        ('Answer the next question with say 3.0 to mask bad detector regions',''),
        ('Number of refinement cycles :\s','50'),
        ('Detector (D) or crystal (C) coordinates for spherical harmonics', ''),
        ('Suitable spherical harmonic orders are 4,1 for weak absorption', ''),
        ('Highest odd order for spherical harmonics', '3'),
        ('Marquardt damping factor [0.0001]', ''),
        ('Allow for crystal decomposition by B-value refinement', 'Y'),
        ('Linear (L) or quadratic (S) B-value dependence on frame number', 'L'),
        ('Apply face-indexed absorption corrections', 'N'), #maybe yes
        ('Repeat parameter refinement (R) or accept (A) ', ''),
        ('Apply extra linear correction to each reflection for radiation damage N', 'N'), #maybe yes
        ('High resolution limit ', ''), 
        ('|I-<I>|/su ratio for rejection', ''), 
        (' This is only used for rejections, not for final sigma(I) values 0.04', ''), 
        ('Repeat parameter refinement (P) or accept (A) ', ''),
        ('p for (gI)^p in error model 2.0', ''),
        ('Enter new value for g or <CR> to accept', ''),
        ('Repeat parameter refinement ', ''),
        ('Write Postscript diagnostic file (Y or N) ', ''),
        ('Enter name of Postscript file ', ''),
        ('Short (<21 chars) title for Postscript plots', ''),
        ('Spatial display of (I-<I>)/su greater than ', ''),
        ('Repeat (R), write unmerged .hkl (W), merged .hkl (M), .sca (S)', ''),
        ('Reflection output file ', hklfile),
        ('Mu*r of equivalent sphere for additional absorption correction 2', muofr),
        ('Apply lambda/2 correction (2) for a graphite monochromator or lambda/3 (3) for Ge or Si monochromator or no correction (0)  ', monoc), #need coorectio editor
        ('Repeat (R), write unmerged .hkl (W), merged .hkl (M), .sca (S)', ''),
        ('Expected', ''),
        ('Expected', '')
        ]
        return input
    def read_shell_output(self):
        import re
        max = 10
        # dlg = wx.ProgressDialog("Sadabs in Progress","Please wait for sadabs to finish", maximum = max, parent=self, style = wx.PD_CAN_ABORT
        #                         | wx.PD_APP_MODAL
        #                         | wx.PD_ELAPSED_TIME
        #                         | wx.PD_ESTIMATED_TIME
        #                         | wx.PD_REMAINING_TIME
        #                         )
        # count = 1
        runed=False
        while True:
            output =self.sadabs_run.stdout.readline()
            print(output)
            if not len(output)==3:
                if not len(output)==2:
                    if output == '':
                        break
            if re.search('Data to parameter ratio too low to',  output):
                    error = wx.MessageDialog(self, "Data to parameter ratio too low to determine scaling parameters!",
                               'Error', wx.OK | wx.ICON_ERROR)
                    error.ShowModal()
                    error.Destroy()
                    # dlg.Update(10)
            # if "Enter filename" in output:
                # count=count+1
                # dlg.Update(count)
            if re.search('Cell and Laue group inconsistent', output):  
                error = wx.MessageDialog(self, "Cell and Laue group inconsistent !",
                                   'Error', wx.OK | wx.ICON_ERROR)
                error.ShowModal()
                error.Destroy()
                # dlg.Update(10)
            if re.search("no reflections stored -aborting", output):
                    error = wx.MessageDialog(self, "no reflections stored -aborting !",
                        'Error', wx.OK | wx.ICON_ERROR)
                    error.ShowModal()
                    error.Destroy()
                    # dlg.Update(10)
            if re.search("or quit", output):
                if not runed:
                    # count=10
                    runed=True
                    # dlg.Update(count)
                    self.alldone()
                   
                
#            if  "Effective data to parameter ratio" in output  
    def tst(self, event):
        cmd=[]
        input =self.instruct(event)
        for expected, lines in input:
            cmd.append(lines)
        cmd="\n".join(cmd)
        if cmd:    
            self.sadabs_run = subprocess.Popen([self.phtosadabs], bufsize=0,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf8')
            self.sadabs_run.stdin.write(cmd)
            self.read_shell_output()

        #dlg.ShowModal()
        #dlg.Destroy()
    def onclose(self, event):
        self.Close()
    def alldone(self):
        info = wx.MessageDialog(self, "Sadabs has finished",
                                 'Done', wx.OK | wx.ICON_INFORMATION)
        info.ShowModal()
        info.Destroy()
