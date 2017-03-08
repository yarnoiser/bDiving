import bge
import bpy

fluid = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()
world = scene.objects['WorldConfig']

def pressure(depth, temperature):
    return depth * fluid['density'] * world['GRAVITY']

def drag(velocity, area, dragCoefficient):
    # drag equation
    # dragForce = 1/2 * fluidDensity * velocity^2 * referenceArea * dragCoefficient
    return 0.5 * fluid['density'] * velocity ** 2 * area * dragCoefficient

def submerged(object):
    fluidZ = fluid.position[2]
    objectZ = object.position[2]
    return (objectZ <= fluidZ)

for object in world['waterPhysicsObjects']:
      if submerged(object):
          object['submerged'] = True
          # Buoyancy force
          object.applyForce([0.0, 0.0, object['volume'] * fluid['density'] * 
                             world['GRAVITY']],
                             False)
            
      # Friction force
      dragVect = object.worldLinearVelocity.copy()
      # assume player is a sphere for drag coefficient
      # https://en.wikipedia.org/wiki/Drag_coefficient
      dragMagnitude = drag(dragVect.magnitude, 1, 0.47)
      dragVect.negate()
      dragVect.normalize()
      object.applyForce(dragVect * dragMagnitude, False)

