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
import os, sys, tarfile 
import sqlite3
global path
path = sys.path[0]
 
def getinfocif(ids,filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number,cname, Z, wavelength, R, publisher, pubyear, pubvolume, pubpgfirst, pubpglast, maindirname):
        database = sqlite3.connect(os.path.join(maindirname,"STRUCTURAL_DATABASE.db")) # or use :memory: to put it in RAM
        cursor = database.cursor()
        cursor.execute('''CREATE TABLE structures
                      (ids, filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number,
                       cname, Z, wavelength, R, publisher, pubyear, pubvolume, pubpgfirst, pubpglast)''')
        database.commit()
        cifs=getcifs(maindirname)
        # print dir
        ids=1
#        print ("reads",cifs)
        for filename in cifs:
            
            dir_=os.path.dirname(filename)
            relDir = os.path.relpath(dir_, maindirname)
            tmp = open(filename,'r')
            temp=tmp.readlines()
            tmp.close()
            filelink=os.path.join(relDir, os.path.basename(filename))
            for i, cifline in enumerate(temp):
                cifline=cifline.replace("\r","").replace("\n","")
                if cifline.startswith("_chemical_formula_sum"):
                    if len(((cifline).replace("_chemical_formula_sum","")).replace(" ",""))<2:
                       formula=(temp[i+1]).replace("\r","").replace("\n","")
                    else:
                       formula=((cifline).replace("_chemical_formula_sum","")).replace(" ","")
                if cifline.startswith("_cell_length_a"):
                    ca=((cifline).replace("_cell_length_a","")).replace(" ","")
                if cifline.startswith("_cell_length_b"):
                    cb=((cifline).replace("_cell_length_b","")).replace(" ","")
                if cifline.startswith("_cell_length_c"):
                    cc=((cifline).replace("_cell_length_c","")).replace(" ","")
                if cifline.startswith("_cell_angle_alpha"):
                    alpha=((cifline).replace("_cell_angle_alpha","")).replace(" ","")
                if cifline.startswith("_cell_angle_beta"):
                    beta=((cifline).replace("_cell_angle_beta","")).replace(" ","")
                if cifline.startswith("_cell_angle_gamma"):
                    gamma=((cifline).replace("_cell_angle_gamma","")).replace(" ","")
                if cifline.startswith("_cell_volume"):
                    volume=((cifline).replace("_cell_volume","")).replace(" ","")
                if cifline.startswith("_space_group_crystal_system"):
                    csystem=((cifline).replace("_space_group_crystal_system","")).replace(" ","")
                if cifline.startswith("_symmetry_cell_setting"):
                    csystem=((cifline).replace("_symmetry_cell_setting","")).replace(" ","")
                if cifline.startswith("_space_group_IT_number"):
                    number=((cifline).replace("_space_group_IT_number","")).replace(" ","")
                if cifline.startswith("_symmetry_space_group_name_H-M"):
                    cname=((cifline).replace("_symmetry_space_group_name_H-M","")).replace(" ","")
                if cifline.startswith("_cell_formula_units_Z"):
                    Z=((cifline).replace("_cell_formula_units_Z","")).replace(" ","")
                if cifline.startswith("_diffrn_radiation_wavelength"):
                    wavelength=((cifline).replace("_diffrn_radiation_wavelength","")).replace(" ","")
                if cifline.startswith("_refine_ls_R_factor_all"):
                    R=((cifline).replace("_refine_ls_R_factor_all","")).replace(" ","")
                if cifline.startswith("_journal_name_full"):
                    publisher=((cifline).replace("_journal_name_full","")).replace(" ","")
                if cifline.startswith("_journal_year"):
                    pubyear=((cifline).replace("_journal_year","")).replace(" ","") 
                if cifline.startswith("_journal_volume"):
                    pubvolume=((cifline).replace("_journal_volume","")).replace(" ","")  
                if cifline.startswith("_journal_page_first"):
                    pubpgfirst=((cifline).replace("_journal_page_first","")).replace(" ","")  
                if cifline.startswith("_journal_page_last  "):
                    pubpglast=((cifline).replace("_journal_page_last","")).replace(" ","")  
          
            cursor.execute('''INSERT INTO structures (ids, filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number,
                               cname, Z, wavelength, R, publisher, pubyear, pubvolume, pubpgfirst, pubpglast) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
                              (ids,filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number,cname, Z, wavelength, R, publisher, pubyear, pubvolume, pubpgfirst, pubpglast))
#            print((ids,filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number,cname, Z, wavelength, R, publisher, pubyear, pubvolume, pubpgfirst, pubpglast))
            ids=ids+1
        database.commit()
        
#def openweb(self, event, htmfile):
#         webbrowser.open(htmfile)
def getcifs(maindirname):
        try: 
#            dlg = wx.DirDialog("Choose a directory with cif database:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
#            if dlg.ShowModal() == wx.ID_OK:
                try:
                    ciflist=[]
#                   
                    for dirpath, dirnames, filenames in os.walk(maindirname):
                        for filename in filenames:
                            if (filename.lower()).endswith(".cif"): 
                                    ciflist.append(os.path.join(dirpath, filename)) 
                except UnicodeEncodeError:
                    pass 
#                print ("scan",ciflist)
                return ciflist
        except OSError:
         pass
#getinfocif(ids,filelink, formula, ca, cb, cc, alpha, beta, gamma, volume, csystem, number,cname, Z, wavelength, R, publisher, folder)