import bge
from equipment import ROOM_TEMPERATURE
from waterPhysics import pressure

world = bge.logic.getCurrentScene().objects['WorldConfig']
gravity = world['gravity']
diver = bge.logic.getCurrentController().owner
diver['depth'] = diver.worldPosition[2]
diver['temperature'] = ROOM_TEMPERATURE
diver['pressure'] = pressure(gravity, diver['depth'], diver['temperature'])

diver['volume'] = diver['baseVolume'] \
                  + diver['bcd'].volume(diver['pressure'] \
                                        , diver['temperature']) \
                  + diver['airCylinder'].volume

diver.mass = (diver['baseMass'] \
             + diver['bcd'].mass() \
             + diver['airCylinder'].mass() \
             + diver['weight']) \
             / 1000

def getDebugInfo(diver):
    return "depth:\t\t\t" + str(diver['depth']) \
       + "\npressure:\t\t" + str(diver['pressure']) \
       + "\ntemperature:\t\t" + str(diver['temperature']) \
       + "\n" \
       + "\nTotal Mass:\t\t" + str(diver.mass) \
       + "\nBase Mass:\t\t" + str(diver['baseMass']) \
       + "\nAir Cylinder Mass:\t" + str(diver['airCylinder'].mass()) \
       + "\nBCD Mass:\t\t" + str(diver['bcd'].mass()) \
       + "\n" \
       + "\nAir Cylinder Moles:\t" + str(diver['airCylinder'].moles) \
       + "\nBCD Moles:\t\t" + str(diver['bcd'].moles) \
       + "\n" \
       + "\nBase Volume:\t\t" + str(diver['baseVolume']) \
       + "\nAir Cylinder Volume:\t" + str(diver['airCylinder'].volume) \
       + "\nBCD Volume:\t\t" + str(diver['bcd'].volume(diver['pressure']
                                                     , diver['temperature']))
                                                     

# BCD Controls
def inflate(moles):
    fromTank = diver['airCylinder'].removeAir(moles)
    diver['bcd'].addAir(fromTank, diver['pressure'], diver['temperature'])

def deflate(moles):
    diver['bcd'].removeAir(moles)

sensors = diver.sensors
if sensors['Mouse Left'].triggered:
    inflate(1000)
    
if sensors['Mouse Right'].triggered:
    deflate(1000)

if sensors['P Key'].triggered:
    print("=================================")
    print(getDebugInfo(diver))
    print("=================================")