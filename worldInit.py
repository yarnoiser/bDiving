import bge
from waterPhysics import hasWaterPhysics

def hasWorldPhysics(obj):
  return 'worldPhysics' in obj and obj['worldPhysics'] == True

controller = bge.logic.getCurrentController()
world = controller.owner
scene = bge.logic.getCurrentScene()

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

# get list of objects that have waterPhysics
waterPhysicsList = []
for obj in scene.objects:
    if hasWaterPhysics(obj):
      waterPhysicsList.append(obj)

world['waterPhysicsObjects'] = waterPhysicsList

