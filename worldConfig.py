import bge
from waterPhysics import hasWaterPhysics

controller = bge.logic.getCurrentController()
config = controller.owner
scene = bge.logic.getCurrentScene()

# set gravity constant available to other scripts
config['GRAVITY'] = 9.81
# set world's gravity to equal our constant
bge.logic.setGravity([0.0, 0.0, 0.0 - config['GRAVITY']])

# get list of objects that have waterPhysics
waterPhysicsList = []
for object in scene.objects:
    if hasWaterPhysics(object):
      waterPhysicsList.append(object)

config['waterPhysicsObjects'] = waterPhysicsList
