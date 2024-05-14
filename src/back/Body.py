class Body:
    def __init__(self, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        self. vx = vx
        self.vy = vy

    def __repr__(self) -> str:
        repr_ = "\n"
        repr_ += "-"*25
        repr_ += f"\nMassa: {self.mass}"
        repr_ += f"\nPosition: ({self.x}, {self.y})\n"
        repr_ += f"Speed: ({self.vx}, {self.vy})\n"
        repr_ += "-"*25
        
        return repr_

if __name__ == '__main__':
    b1 = Body(1, 1, 1, 1, 1)