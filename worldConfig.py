import bge

# True if the object has water physics
def hasWaterPhysics(obj):
    return 'waterPhysics' in obj and obj['waterPhysics'] == True

controller = bge.logic.getCurrentController()
config = cont.owner
scene = bge.logic.getCurrentScene()

# set gravity constant available to other scripts
GRAVITY = 9.81
# set world's gravity to equal our constant
bge.logic.setGravity([0.0, 0.0, 0.0 - GRAVITY])

# get list of objects that have waterPhysics
waterPhysicsList = []
for object in scene.objects:
    if hasWaterPhysics(object):
      waterPhysicsList.append(object)

scene.waterObjects = waterPhysicsList

