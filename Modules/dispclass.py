"""Element: functions for element types
   Copyright: 2008, Robert B. Von Dreele (Argonne National Laboratory)
"""

#import wx
import math
import sys
import os.path
#import  wx.lib.colourselect as wscs
#import wx.lib.buttons as wlb

class disper(object):
    def __init__(self, element, energy, path):
        self.path=path
        self.energy=energy
        self.element=element
        orb=self.GetXsectionCoeff(element)
        self.fpps(orb, energy)  
    def GetXsectionCoeff(self, El):
        """Read atom orbital scattering cross sections for fprime calculations via Cromer-Lieberman algorithm
        @param El: 2 character element symbol
        @return: Orbs: list of orbitals each a dictionary with detailed orbital information used by FPcalc
        each dictionary is:
        'OrbName': Orbital name read from file
        'IfBe' 0/2 depending on orbital
        'BindEn': binding energy
        'BB': BindEn/0.02721
        'XSectIP': 5 cross section inflection points
        'ElEterm': energy correction term
        'SEdge': absorption edge for orbital
        'Nval': 10/11 depending on IfBe
        'LEner': 10/11 values of log(energy)
        'LXSect': 10/11 values of log(cross section)
        """
        AU = 2.80022e+7
        C1 = 0.02721
        ElS = El.upper()
        ElS = ElS.ljust(2)
        filename = os.path.join(sys.path[0],"data",'Xsect.dat')
        try:
            xsec = open(filename,'Ur')
        except:
            print "File Xsect.dat not found in directory %s" % sys.path[0]
            #wx.MessageBox(message="File Xsect.dat not found in directory %s" % sys.path[0],
            #    caption="No Xsect.dat file",style=wx.OK | wx.ICON_EXCLAMATION |wx.STAY_ON_TOP)
            sys.exit()
        S = '1'
        Orbs = []
        while S:
            S = xsec.readline()
            if S[:2] == ElS:
                S = S[:-1]+xsec.readline()[:-1]+xsec.readline()
                OrbName = S[9:14]
                S = S[14:]
                IfBe = int(S[0])
                S = S[1:]
                val = S.split()
                BindEn = float(val[0])
                self.BB = BindEn/C1
                Orb = {'OrbName':OrbName,'IfBe':IfBe,'BindEn':BindEn,'BB':self.BB}
                Energy = []
                XSect = []
                for i in range(11):
                    Energy.append(float(val[2*i+1]))
                    XSect.append(float(val[2*i+2]))
                XSecIP = []
                for i in range(5): XSecIP.append(XSect[i+5]/AU)
                Orb['XSecIP'] = XSecIP
                if IfBe == 0:
                    Orb['SEdge'] = XSect[10]/AU
                    Nval = 11
                else:
                    Orb['ElEterm'] = XSect[10]
                    del Energy[10]
                    del XSect[10]
                    Nval = 10
                    Orb['SEdge'] = 0.0
                Orb['Nval'] = Nval
                D = dict(zip(Energy,XSect))
                Energy.sort()
                X = []
                for key in Energy:
                    X.append(D[key])
                XSect = X
                LEner = []
                LXSect = []
                for i in range(Nval):
                    LEner.append(math.log(Energy[i]))
                    if XSect[i] > 0.0:
                        LXSect.append(math.log(XSect[i]))
                    else:
                        LXSect.append(0.0)
                Orb['LEner'] = LEner
                Orb['LXSect'] = LXSect
                Orbs.append(Orb)
        xsec.close()
    #    print(Orbs)
        return Orbs
    
    def Aitken(self, Orb, LKev):
        Nval = Orb['Nval']
        j = Nval-1
        LEner = Orb['LEner']
        for i in range(Nval):
            if LEner[i] <= LKev: j = i
        if j > Nval-3: j= Nval-3
        T = [0,0,0,0,0,0]
        LXSect = Orb['LXSect']
        for i in range(3):
           T[i] = LXSect[i+j]
           T[i+3] = LEner[i+j]-LKev
        T[1] = (T[0]*T[4]-T[1]*T[3])/(LEner[j+1]-LEner[j])
        T[2] = (T[0]*T[5]-T[2]*T[3])/(LEner[j+2]-LEner[j])
        T[2] = (T[1]*T[5]-T[2]*T[4])/(LEner[j+2]-LEner[j+1])
        C = T[2]
        return C
    
    def DGauss(self, Orb,CX,RX,ISig):
        ALG = (0.11846344252810,0.23931433524968,0.284444444444,
        0.23931433524968,0.11846344252810)
        XLG = (0.04691007703067,0.23076534494716,0.5,
        0.76923465505284,0.95308992296933)
        
        D = 0.0
        B2 = Orb['BB']**2
        R2 = RX**2
        XSecIP = Orb['XSecIP']
        for i in range(5):
            X = XLG[i]
            X2 = X**2
            XS = XSecIP[i]
            if ISig == 0:
                S = self.BB*(XS*(B2/X2)-CX*R2)/(R2*X2-B2)
            elif ISig == 1:
                S = 0.5*self.BB*B2*XS/(math.sqrt(X)*(R2*X2-X*B2))
            elif ISig == 2:
                T = X*X2*R2-B2/X
                S = 2.0*self.BB*(XS*B2/(T*X2**2)-(CX*R2/T))
            else:
                S = self.BB*B2*(XS-Orb['SEdge']*X2)/(R2*X2**2-X2*B2)
            A = ALG[i]
            D += A*S
        return D 
    def  fpps(self, Orbs, KEv):   
        AU = 2.80022e+7
        C1 = 0.02721
        C = 137.0367
        FP = 0.0
        FPP = 0.0
        Mu = 0.0
        LKev = math.log(KEv)
        RX = KEv/C1
        if Orbs:
            for Orb in Orbs:
                CX = 0.0
                BB = Orb['BB']
                BindEn = Orb['BindEn']
                if Orb['IfBe'] != 0: ElEterm = Orb['ElEterm']
                if BindEn <= KEv:
                    CX = math.exp(self.Aitken(Orb,LKev))
                    Mu += CX
                    CX /= AU
                Corr = 0.0
                if Orb['IfBe'] == 0 and BindEn >= KEv:
                    CX = 0.0
                    FPI = self.DGauss(Orb,CX,RX,3)
                    Corr = 0.5*Orb['SEdge']*BB**2*math.log((RX-BB)/(-RX-BB))/RX
                else:
                    FPI = self.DGauss(Orb,CX,RX,Orb['IfBe'])
                    if CX != 0.0: Corr = -0.5*CX*RX*math.log((RX+BB)/(RX-BB))
                FPI = (FPI+Corr)*C/(2.0*math.pi**2)
                FPPI = C*CX*RX/(4.0*math.pi)
                FP += FPI
                FPP += FPPI
            FP -= ElEterm
        print(round(FP, 4), round(FPP, 4), round(Mu, 2))
        return (FP, FPP, Mu)
    """
    CELL  0.68881   20.2280    9.8620   22.7260    90.000    90.000    90.000
    ZERR        4    0.0040    0.0020    0.0050     0.000     0.000     0.000
    LATT 1
    SYMM     0.50000 - X ,            - Y ,    0.50000 + Z
    SYMM     0.50000 + X ,    0.50000 - Y ,    0.50000 - Z
    SYMM             - X ,    0.50000 + Y ,            - Z
    SFAC C H B CO F N
    DISP  C     0.003     0.002      10.6
    DISP  H     0.000     0.000       0.7
    DISP  B     0.001     0.001       6.2
    DISP Co     0.348     0.924    3658.2
    DISP  F     0.016     0.010      46.7
    DISP  N     0.006     0.003      18.0"""
disper("Co", 18.000, sys.path[0]) 

