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
            
            # with open('src/mailbox','r+') as file:
            #     file.seek(0)
            #     content = file.readlines()
            #     self.boxStatus = content[0].strip()
                
            #     if self.boxStatus == '0':
            #         #os.system(clear)
            #         #currentId = content[1].strip + 1
                    
            #         print(content)
                    # data = []
                    # data = content[2]
                    # dataDict = json.loads(data)
                    # for element in dataDict:
                    #     planets.append(element)
                        
                    # content[0] = '1'
                    # print(content)
                    # file.seek(0)
                    # file.write("\n".join(content))
            #     continue

    def firstBit(self):
        try:
            with open("../mailbox", 'r', encoding="utf-8") as file:
                return file.read(1)
        except:
            return 0
    
    def storePlanet(self,obj):
        planets.append(obj)
        self.boxStatus = '0'
       # with open('src/mailbox','w') as file:
        #    file.write(f"0\n{currentId}\n{json.dumps(planets)}\n")

                    
                    
                
            
       
            
