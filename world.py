import bge
from waterPhysics import hasWaterPhysics

controller = bge.logic.getCurrentController()
world = controller.owner
scene = bge.logic.getCurrentScene()

def hasWorldPhysics(obj):
  return 'worldPhysics' in obj and obj['worldPhysics'] == True

def init():
    # set gravity constant available to other scripts
    world['GRAVITY'] = 9.81
    # set world's gravity to 0 (we are implementing our own)
    bge.logic.setGravity([0.0, 0.0, 0.0])

    # get list of objects that have worldPhysics
    worldPhysicsList = []
    for obj in scene.objects:
     if hasWorldPhysics(obj):
       worldPhysicsList.append(obj)
    world['worldPhysicsObjects'] = worldPhysicsList

def update():
    for obj in world['worldPhysicsObjects']:
        obj.applyForce([0.0, 0.0, 0 - (obj.mass * world['GRAVITY'])])


