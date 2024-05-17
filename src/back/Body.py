class Body:
    def __init__(self, mass, x, y, vx, vy, custom_repr=False):
        self.mass = mass
        self.x = x
        self.y = y
        self. vx = vx
        self.vy = vy
        self.custom_repr = custom_repr

    @property
    def position(self, x , y):
        return self._position

    @position.setter
    def position(self, values):
        self._position = values

    @property
    def speed(self, vx , vy):
        return self._speed

    @property
    def mass(self):
        return self._mass

    def __repr__(self) -> str:
        if self.custom_repr:
            return f"{self.mass}KG ({self.x}, {self.y}) ({self.vx}, {self.vy})"