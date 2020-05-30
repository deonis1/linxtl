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
import sys, os

import re

class collision():
    def __init__(self, input):
        self.pattern=re.compile(r'^[A-Za-z][\w\_]{1,4}\^([A-Za-z]\_\$)\d{1,3}')
        self.pat_nopart=re.compile(r'^[A-Za-z][\w\_]{1,4}(\_\$)\d{1,3}')
        self.parseinput(input)
        
    def parse_line(self, line):
        i_list=[]
        prefix =None
        for item in line:
            if self.pattern.match(item) or  self.pat_nopart.match(item):
                if "^" in item:
                   prefix="_"+(item.split("_")[1]).split("^")[0]+" "
                   i_list.append(item.split("_")[0]+"_"+item.split("_")[2]+"^"+(item.split("_")[1]).split("^")[-1])  #C10_5^a_$7 C10_$7^a
                else: 
                   prefix="_"+(item.split("_")[1]).split("^")[0]+" "
                   i_list.append(item.split("_")[0]+"_"+item.split("_")[2]) 
        return i_list, prefix   
    def iter_list(self, filler, list):
        out=[]
        for i in list:
            out.append(filler)
            out.append(i)
        return out
    def parseinput(self, input):
  
        list_free=[]
        for lines in input.split('\n'):
            list_line=lines.split()
            item_list, prefix=self.parse_line(list_line)
            try:
               out_list=self.iter_list(list_line[8], item_list)
               if out_list:
#                    print(out_list)
                    if len(out_list)==2:
                        list_free.append("FREE"+prefix+' '.join(out_list))
                    if len(out_list)==4:
                        list_free.append("FREE"+prefix+' '.join(out_list[0:2])+"\n"+"FREE"+prefix+' '.join(out_list[2:4]))
                    if len(out_list)==6:
                        list_free.append("FREE"+prefix+' '.join(out_list[0:2])+"\n"+"FREE"+prefix+' '.join(out_list[2:4]) +"\n"+"FREE"+prefix+' '.join(out_list[4:6]))
                    if len(out_list)==8:
                       list_free.append("FREE"+prefix+' '.join(out_list[0:2])+"\n"+"FREE"+prefix+' '.join(out_list[2:4]) +"\n"+"FREE"+prefix+' '.join(out_list[4:6])+"\n"+"FREE"+prefix+' '.join(out_list[6:8]))
                    if len(out_list)==10:
                       list_free.append("FREE"+prefix+' '.join(out_list[0:2])+"\n"+"FREE"+prefix+' '.join(out_list[2:4]) +"\n"+"FREE"+prefix+' '.join(out_list[4:6])+"\n"+"FREE"+prefix+' '.join(out_list[6:8])+"\n"+"FREE"+prefix+' '.join(out_list[8:10]))
                    if len(out_list)==12:
                       list_free.append("FREE"+prefix+' '.join(out_list[0:2])+"\n"+"FREE"+prefix+' '.join(out_list[2:4])
                       +"\n"+"FREE"+prefix+' '.join(out_list[4:6])+"\n"+"FREE"+prefix+' '.join(out_list[6:8])
                       +"\n"+"FREE"+prefix+' '.join(out_list[8:10])+"\n"+"FREE"+prefix+' '.join(out_list[10:12]))
            except IndexError:
                pass
        print(list_free)
        return list_free
#collision(input)