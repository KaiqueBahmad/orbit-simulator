from Body import Body
import json

class GravitationSystem:

    def __init__(self, bodies:list, tickLength:float):
        self.bodies:list = bodies
        self.tickLength:float = tickLength
    
    def nextTick(self):
        pass

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
    b1:Body = Body(300, 200, 10, 100, 200)
    b2:Body = Body(500, 1200, -200, 100, 200)
    b3:Body = Body(300, -1100, -900, 100, 200)
    gs = GravitationSystem([b1, b2, b3], 0.1)
    print(gs.createMapPosition())


