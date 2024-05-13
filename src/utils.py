from back.Body import Body
import typing
import math

#Exemplo de função para ajudar quem for escrever aqui
def zero_filled_array(array_size): #Coloque nomes entendíveis nos argumentos
    array = []
    for i in range(array_size):
        array.append(0)
    return array #A saída NAO deve ser um print, deve ser sempre um retorno
                 # Use prints apenas para DEBUGAR assim que o código estiver
                 # funcionando, remova os prints!!

#G stands for the gravitional constant, bigger it's more powerful gravity will be
def forceBetween(b1:Body, b2:Body, G:float=1) -> list :
    distance:float = ( (b1.x - b2.x)**2 + (b1.y - b2.y)**2 )**(1/2)
    sin:float = abs(b2.y - b1.y) / distance
    cos:float = (1-sin**2)**(1/2)
    #Calculates the force between the bodies
    force:float =  (b1.mass * b2.mass) / distance**2
    force *= G #Applies the gravitiational constant
    fx:float = force * cos # Decomposes the force to X
    fy:float = force * sin # Decomposes the force to Y
    return [fx, fy]        # The return is the decomposed forces

