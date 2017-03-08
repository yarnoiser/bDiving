import bge
import equipment

diver = bge.logic.getCurrentController().owner

equipment.equip(diver, equipment.genericBcd, equipment.genericCylinder, 3000)

# ensure original volume is preserved for use in future calculations
diver['baseVolume'] = diver['volume']

# ensure original mass is preserved for use in future calculations
diver['baseMass'] = diver.mass
