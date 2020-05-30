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
import webbrowser 
global ossystem
ossystem=sys.platform
class Bang(wx.Dialog):
    def __init__(self, path, dirname, fnoe, filenamenoext):
        wx.Dialog.__init__(self, None, -1, 'Bonds and angles', style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER  )
        self.dirname=dirname
        self.fnoe=fnoe
        
        self.filenamenoext=filenamenoext
        self.path=path    
        self.text_ctrl1 = wx.TextCtrl(self, -1, "")
        self.text_ctrl1.SetFocus()
        self.radio_btn_1 = wx.RadioButton(self, -1, "Html table")
        self.radio_btn_2 = wx.RadioButton(self, -1, "List")
        self.OK = wx.Button(self, -1, "Ok")
#        self.info = wx.Button(self, -1, "Ok")
        self.label_1 = wx.StaticText(self, wx.ID_ANY, ("If no atom selected, then all bonds and angles will be listed. You can exclude bonds from report by applying a filter. For example, Ni1/N1 P1 O1. Bonds and angles to N1 P1 O1 atoms will be omited. In batch mode click OK to create a table, or click Cancel to move to the next structure"))
        self.button_2 = wx.Button(self, wx.ID_CANCEL, "Cancel")
        self.Bind(wx.EVT_BUTTON, self.ONOK, self.OK)
        self.__set_properties()
        
        self.__do_layout()
        # end wxGlade
 
    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties        
        displays = (wx.Display(i) for i in range(wx.Display.GetCount()))
        sizes = [display.GetGeometry().GetSize() for display in displays]
        displaySize=sizes[0].Get()
        xres,yres= (displaySize[0]/1.2, displaySize[1]/1.2)
        
        # begin wxGlade: MainSaint.__set_properties
        if ossystem.startswith("win"):
           buttonsize=(xres/33*xres/yres,yres/33)
           textsize=(xres/10*xres/yres,yres/33)
        elif ossystem.startswith("lin"):
           buttonsize=(xres/33*xres/yres,yres/33)
           textsize=(xres/10*xres/yres,yres/33)
        elif ossystem.startswith("darwin"):
           buttonsize=(xres/33*xres/yres,yres/33)
           textsize=(xres/10*xres/yres,yres/33)
        else:
            buttonsize=(xres/33*xres/yres,yres/33)
            textsize=(xres/10*xres/yres,yres/33)
        self.SetTitle("Choose an atom")
        self.SetSize((xres/6*xres/yres, yres/4))
        self.SetMinSize((315, 250))
        self.text_ctrl1.SetMinSize((379, 30))
        self.radio_btn_1.SetMinSize((150, 30))
        self.radio_btn_1.SetValue(True)
        self.radio_btn_2.SetMinSize((107, 30))
        self.label_1.SetMinSize((xres/6.5*xres/yres, yres/5))

        self.text_ctrl1.SetMinSize((250, 35))
        # end wxGlade
    
    def __do_layout(self):
        xres,yres= wx.DisplaySize()
        # begin wxGlade: MyFrame1.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.text_ctrl1, 0, wx.LEFT | wx.RIGHT | wx.TOP | wx.EXPAND, 3)
        sizer_4.Add(self.radio_btn_1, 1, wx.LEFT, 10)
        sizer_4.Add(self.radio_btn_2, 1, wx.LEFT | wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_1, 1, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND, yres/180)
        sizer_5.Add(self.OK, 1, wx.ALL, 5)
        sizer_5.Add((89, 30), 0, 0, 0)
        sizer_5.Add(self.button_2, 1, wx.ALL, 5)
        sizer_3.Add(sizer_5, 0, wx.BOTTOM | wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        self.SetSizerAndFit(sizer_2)

        self.Layout()
        # end wxGlade
        # end 
    def ONOK(self, event):
        if os.path.exists(os.path.join(self.dirname,'publish.cif'))==True: 
            valueb2=self.radio_btn_1.GetValue()
            valueb1=self.radio_btn_2.GetValue()
            if valueb1==True:
                self.ontext(event)
            elif valueb2==True:
                self.htmltable(event)
        elif os.path.exists(self.fnoe+'.cif')==True: 
            valueb2=self.radio_btn_1.GetValue()
            valueb1=self.radio_btn_2.GetValue()
            if valueb1==True:
                self.ontext(event)
            elif valueb2==True:
                self.htmltable(event)
        else:
             wx.MessageBox(self.fnoe+'.cif file was not found', 'Error', wx.OK | wx.ICON_INFORMATION)
    def ontext(self, event):    
        b,a=(self.onBA(event))
        result=', '.join(b)+"; "+', '.join(a)
        self.dataObj = wx.TextDataObject()
        self.dataObj.SetText(result)
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(self.dataObj)
            wx.TheClipboard.Close()
            dlg = wx.MessageDialog(self, "The following data was copied to clipboard:   "+result   ,
                                'Data was copied to clipboard', wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy() 
        else:
            showd = wx.MessageDialog(self, result, "Unable to open the clipboard", "Error", wx.OK | wx.ICON_INFORMATION)
            showd.ShowModal()
   
        
        
    def onBA(self, event): 
        inatom=self.text_ctrl1.GetValue()+" "
        if "/" in inatom:
            inatom=inatom.split("/")[0]
        else:
            inatom=inatom
        listnumber=[]
        loops=[]
        loshrink=[]
        listofbonds=[]
        listofangels=[]
        if os.path.exists(os.path.join(self.dirname,'publish.cif'))==True: 
            firstf=open(os.path.join(self.dirname,'publish.cif'),'r')
            first=firstf.readlines()
            firstf.close()
        elif os.path.exists(self.fnoe+'.cif')==True: 
            firstf=open(self.fnoe+'.cif','r')
            first=firstf.readlines()
            firstf.close()
        for number, line in enumerate(first):
            if line.startswith(" _geom_bond_publ_flag"):
                listnumber.insert(0,number)
            elif line.startswith(" _geom_angle_publ_flag"):
                listnumber.insert(1,number)
            elif line.startswith("loop_"):
                loops.append(number)
#              # # printloops, listnumber
        for loo in loops:
           for x in listnumber:
                if int(loo)>=int(x):
                    loshrink.append(loo)
        if len(loshrink)<2:
            showd = wx.MessageDialog(self, "Torsion angles were not found in cif (publish.cif) file. Would you like to proceed anyway?", "Error", wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
            answ=showd.ShowModal()
            if answ == wx.ID_YES:
                showd.Destroy()
                getbonds=first[(listnumber[0]+1):loshrink[0]]
                getangels=first[(listnumber[1]+1):]
        elif len(loshrink)>=2:
            getbonds=first[(listnumber[0]+1):loshrink[0]]
            getangels=first[(listnumber[1]+1):loshrink[1]]
        revbond=[]
        revangels=[]
#        # print getbonds
        for itemb in getbonds:
            if len(itemb)>3:
                if len(inatom.replace(" ",""))==0:
#                   # print (itemb.replace(".?","")).split(' ')[0]+"-"+(itemb.replace(".?","")).split(' ')[1]+" = "+(itemb.replace(".?","")).split(' ')[2]
                   revbond.append((itemb.replace(".?","")).split(' ')[0]+"-"+(itemb.replace(".?","")).split(' ')[1]+" = "+(itemb.replace(".?","")).split(' ')[2])
                else:
                   if inatom in itemb:
                      revbond.append((itemb.replace(".?","")).split(' ')[0]+"-"+(itemb.replace(".?","")).split(' ')[1]+" = "+(itemb.replace(".?","")).split(' ')[2])
           
        for itema in getangels:
            if len(itema)>3:
                if len(inatom.replace(" ",""))==0:
                    revangels.append((itema.replace(".?","")).split(' ')[0]+"-"+(itema.replace(".?","")).split(' ')[1]+"-"+(itema.replace("..?","")).split(' ')[2]+" = "+(itema.replace("..?","")).split(' ')[3])
                else:
                    if inatom in itema:
                       revangels.append((itema.replace(".?","")).split(' ')[0]+"-"+(itema.replace(".?","")).split(' ')[1]+"-"+(itema.replace("..?","")).split(' ')[2]+" = "+(itema.replace("..?","")).split(' ')[3])
        revbonds=self.sortbyfirst(event, revbond)
        return (revbonds, revangels)
    def sortbyfirst(self, event, revbonds):
        inatom=self.text_ctrl1.GetValue()
        if not "/" in inatom:
           inatom=inatom
        else:
           inatom=inatom.split("/")[0]
        bonds=revbonds
        bons=[]
        angs=[]
        for i in bonds:
            ifirst=i.split("=")[0]
            isecond=i.split("=")[1]
            if ifirst.startswith(inatom):
                bons.append(i)
            else:
                zero=ifirst.split("-")[0]
                one=ifirst.split("-")[1]
                ifirst=one.strip()+"-"+zero.strip()
                ibons=ifirst+"="+isecond
                bons.append(ibons)
#        for a in angls:
#            afirst=a.split("=")[0]
#            asecond=a.split("=")[1]
#            if afirst.endswith(inatom+" "):
#                azero=afirst.split("-")[0]
#                aone=afirst.split("-")[1]
#                atwo=afirst.split("-")[2]
#                afirst=atwo.strip()+"-"+one.strip()+"-"+zero.strip()
#                # print afirst
#                angels=afirst+"="+asecond
#                angs.append(angels) 
#            else:
#                # print a
#                angs.append(a)
        return bons   
            
    def filter(self, event):
        b,a=self.onBA(event)
        newangles=[]
        newbonds=[]
        inatom=self.text_ctrl1.GetValue()+" "
        if "/" in inatom:
           # print "inatome ==========", inatom.split("/")
           fil=inatom.split("/")[1]
           fil=fil.split(" ")
           fil=filter(None, fil) 
#           newbonds=[bond for bond in b for f in fil if f in bond] 
           for f in fil:
                for bond in b:
                    if f in bond:
                        newbonds.append(bond)
           b = [x for x in b if x not in newbonds]
                     
           for fa in fil:
                for ang in a:
                    if fa in ang:
                        newangles.append(ang)
           # print newangles
           a = [x for x in a if x not in newangles]
           # print "angles", a   
           return (b, set(a))
        else:
           return (b, a)
    
    def htmltable(self, event):
#        self.webpage=self.dirnameslash+'htmltable.htm'
        b,a=self.filter(event)
       # # printb,a
        listb=[]
        lista=[]
        for item in b:
            listb.append(item.split("="))
        for item in a:
            lista.append(item.split("="))
        import HTML
        htmlcodeb = HTML.table(listb+lista)
#        # print self.fnoe
        start='''<html><body><center><H3> Selected Bond Distances (&#8491) and Angles (deg) for Compound  '''+ str(self.filenamenoext) +'''</H3>'''
        end='''</center></body></html>'''
        htmltable=start+htmlcodeb+end
        table=open(os.path.join(self.dirname, "bonds_angles_"+self.filenamenoext+".htm"),'w')
        table.writelines(htmltable)
        table.close()
        dlg = wx.MessageDialog(self, "The table was saved as :   "+os.path.join(self.dirname,"bonds_angles_"+self.filenamenoext+".htm"+"  Do you want to open it?")   ,
                                'Html Table', wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
        result=dlg.ShowModal()
        dlg.Destroy() 
      
#        dialog=wx.MessageDialog(self,"This will update Linxtl. Would you like to proceed? It might take some time, depending on the speed of your internet connection.","Update?",wx.YES_NO | wx.CANCEL | wx.ICON_QUESTION)
#        dialog.Centre()
#        result=dialog.ShowModal()
#        dialog.Destroy()
        if result == wx.ID_YES:
            if ossystem.startswith("win"):
                os.chdir(self.dirname)
                webbrowser.open('file://%s' % os.path.join(self.dirname,"bonds_angles_"+self.filenamenoext+".htm"))
            elif ossystem.startswith("darwin"):
                os.chdir(self.dirname)
                webbrowser.open('file://%s' % os.path.join(self.dirname,"bonds_angles_"+self.filenamenoext+".htm"))  
            else:
                os.chdir(self.dirname)
                webbrowser.open('file://%s' % os.path.join(self.dirname,"bonds_angles_"+self.filenamenoext+".htm"))
                #webbrowser.open('publish.html')
    #        webbrowser.open(os.path.join(self.dirname,"bonds_angles_"+self.filenamenoext+".htm"))

