#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os, sys, urllib2, httplib, shutil
import subprocess
global path
path = sys.path[0]
ossystem=sys.platform
print(path)
def reboot():
   os.chmod(os.path.join(path,'linxtl.py'), 0755)
   os.chmod(os.path.join(path,'launcher-setup.py'), 0755)
   os.chmod(os.path.join(path, 'Modules', 'external.py'), 0755)
   try:
        if os.path.exists(os.path.join(path, "libcif.py")):
          os.remove(os.path.join(path, "libcif.pyc"))
          os.remove(os.path.join(path, "libcif.py"))
        if os.path.exists(os.path.join(path, "HTML.py")):
          os.remove(os.path.join(path, "HTML.py"))
          os.remove(os.path.join(path, "HTML.pyc"))
        if os.path.exists(os.path.join(path, "external.py")):
          os.remove(os.path.join(path, "external.py"))
          os.remove(os.path.join(path, "external.pyc"))
   except OSError:
       pass
   
   subprocess.Popen([sys.executable, os.path.join(path,'linxtl.py')], shell=False) 
   if ossystem.startswith("lin"):
      subprocess.Popen([sys.executable, os.path.join(path, "launcher-setup.py")], shell=False)
def lininstall():
    root_src_dir = os.path.join(path, 'updatelinxtl')
    root_dst_dir = os.path.join(path)
    source=os.path.join(root_src_dir, [name for name in os.listdir(root_src_dir)][0])
    print ("Source folder ...",source)

    for src_dir, dirs, files in os.walk(source):
        dst_dir = src_dir.replace(source, root_dst_dir)
       # printdst_dir
        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)
    shutil.rmtree(os.path.join(path, 'updatelinxtl'))
    os.remove(os.path.join(path, 'download'))
    reboot()
def unzipp():
    
    import  zipfile
    z = zipfile.ZipFile(os.path.join(path, 'download'))
    z.extractall(os.path.join(path, 'updatelinxtl'))
try:
      
            import urllib2
            url = "http://sourceforge.net/projects/linxtl/files/latest/download"
            file_name = url.split('/')[-1]
            u = urllib2.urlopen(url)
            f = open(os.path.join(path,file_name), 'wb')
            meta = u.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            print ("Downloading: %s Bytes: %s" % (file_name, file_size))
            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
                file_size_dl += len(buffer)
                f.write(buffer)
                status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
                status = status + ">"*(len(status)+1)
         
            f.close()
            unzipp()
            lininstall()

except urllib2.HTTPError, e:
    print ('Unable to get latest version info - HTTPError = ' + str(e.reason))
    sys.exit(2)	
        
except urllib2.URLError, e:
    print ('Unable to get latest version info - URLError = ' + str(e.reason))
    sys.exit(2)	
            
except httplib.HTTPException, e:
    print ('Unable to get latest version info - HTTPException')
    sys.exit(2)	
            
except Exception, e:
    import traceback
    print ('Unable to get latest version info - Exception = ' + traceback.format_exc())
    sys.exit(2)
