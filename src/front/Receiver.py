# Utilitário para acompanhar em tempo real
# a mudança do texto de um arquivo
import json
import os
import time
from PySide6.QtCore import QRunnable, Slot, QThreadPool
from time import sleep

# Fica lendo o arquivo em loop, quando ele mudar, limpa a tela e exibe o arquivo
class Receiver():
    
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.planets = []
        
    def run(self):
        loop = True
        while loop:
            print(self.firstBit())
            if self.firstBit() == '0':
                with open('src/mailbox','r+', encoding='utf-8') as file:
                    file.seek(0)
                    content = file.readlines()
                    if len(content) >= 3:
                        data = content[2]
                    else:
                        data = "[]"
                    iwrote = False
                    dataDict = json.loads(data)
                    replacePlanetsOnScreen(data)
                    print(self.main_screen.planets_queue)
                    if len(self.main_screen.planets_queue) > 0:
                        new_planets_string = json.dumps(self.main_screen.planets_queue)
                        file.seek(0)
                        file.write(f"2\n\n{new_planets_string}")
                        self.main_screen.planets_queue = []
                    else:
                        file.seek(0)
                        file.write("1")

    def replacePlanetsOnScreen(planetsData):
        pass
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
            
