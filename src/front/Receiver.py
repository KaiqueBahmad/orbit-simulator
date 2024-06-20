# Utilitário para acompanhar em tempo real
# a mudança do texto de um arquivo
import json
import os
import time
from PySide6.QtCore import QRunnable, Slot, QThreadPool
from time import sleep
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import QEventLoop, QObject
from PySide6.QtCore import Signal, Slot,QThread
# Fica lendo o arquivo em loop, quando ele mudar, limpa a tela e exibe o arquivo
class Receiver(QRunnable):
    

    def __init__(self, main_screen):
        super(Receiver, self).__init__()
        self.main_screen = main_screen
        self.signals = ReceiverSignals()
        
    @Slot()
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
                    self.signals.addPlanetsSignal.emit(data)
                    print("evento enviado")
                    #self.replacePlanetsOnScreen(dataDict)
                    if len(self.main_screen.planets_queue) > 0:
                        new_planets_string = json.dumps(self.main_screen.planets_queue)
                        file.seek(0)
                        file.truncate()
                        file.seek(0)
                        file.write(f"2\n\n{new_planets_string}\n")
                        self.main_screen.planets_queue = []
                    else:
                        file.seek(0)
                        file.write("1")

    
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


class ReceiverSignals(QObject):
    addPlanetsSignal = Signal(str)
    


