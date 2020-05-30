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
import os, sys
global ossystem
ossystem=sys.platform
import pexpect
unit_cell=("8.0410  11.1276  13.1597   67.800   76.328   86.327").split()   
output="/home/denis/file"
hkllife="/home/denis/dstgb2_0m0/dstgb2_0m.hkl"
pathtoxprep="/home/denis/.linxtl/bin/xprep"
formula="C20H30N2P1S2O1"
#for num in range(100):
#    print('{}  {}  {}'.format(num, num, num))
def autoxprep(pathtoxprep, output, unitcell, formula):
    client = pexpect.spawn(pathtoxprep+" "+hkllife)
    log=""
    input = [
        ('Enter cell .+:\r\n\s', ' '.join(["%s" % v for v in unit_cell])),
        ('Lattice type \[.+Select option\s\[.+\]:\s',''),
        ('Select option\s\[.+\]:\s',''),
        ('Determination of reduced .+Select option\s\[.+\]:\s',''), 
        ('Select option\s\[.+\]:\s',''),
        ('Select option\s\[.+\]:\s',''),
        ('Select option\s\[.+\]:\s',''),
        ('Select option\s\[.+\]:\s',''),
        ('Select option\s\[.+\]:\s',''),
        ('Select option\s\[.+\]:\s','C'),
        ('Enter formula; .+:\r\n\r\n', formula), 
        ('Tentative Z .+Select option\s\[.+\]:\s',''),
        ('Select option\s\[.+\]:\s','F'),
        ('Output file name .+:\s', output), 
        ('format\s\[.+\]:\s','S'),  
        ('Do you wish to .+\s\[.+\]:\s',''), 
        ('Select option\s\[.+\]:\s','Q')
    ]
    for expected, cmd in input:
        log += client.read_nonblocking(size=2000)
        client.sendline(cmd)
        if expected is None:
            time.sleep(.1)
#    print(client.read())
    if client.isalive():
        client.wait()
autoxprep(pathtoxprep, output, unit_cell, formula)