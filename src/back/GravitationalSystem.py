from Body import Body
import json
from typing import *
import utils
from pprint import pprint

class GravitationalSystem:

    def __init__(self, bodies:List[Body], tickLength:float):
        self.bodies:List[Body] = bodies
        self.tickLength:float = tickLength
    
    def addBody(self, body:Body):
        self.bodies.append(body)        

    def nextTick(self):
        forcesList = []
        permutations:List[Tuple[Body, Body]] = utils.allPeersList(self.bodies)
        forces = {}
        for i in permutations:
            forces[i] = utils.forceBetween(i[0], i[1], G=0.0001)
            if forces[i] == [-1, -1]:
                self.bodies.remove(i[0])
                self.bodies.remove(i[1])
                planetaSoma = Body(
                    mass= i[0].mass + i[1].mass,
                    x= i[0].x,
                    y=i[0].y,
                    vx= i[0].vx + i[1].vx,
                    vy= i[0].vy + i[1].vy
                )
                self.addBody(planetaSoma)
                return self.nextTick()
                
        for i in self.bodies:
            resultant_force = [0, 0]
            for j in self.bodies:
                if (i, j) in forces:
                    force_to_add = forces[(i, j)] 
                    resultant_force[0] += force_to_add[0]
                    resultant_force[1] += force_to_add[1]
                elif (j, i) in forces:
                    force_to_add = forces[(j, i)] 
                    resultant_force[0] -= force_to_add[0]
                    resultant_force[1] -= force_to_add[1]
            i.x  += i.vx * self.tickLength
            i.y  += i.vy * self.tickLength
            i.vx += resultant_force[0] * self.tickLength
            i.vy += resultant_force[1] * self.tickLength



    def setTickLength(self, length:float):
        self.tickLength = length
    
    def createMapPosition(self) -> str:
        objects = [json.dumps(CappedBody(x).__dict__) for x in self.bodies]
        objects  = ", ".join(objects)
        objects  = f"[{objects}]"
        return objects

class CappedBody:
    def __init__(self, body:Body):
        self.mass = body.mass
        self.x = body.x
        self.y = body.y

if __name__ == "__main__":
    b1:Body = Body(300, 200, 10, 100, 200, custom_repr=True)
    b2:Body = Body(500, 1200, -200, 100, 200, custom_repr=True)
    b3:Body = Body(300, -1100, -900, 100, 200, custom_repr=True)
    gs = GravitationalSystem([b1, b2, b3], 1)
    for i in range(50):
        [pprint(x) for x in gs.bodies]
        gs.nextTick()
        print("-"*50)
    # print(gs.createMapPosition())


