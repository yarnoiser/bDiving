import bge
from equipment import ROOM_TEMPERATURE
from waterPhysics import pressure

world = bge.logic.getCurrentScene().objects['WorldConfig']
gravity = world['gravity']
diver = bge.logic.getCurrentController().owner
currentDepth = diver.worldPosition[2]
currentTemperature = ROOM_TEMPERATURE
currentPressure = pressure(gravity, currentDepth, currentTemperature)

diver['volume'] = diver['baseVolume'] \
                  + diver['bcd'].volume(currentPressure \
                                        , currentTemperature) \
                  + diver['airCylinder'].volume

diver.mass = (diver['baseMass'] \
             + diver['bcd'].mass() \
             + diver['airCylinder'].mass() \
             + diver['weight']) \
             / 1000

# BCD Controls
def inflate(moles):
    fromTank = diver['airCylinder'].removeAir(moles)
    diver['bcd'].addAir(fromTank, currentPressure, currentTemperature)

def deflate(moles):
    diver['bcd'].removeAir(moles)

sensors = diver.sensors
if sensors['Mouse Left'].triggered:
    inflate(1000)
    
if sensors['Mouse Right'].triggered:
    deflate(1000)
