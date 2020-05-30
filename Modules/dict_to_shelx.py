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
import re, os
class mxtosm(object):
    def __init__(self, event, cifrestrains):
        self.ciffile=cifrestrains
        self.constraints(event)
    def openfile(self):
        cif=open(self.ciffile, 'r')
        ciflist=cif.readlines()
        cif.close()
        return ciflist
    def getlength(self, cifdist, atom, btom):
        for li in cifdist:
            if atom and btom in ' '.join(li):
                return(float(li[4]))
    def dictdeclare(self, event):
        cifdist = []
        cifang = []
        pattern = re.compile(r"(\s?[A-GI-Za-gi-z0-9]{1,5}\s{1,}){1,3}([a-z\s]{4,}){1}(\d\.\d{1,4})\s{1,}(\d\.\d{1,4})")
        patang = re.compile(r"(\s?[A-GI-Za-gi-z0-9]{1,5}\s{1,}){4}(\d{2,3}\.\d{1,3})\s{1,}(\d{1,3}\.\d{1,3})")
        ciflist=self.openfile()
        for l in ciflist:
            if pattern.match(l):
#                print(l.split())
                cifdist.append(l.split())
            if patang.match(l):
#                print(l.split())
                if len(l.split())==6:
                    cifang.append(l.split())
        return cifdist, cifang
    def calcdist(self, gamma, a, b):
        import math
        c_dang=round(math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(gamma))), 2)
        return c_dang

    def constraints(self, event):
        cifdist,cifang = self.dictdeclare(event)
        dfix=[]
        dang=[]
        for items in cifdist:
            dfix.append("DFIX_"+items[0].upper()+" "+items[4].upper()+" "+items[5].upper()+" "+items[1].upper()+" "+items[2].upper())
        for item in cifang:
#            print(item)
            Atom=item[1]
            Btom=item[2]
            Ctom=item[3]
            gamma=float(item[4])
            a=self.getlength(cifdist, Atom, Btom)
            b=self.getlength(cifdist, Btom, Ctom)
            dang.append('DANG_'+item[0].upper()+' '+str(self.calcdist(gamma, a, b))+" 0.02 "+Atom+" "+Ctom)
        return dfix, dang
