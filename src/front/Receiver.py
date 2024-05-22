# Utilitário para acompanhar em tempo real
# a mudança do texto de um arquivo
import json
import os
import time

clear = ""
if os.name == "posix":
    clear = 'clear'
if os.name == "nt":
    clear = 'cls'

# Fica lendo o arquivo em loop, quando ele mudar, limpa a tela e exibe o arquivo
last_content = ''
class Receiver:
    def __init__(self):
        self.currentId
        self.planets = []
    def storeData(self,obj):
        status = obj[0]
        Receiver.currentId = obj[1]
        data = obj[2]
        datadict = json.loads(data)
        self.planets = []
        for i in datadict:
            self.planets.append(i)
    def storePlanet(obj):
        Receiver.planets.append(obj)
        with open('src/mailbox','w') as file:
            file.write(f"2\n{Receiver.currentId}{json.dumps(Receiver.planets)}\n")
        
    def readMailbox(self):
    
        with open('src/mailbox','r') as file:

            content = file.readlines()
            if content != last_content:
                os.system(clear)
                last_content = content
                Receiver.storeData(Receiver,content)
                print(Receiver.planets)
        
            

