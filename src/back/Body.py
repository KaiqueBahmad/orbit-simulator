class Body:
    def __init__(self, mass, x, y, vx, vy, custom_repr=False):
        self.mass = mass
        self.x = x
        self.y = y
        self. vx = vx
        self.vy = vy
        self.custom_repr = custom_repr

    def __repr__(self) -> str:
        if self.custom_repr:
            return f"{self.mass}KG ({self.x}, {self.y}) ({self.vx}, {self.vy})"
        else:
            return super().__repr__()
if __name__ == '__main__':
    b1 = Body(1, 1, 1, 1, 1)
