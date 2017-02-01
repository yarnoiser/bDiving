import bge
import equipment

diver = bge.logic.getCurrentController().owner

diver.equip(equipment.genericCylinder, equipment.genericBcd, 3000)


