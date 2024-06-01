# Utilitário para acompanhar em tempo real
# a mudança do texto de um arquivo
import json
import os
import time
from PySide6.QtCore import QRunnable, Slot, QThreadPool
from time import sleep
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import DispatchQueue, QEventLoop, QObject
# Fica lendo o arquivo em loop, quando ele mudar, limpa a tela e exibe o arquivo
class Receiver(QObject):
    
    def __init__(self, main_screen):
        self.main_screen = main_screen
      
    def run(self):
        loop = True
        while loop:
            if self.firstBit() == '0':
                with open('src/mailbox','r+', encoding='utf-8') as file:
                    file.seek(0)
                    content = file.readlines()
                    if len(content) >= 3:
                        data = content[2]
                    else:
                        data = "[]"
                    iwrote = False
                    try:
                        dataDict = json.loads(data)
                    except:
                        continue
                    self.replacePlanetsOnScreen(dataDict)
                    print(self.main_screen.planets_queue)
                    if len(self.main_screen.planets_queue) > 0:
                        new_planets_string = json.dumps(self.main_screen.planets_queue)
                        file.seek(0)
                        file.write(f"2\n\n{new_planets_string}")
                        self.main_screen.planets_queue = []
                    else:
                        file.seek(0)
                        file.write("1")

    def replacePlanetsOnScreen(self, planetsData):
        self.main_screen.addThose(planetsData)
        #self.planetsOnScreen = self.planetsIncoming
        #print(planetsData)
        #print(type(planetsData))
        #self.planetsIncoming = [self.mountPlanetInstance(planet) for planet in planetsData]
        #for i in self.planetsOnScreen:
        #    i.deleteLater()

    def mountPlanetInstance(self, planet):
        self.novoPlaneta = QLabel(self.main_screen.background)
        self.novoPlaneta.setGeometry(int(planet["x"]), int(planet["y"]), 30, 30)
        self.novoPlaneta.setStyleSheet("background-color: white")
    

#this is how to delete a planet
#self.novoPlaneta.deleteLater()


    def firstBit(self):
        try:
            with open("src/mailbox", 'r', encoding="utf-8") as file:
                return file.read(1)
        except Exception as exc:
            return 1
    
    def storePlanet(self,obj):
        self.planets.append(obj)
        self.boxStatus = '0'  
        print(self.planets)
            
