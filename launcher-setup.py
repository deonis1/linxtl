#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, subprocess, shutil, time
ossystem=sys.platform

homef=os.getenv("HOME")
path = sys.path[0]
desktop=None
def setuplauncher(path, ossystem, homef, desktop):
    if ossystem.startswith("win"):
        win=os.getenv('USERPROFILE')
        print ("Automatic shortcut creation is not yet supported for Windows. Right-click on linxtl.py file, and then click Create Shortcut.")
        time.sleep(8)
    elif ossystem.startswith("lin"):
            ########### You need to be root to install a Linxtl icon into /usr/share/applications, but you can always install the icon to desktop without root permition####
            if not os.path.exists(os.path.join(homef,".local","share","applications")):
                os.makedirs(os.path.join(homef,".local","share","applications"))
                file=open(os.path.join(homef,"Desktop","Linxtl.desktop"), 'w')
                file.write(desktop)
                file.close
                os.chmod(os.path.join(homef,"Desktop","Linxtl.desktop"), 0o755)
                file=open(os.path.join(homef,".local","share","applications","Linxtl.desktop"), 'w')
                file.write(desktop)
                file.close
                os.chmod(os.path.join(homef,".local","share","applications","Linxtl.desktop"), 0o755)
            else:
                file=open(os.path.join(homef,"Desktop","Linxtl.desktop"), 'w')
                file.write(desktop)
                file.close
                os.chmod(os.path.join(homef,"Desktop","Linxtl.desktop"), 0o755)
                file=open(os.path.join(homef,".local","share","applications","Linxtl.desktop"), 'w')
                file.write(desktop)
                file.close
                os.chmod(os.path.join(homef,".local","share","applications","Linxtl.desktop"), 0o755)
    elif ossystem.startswith("darwin"):
        file=open(os.path.join("/Applications","Linxtl.command"), 'w')
        file.write(desktop)
        file.close
        os.chmod(os.path.join("/Applications","Linxtl.command"), 0o755)
def desktop(path, desktop):
    if ossystem.startswith("lin"):
        a='''[Desktop Entry]
        Name=Linxtl
        Comment=Crystallographic toolbox for Linux'''+'\n'
        b="Exec="+os.path.join(path, "linxtl.py")+'\n'
        c="TryExec="+os.path.join(path, "linxtl.py")+'\n'
        d="Icon="+os.path.join(path, "icon/main.ico")+'\n'
        e='''StartupNotify=false
        Terminal=false
        Type=Application
        Categories=GNOME;GTK;Education;Chemistry;'''
        desktop=a+b+c+d+e
        #print desktop
        file=open(os.path.join(path,"Linxtl.desktop"), 'w')
        file.write(desktop)
        file.close
        os.chmod(os.path.join(path,"Linxtl.desktop"), 0o755)
        setuplauncher(path,ossystem, homef, desktop)
    elif ossystem.startswith("darwin"):
        pf=os.path.join(path,"linxtl.py")
        desktop="python "+pf
        file=open(os.path.join(path,"Linxtl.command"), 'w')
        file.write(desktop)
        file.close
        os.chmod(os.path.join(path,"Linxtl.command"), 0o755)
        setuplauncher(path,ossystem, homef, desktop)
desktop(path,desktop)
print ("##############Installation complete!##############")
time.sleep(5)




#def ShowMessage():
#    wx.MessageBox('The Launcher has been successfully installed', 'Info', wx.OK | wx.ICON_INFORMATION)

#ShowMessage()
