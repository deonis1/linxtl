#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, subprocess, shutil
from subprocess import Popen
path = sys.path[0]
print ("You need to be root to install dependencies")
print ("You are here:  ", path)
system = input('For Debian, Ubuntu and Mint type [d], for RedHat, Fedora, Suse type [r]: ')
if system=="d":
    selection = input('Please enter a path to install Linxtl: ')
    # print"installing to: ", selection
    if os.path.exists(selection)==True:
        # print"Path exist ", selection
        yesno= input('Overwrite? y/n: ')
        if yesno=="y":
            try:
              shutil.rmtree(selection)
              shutil.copytree(path, selection)  
            except shutil.Error:
                pass
        elif yesno=="n":
            print ("installation of Linxtl was abborted")
    else:
        try:
           shutil.copytree(path, selection)  
        except shutil.Error:
                pass
    os.system('chmod -R 777 '+selection+'/')
    print ("############### Installing dependencies ################")
    print ("############### Installing python-wxgtk4 ###############")
    proc=subprocess.Popen('apt-get install -y python3-wxgtk4.0 python3-wxgtk-webview4.0', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
    proc.wait()
    yesno= input('Some packages supported by Linxtl might require Wine. Do you want to install it? y/n: ')
    if yesno=="y":
        # print"################################# Installing wine ###############################"
        proc=subprocess.Popen('apt-get install -y wine', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
        proc.wait()
    elif yesno=="n":
         print ("installation of wine was abborted")

    yesno= input('Some packages supported by Linxtl might require libgfortran. Do you want to install it? y/n: ')
    if yesno=="y":
        # print"################################# Installing libgfortran ###############################"
        proc=subprocess.Popen('apt-get install -y libgfortran3', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
        proc.wait()
    elif yesno=="n":
         print ("installation of libgfortran was abborted")
    # print"installation completed"
elif system=="r":
    selection = input('Please enter a path to install Linxtl: ')
    # print"installing to: ", selection
    if os.path.exists(selection)==True:
        print ("Path exist ", selection)
        yesno= input('Owerride? y/n: ')
        if yesno=="y":
            try:
              shutil.rmtree(selection)
              shutil.copytree(path, selection)
              
            except shutil.Error:
                pass
        elif yesno=="n":
             print ("installation of Linxtl was abborted")
    else:
        try:
           shutil.copytree(path, selection)
           os.chmod(selection)
        except shutil.Error:
                pass
    os.system('chmod -R 755 '+selection)
    print ("#################### Installing dependencies #################")
    print ("################### Installing python-wxgtk2.8 ###############")
    proc=subprocess.Popen('yum install wxPython', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
    proc.wait()
    yesno= input('Some packages supported by Linxtl might require Wine. Do you want to install it? y/n: ')
    if yesno=="y":
        print ("############### Installing wine ################")
        proc=subprocess.Popen('yum install wine', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
        proc.wait()
    elif yesno=="n":
        print ("installation of wine was abborted")

    yesno= input('Some packages supported by Linxtl might require libgfortran. Do you want to install it? y/n: ')
    if yesno=="y":
        print ("##################### Installing libgfortran ######################")
        proc=subprocess.Popen('yum install libgfortran3', shell=True, stdin=None, stdout=None, stderr=None, executable="/bin/bash")
        proc.wait()
    elif yesno=="n":
         print ("installation of libgfortran was abborted")     
os.chmod(os.path.join(path,'linxtl.py'), 0o755)

os.chmod(os.path.join(path,'external.py'), 0o755)
#Popen(os.path.join(path,'linxtl.py'), shell=True)
Popen(os.path.join(path,"launcher-setup.py"), shell=True)
os.chmod(os.path.join(path,'launcher-setup.py'), 0o755)
print ("installation complet")
