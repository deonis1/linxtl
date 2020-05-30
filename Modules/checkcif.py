#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GUI generated with help of wxGlade 0.6.3 on Thu Jan 14 23:40:49 2010
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
import wx
import sys, os
import re
import webbrowser
global ossystem
ossystem = sys.platform
from checkcifgui import checkcifgui
from cif_reader import cifread
import json

class Options(wx.Dialog):
    def __init__(self, parent, version, fnoe, dirname, path, text):
        wx.Dialog.__init__(self, parent, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.version = version
        self.fnoe = fnoe
        self.dirname = dirname
        self.path = path
        self.text = text
        self.userdir=os.path.join(self.path,"user")
        self.pattern = re.compile(r"^(^_)[_A-Za-z]{1,}[\s]{1,}['?\"?\w\d\/\s\.\-]{1,}")
        self.pcffile = self.fnoe + ".pcf"
        self.ciffile = self.fnoe + ".cif"
        self.publishcif = os.path.join(self.dirname, "publish.cif")
        self.publishtmp = os.path.join(self.dirname, "publish.tmp")
        userdir = os.path.join(self.path, "user")
        listusers = [f for f in os.listdir(userdir) if f.endswith(".cif")]
        listdev = [d for d in os.listdir(os.path.join(userdir, "device")) if d.endswith(".dev")]
        self.tmpfile = self.create_tmp_file()
        self.pcfr_dict = self.get_pcf_file()
        self.cif_class =  cifread(self.ciffile)

        if self.cif_class:
           self.cif_dict = self.cif_class.read_cif_file()
        else:
           wx.MessageBox( self.ciffile  + ' cif file was not found', 'Error',  wx.OK | wx.ICON_INFORMATION)

        self.dialog_value_dict = self.update_from_pcf(self.pcfr_dict)
        self.dialog_value_dict["_space_group_crystal_system"] = self.cif_dict["_space_group_crystal_system"]

        self.dialog_value_dict["user"] = 0
        self.dialog_value_dict["userlist"] = listusers
        self.dialog_value_dict["dev"] = listdev
        self.dialog_value_dict["dev_default"] = "default.dev"
        if self.tmpfile:
            self.dialog_value_dict["user"] = self.tmpfile["user"]
            self.dialog_value_dict["dev_default"] = self.tmpfile["dev_default"].replace("'", "")

        if  self.get_full_spc_from_cif():
            self.dialog_value_dict["_space_group_name_Hall"] =  self.get_full_spc_from_cif()
        self.cifgui = checkcifgui(parent, version, fnoe, dirname, path, text)
        self.cifgui.Bind(wx.EVT_BUTTON, self.create_report, self.cifgui.okay)
        self.cifgui.set_values(self.dialog_value_dict)
        self.cifgui.Show()

    def get_full_spc_from_cif(self):
        hall_gp = False
        if "_space_group_name_Hall" in self.cif_dict:
           hall_gp = (self.cif_dict["_space_group_name_Hall"]).replace("'","").replace('"','')
        return hall_gp

    def create_tmp_file(self):
        if not os.path.exists(os.path.join(self.dirname, "lin.json")):
            tmpjson = {"_exptl_crystal_colour":"'Yellow'", "dev_default":"default.dev", "user":"user.cif" }
            with open(os.path.join(self.dirname, "lin.json"), "w") as tmp:
                 json.dump(tmpjson, tmp)
            tmpjson = False
        else:
             with open(os.path.join(self.dirname, "lin.json"), "r") as tmp:
                 tmpjson = json.load(tmp)
             return tmpjson

    def update_tmp_file(self, data):
            with open(os.path.join(self.dirname, "lin.json"), "w") as tmp:
                 json.dump(data, tmp)

    def update_dict(self,  d1, d2):
        d2.update(d1)
        return d2

    def savepcf_data(self, data):
        with open(self.fnoe + '.pcf', "w") as pcftosave:
            pcftosave.write(data)

    def get_pcf_file(self):
        if os.path.exists(os.path.join(self.path, "user", "device", self.pcffile)) == True:
            pcfr_dict = {}
            with open(self.pcffile, 'r') as pcfr:
                for entry in pcfr:
                    if not len(entry.strip()) == 0:
                        try:
                            line = entry.split(" ", 1)
                            pcfr_dict[line[0]] = line[1].strip().replace("'", "").replace('"', '')
                            print(line[1].strip().replace("'", ""))
                        except IndexError:
                            pass

            return pcfr_dict
        else:
            wx.MessageBox( self.pcffile  + ' pcf file was not found', 'Error',  wx.OK | wx.ICON_INFORMATION)
            return False

    def update_pcf_file(self, pcfobject):
        pcf =  open(self.pcffile, 'r')
        pcfarr = pcf.readlines()
        for n, line in enumerate(pcfarr):
            if self.pattern.match(line):
                lline = line.strip().split(" ", 1)
                if lline[0] in pcfobject:
                    newvalue = pcfobject[lline[0]]
                    pcfarr[n] = '{:33} {:>}'.format(lline[0], newvalue+"\n")

        pcf =  open(self.pcffile, 'w')
        pcf.writelines(pcfarr)
        pcf.close()

    def update_from_pcf(self, pcfr_dict):
        if pcfr_dict:
            dialog_value_dict = {"_chemical_formula_moiety": "?", "_refine_ls_hydrogen_treatment": "?",
                             "_space_group_name_Hall": "?","_diffrn_ambient_temperature": "?",
                             "_exptl_absorpt_correction_T_min": "?",
                             "_exptl_absorpt_correction_T_max": "?", "_exptl_crystal_size_min": "?",
                             "_exptl_crystal_size_mid": "?", "_exptl_crystal_size_max": "?",
                             "_exptl_crystal_description": "?", "_exptl_crystal_colour": "?",
                             "_cell_formula_units_Z": "?", "_space_group_crystal_system":"?"}



            for k in dialog_value_dict.keys():
               try:
                   dialog_value_dict[k] = pcfr_dict[k]
               except KeyError:
                   pass
            return dialog_value_dict

    def get_dev_dict(self):
        dev_dict = {}
        if os.path.exists(os.path.join(self.path, "user", "device", self.device)) == True:
            if not (os.path.join(self.path, "user", "device", self.device)).endswith("default.dev"):
                dev = os.path.join(self.path, "user", "device", self.device)
                with open(dev, 'r') as devfile:
                    for entry in devfile:
                        if not len(entry.strip()) == 0:
                            try:
                                line = entry.split(" ", 1)
                                dev_dict[line[0]] = line[1].strip()
                            except IndexError:
                                pass
                return dev_dict
            else:
                return dev_dict
        else:
            wx.MessageBox(os.path.join(self.path, "user", "device", self.device) + 'dev file was not found', 'Error',
                          wx.OK | wx.ICON_INFORMATION)

    def check_values(self, checkdict):
        for k in checkdict.keys():
            if not checkdict[k].replace('"', '').replace("'", "").replace(".","").isdigit():
               if not "'" in checkdict[k].replace('"', ''):
                   if not str(checkdict[k])=="?":
                       checkdict[k] = "'"+str(checkdict[k])+"'"
                   else:
                       checkdict[k] =  str(checkdict[k])
        return checkdict

    def concatenate(self, filenames, out):
        with open(out, 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)

    def checksqz(self):
        for files in os.listdir(self.dirname):
            if files.endswith("sq.fab"):
                mes = wx.MessageDialog(self, "Squeeze data was found. Use ABIN instruction in the res file to add it", "Squeeze data found", wx.OK | wx.ICON_INFORMATION)
                mes.ShowModal() # Shows it
                break

    def checkcif(self):
        publ = wx.MessageDialog(self, "Do you want to check publish.cif", "publish.cif ...", wx.YES_NO)
        igot = publ.ShowModal() # shows it
        if igot == wx.ID_YES:
            webbrowser.open("http://journals.iucr.org/services/cif/checkcif.html")

    def create_report(self, event):
        dialog_values = self.cifgui.get_values()
        dialog_values["_computing_publication_material"] = "'Linxtl "+self.version+"'"
        self.device = dialog_values["dev_default"]  # choose device from dialog
        dev_dict = self.get_dev_dict()
        after_pcf = self.update_dict(dev_dict, self.pcfr_dict) #update with device
        after_pcf = self.update_dict(dialog_values, after_pcf) #update with dialog
        after_pcf = self.check_values(after_pcf) #correct '
        #print(after_pcf)
        self.update_pcf_file(after_pcf)
        self.cif_class.update_cif_file(after_pcf, self.publishtmp)
        filenames = [os.path.join(self.userdir, after_pcf["user"].replace("'", "")), self.publishtmp]
        self.concatenate(filenames, self.publishcif)
        tmpjson = {"_exptl_crystal_colour":dialog_values["_exptl_crystal_colour"], "dev_default":dialog_values["dev_default"] , "user":dialog_values["user"]}
        self.update_tmp_file(tmpjson)
        self.checksqz()
        self.checkcif()
        self.cifgui.Close(True)
