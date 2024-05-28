# Utilitário para acompanhar em tempo real
# a mudança do texto de um arquivo
import json
import os
import time
from PySide6.QtCore import QRunnable, Slot, QThreadPool
from time import sleep

clear = ""
if os.name == "posix":
    clear = 'clear'
if os.name == "nt":
    clear = 'cls'

# Fica lendo o arquivo em loop, quando ele mudar, limpa a tela e exibe o arquivo
previous_content = []
planets = []
currentId = "0"
class Receiver(QRunnable):
    
    @Slot()    
    def run(self):
        loop = True
        while loop:
            if self.firstBit() == '0':
                data = []
                with open('src/mailbox','r+', encoding='utf-8') as file:
                    file.seek(0)
                    content = file.readlines()
                    data = content[2]
                    dataDict = json.loads(data)
                    for element in dataDict:
                        planets.append(element)
                    file.seek(0)
                    file.write("1")

    def firstBit(self):
        try:
            with open("../mailbox", 'r', encoding="utf-8") as file:
                return file.read(1)
        except:
            return 1
    
    def storePlanet(self,obj):
        planets.append(obj)
        self.boxStatus = '0'            
            