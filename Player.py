# https://studentcscc-my.sharepoint.com/:p:/r/personal/gcorder1_student_cscc_edu/Documents/CSCC%20Classes/Semester%2010/3D%20Game%20Engine%20Concepts/Slides/Project4%20Lecture.pptx?d=w3f66872697ba414f85a8b35b9b22c3b6&csf=1&web=1&e=delq41&nav=eyJzSWQiOjI4NCwiY0lkIjozMzUyODM1OX0
from CollideObjectBase import SphereCollideObject
from panda3d.core import Loader, NodePath, Vec3
from direct.task.Task import TaskManager
from typing import Callable
from direct.task import Task
class Spaceship(SphereCollideObject):
    def __init__(self, loader: Loader, taskMgr: TaskManager, accept: Callable[[str, Callable], None], modelPath: str, parentNode: NodePath, nodeName: str, texPath: str, posVec: Vec3, scaleVec: float):
        super(Spaceship, self).__init__(loader, modelPath, parentNode, nodeName, Vec3(0,0,0), 1)
        self.taskMgr = taskMgr
        self.accept = accept
        self.modelNode.setPos(posVec)
        self.modelNode.setScale(scaleVec)
        self.modelNode.setName(nodeName)
        tex = loader.loadTexture(texPath)
        self.modelNode.setTexture(tex, 1)

        self.setKeyBindings