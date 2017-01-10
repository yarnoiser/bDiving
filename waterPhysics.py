import bge
import bpy

scene = bge.logic.getCurrentScene()

fluid = bge.logic.getCurrentController().owner

GRAVITY = 9.81

def hasWaterPhysics(obj):
    return 'waterPhysics' in obj

def compression(depth):
    return 1 + (depth * 0.1) * fuid['density']

def drag(velocity, area, dragCoefficient):
    # drag equation
    # dragForce = 1/2 * fluidDensity * velocity^2 * referenceArea * dragCoefficient
    return 0.5 * fluid['density'] * velocity ** 2 * area * dragCoefficient

def submerged(object):
    fluidZ = fluid.position[2]
    objectZ = object.position[2]
    return (objectZ <= fluidZ)

for object in scene.objects:
    if hasWaterPhysics(object):
        print(object['submerged'])
        if submerged(object):
            object['submerged'] = True
            # Buoyancy force
            object.applyForce([0.0, 0.0, object['volume'] * fluid['density'] * GRAVITY],
                          False)
            
            # Friction force
            dragVect = object.worldLinearVelocity.copy()
            # assume player is a sphere for drag coefficient
            # https://en.wikipedia.org/wiki/Drag_coefficient
            dragMagnitude = drag(dragVect.magnitude, 1, 0.47)
            dragVect.negate()
            dragVect.normalize()
            object.applyForce(dragVect * dragMagnitude, False)
        else:
            object['submerged'] = False

