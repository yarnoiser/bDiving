import bge
from equipment import *
from waterPhysics import *

world = bge.logic.getCurrentScene().objects['WorldConfig']
gravity = world['gravity']
diver = bge.logic.getCurrentController().owner

def getDebugInfo(diver):
    return "depth:\t\t\t" + str(diver['depth']) \
       + "\npressure:\t\t" + str(diver['pressure']) \
       + "\ntemperature:\t\t" + str(diver['temperature']) \
       + "\nTotal Mass:\t\t" + str(diver.mass) \
       + "\n" \
       + "\nBase Mass:\t\t" + str(diver['baseMass']) \
       + "\nBase Volume:\t\t" + str(diver['baseVolume']) \
       + "\n" \
       + "\nAir Cylinder Mass:\t" + str(diver['airCylinder'].mass()) \
       + "\nAir Cylinder Moles:\t" + str(diver['airCylinder'].moles) \
       + "\nAir Cylinder Volume:\t" + str(diver['airCylinder'].volume) \
       + "\n" \
       + "\nBCD Mass:\t\t" + str(diver['bcd'].mass()) \
       + "\nBCD Moles:\t\t" + str(diver['bcd'].moles) \
       + "\nBCD Volume:\t\t" + str(diver['bcd'].volume(diver['pressure']
                                                     , diver['temperature']))
                                                     

# BCD Controls
def inflate(moles):
    fromTank = diver['airCylinder'].removeAir(moles)
    diver['bcd'].addAir(fromTank, diver['pressure'], diver['temperature'])

def deflate(moles):
    diver['bcd'].removeAir(moles)
 
def init():
    diver = bge.logic.getCurrentController().owner

    equip(diver, genericBcd(), genericCylinder(), 3000)

    # ensure original volume is preserved for use in future calculations
    diver['baseVolume'] = diver['volume']

    # ensure original mass is preserved for use in future calculations
    diver['baseMass'] = diver.mass

    diver['temperature'] = ROOM_TEMPERATURE
    diver['pressure'] = AIR_PRESSURE_SEA_LEVEL

def update():
    diver['volume'] = diver['baseVolume'] \
                      + diver['bcd'].volume(diver['pressure'] \
                                            , diver['temperature']) \
                      + diver['airCylinder'].volume

    diver.mass = (diver['baseMass'] \
                 + diver['bcd'].mass() \
                 + diver['airCylinder'].mass() \
                 + diver['weight'])
    
    sensors = diver.sensors
    if sensors['Mouse Left'].triggered:
        inflate(1000)
    
    if sensors['Mouse Right'].triggered:
        deflate(1000)

    if sensors['P Key'].triggered:
        print("=================================")
        print(getDebugInfo(diver))
        print("=================================")
