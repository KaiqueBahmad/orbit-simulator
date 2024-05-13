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

def allPeersList(source:list) -> list:
    
    return []


#G stands for the gravitional constant, bigger it's more powerful gravity will be
def forceBetween(b1:Body, b2:Body, G:float=1) -> list :
    distance:float = ( (b1.x - b2.x)**2 + (b1.y - b2.y)**2 )**(1/2)
    sin:float = b2.y - b1.y / distance
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


if __name__ == "__main__":
    print(allPeersList([1,2]))
    # b1 = Body(120000000, 0, 0, 0, 0)
    # b2 = Body(120000, -3, 0, 0,0)
    # G = 6.6743*10**(-11)
    # print(forceBetween(b1, b2,G=G))


