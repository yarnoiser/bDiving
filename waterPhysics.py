import bge
import bpy

FRICTION = 0

scene = bge.logic.getCurrentScene()

fluid = bge.logic.getCurrentController().owner

GRAVITY = 9.81

def hasWaterPhysics(obj):
    return 'volume' in obj

def airCompression(depth):
    return 1 + (depth * 0.1) * fuid['density']

def submerged(object):
    fluidZ = fluid.position[2]
    objectZ = object.position[2]
    return (objectZ <= fluidZ)

for object in scene.objects:
    if hasWaterPhysics(object):
        if submerged(object):
            # Buoyancy force
            object.applyForce([0.0, 0.0, object['volume'] * fluid['density'] * GRAVITY],
                          False)
            
            # Friction force
            FrictionVect = object.worldLinearVelocity.copy()
            FrictionVect.negate()
            FrictionVect.normalize()
            object.applyForce(FrictionVect * FRICTION, False)
                             
