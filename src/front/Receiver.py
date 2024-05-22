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
        loop = True
        while loop:
            with open('src/mailbox','r') as file:
                
                content = file.readlines()
                
                self.boxStatus = content[0].strip()
                print(self.boxStatus)
                if self.boxStatus == '0':
                    #os.system(clear)
                    currentId = content[1].strip
                    
                    print(content)
                    data = []
                    data = content[2]
                    dataDict = json.loads(data)
                    for element in dataDict:
                        planets.append(element)
                    content[0] = '1\n'
                    print(content)
                    with open('src/mailbox', 'w') as file:
                        file.writelines(content)
                continue
                
                
                    
                    
                
            
       
            

