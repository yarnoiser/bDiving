import bge
import bpy

GRAVITY = 9.8
FRICTION = 7

def hasWaterPhysics(object):
    try:
        object['volume']
    except:
        return False
    return True

fluid = bge.logic.getCurrentController().owner

def submerged(object):
    fluidZ = fluid.position[2]
    objectZ = object.position[2]
    return (objectZ <= fluidZ)

scene = bge.logic.getCurrentScene()

for object in bpy.data.groups['waterPhysics']:
    if submerged(object):
    # Buoyancy force
    object.applyForce([0.0, 0.0, object['volume'] * fluid['density'] * GRAVITY],
                      False)
            
    # Friction force
    FrictionVect = object.worldLinearVelocity.copy()
    FrictionVect.negate()
    FrictionVect.normalize()
    object.applyForce(FrictionVect * FRICTION, False)
                             
        