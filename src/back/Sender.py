#This will be what will send the data to mailbox
# Exemplo de BackEnd da nossa arquitetura
# Esse programa pode ser desrito em um 
# loop de 3 ações
# 1) Escrever no arquivo
# 2) Aguardar a tela marcar que leu 
# 3) Volta à primeira etapa
import json
from random import randint
from GravitationalSystem import GravitationalSystem
from Body import Body
from time import time, sleep
from threading import Thread
from utils import firstBit
# Mailer: a ideia é que ele é o "mensageiro" que entrega as mensagens
# para a bridge, e ele segue um protocolo simples
# 1° Linha é um 0 ou 1, que significa respectivamente Lido / Não Lido
# 2° Linha é um ID que representa o n° da mensagem enviada, sequencialmente 1, depois 2, depois 3 ...
# 3° e as posteriores são o conteudo em JSON
# Exemplo de arquivo:
# 0
# 100
# {
#    "atributo1": "valor1",
#    "atributo2": 2
# }
class Sender:
    def __init__(self, gravitySystem:GravitationalSystem):
        self.currentId = 0
        self.gravitySystem = gravitySystem
        self.framerate = 30
    
    def setFramerate(self, newFramerate):
        self.framerate = newFramerate

    def simulate(self):
        # This should do the simulation of the system
        pass
    
    def save(self, obj):
            with open('../mailbox','w', encoding='utf-8' ) as file:
                self.currentId += 1
                file.write(f"0\n{self.currentId}\n{obj}\n")
        # while True:
        #     with open('../mailbox','r+', encoding='utf-8' ) as file:
        #         if file.read(1) == '0':
        #             file.close()
        #             continue
        #         file.seek(0)
        #         file.write(f"0\n{self.currentId}\n{json.dumps(obj)}\n")
        #         self.currentId = self.currentId + 1
        #         file.close()
        #         break


    def genSecond(self, store=False, where=None):
        secondFrames = []
        framesGenerated = 0
        framesToGenerate = int(1/self.gravitySystem.tickLength)
        for i in range(framesToGenerate):
            if i/framesToGenerate > (framesGenerated + 1)/self.framerate:
                framesGenerated += 1
                self.gravitySystem.nextTick()
                secondFrames.append(self.gravitySystem.createMapPosition())
                continue
            self.gravitySystem.nextTick()
        secondFrames.append(self.gravitySystem.createMapPosition())
        if store:
            where[0] = secondFrames
        else:
            return secondFrames
        
    def loop(self):
        actualFrames = []
        futureFrames = self.genSecond()
        secondsPerFrame = 1 / self.framerate
        thread = Thread(target=lambda :None)
        thread.start()
        while True:
            thread.join()
            actualFrames = futureFrames[0]
            futureFrames = [False]
            thread = Thread(target=self.genSecond, kwargs={"store":True,"where":futureFrames})
            thread.start()
            for i in range(self.framerate):
                
                if firstBit() == "0":
                    pass
                else:
                    status = firstBit()
                    if status == "1":
                        self.save(actualFrames[i])
                    elif status == "2":
                        # Função para ler a 3° linha do arquivo verificar se dá pra montar um planeta
                        # montar o planeta e adicionar no sistema
                        # self.gravitySystem.addBody(None)
                        pass
                sleep(secondsPerFrame)

    def benchmark(self):
        t1 = time()
        qtd = 100000
        print(self.gravitySystem.createMapPosition())
        for i in range(qtd):
            self.gravitySystem.nextTick()
            self.gravitySystem.createMapPosition()
        t2 = time()
        delta = t2-t1
        print("--------------------------")
        print(self.gravitySystem.createMapPosition())

        print(f"Benchmark levou {delta:.2} segundos")
        print(f"Gerando {int(qtd/delta)} ticks/s")

if __name__ == '__main__':
    system = GravitationalSystem([], 0.0001)
    system.addBody(Body(1000, 100, -100, 25, 25))
    system.addBody(Body(2000, 150, -200, 35, 15))
    system.addBody(Body(10000, 0, 0, 10, 10))
    sender = Sender(system)
    sender.loop()

