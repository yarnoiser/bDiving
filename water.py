import bge
from waterPhysics import *

fluid = bge.logic.getCurrentController().owner
scene = bge.logic.getCurrentScene()
world = scene.objects['World']

def init():
    # get list of objects that have waterPhysics
    waterPhysicsList = []
    for obj in scene.objects:
        if hasWaterPhysics(obj):
          waterPhysicsList.append(obj)

    fluid['waterPhysicsObjects'] = waterPhysicsList

def update():
    for obj in fluid['waterPhysicsObjects']:
          if submerged(obj, fluid):
              obj['submerged'] = True
              obj['depth'] = depth(obj, fluid)
              obj['temperature'] = ROOM_TEMPERATURE
              obj['pressure'] = pressure(world['GRAVITY'], fluid['density'], obj['depth'])
              # Buoyancy force
              buoyancy = obj['volume'] * fluid['density'] * world['GRAVITY']
              obj.applyForce([0.0, 0.0, buoyancy], False)
                          
            
              # Friction force
              dragVect = obj.worldLinearVelocity.copy()
              # assume player is a sphere for drag coefficient
              # https://en.wikipedia.org/wiki/Drag_coefficient
              dragMagnitude = drag(fluid['density'], dragVect.magnitude, 1, DRAG_COEFFICIENT_SPHERE)
              dragVect.negate()
              dragVect.normalize()
              obj.applyForce(dragVect * dragMagnitude, False)
