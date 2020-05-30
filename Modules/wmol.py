import os
import sys
import json
import webbrowser

class wmol(object):
    def __init__(self, filename):
       self.fnamefull=filename
       self.wdir = os.path.dirname(os.path.realpath(__file__))
    #    self.path = sys.path[0]
       self.wdir = os.path.join(self.wdir, "wmol")
       self.datajs = os.path.join(self.wdir, 'js', "main.js")
       self.exe = os.path.join(self.wdir, "index_main.html")
       self.writetmp()

    def getfile(self):
       datadict = {}
       file_to_read= open(self.fnamefull, 'r')
       data = [l.lstrip() for l in file_to_read]
       print(os.path.splitext(self.fnamefull)[1])
       datadict["ext"] = os.path.splitext(self.fnamefull)[1][1:]
       datadict["data"] = data
       return datadict


    def writetmp(self):
        if self.fnamefull:
           with open(self.datajs, 'w') as f:
               f.write("var thefile ="+json.dumps(self.getfile()))
        self.openwmol()

    def openwmol(self):
        webbrowser.open(self.exe)

if __name__ == "__main__":
    args = sys.argv
    filepath = args[1]
    if len(filepath)==0:
       print("Please provide file name as input for wmol")
    else:
        if os.path.isabs(filepath):
            if os.path.exists(filepath):      
                wmol(filepath)
            else:
                print("File ", filepath, "does not exist!")
        else:
            curdir = os.curdir
            filepath = os.path.join(curdir, filepath)
            wmol(filepath)
    