from Body import Body
import typing
import math
import json
from pprint import pprint


#Exemplo de função para ajudar quem for escrever aqui
def zero_filled_array(array_size): #Coloque nomes entendíveis nos argumentos
    array = []
    for i in range(array_size):
        array.append(0)
    return array #A saída NAO deve ser um print, deve ser sempre um retorno
            # Use prints apenas para DEBUGAR assim que o código estiver
            # funcionando, remova os prints!!

def somaLista(a:list,b:list) -> list:
    soma = [a[0]+b[0], a[1]+b[1]]
    return soma

def allPeersList(source:list) -> list:
    retorno = set()
    for element in source:
        for element_ in source:
            if element == element_:
                continue
            retorno.add((element, element_))
    return list(retorno)

#G stands for the gravitional constant, bigger it's more powerful gravity will be
def forceBetween(b1:Body, b2:Body, G:float=1) -> list :
    distance:float = ( (b1.x - b2.x)**2 + (b1.y - b2.y)**2 )**(1/2)
    sin:float = (b2.y - b1.y) / distance
    cos:float = (1-sin**2)**(1/2)
    #Calculates the force between the bodies
    force:float =  (b1.mass * b2.mass) / distance**2
    force *= G #Applies the gravitiational constant
    fx:float = abs(force * cos) # Decomposes the force to X
    fy:float = abs(force * sin) # Decomposes the force to Y
    if (b1.x > b2.x):
        fx = -fx
    if (b1.y > b2.y):
        fy = -fy
    return [fx, fy]        # The return is the decomposed forces

def firstBit():
        try:
            with open("src/mailbox", 'r', encoding="utf-8") as file:
                return file.read(1)
        except:
            return 0
        
def readThirdLine():
    try:
        with open("src/mailbox", 'r', encoding="utf-8") as file:
            return file.readlines()[2]
    except:
        return '[]'

def parseStringToBody(string):
    dados = json.loads(string)
    retorno = []
    if type(dados) == list:
        for i in dados:
            mass = float(i["mass"])
            x = float(i["x"])
            y = float(i["y"])
            vx = float(i["vx"])
            vy = float(i["vy"])
            retorno.append(Body(mass, x, y, vx, vy))
    else:
        mass = float(dados["mass"])
        x = float(dados["x"])
        y = float(dados["y"])
        vx = float(dados["vx"])
        vy = float(dados["vy"])
        retorno = [Body(mass, x, y, vx, vy)]
    if type(retorno) == Body or (type(retorno) and (len(retorno) == 0 or type(retorno[0]) == Body)):
        return retorno
    else:
        return []

if __name__ == "__main__":
    toParse = '[{"mass":150, "x":300,"y":500,"vx":100,"vy":200},{"mass":150, "x":300,"y":500,"vx":100,"vy":200}]'
    pprint(parseStringToBody(toParse))

