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
import string
try:
    import vtk
    from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor
except ImportError:
    pass
def length(filename):
    file = open(filename)
    gtext = file.readlines()
    file.close()
    lengthf=len(gtext)
    return lengthf
def hklsizer(filename):
    l=length(filename)
    if l>=3000000:
        n=300
    elif l>=2000000:
        n=120
    elif l>=500000:
        n=30
    elif l>=100000:
        n=5
    else:
        n=2
    return n
def scapoints(gtext, filename):
    points = vtk.vtkPoints()
    n=hklsizer(filename)
    try:
        for lines in gtext[5::n]:
            z=lines.split()[2]
            if not len(z)>=6:
                x=float(lines.split()[0])
                y=float(lines.split()[1])
                z=float(lines.split()[2])
                points.InsertNextPoint(x+1000, y+1000, z+1000)
        return points
    except IndexError:
        pass

def hklpoints(gtext, filename):
    points = vtk.vtkPoints()
    n=hklsizer(filename)
    xyz=[]
   
    for lines in gtext[1::n]:
        try:
            z=lines.split()[2]
            if not len(z)>=6:
#                print(int(lines.split()[0]), int(lines.split()[1]), int(lines.split()[2]))
                x=int(lines.split()[0])
                y=int(lines.split()[1])
                z=int(lines.split()[2])
                points.InsertNextPoint(x+1000, y+1000, z+1000)
        except IndexError:
           pass
#                xyz.append(str(x)+" "+str(y)+" "+str(z))
#        writef(xyz)
    return points

def xdspoints(gtext, filename):
    points = vtk.vtkPoints()
    n=hklsizer(filename)
    xyz=[]
    for lines in gtext[1::n]:
        try:
            z=lines.split()[2]
            if not len(z)>=6:
#                print(int(lines.split()[0]), int(lines.split()[1]), int(lines.split()[2]))
                x=int(lines.split()[4])
                y=int(lines.split()[5])
                z=int(lines.split()[6])
#                print(x,y,z)
                points.InsertNextPoint(x+1000, y+1000, z+1000)
        except IndexError:
           pass
#                xyz.append(str(x)+" "+str(y)+" "+str(z))
#        writef(xyz)
    return points
   
def p4ppoints(gtext, filename):
  
        points = vtk.vtkPoints()
        for lines in gtext: 
            if lines.startswith("REF"):
                try:
                    if not len(str(lines.split()[4]))>6:
    #                    print(lines)
                        x, y, z =(float(lines.split()[2]), float(lines.split()[3]), float(lines.split()[4]))
                        points.InsertNextPoint(x+1000, y+1000, z+1000)
                except IndexError:
                    pass
        return points
  
    
def respoints(gtext, filename):
    
        points = vtk.vtkPoints()
        sfac=getsfac(gtext)
        resfac=sfac[0].upper().replace('\R','').replace('\N','')
        atomlist=resfac[4:].split()
        carbons=[]
        allatoms=[]
        for num in range(10):
            for label in atomlist:
                for lines in gtext: 
                    if lines.upper().startswith(label.upper()+str(num)):
                        try:
                            x, y, z =(abs(float(lines.split()[2])), abs(float(lines.split()[3])), abs(float(lines.split()[4])))
                            points.InsertNextPoint(x, y, z) 
                        except IndexError:
                             pass
        return points

 
def scascalar(gtext, filename, s):
        scalar = vtk.vtkFloatArray()
        n=hklsizer(filename)
        for lines in gtext[5::n]: 
            try:
                z=lines.split()[2]
                if not len(z)>=7:
                    x =(float(lines.split()[3]))
                    if isinstance(s, int ):
                       scalar.InsertNextValue(s)
                       
                    else:
                       m=int(s.split(":")[1])
                       scalar.InsertNextValue(x/m) 
            except IndexError:
                pass
        return scalar

def hklscalar(gtext, filename, s):
        scalar = vtk.vtkFloatArray()
        n=hklsizer(filename)
        for lines in gtext[0::n]: 
            try:
                z=lines.split()[2]
                if not len(z)>=7:
                    x =(float(lines.split()[3]))
                    if isinstance(s, int ):
                       scalar.InsertNextValue(s)
                    else:
                       m=int(s.split(":")[1])
                       scalar.InsertNextValue(x/m) 
            except IndexError:
                pass
        return scalar

def xdsscalar(gtext, filename, s):
        scalar = vtk.vtkFloatArray()
        n=hklsizer(filename)
        for lines in gtext[0::n]: 
            try:
                z=lines.split()[2]
                if not len(z)>=7:
                    x =(float(lines.split()[3]))
                    if isinstance(s, int ):
                       scalar.InsertNextValue(s)
                    else:
                       m=int(s.split(":")[1])
                       scalar.InsertNextValue(x/m) 
            except IndexError:
                pass
        return scalar
     
def p4pscalar(gtext, filename, s):
   
        scalar = vtk.vtkFloatArray()
        for lines in gtext: 
            if lines.startswith("REF"):
                try:
                    if not len(str(lines.split()[4]))>6:
                        x=(float(lines.split()[11]))
                        if isinstance(s, int ):
                           scalar.InsertNextValue(s)
                        else:
                           m=int(s.split(":")[1]) 
                           scalar.InsertNextValue(x/(m)) 
                except IndexError:
                    pass
        return scalar
 
    
def resscalar(gtext, filename, s):
  
        scalar = vtk.vtkFloatArray()
        sfac=getsfac(gtext)
        resfac=sfac[0].upper().replace('\R','').replace('\N','')
        atomlist=resfac[4:].split()
        for num in range(10):
            for label in atomlist:
                for lines in gtext: 
                    if lines.upper().startswith(label.upper()+str(num)) :
                        if not lines.upper().startswith("H"+str(num)) :
                            try:
                               x=(float(abs(float(lines.split()[6]))))
        #                      x, y, z = float(data[0]), float(data[1]), float(data[2])
                               scalar.InsertNextValue(s)
                            except IndexError:
                                pass
        return scalar
   


def fileopen(filename):
        file = open(filename)
        gtext = file.readlines()
        file.close()
        num=1
        for n, lines in enumerate(gtext):
            if "END_OF_HEADER" in lines:
                num=n
        return gtext[int(num)+1:];
def readPoints(filename):
    gtext=fileopen(filename)
    if filename.lower().endswith('.res'):
        points=respoints(gtext, filename)
    if filename.lower().endswith('.ins'):
        points=respoints(gtext, filename)
    elif filename.lower().endswith('.hkl'):
        print("gothkl")
        points=hklpoints(gtext, filename)
    elif filename.lower().endswith('.sca'):
        points=scapoints(gtext, filename)
    elif filename.lower().endswith(".p4p"):
        points=p4ppoints(gtext, filename)   
    elif filename.lower().endswith(".xds"):
        points=xdspoints(gtext, filename)
    return points;

    
def readScalars(filename, s):
    gtext=fileopen(filename)
    if filename.lower().endswith('.res'):
        scalar=resscalar(gtext, filename, s)
    if filename.lower().endswith('.ins'):
        scalar=resscalar(gtext, filename, s)
    elif filename.lower().endswith('.hkl'):
        scalar=hklscalar(gtext, filename, s)
    elif filename.lower().endswith('.sca'):
        scalar=scascalar(gtext, filename, s)
    elif filename.lower().endswith(".p4p"):
        scalar=p4pscalar(gtext, filename, s)
    elif filename.lower().endswith(".xds"):
        scalar=xdsscalar(gtext, filename, s)    
        
    return scalar;
def getsfac(gtext):
            return([line for line in gtext if line.lower().startswith('sfac')]) 
def striplist(lines): 
        return([line for line in lines if line.strip()]) 
def getnums(filename):
        file = open(filename)
        gtext = file.readlines()
        file.close()
        for lines in gtext:
            if "CELL" in lines:
                cell=lines.split(' ')
                a,b,c,alpha,beta,gamma=striplist(cell)[2:8]
                a=float(a)
                b=float(b)
                c=float(c)
                alpha=float(alpha)
                beta=float(beta)
                gamma=float(gamma)
        sfac=getsfac(gtext)
        resfac=sfac[0].upper().replace('\R','').replace('\N','')
        atomlist=resfac[4:].split()
        atomlist.insert(0, 'Q')
        carbons=[]
#        print atomlist
        allatoms=[]
        for num in range(10):
            for label in atomlist:
                for lines in gtext: 
                    if lines.upper().startswith(label.upper()+str(num)) :
                       allatoms.append(' '.join(lines.upper().split()[0:6]))
                    elif lines.upper().startswith(label.upper()+" "):
#                        print lines
                        allatoms.append(' '.join(lines.upper().split()[0:6]))
                  
        allatoms=list(set(allatoms)) 
        for line in allatoms: 
                           xc=float(oxiline.split()[2])
                           #print xc
                           yc=float(oxiline.split()[3])
                           #print yc
                           zc=float(oxiline.split()[4])
                           #print zc
                           xa=float(line.split()[2])
                           #print xa
                           ya=float(line.split()[3])
                           #print ya
                           za=float(line.split()[4])
                           #print za, a,b,c
                           
                           xcom=((xc-xa)*a)**2
                           ycom=((yc-ya)*b)**2
                           zcom=((zc-za)*c)**2
                           bc=2*b*c*math.cos(math.radians(alpha))*(yc-ya)*(zc-za)
                           ac=2*a*c*math.cos(math.radians(beta))*(zc-za)*(xc-xa)
                           ab=2*a*b*math.cos(math.radians(gamma))*(yc-ya)*(xc-xa)
                           calcbond=math.sqrt(xcom+ycom+zcom+bc+ac+ab)
                           if 1.4>calcbond>0.5:
#                                print  oxy," ",line.split()[0], "=", calcbond
                                proc.append(str(line)+"="+str(calcbond))
    
#        print  proc
def readConnections(filename):
    bonds=getnums(filename)
    connections=vtk.vtkCellArray()
    file = open(filename)
    gtext = file.readlines()
    file.close()
    sfac=getsfac(gtext)
    resfac=sfac[0].upper().replace('\R','').replace('\N','')
    atomlist=resfac[4:].split()
    carbons=[]
#    print atomlist
    allatoms=[]
    for num in range(10):
        for label in atomlist:
            for lines in gtext: 
                if lines.upper().startswith(label.upper()+str(num)) :
#                   allatoms.append(' '.join(lines.upper().split()[2:6]))
                    x, y, z =((lines.split()[2]), (lines.split()[3]), float(lines.split()[4]))
                    connections.InsertNextCell(2)
                    connections.InsertCellPoint(1)
                    connections.InsertCellPoint(2)
#                    connections.GetCell(1,2) 
      
    return connections
def getsfac(gtext):
        return([line for line in gtext if line.lower().startswith('sfac')]) 
def striplist(lines): 
    return([line for line in lines if line.strip()]) 