import bge

world = bge.logic.getCurrentController().owner

for obj in world['worldPhysicsObjects']:
  obj.applyForce([0.0, 0.0, 0 - (obj.mass * world['GRAVITY'])])


