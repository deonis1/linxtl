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
import sys
import os
import math
event=None
class calcrest(object):
    def __init__(self, event, text, cell, sfac):
        self.restext=text
        self.cell=cell
        self.sfac=sfac
#        self.calcbonds(event)
    def remdubs(self, l):
        b_set = set(tuple(x) for x in l)
        stripped_list = [ list(x) for x in b_set]
        return stripped_list
    def calcbonds(self, event):
        gtext=self.ontext()
        allatoms=self.getallatoms(event, gtext)
        bonds=(self.oncalcallbonds(event, allatoms, allatoms))
        for i, a in enumerate(bonds):
            bonds[i]=sorted(a, reverse=True)
        atoms_and_length=self.remdubs(bonds) 
#        print(atoms_and_length)
#        listof_bonds=[],[],[],[],[],[] # carbons single, double, triple, oxygen-carbon, single, double, tripple
        dfix=[]
        for x in atoms_and_length:
            l="DFIX", x[2].upper(), "0.02", x[0].upper(), x[1].upper()
            dfix.append(l)
        return "\n".join("  ".join(map(str,l)) for l in dfix)

    def ontext(self):
        return self.restext
    def oncalcallbonds(self, event, allatoms, carbons):
            atombonds = []
            gtext=self.ontext()
            a, b, c, alpha, beta, gamma = [float(list_item) for list_item in self.cell]  # list of strings to float
            for line in carbons:
                for atom in allatoms:
                    xc = float(atom.split()[2])
                    yc = float(atom.split()[3])
                    zc = float(atom.split()[4])
                    xa = float(line.split()[2])
                    ya = float(line.split()[3])
                    za = float(line.split()[4])
                    xcom = ((xc - xa) * a) ** 2
                    ycom = ((yc - ya) * b) ** 2
                    zcom = ((zc - za) * c) ** 2
                    bc = 2 * b * c * math.cos(math.radians(alpha)) * (yc - ya) * (zc - za)
                    ac = 2 * a * c * math.cos(math.radians(beta)) * (zc - za) * (xc - xa)
                    ab = 2 * a * b * math.cos(math.radians(gamma)) * (yc - ya) * (xc - xa)
                    calcbond = math.sqrt(xcom + ycom + zcom + bc + ac + ab)
                    if 1.9>=calcbond>=1 :
                        atombonds.append([atom.split()[0], line.split()[0], str(round(calcbond, 2))])
            return atombonds
    
    def getallatoms(self, event, gtext):
            allatoms=[]
            import re
            pattern =  re.compile(r'^([A-Za-z0-9]{1,4}\s+\d{1,3}(?:\s+-?\d+\.\d+){5})')
#            for a in sfac:
            for lines in gtext:
                    if pattern.match(lines):
                        if not lines.startswith("Q"):
                            if not lines.startswith("H"):
                               allatoms.append(' '.join(lines.split()[0:5]))
            return allatoms
   
    def striplist(self, lines): 
        return([line for line in lines if line.strip()]) 

