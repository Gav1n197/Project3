## Project3 2/20/25 3DGameEngineConcepts
## Comments on column 81, 
## All file names and folder names are capitalized (Assets/Planets/Textures/WhitePlanet.png)

import math, sys, random
from direct.showbase.ShowBase import ShowBase 
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses
#from direct.task import Task

class MyApp(ShowBase):
    def __init__(self): ## Constructor
        ShowBase.__init__(self)
        self.accept('escape', self.quit)  ## Esc to escape
        self.setupScene()
        self.setCamera()
        
        fullCycle = 60
        for i in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)  ##Concantenation of nicknames for each drone made

            self.DrawCloudDefense(self.planet1, nickName)
            self.drawBaseballSeams(self.SpaceStation1, nickName, i, fullCycle, 2)
            self.drawCircleX(self.planet3, nickName, i, fullCycle, 225)
            self.drawCircleY(self.planet4, nickName, i, fullCycle, 175)
            self.drawCircleZ(self.planet5, nickName, i, fullCycle, 425)


    def setupScene(self): ## snailCase for entire project
        self.universe = spaceJamClasses.Universe(self.loader, "Assets/Universe/Universe.x", self.render, "Universe", "Assets/Universe/Universe.jpg", (0,0,0), 10000)

        self.planet1 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet1", "Assets/Planets/Textures/Mercury.jpg",       ( 160,   5000, 1890), 320) 
        self.planet2 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet2", "Assets/Planets/Textures/Moon.jpg",          ( 400,   5400, 2270), 120) 
        self.planet3 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet3", "Assets/Planets/Textures/WhitePlanet.jpg",   (-2700,  6200, 1270), 150) 
        self.planet4 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet4", "Assets/Planets/Textures/Neptune.jpg",       (-2500,  6000, 970),  100) 
        self.planet5 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet5", "Assets/Planets/Textures/Venus.jpg",         ( 3000, -6000, 230),  350)
        self.planet6 = spaceJamClasses.Planet(self.loader, "Assets/Planets/protoPlanet.x", self.render, "planet6", "Assets/Planets/Textures/GreyPlanet.jpg",    (-3000, -6000, 730),  250) 

        self.player = spaceJamClasses.Player(self.loader, "Assets/Spaceships/Dumbledore/Dumbledore.x", self.render, "player", (0, 0, 0), 1, (0, 93, 0))
        
        self.SpaceStation1 = spaceJamClasses.SpaceStation(self.loader, "Assets/SpaceStation/SpaceStation1B/spaceStation.x", self.render, "spaceStation1", "Assets/Planets/Textures/Mercury.jpg", (40, 50, 23), 1) 

    def drawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "Assets/DroneDefender/octotoad1_auv.png", position, 5)
    
    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 200 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "Assets/DroneDefender/octotoad1_auv.png", position, 10)
    
    def drawCircleX(self, centralObject, droneName, step, fullCircle, radius):
        unitVec = defensePaths.CircleX(step, fullCircle)
        unitVec.normalize()
        position = unitVec * radius + centralObject.modelNode.getPos() # adds relativity to the central object
        spaceJamClasses.Drone(self.loader, "Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def drawCircleY(self, centralObject, droneName, step, fullCircle, radius):
        unitVec = defensePaths.CircleY(step, fullCircle)
        unitVec.normalize()
        position = unitVec * radius + centralObject.modelNode.getPos() # adds relativity to the central object
        spaceJamClasses.Drone(self.loader, "Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "Assets/DroneDefender/octotoad1_auv.png", position, 5)
    
    def drawCircleZ(self, centralObject, droneName, step, fullCircle, radius):
        unitVec = defensePaths.CircleZ(step, fullCircle)
        unitVec.normalize()
        position = unitVec * radius + centralObject.modelNode.getPos() # adds relativity to the central object
        spaceJamClasses.Drone(self.loader, "Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "Assets/DroneDefender/octotoad1_auv.png", position, 5)

    def setCamera(self):
        self.disable_mouse()
        self.camera.reparentTo(self.player.modelNode)
        self.camera.setFluidPos(-50, 0, 0)

    def quit(self):
        sys.exit()


app = MyApp()
app.run()