import math
import ast
from math import e
from decimal import *
getcontext().prec = 28


def toList(NestedTuple):
    return list(map(toList, NestedTuple)) if isinstance(NestedTuple, (list, tuple)) else NestedTuple


def Init():
    global vehTypesEquipped
    global vehsAttributes
    global vehsAttNames
    
    vehsAttributes = []
    vehsAttNames = []
    vehTypesAttributes = Vissim.Net.VehicleTypes.GetMultipleAttributes(['No', 'IsConnected'])
    vehTypesEquipped = [x[0] for x in vehTypesAttributes if x[1] == True]
    


def GetVissimDataVehicles():
    global vehsAttributes
    global vehsAttNames
    vehsAttributesNames = ['No', 'VehType\No','Lane\Link', 'Speed','InQueue','NumStops','DistanceToSigHead']
    vehsAttributes = toList(Vissim.Net.Vehicles.GetMultipleAttributes(vehsAttributesNames))
    vehsAttNames = {}
    cnt = 0
    for att in vehsAttributesNames:
        vehsAttNames.update({att: cnt})
        cnt += 1



def GetSignalsData():
    global SignalAttributes
    global SigAttNames
    SignalAttributes = []
    SigAttNames = []
    SignalAttributesNames = ['No','GreenStart', 'GreenEnd', 'SigState', 'GreenTimeDuration']
    SignalAttributes = toList(Vissim.Net.SignalControllers.ItemByKey(1).SGs.GetMultipleAttributes(SignalAttributesNames))
    SigAttNames = {}
    ctt = 0
    for ftt in SignalAttributesNames:
        SigAttNames.update({ftt: ctt})
        ctt+=1


def GetLinksData():
    global LinkAttributes
    global LinAttNames
    LinkAttributes = []
    LinAttNames = []
    LinkAttributesNames = ['No','Count:Vehs']
    LinkAttributes = toList(Vissim.Net.Links.GetMultipleAttributes(LinkAttributesNames))
    LinAttNames = {}
    ppc = 0
    for ftt in LinkAttributesNames:
        LinAttNames.update({ftt: ppc})
        ppc+=1


def Signal():

    Seconds = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    CLength=60
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('ContrByCOM',True)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('ContrByCOM',True)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('ContrByCOM',True)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('ContrByCOM',True)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('GreenTimeDuration',27)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('GreenTimeDuration',27)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenTimeDuration',27)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('GreenTimeDuration',27)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('GreenStart',2)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenTimeDuration'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')+3)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenTimeDuration'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')+3)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenTimeDuration'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')+3)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenStart')+Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenTimeDuration'))


    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('GreenTimeDuration',27)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenTimeDuration',27)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('GreenTimeDuration',27)
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('GreenTimeDuration',27)



    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenStart'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenStart'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('GreenEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('GreenStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenStart'))
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('GreenEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd'))



    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenStart')-1:
        if Seconds <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:               
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','GREEN')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
            if Seconds < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')+2:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')


    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenStart')-1:
        if Seconds <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','GREEN')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
       
        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
            if Seconds < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')+2:                 
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')


    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')-1:
        if Seconds <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','GREEN')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
            if Seconds < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')+2:             
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')


    if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenStart')-1:
        if Seconds <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','GREEN')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')


        if Seconds >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-1:             
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SigState','RED')
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SigState','RED')





def SFR():


    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    CySec = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    SimSec = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')

    if SimSec<=1:

        f2= open("3.txt","w")
        f2.close()

        f2= open("4.txt","w")
        f2.close()
        Vissim.Net.Detectors.ItemByKey(1).SetAttValue('VehicleNumber',0)
        Vissim.Net.Detectors.ItemByKey(2).SetAttValue('VehicleNumber',0)
        Vissim.Net.Detectors.ItemByKey(3).SetAttValue('VehicleNumber',0)
        Vissim.Net.Detectors.ItemByKey(4).SetAttValue('VehicleNumber',0)
        Vissim.Net.Detectors.ItemByKey(9).SetAttValue('VehicleNumber',0)
        Vissim.Net.Detectors.ItemByKey(10).SetAttValue('VehicleNumber',0)
        Vissim.Net.Detectors.ItemByKey(11).SetAttValue('VehicleNumber',0)
        Vissim.Net.Detectors.ItemByKey(12).SetAttValue('VehicleNumber',0)



        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('SFR',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue('SFR',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue('SFR',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue('SFR',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue('SFR',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue('SFR',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue('SFR',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue('SFR',0)



        Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('vh',0)
        Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('vh',0)
        Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('vh',0)
        Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('vh',0)

        Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('vh',0)
        Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('vh',0)
        Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('vh',0)
        Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('vh',0)



    s1=0

    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenStart')+4:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-4:
            if Vissim.Net.Links.ItemByKey(8).AttValue ('Count:Vehs')>=15:
                if Vissim.Net.Links.ItemByKey(8).AttValue ('Max:Vehs\InQueue')==1:
                    kp = Vissim.Net.Detectors.ItemByKey(1).AttValue ('VehNo')        
                    if kp > 0:
                        s1=kp
                    if s1>0:
                        f2= open("3.txt","a")
                        f2.write(str(s1))
                        f2.write("\n")
                        f2.close()
                        Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('vh',1)


        
        if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-2:
            if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
                if Vissim.Net.Detectors.ItemByKey(1).AttValue ('vh')==1:
                    f2 = open("3.txt","r")                        
                    ggg = f2.readlines()
                    f2.close()
                    s2=[]
                    for x in ggg:
                        if x not in s2:
                            s2.append(x)
                    kk=len(s2)
                    Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('VehicleNumber',kk)
                    SFR1=round((Vissim.Net.Detectors.ItemByKey(1).AttValue ('VehicleNumber')/((Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-4)-(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenStart')+4)))*3600)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SFR',SFR1)                    
                    f2= open("SFR1a.txt","a")
                    f2.write(str(SFR1)+',')
                    f2.write("\n")
                    f2.close()
                if Vissim.Net.Detectors.ItemByKey(1).AttValue ('vh')==0:
                    Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('VehicleNumber',-10)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('SFR',-10)                    
                    f2= open("SFR1a.txt","a")
                    f2.write(str(-10)+',')
                    f2.write("\n")
                    f2.close()                    



    
    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd'):
            f2= open("3.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(1).SetAttValue('VehicleNumber',0)

            Vissim.Net.Detectors.ItemByKey(1).SetAttValue ('vh',0)
                
        












    s3=0

    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenStart')+4:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-4:
            if Vissim.Net.Links.ItemByKey(16).AttValue ('Count:Vehs')>=15:
                if Vissim.Net.Links.ItemByKey(16).AttValue ('Max:Vehs\InQueue')==1:
                    kp = Vissim.Net.Detectors.ItemByKey(10).AttValue ('VehNo')        
                    if kp > 0:
                        s3=kp
                    if s3>0:
                        f2= open("4.txt","a")
                        f2.write(str(s3))
                        f2.write("\n")
                        f2.close()
                        Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('vh',1)


        
        if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-2:
            if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-1:
                if Vissim.Net.Detectors.ItemByKey(10).AttValue ('vh')==1:
                    f2 = open("4.txt","r")                        
                    ggg = f2.readlines()
                    f2.close()
                    s4=[]
                    for x in ggg:
                        if x not in s4:
                            s4.append(x)
                    kk=len(s4)
                    Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('VehicleNumber',kk)
                    SFR1=round((Vissim.Net.Detectors.ItemByKey(10).AttValue ('VehicleNumber')/((Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-4)-(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenStart')+4)))*3600)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('SFR',SFR1)                    
                    f2= open("SFR1b.txt","a")
                    f2.write(str(SFR1)+',')
                    f2.write("\n")
                    f2.close()
                if Vissim.Net.Detectors.ItemByKey(10).AttValue ('vh')==0:
                    Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('VehicleNumber',-10)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('SFR',-10)                    
                    f2= open("SFR1b.txt","a")
                    f2.write(str(-10)+',')
                    f2.write("\n")
                    f2.close()                    


    
    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-1:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd'):
            f2= open("4.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(10).SetAttValue('VehicleNumber',0)

            Vissim.Net.Detectors.ItemByKey(10).SetAttValue ('vh',0)















    s1=0

    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenStart')+4:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-4:
            if Vissim.Net.Links.ItemByKey(4).AttValue ('Count:Vehs')>=15:
                if Vissim.Net.Links.ItemByKey(4).AttValue ('Max:Vehs\InQueue')==1:
                    kp = Vissim.Net.Detectors.ItemByKey(2).AttValue ('VehNo')        
                    if kp > 0:
                        s1=kp
                    if s1>0:
                        f2= open("3.txt","a")
                        f2.write(str(s1))
                        f2.write("\n")
                        f2.close()
                        Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('vh',1)
        
        if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-2:
            if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
                if Vissim.Net.Detectors.ItemByKey(2).AttValue ('vh')==1:
                    f2 = open("3.txt","r")                        
                    ggg = f2.readlines()
                    f2.close()
                    s2=[]
                    for x in ggg:
                        if x not in s2:
                            s2.append(x)
                    kk=len(s2)
                    Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('VehicleNumber',kk)
                    SFR1=round((Vissim.Net.Detectors.ItemByKey(2).AttValue ('VehicleNumber')/((Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-4)-(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenStart')+4)))*3600)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SFR',SFR1)
                    
                    f2= open("SFR2a.txt","a")
                    f2.write(str(SFR1)+',')
                    f2.write("\n")
                    f2.close()

                if Vissim.Net.Detectors.ItemByKey(2).AttValue ('vh')==0:
                    Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('VehicleNumber',-10)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('SFR',-10)                    
                    f2= open("SFR2a.txt","a")
                    f2.write(str(-10)+',')
                    f2.write("\n")
                    f2.close()     

    
    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd'):
            f2= open("3.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(2).SetAttValue('VehicleNumber',0)

            Vissim.Net.Detectors.ItemByKey(2).SetAttValue ('vh',0)
                
        
        






    s3=0

    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+4:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-4:
            if Vissim.Net.Links.ItemByKey(14).AttValue ('Count:Vehs')>=15:
                if Vissim.Net.Links.ItemByKey(14).AttValue ('Max:Vehs\InQueue')==1:
                    kp = Vissim.Net.Detectors.ItemByKey(12).AttValue ('VehNo')        
                    if kp > 0:
                        s3=kp
                    if s3>0:
                        f2= open("4.txt","a")
                        f2.write(str(s3))
                        f2.write("\n")
                        f2.close()
                        Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('vh',1)
        
        if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-2:
            if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-1:
                if Vissim.Net.Detectors.ItemByKey(12).AttValue ('vh')==1:
                    f2 = open("4.txt","r")                        
                    ggg = f2.readlines()
                    f2.close()
                    s4=[]
                    for x in ggg:
                        if x not in s4:
                            s4.append(x)
                    kk=len(s4)
                    Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('VehicleNumber',kk)
                    SFR1=round((Vissim.Net.Detectors.ItemByKey(12).AttValue ('VehicleNumber')/((Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-4)-(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenStart')+4)))*3600)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SFR',SFR1)
                    
                    f2= open("SFR2b.txt","a")
                    f2.write(str(SFR1)+',')
                    f2.write("\n")
                    f2.close()

                if Vissim.Net.Detectors.ItemByKey(12).AttValue ('vh')==0:
                    Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('VehicleNumber',-10)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('SFR',-10)                    
                    f2= open("SFR2b.txt","a")
                    f2.write(str(-10)+',')
                    f2.write("\n")
                    f2.close()     

    
    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-1:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd'):
            f2= open("4.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(12).SetAttValue('VehicleNumber',0)

            Vissim.Net.Detectors.ItemByKey(12).SetAttValue ('vh',0)
                
        














    s1=0

    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+4:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-4:
            if Vissim.Net.Links.ItemByKey(5).AttValue ('Count:Vehs')>=15:
                if Vissim.Net.Links.ItemByKey(5).AttValue ('Max:Vehs\InQueue')==1:
                    kp = Vissim.Net.Detectors.ItemByKey(3).AttValue ('VehNo')        
                    if kp > 0:
                        s1=kp
                    if s1>0:
                        f2= open("3.txt","a")
                        f2.write(str(s1))
                        f2.write("\n")
                        f2.close()
                        Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('vh',1)
        
        if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-2:
            if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
                if Vissim.Net.Detectors.ItemByKey(3).AttValue ('vh')==1:
                    f2 = open("3.txt","r")                        
                    ggg = f2.readlines()
                    f2.close()
                    s2=[]
                    for x in ggg:
                        if x not in s2:
                            s2.append(x)
                    kk=len(s2)
                    Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('VehicleNumber',kk)
                    SFR1=round((Vissim.Net.Detectors.ItemByKey(3).AttValue ('VehicleNumber')/((Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-4)-(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenStart')+4)))*3600)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SFR',SFR1)
                    
                    f2= open("SFR3a.txt","a")
                    f2.write(str(SFR1)+',')
                    f2.write("\n")
                    f2.close()



                if Vissim.Net.Detectors.ItemByKey(3).AttValue ('vh')==0:
                    Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('VehicleNumber',-10)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('SFR',-10)                    
                    f2= open("SFR3b.txt","a")
                    f2.write(str(-10)+',')
                    f2.write("\n")
                    f2.close()     

    
    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd'):
            f2= open("3.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(3).SetAttValue('VehicleNumber',0)

            Vissim.Net.Detectors.ItemByKey(3).SetAttValue ('vh',0)
                







    s3=0

    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenStart')+4:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-4:
            if Vissim.Net.Links.ItemByKey(12).AttValue ('Count:Vehs')>=15:
                if Vissim.Net.Links.ItemByKey(12).AttValue ('Max:Vehs\InQueue')==1:
                    kp = Vissim.Net.Detectors.ItemByKey(11).AttValue ('VehNo')        
                    if kp > 0:
                        s3=kp
                    if s3>0:
                        f2= open("4.txt","a")
                        f2.write(str(s3))
                        f2.write("\n")
                        f2.close()
                        Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('vh',1)
        
        if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-2:
            if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-1:
                if Vissim.Net.Detectors.ItemByKey(11).AttValue ('vh')==1:
                    f2 = open("4.txt","r")                        
                    ggg = f2.readlines()
                    f2.close()
                    s4=[]
                    for x in ggg:
                        if x not in s4:
                            s4.append(x)
                    kk=len(s4)
                    Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('VehicleNumber',kk)
                    SFR1=round((Vissim.Net.Detectors.ItemByKey(11).AttValue ('VehicleNumber')/((Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-4)-(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenStart')+4)))*3600)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('SFR',SFR1)
                    
                    f2= open("SFR3b.txt","a")
                    f2.write(str(SFR1)+',')
                    f2.write("\n")
                    f2.close()



                if Vissim.Net.Detectors.ItemByKey(11).AttValue ('vh')==0:
                    Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('VehicleNumber',-10)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('SFR',-10)                    
                    f2= open("SFR3b.txt","a")
                    f2.write(str(-10)+',')
                    f2.write("\n")
                    f2.close()     

    
    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-1:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd'):
            f2= open("4.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(11).SetAttValue('VehicleNumber',0)

            Vissim.Net.Detectors.ItemByKey(11).SetAttValue ('vh',0)
                





    s1=0

    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenStart')+4:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-4:
            if Vissim.Net.Links.ItemByKey(1).AttValue ('Count:Vehs')>=15:
                if Vissim.Net.Links.ItemByKey(1).AttValue ('Max:Vehs\InQueue')==1:
                    kp = Vissim.Net.Detectors.ItemByKey(4).AttValue ('VehNo')        
                    if kp > 0:
                        s1=kp
                    if s1>0:
                        f2= open("3.txt","a")
                        f2.write(str(s1))
                        f2.write("\n")
                        f2.close()
                        Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('vh',1)
        
        if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-2:
            if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-1:
                if Vissim.Net.Detectors.ItemByKey(4).AttValue ('vh')==1:
                    f2 = open("3.txt","r")                        
                    ggg = f2.readlines()
                    f2.close()
                    s2=[]
                    for x in ggg:
                        if x not in s2:
                            s2.append(x)
                    kk=len(s2)
                    Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('VehicleNumber',kk)
                    SFR1=round((Vissim.Net.Detectors.ItemByKey(4).AttValue ('VehicleNumber')/((Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-4)-(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenStart')+4)))*3600)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SFR',SFR1)
                    
                    f2= open("SFR4a.txt","a")
                    f2.write(str(SFR1)+',')
                    f2.write("\n")
                    f2.close()

                if Vissim.Net.Detectors.ItemByKey(4).AttValue ('vh')==0:
                    Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('VehicleNumber',-10)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('SFR',-10)                    
                    f2= open("SFR4a.txt","a")
                    f2.write(str(-10)+',')
                    f2.write("\n")
                    f2.close()     


    
    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-1:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd'):
            f2= open("3.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(4).SetAttValue('VehicleNumber',0)

            Vissim.Net.Detectors.ItemByKey(4).SetAttValue ('vh',0)








    s3=0

    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenStart')+4:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-4:
            if Vissim.Net.Links.ItemByKey(9).AttValue ('Count:Vehs')>=15:
                if Vissim.Net.Links.ItemByKey(9).AttValue ('Max:Vehs\InQueue')==1:
                    kp = Vissim.Net.Detectors.ItemByKey(9).AttValue ('VehNo')        
                    if kp > 0:
                        s3=kp
                    if s3>0:
                        f2= open("4.txt","a")
                        f2.write(str(s3))
                        f2.write("\n")
                        f2.close()
                        Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('vh',1)
        
        if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-2:
            if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-1:
                if Vissim.Net.Detectors.ItemByKey(9).AttValue ('vh')==1:
                    f2 = open("4.txt","r")                        
                    ggg = f2.readlines()
                    f2.close()
                    s4=[]
                    for x in ggg:
                        if x not in s4:
                            s4.append(x)
                    kk=len(s4)
                    Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('VehicleNumber',kk)
                    SFR1=round((Vissim.Net.Detectors.ItemByKey(9).AttValue ('VehicleNumber')/((Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-4)-(Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenStart')+4)))*3600)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('SFR',SFR1)
                    
                    f2= open("SFR4b.txt","a")
                    f2.write(str(SFR1)+',')
                    f2.write("\n")
                    f2.close()

                if Vissim.Net.Detectors.ItemByKey(9).AttValue ('vh')==0:
                    Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('VehicleNumber',-10)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('SFR',-10)                    
                    f2= open("SFR4b.txt","a")
                    f2.write(str(-10)+',')
                    f2.write("\n")
                    f2.close()     


    
    if CySec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-1:
        if CySec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd'):
            f2= open("4.txt","w")
            f2.close()
            Vissim.Net.Detectors.ItemByKey(9).SetAttValue('VehicleNumber',0)

            Vissim.Net.Detectors.ItemByKey(9).SetAttValue ('vh',0)




def A1():
    global A11
    global A12
    global A13
    global A14
    Cl=120
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    CySec = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    SimSec = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')


    if SimSec <=1:

        f2= open("11.txt","w")
        f2.close()

        f2= open("12.txt","w")
        f2.close()


        f2= open("13.txt","w")
        f2.close()


        f2= open("14.txt","w")
        f2.close()


        f2= open("1001.txt","w")
        f2.close()

        f2= open("1002.txt","w")
        f2.close()


        f2= open("1003.txt","w")
        f2.close()


        f2= open("1004.txt","w")
        f2.close()


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('GreenEnd'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleStart')+Cl)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleStart')+Cl)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('CycleEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleStart')+Cl)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('CycleEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleStart')+Cl)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleStart'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleStart'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleStart'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('CycleEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleStart'))
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('CycleEnd', Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd'))








        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('n',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('n',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('n',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('n',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A1',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A2',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A2',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A2',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A2',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A3',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A3',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A3',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A3',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A4',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A4',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A4',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A4',0)


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A5',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A5',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A5',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A5',0)


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('n',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('n',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('n',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('n',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A1',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A2',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A2',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A2',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A2',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A3',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A3',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A3',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A3',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A4',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A4',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A4',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A4',0)


        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A5',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A5',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A5',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A5',0)




    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleStart'):
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd')-3:          
            f1=0
            kp = Vissim.Net.Detectors.ItemByKey(5).AttValue ('VehNo')        
            if kp > 0:
                f1=kp
            if f1>0:
                f2= open("11.txt","a")
                f2.write(str(f1))
                f2.write("\n")
                f2.close()            
            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd')-4:
                f2 = open("11.txt","r")                        
                ggg = f2.readlines()
                f2.close()
                s2=[]
                for x in ggg:
                    if x not in s2:
                        s2.append(x)
                kk=len(s2)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('n',kk)

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-2:
            pp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('n')]
            pp2=[]
            kk=0
            for i in range(len(pp)):
                if pp[i]>0:
                    pp2.append(i)
                    kk=kk+pp[i]
            if len(pp2)==len(pp):
                A11=pp[0]/kk
                f2= open("A11a.txt","a")
                f2.write(str(A11)+',')
                f2.write("\n")
                f2.close()
            if len(pp2)<len(pp):
                A11=-10
                f2= open("A11a.txt","a")
                f2.write(str(-10)+',')
                f2.write("\n")
                f2.close()
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A1',A11)

                    
            
    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd'):
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd')+1:     
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleStart')+Cl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd')+Cl)
            f2= open("11.txt","w")
            f2.close()
            
















    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleStart'):
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd')-3:          
            f1001=0
            kp = Vissim.Net.Detectors.ItemByKey(16).AttValue ('VehNo')        
            if kp > 0:
                f1001=kp
            if f1001>0:
                f2= open("1001.txt","a")
                f2.write(str(f1001))
                f2.write("\n")
                f2.close()            
            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd')-4:
                f2 = open("1001.txt","r")                        
                ggg = f2.readlines()
                f2.close()
                s2=[]
                for x in ggg:
                    if x not in s2:
                        s2.append(x)
                kk=len(s2)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('n',kk)

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-2:
            pp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('n')]
            pp2=[]
            kk=0
            for i in range(len(pp)):
                if pp[i]>0:
                    pp2.append(i)
                    kk=kk+pp[i]
            if len(pp2)==len(pp):
                A11=pp[4]/kk
                f2= open("A11b.txt","a")
                f2.write(str(A11)+',')
                f2.write("\n")
                f2.close()
            if len(pp2)<len(pp):
                A11=-10
                f2= open("A11b.txt","a")
                f2.write(str(-10)+',')
                f2.write("\n")
                f2.close()
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A1',A11)

                    
            
    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd'):
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd')+1:     
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleStart')+Cl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd')+Cl)
            f2= open("1001.txt","w")
            f2.close()
            































    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleStart'):
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd')-3:          
            f6=0
            kp6 = Vissim.Net.Detectors.ItemByKey(6).AttValue ('VehNo')        
            if kp6 > 0:
                f6=kp6
            if f6>0:
                f2= open("12.txt","a")
                f2.write(str(f6))
                f2.write("\n")
                f2.close()            
            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd')-4:
                f2 = open("12.txt","r")                        
                ggg = f2.readlines()
                f2.close()
                s6=[]
                for x in ggg:
                    if x not in s6:
                        s6.append(x)
                kk6=len(s6)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('n',kk6)


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-2:

            pp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('n')]
            pp2=[]
            kk=0
            for i in range(len(pp)):
                if pp[i]>0:
                    pp2.append(i)
                    kk=kk+pp[i]
            if len(pp2)==len(pp):
                A12=pp[1]/kk
                f2= open("A12a.txt","a")
                f2.write(str(A12)+',')
                f2.write("\n")
                f2.close()
            if len(pp2)<len(pp):
                A12=-10
                f2= open("A12a.txt","a")
                f2.write(str(-10)+',')
                f2.write("\n")
                f2.close()
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A1',A12)                    


    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd'):
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd')+1:     
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleStart')+Cl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd')+Cl)
            f2= open("12.txt","w")
            f2.close()
            

















    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleStart'):
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd')-3:          
            f6=0
            kp6 = Vissim.Net.Detectors.ItemByKey(15).AttValue ('VehNo')        
            if kp6 > 0:
                f6=kp6
            if f6>0:
                f2= open("1002.txt","a")
                f2.write(str(f6))
                f2.write("\n")
                f2.close()            
            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd')-4:
                f2 = open("1002.txt","r")                        
                ggg = f2.readlines()
                f2.close()
                s6=[]
                for x in ggg:
                    if x not in s6:
                        s6.append(x)
                kk6=len(s6)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('n',kk6)


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-2:
            pp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('n')]
            pp2=[]
            kk=0
            for i in range(len(pp)):
                if pp[i]>0:
                    pp2.append(i)
                    kk=kk+pp[i]
            if len(pp2)==len(pp):
                A12=pp[5]/kk
                f2= open("A12b.txt","a")
                f2.write(str(A12)+',')
                f2.write("\n")
                f2.close()
            if len(pp2)<len(pp):
                A12=-10
                f2= open("A12b.txt","a")
                f2.write(str(-10)+',')
                f2.write("\n")
                f2.close()
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A1',A12)                    


    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd'):
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd')+1:     
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleStart')+Cl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd')+Cl)
            f2= open("1002.txt","w")
            f2.close()










    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleStart'):
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd')-3:          
            f7=0
            kp7 = Vissim.Net.Detectors.ItemByKey(7).AttValue ('VehNo')        
            if kp7 > 0:
                f7=kp7
            if f7>0:
                f2= open("13.txt","a")
                f2.write(str(f7))
                f2.write("\n")
                f2.close()            
            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd')-4:
                f2 = open("13.txt","r")                        
                ggg = f2.readlines()
                f2.close()
                s7=[]
                for x in ggg:
                    if x not in s7:
                        s7.append(x)
                kk7=len(s7)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('n',kk7)
    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-2:
            pp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('n')]
            pp2=[]
            kk=0
            for i in range(len(pp)):
                if pp[i]>0:
                    pp2.append(i)
                    kk=kk+pp[i]
            if len(pp2)==len(pp):
                A13=pp[2]/kk
                f2= open("A13a.txt","a")
                f2.write(str(A13)+',')
                f2.write("\n")
                f2.close()
            if len(pp2)<len(pp):
                A13=-10
                f2= open("A13a.txt","a")
                f2.write(str(-10)+',')
                f2.write("\n")
                f2.close()
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A1',A13)



    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd'):
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd')+1:     
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleStart')+Cl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd')+Cl)
            f2= open("13.txt","w")
            f2.close()








    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleStart'):
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd')-3:          
            f7=0
            kp7 = Vissim.Net.Detectors.ItemByKey(14).AttValue ('VehNo')        
            if kp7 > 0:
                f7=kp7
            if f7>0:
                f2= open("1003.txt","a")
                f2.write(str(f7))
                f2.write("\n")
                f2.close()            
            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd')-4:
                f2 = open("1003.txt","r")                        
                ggg = f2.readlines()
                f2.close()
                s7=[]
                for x in ggg:
                    if x not in s7:
                        s7.append(x)
                kk7=len(s7)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('n',kk7)
    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-2:
            pp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('n')]
            pp2=[]
            kk=0
            for i in range(len(pp)):
                if pp[i]>0:
                    pp2.append(i)
                    kk=kk+pp[i]
            if len(pp2)==len(pp):
                A13=pp[6]/kk
                f2= open("A13b.txt","a")
                f2.write(str(A13)+',')
                f2.write("\n")
                f2.close()
            if len(pp2)<len(pp):
                A13=-10
                f2= open("A13b.txt","a")
                f2.write(str(-10)+',')
                f2.write("\n")
                f2.close()
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A1',A13)



    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd'):
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd')+1:     
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleStart')+Cl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd')+Cl)
            f2= open("1003.txt","w")
            f2.close()
















    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleStart'):
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd')-3:          
            f8=0
            kp8 = Vissim.Net.Detectors.ItemByKey(8).AttValue ('VehNo')        
            if kp8 > 0:
                f8=kp8
            if f8>0:
                f2= open("14.txt","a")
                f2.write(str(f8))
                f2.write("\n")
                f2.close()            
            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd')-4:
                f2 = open("14.txt","r")                        
                ggg = f2.readlines()
                f2.close()
                s8=[]
                for x in ggg:
                    if x not in s8:
                        s8.append(x)
                kk8=len(s8)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('n',kk8)

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-2:
            pp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('n')]
            pp2=[]
            kk=0
            for i in range(len(pp)):
                if pp[i]>0:
                    pp2.append(i)
                    kk=kk+pp[i]
            if len(pp2)==len(pp):
                A14=pp[3]/kk
                f2= open("A14a.txt","a")
                f2.write(str(A14)+',')
                f2.write("\n")
                f2.close()
            if len(pp2)<len(pp):
                A14=-10
                f2= open("A14a.txt","a")
                f2.write(str(-10)+',')
                f2.write("\n")
                f2.close()
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A1',A14)



    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd'):
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd')+1:     
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleStart')+Cl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd')+Cl)
            f2= open("14.txt","w")
            f2.close()







    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleStart'):
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd')-3:          
            f8=0
            kp8 = Vissim.Net.Detectors.ItemByKey(13).AttValue ('VehNo')        
            if kp8 > 0:
                f8=kp8
            if f8>0:
                f2= open("1004.txt","a")
                f2.write(str(f8))
                f2.write("\n")
                f2.close()            
            if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd')-4:
                f2 = open("1004.txt","r")                        
                ggg = f2.readlines()
                f2.close()
                s8=[]
                for x in ggg:
                    if x not in s8:
                        s8.append(x)
                kk8=len(s8)
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('n',kk8)
    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-2:
            pp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('n'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('n')]
            pp2=[]
            kk=0
            for i in range(len(pp)):
                if pp[i]>0:
                    pp2.append(i)
                    kk=kk+pp[i]
            if len(pp2)==len(pp):
                A14=pp[7]/kk
                f2= open("A14b.txt","a")
                f2.write(str(A14)+',')
                f2.write("\n")
                f2.close()
            if len(pp2)<len(pp):
                A14=-10
                f2= open("A14b.txt","a")
                f2.write(str(-10)+',')
                f2.write("\n")
                f2.close()
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A1',A14)



    if SimSec > Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd'):
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd')+1:     
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('CycleStart',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleStart')+Cl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('CycleEnd',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd')+Cl)
            f2= open("1004.txt","w")
            f2.close()






def A2():
    GetVissimDataVehicles()

    Cl=120
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    CySec = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    SimSec = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')

    if SimSec<=1: 
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('n1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('n1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('n1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('n1',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('s1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('s1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('s1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('s1',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('s',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('s',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('s',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('s',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('n1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('n1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('n1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('n1',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('s1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('s1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('s1',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('s1',0)

        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('s',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('s',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('s',0)
        Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('s',0)



        f2 = open("21.txt","w")
        f2.write(str([]))
        f2.close()

        f2 = open("2100.txt","w")
        f2.write(str([]))
        f2.close()

        f2 = open("2001.txt","w")
        f2.write(str([]))
        f2.close()

        f2 = open("20100.txt","w")
        f2.write(str([]))
        f2.close()





        f2 = open("22.txt","w")
        f2.write(str([]))
        f2.close()


        f2 = open("2200.txt","w")
        f2.write(str([]))
        f2.close()

        f2 = open("2002.txt","w")
        f2.write(str([]))
        f2.close()


        f2 = open("20200.txt","w")
        f2.write(str([]))
        f2.close()




        f2 = open("23.txt","w")
        f2.write(str([]))
        f2.close()


        f2 = open("2300.txt","w")
        f2.write(str([]))
        f2.close()

        f2 = open("2003.txt","w")
        f2.write(str([]))
        f2.close()


        f2 = open("20300.txt","w")
        f2.write(str([]))
        f2.close()



        f2 = open("24.txt","w")
        f2.write(str([]))
        f2.close()

        f2 = open("2400.txt","w")
        f2.write(str([]))
        f2.close()


        f2 = open("2004.txt","w")
        f2.write(str([]))
        f2.close()

        f2 = open("20400.txt","w")
        f2.write(str([]))
        f2.close()





    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd')-5:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd')-4:
            k=0
            k4=[]
            k5=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '8':
                            NumStops=vehAttributes[vehsAttNames['NumStops']]
                            k=k+NumStops
                            No=vehAttributes[vehsAttNames['No']]
                            k4.append(No)
                            k5.append(NumStops)

            f2= open("211.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()

            f2= open("2111.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('s1',k)
            f1 = open("21.txt","r")                        
            kgk = f1.readline()
            f1.close()
            f1 = open("2100.txt","r")                        
            kgg = f1.readline()
            f1.close()

            Aseq = ast.literal_eval(kgk)
            mseg = ast.literal_eval(kgg)
            kl=0
            for vehAttributes in vehsAttributes:
                No=vehAttributes[vehsAttNames['No']]
                if No in Aseq:
                    Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                    if Lane == '8':
                        NumStops=mseg[Aseq.index(No)]   
                        kl=kl+NumStops
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('n1',kl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('s',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('s1')-Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('n1'))


    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd')-4:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('CycleEnd')-3:

            f2 = open("211.txt","r")                        
            kgk = f2.readline()
            f2.close()
            f2 = open("2111.txt","r")                        
            kgg = f2.readline()
            f2.close()


            k4 = ast.literal_eval(kgk)
            k5 = ast.literal_eval(kgg)
            
            f2= open("21.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()       

            f2= open("2100.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()    

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-2:
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A1')>0:
                ppp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('s')]
                ppp2=[]
                kkk=0
                for i in range(len(ppp)):
                    if ppp[i]>0:
                        ppp2.append(i)
                        kkk=kkk+ppp[i]
                if len(ppp2)==len(ppp):
                    A21=(ppp[0]/kkk)/Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A1')
                    f2= open("A21a.txt","a")
                    f2.write(str(A21)+',')
                    f2.write("\n")
                    f2.close()
                if len(ppp2)<len(ppp):
                    A21=-10
                    f2= open("A21a.txt","a")
                    f2.write(str(A21)+',')
                    f2.write("\n")
                    f2.close()
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A1')<= 0:
                A21=-10
                f2= open("A21a.txt","a")
                f2.write(str(A21)+',')
                f2.write("\n")
                f2.close()                
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A2',A21)                    














































    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd')-5:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd')-4:
            k=0
            k4=[]
            k5=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '16':
                            NumStops=vehAttributes[vehsAttNames['NumStops']]
                            k=k+NumStops
                            No=vehAttributes[vehsAttNames['No']]
                            k4.append(No)
                            k5.append(NumStops)

            f2= open("211999.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()

            f2= open("2111999.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('s1',k)
            f1 = open("2001.txt","r")                        
            kgk = f1.readline()
            f1.close()
            f1 = open("20100.txt","r")                        
            kgg = f1.readline()
            f1.close()

            Aseq = ast.literal_eval(kgk)
            mseg = ast.literal_eval(kgg)
            kl=0
            for vehAttributes in vehsAttributes:
                No=vehAttributes[vehsAttNames['No']]
                if No in Aseq:
                    Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                    if Lane == '16':
                        NumStops=mseg[Aseq.index(No)]   
                        kl=kl+NumStops
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('n1',kl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('s',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue('s1')-Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue('n1'))

    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd')-4:
        if SimSec <= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('CycleEnd')-3:

            f2 = open("211999.txt","r")                        
            kgk = f2.readline()
            f2.close()
            f2 = open("2111999.txt","r")                        
            kgg = f2.readline()
            f2.close()


            k4 = ast.literal_eval(kgk)
            k5 = ast.literal_eval(kgg)
            
            f2= open("2001.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()       

            f2= open("20100.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()    

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-2:
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('A1')>0:
                ppp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('s')]
                ppp2=[]
                kkk=0
                for i in range(len(ppp)):
                    if ppp[i]>0:
                        ppp2.append(i)
                        kkk=kkk+ppp[i]
                if len(ppp2)==len(ppp):
                    A21=(ppp[4]/kkk)/Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A1')
                    f2= open("A21b.txt","a")
                    f2.write(str(A21)+',')
                    f2.write("\n")
                    f2.close()
                if len(ppp2)<len(ppp):
                    A21=-10
                    f2= open("A21b.txt","a")
                    f2.write(str(A21)+',')
                    f2.write("\n")
                    f2.close()
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('A1')<= 0:
                A21=-10
                f2= open("A21b.txt","a")
                f2.write(str(A21)+',')
                f2.write("\n")
                f2.close()                
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A2',A21)                    














































    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd')-5:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd')-4:
            k=0
            k4=[]
            k5=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '4':
                            NumStops=vehAttributes[vehsAttNames['NumStops']]
                            k=k+NumStops
                            No=vehAttributes[vehsAttNames['No']]
                            k4.append(No)
                            k5.append(NumStops)

            f2= open("221.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()

            f2= open("2211.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('s1',k)
            f1 = open("22.txt","r")                        
            kgk = f1.readline()
            f1.close()
            f1 = open("2200.txt","r")                        
            kgg = f1.readline()
            f1.close()

            Aseq = ast.literal_eval(kgk)
            mseg = ast.literal_eval(kgg)
            kl=0
            for vehAttributes in vehsAttributes:
                No=vehAttributes[vehsAttNames['No']]
                if No in Aseq:
                    Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                    if Lane == '4':
                        NumStops=mseg[Aseq.index(No)]   
                        kl=kl+NumStops
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('n1',kl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('s',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue('s1')-Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue('n1'))

    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd')-4:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('CycleEnd')-3:

            f2 = open("221.txt","r")                        
            kgk = f2.readline()
            f2.close()
            f2 = open("2211.txt","r")                        
            kgg = f2.readline()
            f2.close()


            k4 = ast.literal_eval(kgk)
            k5 = ast.literal_eval(kgg)
            
            f2= open("22.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()       

            f2= open("2200.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()    




    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-2:
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A1')>0:
                ppp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('s')]
                ppp2=[]
                kkk=0
                for i in range(len(ppp)):
                    if ppp[i]>0:
                        ppp2.append(i)
                        kkk=kkk+ppp[i]
                if len(ppp2)==len(ppp):
                    A22=(ppp[1]/kkk)/Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A1')
                    f2= open("A22a.txt","a")
                    f2.write(str(A22)+',')
                    f2.write("\n")
                    f2.close()
                if len(ppp2)<len(ppp):
                    A22=-10
                    f2= open("A22a.txt","a")
                    f2.write(str(A22)+',')
                    f2.write("\n")
                    f2.close()
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A1')<=0:
                A22=-10
                f2= open("A22a.txt","a")
                f2.write(str(A22)+',')
                f2.write("\n")
                f2.close()                
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A2',A22)       








    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd')-5:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd')-4:
            k=0
            k4=[]
            k5=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '14':
                            NumStops=vehAttributes[vehsAttNames['NumStops']]
                            k=k+NumStops
                            No=vehAttributes[vehsAttNames['No']]
                            k4.append(No)
                            k5.append(NumStops)

            f2= open("221999.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()

            f2= open("2211999.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('s1',k)
            f1 = open("2002.txt","r")                        
            kgk = f1.readline()
            f1.close()
            f1 = open("20200.txt","r")                        
            kgg = f1.readline()
            f1.close()

            Aseq = ast.literal_eval(kgk)
            mseg = ast.literal_eval(kgg)
            kl=0
            for vehAttributes in vehsAttributes:
                No=vehAttributes[vehsAttNames['No']]
                if No in Aseq:
                    Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                    if Lane == '14':
                        NumStops=mseg[Aseq.index(No)]   
                        kl=kl+NumStops
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('n1',kl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('s',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue('s1')-Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue('n1'))

    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd')-4:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('CycleEnd')-3:

            f2 = open("221999.txt","r")                        
            kgk = f2.readline()
            f2.close()
            f2 = open("2211999.txt","r")                        
            kgg = f2.readline()
            f2.close()


            k4 = ast.literal_eval(kgk)
            k5 = ast.literal_eval(kgg)
            
            f2= open("2002.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()       

            f2= open("20200.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()    




    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-2:
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('A1')>0:
                ppp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('s')]
                ppp2=[]
                kkk=0
                for i in range(len(ppp)):
                    if ppp[i]>0:
                        ppp2.append(i)
                        kkk=kkk+ppp[i]
                if len(ppp2)==len(ppp):
                    A22=(ppp[5]/kkk)/Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A1')
                    f2= open("A22b.txt","a")
                    f2.write(str(A22)+',')
                    f2.write("\n")
                    f2.close()
                if len(ppp2)<len(ppp):
                    A22=-10
                    f2= open("A22b.txt","a")
                    f2.write(str(A22)+',')
                    f2.write("\n")
                    f2.close()
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A1')<=0:
                A22=-10
                f2= open("A22b.txt","a")
                f2.write(str(A22)+',')
                f2.write("\n")
                f2.close()                
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A2',A22)       



















    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd')-5:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd')-4:
            k=0
            k4=[]
            k5=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '5':
                            NumStops=vehAttributes[vehsAttNames['NumStops']]
                            k=k+NumStops
                            No=vehAttributes[vehsAttNames['No']]
                            k4.append(No)
                            k5.append(NumStops)

            f2= open("231.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()

            f2= open("2311.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('s1',k)
            f1 = open("23.txt","r")                        
            kgk = f1.readline()
            f1.close()
            f1 = open("2300.txt","r")                        
            kgg = f1.readline()
            f1.close()

            Aseq = ast.literal_eval(kgk)
            mseg = ast.literal_eval(kgg)
            kl=0
            for vehAttributes in vehsAttributes:
                No=vehAttributes[vehsAttNames['No']]
                if No in Aseq:
                    Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                    if Lane == '5':
                        NumStops=mseg[Aseq.index(No)]   
                        kl=kl+NumStops
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('n1',kl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('s',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue('s1')-Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue('n1'))




    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd')-4:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('CycleEnd')-3:

            f2 = open("231.txt","r")                        
            kgk = f2.readline()
            f2.close()
            f2 = open("2311.txt","r")                        
            kgg = f2.readline()
            f2.close()


            k4 = ast.literal_eval(kgk)
            k5 = ast.literal_eval(kgg)
            
            f2= open("23.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()       

            f2= open("2300.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()    



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-2:
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('A1')>0:
                ppp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('s')]
                ppp2=[]
                kkk=0
                for i in range(len(ppp)):
                    if ppp[i]>0:
                        ppp2.append(i)
                        kkk=kkk+ppp[i]
                if len(ppp2)==len(ppp):
                    A23=(ppp[2]/kkk)/Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('A1')
                    f2= open("A23a.txt","a")
                    f2.write(str(A23)+',')
                    f2.write("\n")
                    f2.close()
                if len(ppp2)<len(ppp):
                    A23=-10
                    f2= open("A23a.txt","a")
                    f2.write(str(A23)+',')
                    f2.write("\n")
                    f2.close()
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('A1')<=0:
                A23=-10
                f2= open("A23a.txt","a")
                f2.write(str(A23)+',')
                f2.write("\n")
                f2.close()                
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A2',A23)
















    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd')-5:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd')-4:
            k=0
            k4=[]
            k5=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '12':
                            NumStops=vehAttributes[vehsAttNames['NumStops']]
                            k=k+NumStops
                            No=vehAttributes[vehsAttNames['No']]
                            k4.append(No)
                            k5.append(NumStops)

            f2= open("231999.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()

            f2= open("2311999.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('s1',k)
            f1 = open("2003.txt","r")                        
            kgk = f1.readline()
            f1.close()
            f1 = open("20300.txt","r")                        
            kgg = f1.readline()
            f1.close()

            Aseq = ast.literal_eval(kgk)
            mseg = ast.literal_eval(kgg)
            kl=0
            for vehAttributes in vehsAttributes:
                No=vehAttributes[vehsAttNames['No']]
                if No in Aseq:
                    Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                    if Lane == '12':
                        NumStops=mseg[Aseq.index(No)]   
                        kl=kl+NumStops
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('n1',kl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('s',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue('s1')-Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue('n1'))




    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd')-4:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('CycleEnd')-3:

            f2 = open("231999.txt","r")                        
            kgk = f2.readline()
            f2.close()
            f2 = open("2311999.txt","r")                        
            kgg = f2.readline()
            f2.close()


            k4 = ast.literal_eval(kgk)
            k5 = ast.literal_eval(kgg)
            
            f2= open("2003.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()       

            f2= open("20300.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()    



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-2:
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('A1')>0:
                ppp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('s')]
                ppp2=[]
                kkk=0
                for i in range(len(ppp)):
                    if ppp[i]>0:
                        ppp2.append(i)
                        kkk=kkk+ppp[i]
                if len(ppp2)==len(ppp):
                    A23=(ppp[6]/kkk)/Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('A1')
                    f2= open("A23b.txt","a")
                    f2.write(str(A23)+',')
                    f2.write("\n")
                    f2.close()
                if len(ppp2)<len(ppp):
                    A23=-10
                    f2= open("A23b.txt","a")
                    f2.write(str(A23)+',')
                    f2.write("\n")
                    f2.close()
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('A1')<=0:
                A23=-10
                f2= open("A23b.txt","a")
                f2.write(str(A23)+',')
                f2.write("\n")
                f2.close()                
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A2',A23)













    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd')-5:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd')-4:
            k=0
            k4=[]
            k5=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '1':
                            NumStops=vehAttributes[vehsAttNames['NumStops']]
                            k=k+NumStops
                            No=vehAttributes[vehsAttNames['No']]
                            k4.append(No)
                            k5.append(NumStops)

            f2= open("241.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()

            f2= open("2411.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('s1',k)
            f1 = open("24.txt","r")                        
            kgk = f1.readline()
            f1.close()
            f1 = open("2400.txt","r")                        
            kgg = f1.readline()
            f1.close()

            Aseq = ast.literal_eval(kgk)
            mseg = ast.literal_eval(kgg)
            kl=0
            for vehAttributes in vehsAttributes:
                No=vehAttributes[vehsAttNames['No']]
                if No in Aseq:
                    Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                    if Lane == '1':
                        NumStops=mseg[Aseq.index(No)]   
                        kl=kl+NumStops
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('n1',kl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('s',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('s1')-Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('n1'))

    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd')-4:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('CycleEnd')-3:

            f2 = open("241.txt","r")                        
            kgk = f2.readline()
            f2.close()
            f2 = open("2411.txt","r")                        
            kgg = f2.readline()
            f2.close()


            k4 = ast.literal_eval(kgk)
            k5 = ast.literal_eval(kgg)
            
            f2= open("24.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()       

            f2= open("2400.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-2:
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('A1')>0:
                ppp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('s')]
                ppp2=[]
                kkk=0
                for i in range(len(ppp)):
                    if ppp[i]>0:
                        ppp2.append(i)
                        kkk=kkk+ppp[i]
                if len(ppp2)==len(ppp):
                    A24=(ppp[3]/kkk)/Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('A1')
                    f2= open("A24a.txt","a")
                    f2.write(str(A24)+',')
                    f2.write("\n")
                    f2.close()
                if len(ppp2)<len(ppp):
                    A24=-10
                    f2= open("A24a.txt","a")
                    f2.write(str(A24)+',')
                    f2.write("\n")
                    f2.close()
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('A1')<=0:
                A24=-10
                f2= open("A24a.txt","a")
                f2.write(str(A24)+',')
                f2.write("\n")
                f2.close()                
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A2',A24)   







    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd')-5:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd')-4:
            k=0
            k4=[]
            k5=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '9':
                            NumStops=vehAttributes[vehsAttNames['NumStops']]
                            k=k+NumStops
                            No=vehAttributes[vehsAttNames['No']]
                            k4.append(No)
                            k5.append(NumStops)

            f2= open("241999.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()

            f2= open("2411999.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('s1',k)
            f1 = open("2004.txt","r")                        
            kgk = f1.readline()
            f1.close()
            f1 = open("20400.txt","r")                        
            kgg = f1.readline()
            f1.close()

            Aseq = ast.literal_eval(kgk)
            mseg = ast.literal_eval(kgg)
            kl=0
            for vehAttributes in vehsAttributes:
                No=vehAttributes[vehsAttNames['No']]
                if No in Aseq:
                    Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                    if Lane == '9':
                        NumStops=mseg[Aseq.index(No)]   
                        kl=kl+NumStops
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('n1',kl)
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('s',Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('s1')-Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('n1'))

    if SimSec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd')-4:
        if SimSec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('CycleEnd')-3:

            f2 = open("241999.txt","r")                        
            kgk = f2.readline()
            f2.close()
            f2 = open("2411999.txt","r")                        
            kgg = f2.readline()
            f2.close()


            k4 = ast.literal_eval(kgk)
            k5 = ast.literal_eval(kgg)
            
            f2= open("2004.txt","w")
            f2.write(str(k4))
            f2.write("\n")
            f2.close()       

            f2= open("20400.txt","w")
            f2.write(str(k5))
            f2.write("\n")
            f2.close()


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-2:
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('A1')>0:
                ppp=[Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('s'),Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('s')]
                ppp2=[]
                kkk=0
                for i in range(len(ppp)):
                    if ppp[i]>0:
                        ppp2.append(i)
                        kkk=kkk+ppp[i]
                if len(ppp2)==len(ppp):
                    A24=(ppp[7]/kkk)/Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('A1')
                    f2= open("A24b.txt","a")
                    f2.write(str(A24)+',')
                    f2.write("\n")
                    f2.close()
                if len(ppp2)<len(ppp):
                    A24=-10
                    f2= open("A24b.txt","a")
                    f2.write(str(A24)+',')
                    f2.write("\n")
                    f2.close()
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('A1')<=0:
                A24=-10
                f2= open("A24b.txt","a")
                f2.write(str(A24)+',')
                f2.write("\n")
                f2.close()                
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A2',A24)   



def A3():
    GetVissimDataVehicles()
    Cl=120
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    CySec = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    SimSec = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')
    AllowableSpeed=50




    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-2:
            lmk=0
            kkkk=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '8':
                            kkkk.append(1)
                            speed = vehAttributes[vehsAttNames['Speed']]
                            DistanceToSigHead=vehAttributes[vehsAttNames['DistanceToSigHead']]
                            if DistanceToSigHead==0:
                                DistanceToSigHead=1
                            lmk= lmk+ (speed*DistanceToSigHead)/(AllowableSpeed*DistanceToSigHead)

            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A3',lmk )

            if len(kkkk)==0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A3',-10 )
            A31= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A3')
            f2= open("A31a.txt","a")
            f2.write(str(A31)+',')
            f2.write("\n")
            f2.close()
        



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-2:
            lmk=0
            kkkk=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '16':
                            kkkk.append(1)
                            speed = vehAttributes[vehsAttNames['Speed']]
                            DistanceToSigHead=vehAttributes[vehsAttNames['DistanceToSigHead']]
                            if DistanceToSigHead==0:
                                DistanceToSigHead=1
                            lmk= lmk+ (speed*DistanceToSigHead)/(AllowableSpeed*DistanceToSigHead)

            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A3',lmk )

            if len(kkkk)==0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A3',-10 )
            A31= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('A3')
            f2= open("A31b.txt","a")
            f2.write(str(A31)+',')
            f2.write("\n")
            f2.close()


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-2:
            lmk=0
            kkkk=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '4':
                            kkkk.append(1)
                            speed = vehAttributes[vehsAttNames['Speed']]
                            DistanceToSigHead=vehAttributes[vehsAttNames['DistanceToSigHead']]
                            if DistanceToSigHead==0:
                                DistanceToSigHead=1
                            lmk= lmk+ (speed*DistanceToSigHead)/(AllowableSpeed*DistanceToSigHead)

            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A3',lmk )

            if len(kkkk)==0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A3',-10 )
            A32= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A3')
            f2= open("A32a.txt","a")
            f2.write(str(A32)+',')
            f2.write("\n")
            f2.close()                          
                            



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-2:
            lmk=0
            kkkk=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '14':
                            kkkk.append(1)
                            speed = vehAttributes[vehsAttNames['Speed']]
                            DistanceToSigHead=vehAttributes[vehsAttNames['DistanceToSigHead']]
                            if DistanceToSigHead==0:
                                DistanceToSigHead=1
                            lmk= lmk+ (speed*DistanceToSigHead)/(AllowableSpeed*DistanceToSigHead)

            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A3',lmk )

            if len(kkkk)==0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A3',-10 )
            A32= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('A3')
            f2= open("A32b.txt","a")
            f2.write(str(A32)+',')
            f2.write("\n")
            f2.close()                                  




    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-2:
            lmk=0
            kkkk=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '5':
                            kkkk.append(1)
                            speed = vehAttributes[vehsAttNames['Speed']]
                            DistanceToSigHead=vehAttributes[vehsAttNames['DistanceToSigHead']]

                            if DistanceToSigHead==0:
                                DistanceToSigHead=1
                            lmk= lmk+ (speed*DistanceToSigHead)/(AllowableSpeed*DistanceToSigHead)
 
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A3',lmk )

            if len(kkkk)==0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A3',-10 )
            A33= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('A3')
            f2= open("A33a.txt","a")
            f2.write(str(A33)+',')
            f2.write("\n")
            f2.close()                          
                            


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-2:
            lmk=0
            kkkk=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '12':
                            kkkk.append(1)
                            speed = vehAttributes[vehsAttNames['Speed']]
                            DistanceToSigHead=vehAttributes[vehsAttNames['DistanceToSigHead']]

                            if DistanceToSigHead==0:
                                DistanceToSigHead=1
                            lmk= lmk+ (speed*DistanceToSigHead)/(AllowableSpeed*DistanceToSigHead)
 
            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A3',lmk )

            if len(kkkk)==0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A3',-10 )
            A33= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('A3')
            f2= open("A33b.txt","a")
            f2.write(str(A33)+',')
            f2.write("\n")
            f2.close()                          
                            


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-2:
            lmk=0
            kkkk=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '1':
                            kkkk.append(1)
                            speed = vehAttributes[vehsAttNames['Speed']]
                            DistanceToSigHead=vehAttributes[vehsAttNames['DistanceToSigHead']]

                            if DistanceToSigHead==0:
                                DistanceToSigHead=1
                            lmk= lmk+ (speed*DistanceToSigHead)/(AllowableSpeed*DistanceToSigHead)

            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A3',lmk )

            if len(kkkk)==0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A3',-10 )
            A34= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('A3')
            f2= open("A34a.txt","a")
            f2.write(str(A34)+',')
            f2.write("\n")
            f2.close()                          


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-2:
            lmk=0
            kkkk=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]                        
                        if Lane == '9':
                            kkkk.append(1)
                            speed = vehAttributes[vehsAttNames['Speed']]
                            DistanceToSigHead=vehAttributes[vehsAttNames['DistanceToSigHead']]

                            if DistanceToSigHead==0:
                                DistanceToSigHead=1
                            lmk= lmk+ (speed*DistanceToSigHead)/(AllowableSpeed*DistanceToSigHead)

            Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A3',lmk )

            if len(kkkk)==0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A3',-10 )
            A34= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('A3')
            f2= open("A34b.txt","a")
            f2.write(str(A34)+',')
            f2.write("\n")
            f2.close()                          





def A4():
    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    CySec = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    SimSec = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')

    GetVissimDataVehicles()
    Cl=120
    AllowableSpeed=50

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-2:
            tpt=0
            ffff=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]
                        if Lane == '8':
                            speed = vehAttributes[vehsAttNames['Speed']]
                            tpt=tpt+speed
            lllp= Vissim.Net.Links.ItemByKey(8).AttValue ('Count:Vehs')
            if tpt==0:
                tpt=1
            if lllp>=2:                                            
                ijij= tpt/(lllp*AllowableSpeed)
                kgh=0
                for vehAttributes in vehsAttributes:
                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                        if vehAttributes[vehsAttNames['Lane\Link']] != None:
                            Lane = vehAttributes[vehsAttNames['Lane\Link']]
                            if Lane == '8':
                                speed = vehAttributes[vehsAttNames['Speed']]
                                kgh=kgh+pow((speed/AllowableSpeed)-ijij,2)

                gfd= math.sqrt(kgh/(lllp-1)) 
                if ijij>0:
                    opt=gfd/ijij
                if ijij == 0:
                    opt=-10
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A4',opt)
                    
            if lllp <= 1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A4',-10 )


            A41= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A4')
            f2= open("A41a.txt","a")
            f2.write(str(A41)+',')
            f2.write("\n")
            f2.close()                       







    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-2:
            tpt=0
            ffff=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]
                        if Lane == '16':
                            speed = vehAttributes[vehsAttNames['Speed']]
                            tpt=tpt+speed
            lllp= Vissim.Net.Links.ItemByKey(16).AttValue ('Count:Vehs')
            if tpt==0:
                tpt=1
            if lllp>=2:                                            
                ijij= tpt/(lllp*AllowableSpeed)
                kgh=0
                for vehAttributes in vehsAttributes:
                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                        if vehAttributes[vehsAttNames['Lane\Link']] != None:
                            Lane = vehAttributes[vehsAttNames['Lane\Link']]
                            if Lane == '16':
                                speed = vehAttributes[vehsAttNames['Speed']]
                                kgh=kgh+pow((speed/AllowableSpeed)-ijij,2)

                gfd= math.sqrt(kgh/(lllp-1)) 
                if ijij>0:
                    opt=gfd/ijij
                if ijij == 0:
                    opt=-10
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A4',opt)
                    
            if lllp <= 1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A4',-10 )


            A41= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('A4')
            f2= open("A41b.txt","a")
            f2.write(str(A41)+',')
            f2.write("\n")
            f2.close()                       


    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-2:
            tpt=0
            ffff=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]
                        if Lane == '4':
                            speed = vehAttributes[vehsAttNames['Speed']]
                            tpt=tpt+speed
            lllp= Vissim.Net.Links.ItemByKey(4).AttValue ('Count:Vehs')
            if tpt==0:
                tpt=1
            if lllp>=2:                                            
                ijij= tpt/(lllp*AllowableSpeed)
                kgh=0
                for vehAttributes in vehsAttributes:
                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                        if vehAttributes[vehsAttNames['Lane\Link']] != None:
                            Lane = vehAttributes[vehsAttNames['Lane\Link']]
                            if Lane == '4':
                                speed = vehAttributes[vehsAttNames['Speed']]
                                kgh=kgh+pow((speed/AllowableSpeed)-ijij,2)

                gfd= math.sqrt(kgh/(lllp-1)) 
                if ijij>0:
                    opt=gfd/ijij
                if ijij == 0:
                    opt=-10
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A4',opt)
                    
            if lllp <= 1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A4',-10 )


            A42= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A4')
            f2= open("A42a.txt","a")
            f2.write(str(A42)+',')
            f2.write("\n")
            f2.close()                       



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-2:
            tpt=0
            ffff=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]
                        if Lane == '14':
                            speed = vehAttributes[vehsAttNames['Speed']]
                            tpt=tpt+speed
            lllp= Vissim.Net.Links.ItemByKey(14).AttValue ('Count:Vehs')
            if tpt==0:
                tpt=1
            if lllp>=2:                                            
                ijij= tpt/(lllp*AllowableSpeed)
                kgh=0
                for vehAttributes in vehsAttributes:
                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                        if vehAttributes[vehsAttNames['Lane\Link']] != None:
                            Lane = vehAttributes[vehsAttNames['Lane\Link']]
                            if Lane == '14':
                                speed = vehAttributes[vehsAttNames['Speed']]
                                kgh=kgh+pow((speed/AllowableSpeed)-ijij,2)

                gfd= math.sqrt(kgh/(lllp-1)) 
                if ijij>0:
                    opt=gfd/ijij
                if ijij == 0:
                    opt=-10
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A4',opt)
                    
            if lllp <= 1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A4',-10 )


            A42= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('A4')
            f2= open("A42b.txt","a")
            f2.write(str(A42)+',')
            f2.write("\n")
            f2.close()                       



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-2:
            tpt=0
            ffff=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]
                        if Lane == '5':
                            speed = vehAttributes[vehsAttNames['Speed']]
                            tpt=tpt+speed
            lllp= Vissim.Net.Links.ItemByKey(5).AttValue ('Count:Vehs')
            if tpt==0:
                tpt=1
            if lllp>=2:                                            
                ijij= tpt/(lllp*AllowableSpeed)
                kgh=0
                for vehAttributes in vehsAttributes:
                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                        if vehAttributes[vehsAttNames['Lane\Link']] != None:
                            Lane = vehAttributes[vehsAttNames['Lane\Link']]
                            if Lane == '5':
                                speed = vehAttributes[vehsAttNames['Speed']]
                                kgh=kgh+pow((speed/AllowableSpeed)-ijij,2)

                gfd= math.sqrt(kgh/(lllp-1)) 
                if ijij>0:
                    opt=gfd/ijij
                if ijij == 0:
                    opt=-10
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A4',opt)
                    
            if lllp <= 1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A4',-10 )


            A43= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('A4')
            f2= open("A43a.txt","a")
            f2.write(str(A43)+',')
            f2.write("\n")
            f2.close()




    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-2:
            tpt=0
            ffff=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]
                        if Lane == '12':
                            speed = vehAttributes[vehsAttNames['Speed']]
                            tpt=tpt+speed
            lllp= Vissim.Net.Links.ItemByKey(12).AttValue ('Count:Vehs')
            if tpt==0:
                tpt=1
            if lllp>=2:                                            
                ijij= tpt/(lllp*AllowableSpeed)
                kgh=0
                for vehAttributes in vehsAttributes:
                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                        if vehAttributes[vehsAttNames['Lane\Link']] != None:
                            Lane = vehAttributes[vehsAttNames['Lane\Link']]
                            if Lane == '12':
                                speed = vehAttributes[vehsAttNames['Speed']]
                                kgh=kgh+pow((speed/AllowableSpeed)-ijij,2)

                gfd= math.sqrt(kgh/(lllp-1)) 
                if ijij>0:
                    opt=gfd/ijij
                if ijij == 0:
                    opt=-10
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A4',opt)
                    
            if lllp <= 1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A4',-10 )


            A43= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('A4')
            f2= open("A43b.txt","a")
            f2.write(str(A43)+',')
            f2.write("\n")
            f2.close()



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-2:
            tpt=0
            ffff=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]
                        if Lane == '1':
                            speed = vehAttributes[vehsAttNames['Speed']]
                            tpt=tpt+speed
            lllp= Vissim.Net.Links.ItemByKey(1).AttValue ('Count:Vehs')
            if tpt==0:
                tpt=1
            if lllp>=2:                                            
                ijij= tpt/(lllp*AllowableSpeed)
                kgh=0
                for vehAttributes in vehsAttributes:
                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                        if vehAttributes[vehsAttNames['Lane\Link']] != None:
                            Lane = vehAttributes[vehsAttNames['Lane\Link']]
                            if Lane == '1':
                                speed = vehAttributes[vehsAttNames['Speed']]
                                kgh=kgh+pow((speed/AllowableSpeed)-ijij,2)

                gfd= math.sqrt(kgh/(lllp-1)) 
                if ijij>0:
                    opt=gfd/ijij
                if ijij == 0:
                    opt=-10
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A4',opt)
                    
            if lllp <= 1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A4',-10 )


            A44= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('A4')
            f2= open("A44a.txt","a")
            f2.write(str(A44)+',')
            f2.write("\n")
            f2.close()



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-2:
            tpt=0
            ffff=[]
            for vehAttributes in vehsAttributes:
                if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                    if vehAttributes[vehsAttNames['Lane\Link']] != None:
                        Lane = vehAttributes[vehsAttNames['Lane\Link']]
                        if Lane == '9':
                            speed = vehAttributes[vehsAttNames['Speed']]
                            tpt=tpt+speed
            lllp= Vissim.Net.Links.ItemByKey(9).AttValue ('Count:Vehs')
            if tpt==0:
                tpt=1
            if lllp>=2:                                            
                ijij= tpt/(lllp*AllowableSpeed)
                kgh=0
                for vehAttributes in vehsAttributes:
                    if vehAttributes[vehsAttNames['VehType\No']] in vehTypesEquipped:
                        if vehAttributes[vehsAttNames['Lane\Link']] != None:
                            Lane = vehAttributes[vehsAttNames['Lane\Link']]
                            if Lane == '9':
                                speed = vehAttributes[vehsAttNames['Speed']]
                                kgh=kgh+pow((speed/AllowableSpeed)-ijij,2)

                gfd= math.sqrt(kgh/(lllp-1)) 
                if ijij>0:
                    opt=gfd/ijij
                if ijij == 0:
                    opt=-10
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A4',opt)
                    
            if lllp <= 1:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A4',-10 )


            A44= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('A4')
            f2= open("A44b.txt","a")
            f2.write(str(A44)+',')
            f2.write("\n")
            f2.close()



def A5():
    trt1 = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('SFR')
    trt2 = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue('SFR')
    trt3 = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue('SFR')
    trt4 = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue('SFR')

    trt5 = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue('SFR')
    trt6 = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue('SFR')
    trt7 = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue('SFR')
    trt8 = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue('SFR')


    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue('Seconds',Vissim.Net.Simulation.SimulationSecond)
    CySec = Vissim.Net.SignalControllers.ItemByKey(1).AttValue ('CycSec')
    SimSec = Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue('Seconds')

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-2:
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            if trt1>=0:
                kkpp3=0
                i=0
                while i <=7:
                    if jjijj[i]>0:
                        kkpp3=kkpp3+jjijj[i]
                    i+=1

                if kkpp3 >0: 
                    kkpp4=(trt1/kkpp3)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A5',kkpp4)                
                if kkpp3 ==0:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A5',-10)
            if trt1<0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).SetAttValue ('A5',-10)
                

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd')-1:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('GreenEnd'):
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            kkpp3=0
            kkpp2=0
            i=0
            while i <=7:
                if jjijj[i]>0:
                    kkpp3=kkpp3+pow(jjijj[i],2)
                    kkpp2=kkpp2+jjijj[i]
                i+=1
            kkpp4=0
            if kkpp2 >0: 
                kkpp4=(math.sqrt(kkpp3)/kkpp2)
                    
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A5')>0:
                if kkpp4 >0:
                    A51=kkpp4*Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A5')
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(1).AttValue ('A5')<=0 or kkpp4 <=0:
                A51=-10
                    

            f2= open("A51a.txt","a")
            f2.write(str(A51)+',')
            f2.write("\n")
            f2.close()                                 
            




    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-2:
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            if trt5>=0:
                kkpp3=0
                i=0
                while i <=7:
                    if jjijj[i]>0:
                        kkpp3=kkpp3+jjijj[i]
                    i+=1

                if kkpp3 >0: 
                    kkpp4=(trt5/kkpp3)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A5',kkpp4)                
                if kkpp3 ==0:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A5',-10)
            if trt1<0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).SetAttValue ('A5',-10)
                

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd')-1:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('GreenEnd'):
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            kkpp3=0
            kkpp2=0
            i=0
            while i <=7:
                if jjijj[i]>0:
                    kkpp3=kkpp3+pow(jjijj[i],2)
                    kkpp2=kkpp2+jjijj[i]
                i+=1
            kkpp4=0
            if kkpp2 >0: 
                kkpp4=(math.sqrt(kkpp3)/kkpp2)
                    
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('A5')>0:
                if kkpp4 >0:
                    A51=kkpp4*Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('A5')
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(5).AttValue ('A5')<=0 or kkpp4 <=0:
                A51=-10
                    

            f2= open("A51b.txt","a")
            f2.write(str(A51)+',')
            f2.write("\n")
            f2.close()                                 
            



    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-2:
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            if trt2>=0:
                kkpp3=0
                i=0
                while i <=7:
                    if jjijj[i]>0:
                        kkpp3=kkpp3+jjijj[i]
                    i+=1

                if kkpp3 >0: 
                    kkpp4=(trt2/kkpp3)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A5',kkpp4)                
                if kkpp3 ==0:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A5',-10)
            if trt1<0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).SetAttValue ('A5',-10)
                

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd')-1:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('GreenEnd'):
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            kkpp3=0
            kkpp2=0
            i=0
            while i <=7:
                if jjijj[i]>0:
                    kkpp3=kkpp3+pow(jjijj[i],2)
                    kkpp2=kkpp2+jjijj[i]
                i+=1
            kkpp4=0
            if kkpp2 >0: 
                kkpp4=(math.sqrt(kkpp3)/kkpp2)
                    
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A5')>0:
                if kkpp4 >0:
                    A51=kkpp4*Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A5')
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(2).AttValue ('A5')<=0 or kkpp4 <=0:
                A51=-10
                    

            f2= open("A52a.txt","a")
            f2.write(str(A51)+',')
            f2.write("\n")
            f2.close()







    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-2:
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            if trt6>=0:
                kkpp3=0
                i=0
                while i <=7:
                    if jjijj[i]>0:
                        kkpp3=kkpp3+jjijj[i]
                    i+=1

                if kkpp3 >0: 
                    kkpp4=(trt6/kkpp3)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A5',kkpp4)                
                if kkpp3 ==0:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A5',-10)
            if trt1<0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).SetAttValue ('A5',-10)
                

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd')-1:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('GreenEnd'):
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            kkpp3=0
            kkpp2=0
            i=0
            while i <=7:
                if jjijj[i]>0:
                    kkpp3=kkpp3+pow(jjijj[i],2)
                    kkpp2=kkpp2+jjijj[i]
                i+=1
            kkpp4=0
            if kkpp2 >0: 
                kkpp4=(math.sqrt(kkpp3)/kkpp2)
                    
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('A5')>0:
                if kkpp4 >0:
                    A51=kkpp4*Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('A5')
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(6).AttValue ('A5')<=0 or kkpp4 <=0:
                A51=-10
                    

            f2= open("A52b.txt","a")
            f2.write(str(A51)+',')
            f2.write("\n")
            f2.close()












    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-2:
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            if trt3>=0:
                kkpp3=0
                i=0
                while i <=7:
                    if jjijj[i]>0:
                        kkpp3=kkpp3+jjijj[i]
                    i+=1

                if kkpp3 >0: 
                    kkpp4=(trt3/kkpp3)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A5',kkpp4)                
                if kkpp3 ==0:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A5',-10)
            if trt1<0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).SetAttValue ('A5',-10)
                

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd')-1:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('GreenEnd'):
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            kkpp3=0
            kkpp2=0
            i=0
            while i <=7:
                if jjijj[i]>0:
                    kkpp3=kkpp3+pow(jjijj[i],2)
                    kkpp2=kkpp2+jjijj[i]
                i+=1
            kkpp4=0
            if kkpp2 >0: 
                kkpp4=(math.sqrt(kkpp3)/kkpp2)
                    
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('A5')>0:
                if kkpp4 >0:
                    A51=kkpp4*Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('A5')
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(3).AttValue ('A5')<=0 or kkpp4 <=0:
                A51=-10
                    

            f2= open("A53a.txt","a")
            f2.write(str(A51)+',')
            f2.write("\n")
            f2.close()





    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-2:
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            if trt7>=0:
                kkpp3=0
                i=0
                while i <=7:
                    if jjijj[i]>0:
                        kkpp3=kkpp3+jjijj[i]
                    i+=1

                if kkpp3 >0: 
                    kkpp4=(trt7/kkpp3)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A5',kkpp4)                
                if kkpp3 ==0:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A5',-10)
            if trt1<0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).SetAttValue ('A5',-10)
                

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd')-1:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('GreenEnd'):
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            kkpp3=0
            kkpp2=0
            i=0
            while i <=7:
                if jjijj[i]>0:
                    kkpp3=kkpp3+pow(jjijj[i],2)
                    kkpp2=kkpp2+jjijj[i]
                i+=1
            kkpp4=0
            if kkpp2 >0: 
                kkpp4=(math.sqrt(kkpp3)/kkpp2)
                    
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('A5')>0:
                if kkpp4 >0:
                    A51=kkpp4*Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('A5')
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(7).AttValue ('A5')<=0 or kkpp4 <=0:
                A51=-10
                    

            f2= open("A53b.txt","a")
            f2.write(str(A51)+',')
            f2.write("\n")
            f2.close()









    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-2:
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            if trt4>=0:
                kkpp3=0
                i=0
                while i <=7:
                    if jjijj[i]>0:
                        kkpp3=kkpp3+jjijj[i]
                    i+=1

                if kkpp3 >0: 
                    kkpp4=(trt4/kkpp3)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A5',kkpp4)                
                if kkpp3 ==0:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A5',-10)
            if trt1<0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).SetAttValue ('A5',-10)
                

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd')-1:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('GreenEnd'):
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            kkpp3=0
            kkpp2=0
            i=0
            while i <=7:
                if jjijj[i]>0:
                    kkpp3=kkpp3+pow(jjijj[i],2)
                    kkpp2=kkpp2+jjijj[i]
                i+=1
            kkpp4=0
            if kkpp2 >0: 
                kkpp4=(math.sqrt(kkpp3)/kkpp2)
                    
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('A5')>0:
                if kkpp4 >0:
                    A51=kkpp4*Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('A5')
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(4).AttValue ('A5')<=0 or kkpp4 <=0:
                A51=-10
                    

            f2= open("A54a.txt","a")
            f2.write(str(A51)+',')
            f2.write("\n")
            f2.close()









    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-3:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-2:
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            if trt8>=0:
                kkpp3=0
                i=0
                while i <=7:
                    if jjijj[i]>0:
                        kkpp3=kkpp3+jjijj[i]
                    i+=1

                if kkpp3 >0: 
                    kkpp4=(trt8/kkpp3)
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A5',kkpp4)                
                if kkpp3 ==0:
                    Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A5',-10)
            if trt1<0:
                Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).SetAttValue ('A5',-10)
                

    if CySec >= Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd')-1:
        if CySec < Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('GreenEnd'):
            jjijj=[trt1, trt2, trt3, trt4, trt5, trt6, trt7, trt8]
            kkpp3=0
            kkpp2=0
            i=0
            while i <=7:
                if jjijj[i]>0:
                    kkpp3=kkpp3+pow(jjijj[i],2)
                    kkpp2=kkpp2+jjijj[i]
                i+=1
            kkpp4=0
            if kkpp2 >0: 
                kkpp4=(math.sqrt(kkpp3)/kkpp2)
                    
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('A5')>0:
                if kkpp4 >0:
                    A51=kkpp4*Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('A5')
            if Vissim.Net.SignalControllers.ItemByKey(1).SGs.ItemByKey(8).AttValue ('A5')<=0 or kkpp4 <=0:
                A51=-10
                    

            f2= open("A54b.txt","a")
            f2.write(str(A51)+',')
            f2.write("\n")
            f2.close()
