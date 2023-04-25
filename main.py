import matplotlib.pyplot as plot


class Test:
    def __init__(self):
        self.MASS = 0
        self.AREA = 0
        self.SHAPE = 0
        self.HEIGHT = 0
        self.DRAG_COEFFICIENT = self.SHAPE
        self.GRAVITY = 0
        self.DENSITY = 0
        self.velocity = 0
        self.drag = 0
        self.acceleration = 0

    def dragondznutz(self):
        return self.DRAG_COEFFICIENT * self.AREA * 0.5 * self.DENSITY * self.velocity**2

    def differential_equation(self, x):
        # v-v0 / t-t0 = g - kv^2
        pass

class Graph:
    def draw(self, x, y, title, color):
        plot.title(str(title))
        plot.plot(x, y, color=str(color))
        plot.grid()
        plot.show()
