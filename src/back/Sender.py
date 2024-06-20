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
from utils import firstBit, readThirdLine, parseStringToBody
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
        if len(str(obj)) != 1:
            
            with open('src/mailbox','w', encoding='utf-8' ) as file:
                self.currentId += 1
                file.write(f"0\n{self.currentId}\n{obj}\n")

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
                    continue
                else:
                    status = firstBit()
                    if status == "1":
                        if type(actualFrames) == list:
                            self.save(actualFrames[i])
                    elif status == "2":
                        planetData = readThirdLine()
                        print(planetData)
                        new_planets = parseStringToBody(planetData)
                        print(new_planets)
                        for planet in new_planets:
                            print(planet)
                            self.gravitySystem.addBody(planet)
                        if type(actualFrames) == list:
                            self.save(actualFrames[i])
                        # Função para ler a 3° linha do arquivo verificar se dá pra montar um planeta
                        # montar o planeta e adicionar no sistema
                        # self.gravitySystem.addBody(None)

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
    system = GravitationalSystem([], 0.001)
    system.addBody(Body(1000, 100, -100, 25, 25))
    system.addBody(Body(2000, 150, -200, 35, 15))
    system.addBody(Body(100000, 0, 0, 50, 10))
    sender = Sender(system)
    sender.loop()
    #print(firstBit())
