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
import wx


try:
    import vtk
    from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor
except ImportError, msg:
    app = wx.App()
    wx.MessageDialog(None, 'No VTK6 found on this computer', 'Please install VTK6', wx.OK | wx.ICON_INFORMATION).ShowModal()
    frame = wx.Frame(None)
    frame.Center()
    frame.Show()

import base64
import os, sys

from reader import * 
#fullname="/home/denis/a.hkl"
global path
path = sys.path[0]
global ossystem
ossystem=sys.platform
def create(parent, title):
    return  hkllat(parent, title)
class MyInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):
 
    def __init__(self,parent=None):
        self.AddObserver("MiddleButtonPressEvent",self.middleButtonPressEvent)
        self.AddObserver("MiddleButtonReleaseEvent",self.middleButtonReleaseEvent)
        self.AddObserver("LeftButtonPressEvent",self.leftButtonPressEvent)
#        self.AddObserver("MiddleButtonReleaseEvent",self.leftButtonReleaseEvent)
 
    def middleButtonPressEvent(self,obj,event):
        print("Middle Button pressed")
        self.OnMiddleButtonDown()
        return
#        clickPos = self.GetInteractor().GetEventPosition()
#        self.GetInteractor().GetPicker().Pick(self.GetInteractor().GetEventPosition()[0], self.GetInteractor().GetEventPosition()[1], 0,  
#           self.GetInteractor().GetRenderWindow().GetRenderers().GetFirstRenderer())
#        print(self.GetInteractor().GetPicker().GetPointId())
#        print(self.GetInteractor().GetPicker().GetPCoords())
#        print(self.GetInteractor().GetPicker().GetPickPosition())
##        self.GetInteractor().GetPicker().GetActor().GetProperty().SetColor(0.5, 0.7, 0.0)
#        print(self.GetInteractor().GetPicker().GetActor().GetProperty())
       
    def leftButtonPressEvent(self,obj,event):
            print("Left Button pressed")
            self.OnLeftButtonDown()
            return

    def middleButtonReleaseEvent(self,obj,event):
        print("Middle Button released")
        self.OnMiddleButtonUp()
        return
class p1(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent)
        #to interact with the scene using the mouse use an instance of vtkRenderWindowInteractor. 
        self.widget = wxVTKRenderWindowInteractor(self, -1, size = (700, 700))
        self.widget.Enable(1)
        self.widget.SetPosition((-1,-1))
        self.widget.SetInteractorStyle(MyInteractorStyle())
        self.widget.AddObserver("ExitEvent", lambda o,e,f=self: f.Close())

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.widget, 1, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.Layout()
        self.Refresh()
        self.isploted=False
        self.Update()
        print(self.isploted)

class hkllat(wx.Frame):
    def __init__(self,parent,title):#, fullname):
        # begin wxGlade: MyFrame.__init__
        wx.Frame.__init__(self, parent, title=title)
        filemenu= wx.Menu()
        self.path=path
        self.isploted=False
        self.s=1
        self.vtkversion()
        self.dirname=os.path.expanduser("~")
        menuopen = filemenu.Append(wx.ID_OPEN,"&Open"," Terminate the program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.p1 = p1(self)
        ib = wx.IconBundle()
        ib.AddIconFromFile(os.path.join(self.path, "icon", "hkllat.ico"), wx.BITMAP_TYPE_ICO)
        self.SetIcons(ib)
        self.burefresh = wx.Button(self, wx.ID_ANY, ("Static"))
        self.intenseplus = wx.Button(self, wx.ID_ANY, ("I+"))
        self.intenseminus = wx.Button(self, wx.ID_ANY, ("I-"))
        self.bclear = wx.Button(self, wx.ID_ANY, ("Clear"))
        self.SetBackgroundColour(wx.Colour(245,245,245))
        self.reali = wx.Button(self, wx.ID_ANY, ("I(obs)"))
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuopen)
        self.Bind(wx.EVT_BUTTON, self.onClear, self.bclear)
        self.Bind(wx.EVT_BUTTON, self.onRefresh,  self.burefresh)
        self.Bind(wx.EVT_BUTTON, self.onintensityplus, self.intenseplus)
        self.Bind(wx.EVT_BUTTON, self.onintensityminus, self.intenseminus)
        self.Bind(wx.EVT_BUTTON, self.onreali, self.reali)
#        self.fullname=fullname
#        data=self.ondata(fullname)
#        self.renderthis(data) 
        
        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle(("HKLLAT"))
        self.p1.SetMinSize((700, 700))
        self.burefresh.SetSize((-1, -1))
        self.intenseplus.SetSize((-1, -1))
        self.bclear.SetSize((-1, -1))
        self.intenseminus.SetSize((-1, -1))
        self.reali.SetSize((-1, -1))
        self.SetMinSize((700, 700))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        
        sizer_2.Add(self.p1, 1, wx.EXPAND, 0)
        sizer_4.Add(self.intenseplus, 0, 0, 0)
        sizer_4.Add(self.intenseminus, 0, 0, 0)
#        sizer_4.Add(self.bclear, 0, 0, 0)
        sizer_5.Add(self.reali, 0, 0, 0)
        sizer_5.Add(self.burefresh, 0, 0, 0)
        sizer_3.Add(sizer_5, 0, 0, 0)
        sizer_3.Add(sizer_4, 0, 0, 0)
        
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizerAndFit(sizer_1)
        sizer_1.SetSizeHints(self)
        self.Layout()
        self.Center()
        
    def vtkversion(self):
#        print(vtk.vtkVersion.GetVTKSourceVersion())
        version = vtk.vtkVersion()
        v=version.GetVTKMajorVersion()
        return v
    def onClear(self,e):
        self.ren.RemoveAllViewProps()  # Close the frame.
        self.marker.SetEnabled(0)
        self.Refresh()
        
    def onRefresh(self,e):
        self.s=1
        self.onClear(e)
        data=self.ondata(self.fullname)
        self.renderthis(data) 
        self.Refresh()
    def onreali(self,e):
        self.onClear(e)
        self.s="m:"+str(1000)
        data=self.ondata(self.fullname)
        self.renderthis(data) 
    def onintensityplus(self,e):
        self.bglyth.SetScaleFactor(self.bglyth.GetScaleFactor()*2)
        self.Refresh()
    def onintensityminus(self,e):
        self.bglyth.SetScaleFactor(self.bglyth.GetScaleFactor()/2)
        self.Refresh()
    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def renderthis(self, data):
            ren = vtk.vtkRenderer()
            self.ren=ren
            self.p1.widget.GetRenderWindow().AddRenderer(ren)
            camera =vtk.vtkCamera()
            camera.SetPosition(0, 0, 0)
            camera.SetFocalPoint(0.255739,  0.207345,  0.439719)
            camera.ParallelProjectionOn()
            ball = vtk.vtkSphereSource()
            ball.SetRadius(0.1)
            ball.SetThetaResolution(10)
            ball.SetPhiResolution(10)
            ballGlyph = vtk.vtkGlyph3D()
            self.bglyth=ballGlyph
            if self.vtkversion()==6:
               ballGlyph.SetInputData(data)
            elif self.vtkversion()==5:
               ballGlyph.SetInput(data)
            else:
                ballGlyph.SetInputData(data)
            ballGlyph.SetSourceConnection(ball.GetOutputPort())
       
#            ballGlyph.SetScaleModeToScaleByScalar()
#            ballGlyph.SetColorModeToColorByScalar()
#            ballGlyph.SetScaleFactor(1.0)
            colorTransferFunction = vtk.vtkColorTransferFunction()
            colorTransferFunction.AddRGBPoint(255, 45, 45, 1.0)
            
            ballMapper = vtk.vtkPolyDataMapper()
            ballMapper.SetInputConnection(ballGlyph.GetOutputPort())
            ballMapper.ScalarVisibilityOff()
            ballMapper.SetLookupTable(colorTransferFunction)
            ballActor = vtk.vtkActor()
            ballActor.SetMapper(ballMapper)
            ballActor.GetProperty().SetColor(1, 1, 1)
            ren.AddActor(ballActor)
            ren.SetActiveCamera(camera);
            ren.SetBackground(0.03, 0.1, 0.2)
            ######################################AXES##################################################
            axes = vtk.vtkAxesActor()
            self.marker = vtk.vtkOrientationMarkerWidget()
            self.marker.SetInteractor( self.p1.widget)
            self.marker.SetOrientationMarker( axes )
            self.marker.SetViewport(0.75,0,1,0.25)
            self.marker.SetEnabled(1)
            ############################################################################################
          
            pointPicker = vtk.vtkPropPicker()
#            pointer=vtk.vtkSmartPointer.pointPicker
#            pointPicker.SetTolerance(100)
            self.p1.widget.SetPicker(pointPicker)
        
        
            ren.ResetCamera()
            ren.ResetCameraClippingRange()
            cam = ren.GetActiveCamera()
            cam.Elevation(0)
            cam.Azimuth(0)
            self.isploted = True
            print(self.isploted)
 
        
    def ondata(self, fullname):
            data = vtk.vtkPolyData()
            data.SetPoints(readPoints(self.fullname))
            data.GetPointData().SetScalars(readScalars(self.fullname, self.s))
            self.data=data
            return data
    def load(self, e, fullname):
        self.fullname=fullname
        data=self.ondata(fullname)
        self.renderthis(data) 
    def OnOpen(self,e):
        """ Open a file"""
        if ossystem.startswith("win"):
            self.wildcard = "Reflection file (*.hkl)|*.hkl;*.HKL|XDS spot file (*.xds)|*.xds;*.XDS|hkl2000 input file (*.sca)|*.sca|Data collection parameter file (*.p4p)|*.p4p|All Files (*)|*"
        else:
            self.wildcard = "Reflection file (*.hkl)|*.hkl;*.HKL|XDS SPOT file (*.xds)|*.xds;*.XDS|hkl2000 input file (*.sca)|*.sca|Data collection parameter file (*.p4p)|*.p4p|All Files (*)|*"
        if self.isploted==True:
           self.onClear(e)
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", self.wildcard, wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            fullname=os.path.join(self.dirname, self.filename)
            self.fullname=fullname
            self.load(e, fullname)
        dlg.Destroy()           