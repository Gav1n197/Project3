from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.task import Task
from direct.task.Task import TaskManager
from typing import Callable
from panda3d.core import Loader, NodePath, Vec3

from CollideObjectBase import InverseSphereCollideObject, CapsuleCollidableObject # type: ignore
    # Will need to import SphereCollideObject here later

class Player(ShowBase):
    def __init__(self, loader: Loader, taskMgr: TaskManager, modelPath: str, parentNode: NodePath, nodeName: str, posVec: Vec3, scaleVec: float, Hpr: Vec3):
        self.taskMgr = taskMgr
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)
        self.modelNode.setHpr(Hpr)

        self.setKeyBindings()

    def thrust(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.applyThrust, 'forward-thrust') # might be taskManager instead, taskMgr is whats on the website
        else:
            self.taskMgr.remove('forward-thrust')

    def applyThrust(self, task):
        rate = 5
        #trajectory = self.render.getRelativeVector(self.modelNode, Vec3.forward())
        self.modelNode.setY(self.modelNode, 10) #trajectory was not working, so I used setY instead
        #trajectory.normalize()
        #self.modelNode.setFluidPos(self.modelNode.getPos() + trajectory * rate)
        return task.cont                                    # Continue moving the players ship when returning
    
    def setKeyBindings(self): ##Movement for the player, review Warmup3
        self.accept('space', self.thrust, [1])
        self.accept('space-up', self.thrust, [0])

        self.accept('q', self.leftRoll, [1])
        self.accept('q-up', self.leftRoll, [0])

        self.accept('e', self.rightRoll, [1])
        self.accept('e-up', self.rightRoll, [0])

        self.accept('a', self.LeftTurn, [1])
        self.accept('a-up', self.LeftTurn, [0])

        self.accept('d', self.rightTurn, [1])
        self.accept('d-up', self.rightTurn, [0])

        self.accept('w', self.Up, [1])
        self.accept('w-up', self.Up, [0])

        self.accept('s', self.Down, [1])
        self.accept('s-up', self.Down, [0])

    def leftRoll(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.applyLeftRoll, 'left-roll')
        else:
            self.taskMgr.remove('left-roll')

    def rightRoll(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.applyRightRoll, 'right-roll')
        else:
            self.taskMgr.remove('right-roll')


    def applyLeftRoll(self, task):
        rate = 0.5
        print('leftroll')
        self.modelNode.setR(self.modelNode.getR() - rate)
        return task.cont
        
    def applyRightRoll(self, task):
        rate = 0.5
        print('rightroll')
        self.modelNode.setR(self.modelNode.getR() + rate)
        return task.cont
    
#------------------------------------------------------------------------------------

    def LeftTurn(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.applyLeftTurn, 'left-turn')
        else:
            self.taskMgr.remove('left-turn')

    def rightTurn(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.applyRightTurn, 'right-turn')
        else:
            self.taskMgr.remove('right-turn')


    def applyLeftTurn(self, task):
        rate = 0.5
        print('leftturn')
        self.modelNode.setH(self.modelNode.getH() + rate)
        return task.cont

    def applyRightTurn(self, task):
        rate = 0.5
        print('rightturn')
        self.modelNode.setH(self.modelNode.getH() - rate)
        return task.cont
    
#------------------------------------------------------------------------------------

    def Up(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.applyUp, 'up')
        else:
            self.taskMgr.remove('up')

    def Down(self, keyDown):
        if (keyDown):
            self.taskMgr.add(self.applyDown, 'down')
        else:
            self.taskMgr.remove('down')


    def applyUp(self, task):
        rate = 0.5
        print('applyUp')
        self.modelNode.setP(self.modelNode.getP() + rate)
        return task.cont

    def applyDown(self, task):
        rate = 0.5
        print('applyDown')
        self.modelNode.setP(self.modelNode.getP() - rate)
        return task.cont


class Universe(InverseSphereCollideObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Universe, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), 0.9) ##Uses __init__ function from InverseSphereCollideObject
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class SpaceStation(CapsuleCollidableObject):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(SpaceStation, self).__init__(loader, modelPath, parentNode, nodeName, 1, -1, 5, 1, -1, -5, 10) ##Defines ax, ay, az, etc.
        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Planet(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

class Drone(ShowBase):
    def __init__(self, loader: Loader, modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float): # type: ignore

        self.modelNode = loader.loadModel(modelPath)
        self.modelNode.reparentTo(parentNode)

        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)

        self.modelNode.setName(nodeName)

        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)
    droneCount = 0
