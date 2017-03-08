import bge
from waterPhysics import *

fluid = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()
world = scene.objects['WorldConfig']

for obj in world['waterPhysicsObjects']:
      if submerged(obj, fluid):
          obj['submerged'] = True
          # Buoyancy force
          obj.applyForce([0.0, 0.0, obj['volume'] * fluid['density'] * 
                             world['GRAVITY']],
                             False)
            
          # Friction force
          dragVect = obj.worldLinearVelocity.copy()
          # assume player is a sphere for drag coefficient
          # https://en.wikipedia.org/wiki/Drag_coefficient
          dragMagnitude = drag(fluid['density'], dragVect.magnitude, 1, DRAG_COEFFICIENT_SPHERE)
          dragVect.negate()
          dragVect.normalize()
          obj.applyForce(dragVect * dragMagnitude, False)

