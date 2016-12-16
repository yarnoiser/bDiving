import bge

cont = bge.logic.getCurrentController()
config = cont.owner

bge.logic.setGravity([0.0, 0.0, 0.0 - config['gravity']])


