#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os, sys, tarfile 
global path
import shutil
path = sys.path[0]
maindirname="/home/spasyud/cdb/"
#print(os.path.getsize('/home/spasyud/cdb/STRUCTURAL_DATABASE.db'))
def striplist(lines): 
        return([line for line in lines if line.strip()]) 
def getcifs(maindirname):
        try: 
                try:
                    ciflist=[]
                    for dirpath, dirnames, filenames in os.walk(maindirname):
                        for filename in filenames:
                            size=os.path.getsize(os.path.join(dirpath, filename))
                            
                            if int(size)>=400000:
                                print(filename, size)
                                if (filename.lower()).endswith(".cif"): 
                                    ciflist.append(os.path.join(dirpath, filename)) 
                except UnicodeEncodeError:
                    pass 
#                print ("scan",ciflist)
                return ciflist
        except OSError:
         pass

        
def cifsplitter(ciffile):
            fnamefull=ciffile
            fnoe=os.path.splitext(fnamefull)[0]
            fcif=open(fnamefull, 'r')
            fcifread=fcif.read()
            fcif.close()
            if fcifread.find("_shelx_res_file"):
                resfileb=fcifread.find("_shelx_res_file")
                resfileend=fcifread.find("_shelx_res_checksum")
                hklfileb=fcifread.find("_shelx_hkl_file")
                hklend=fcifread.find("_shelx_hkl_checksum")
    #            # print "resfileb=", resfileb, "resfileend=", resfileend, "hklb=", hklfileb, "hklend=", hklend
                ciffileout=fcifread[:resfileb]
                resfileout=fcifread[resfileb+15:resfileend].replace(";","")
                hklfileout=fcifread[hklfileb+15:(int(hklend)-1)].replace(";","")
                hkllist=hklfileout.split("\n")
                hkloutlist=striplist(hkllist)
                hklfileout="\n".join(hkloutlist) 
                cif=open(fnoe+"_cd.cif", 'w')
                cif.write(ciffileout)
                res=open(fnoe+".res", 'w')
                res.write(resfileout)
                hkl=open(fnoe+'.hkl', 'w')
                hkl.write(hklfileout)
                res.close()
                hkl.close()    
                cif.close()  
                os.remove(fnamefull)
def interact():
    maindirname="/home/spasyud/cdb"
    cifs=getcifs(maindirname)
    for files in cifs:
        cifsplitter(files)
interact()