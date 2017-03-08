import bge
from equipment import ROOM_TEMPERATURE
from waterPhysics import pressure

world = bge.logic.getCurrentScene().objects['WorldConfig']
gravity = world['gravity']
diver = bge.logic.getCurrentController().owner
depth = diver.worldPosition[2]

diver['volume'] = diver['baseVolume'] \
                  + diver['bcd'].volume(pressure(gravity, depth, ROOM_TEMPERATURE)
                                        , ROOM_TEMPERATURE) \
                  + diver['airCylinder'].volume

#diver.mass = diver['baseMass'] \
#             + diver['bcd'].mass() \
#             + diver['airCylinder'].mass() \
#             + diver['weight']
