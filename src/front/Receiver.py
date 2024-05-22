# Utilitário para acompanhar em tempo real
# a mudança do texto de um arquivo
import json
import os
import time

from PySide6.QtCore import QRunnable, Slot, QThreadPool


clear = ""
if os.name == "posix":
    clear = 'clear'
if os.name == "nt":
    clear = 'cls'

# Fica lendo o arquivo em loop, quando ele mudar, limpa a tela e exibe o arquivo
previous_content = []
planets = []
currentId = '0'
class Receiver(QRunnable):
    
    @Slot()    
    def run(self):
        print('start')
        with open('src/mailbox','r') as file:
            
            content = file.readlines()
            
            print(content)
            
            self.currentId = content[0].strip()
            
            if self.currentId == '0':
                #os.system(clear)
                print("sabado")
                print(content)
                Manager.storeData(content)
                print('sex')
                print(Receiver.planets)
            
class Manager():
    
    def storeData(self,obj):
        data = []
        data = obj[2]
        try:
            datadict = json.loads(data)
        except json.JSONDecodeError as e:
            print("erro")
            
        for i in datadict:
            self.planets.append(i)
            print("a")
    
    
    def storePlanet(self,obj):
        self.planets.append(obj)
        with open('src/mailbox','w') as file:
            file.write(f"2\n{Receiver.currentId}\n{json.dumps(Receiver.planets)}\n")
       
            

