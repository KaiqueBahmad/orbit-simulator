class Body:
    def __init__(self, mass, x, y, vx, vy, custom_repr=False):
        self.mass = mass
        self.x = float(x)
        self.y = float(y)
        self. vx = float(vx)
        self.vy = float(vy)
        self.custom_repr = custom_repr

    #def __repr__(self) -> str:
    #    if self.custom_repr:
    #        return f"{self.mass}KG ({self.x}, {self.y}) ({self.vx}, {self.vy})"
