import bge
from equipment import *
from waterPhysics import ROOM_TEMPERATURE, AIR_PRESSURE_SEA_LEVEL

diver = bge.logic.getCurrentController().owner

equip(diver, genericBcd(), genericCylinder(), 3000)

# ensure original volume is preserved for use in future calculations
diver['baseVolume'] = diver['volume']

# ensure original mass is preserved for use in future calculations
diver['baseMass'] = diver.mass

diver['temperature'] = ROOM_TEMPERATURE
diver['pressure'] = AIR_PRESSURE_SEA_LEVEL