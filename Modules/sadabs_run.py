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
import os, sys, re
global ossystem
ossystem=sys.platform
import pexpect, time
unit_cell=("8.0410  11.1276  13.1597   67.800   76.328   86.327").split()
output="/home/denis/file"
outabs="/home/denis/test/outsad.abs"
hklfile="/home/denis/test/outhkl.hkl"
phtosadabs="/home/denis/.linxtl/bin/sadabs"
formula="C20H30N2P1S2O1"
#for num in range(100):
#    print('{}  {}  {}'.format(num, num, num))
dirname="/home/denis/test/"
raw_files=[]
for files in os.listdir(dirname):
    if files.endswith(".raw"):
        raw_files.append(os.path.join(dirname, files))

def __init__(self):
    print("init")
def sortkey(string):    
        return tuple(int(num) if num else alpha for num, alpha in (re.compile(r'(\d+)|(\D+)').findall)(string))  
raw_files=sorted(raw_files, key=sortkey) 
laue="1"
input = [('Expert mode \s\[.+\]:\s',''),
            ('Enter listing filename \s\[.+\]:\s',outabs),
            ('Enter Laue group number:\s',laue),
            ('Enter filename ','\n'.join(["%s" % v for v in raw_files])),
            ('Select option\s\[.+\]:\s',"/"),
            ('Restraint esd for equal consecutive scale\s\[.+\]:\s',''),
            ('Apply angle of incidence correction :\s',''),
            ('Number of refinement cycles :\s','50'),
            ('Detector (D) or crystal (C) coordinates for spherical harmonics', ''),
            ('numerical absorption correction', ''),
            ('Repeat parameter refinement (R) or accept (A) ', ''),
            ('Enter new value for g or <CR> to accept:', ''),
            ('Repeat parameter refinement (P) or accept (A) ', ''),
            ('Write Postscript diagnostic file (Y or N) ', ''),
            ('Enter name of Postscript file ', ''),
            ('Short  title for Postscript plots ', ''),
            ('Repeat (R), write unmerged .hkl (W), merged .hkl (M), .sca (S)', ''),
            ('Reflection output file ', hklfile),
            ('Lambda/0 correction factor ', ''),
            ('Lambda/0 correction factor ', "Q"),
            ]
input1 = [('Expert mode \s\[.+\]:\s','Y'),
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
            ('Mu*r of equivalent sphere for additional absorption correction 2', hklfile),
            ('Apply lambda/2 correction (2) for a graphite monochromator or lambda/3 (3) for Ge or Si monochromator or no correction (0)  ', ''), #need coorectio editor
            ('Repeat (R), write unmerged .hkl (W), merged .hkl (M), .sca (S)', ''),
            ]
def parselog(self,log):
    from probar import progressbar
    progress = progressbar()
    igot=progress.ShowModal()
    if re.search("Enter Laue group number", log):
        proc=10
        longRunning.progress(proc) 
    progress.Destroy()    
def autoxprep(phtosadabs, output, input):
    client = pexpect.spawn(phtosadabs)
    log=""
    for expected, cmd in input:
        log = client.read_nonblocking(size=2000)
        client.sendline(cmd)
        if expected:
            parselog(self, log) 
    if client.isalive():
        client.wait()
      
autoxprep(phtosadabs, output, input1)
