import matplotlib.pyplot as plot


class Test:
    def __init__(self):
        self.mass = 0
        self.area = 0
        self.height = 0


class Graph:
    def draw(self, x, y, title, color):
        plot.title(str(title))
        plot.plot(x, y, color=str(color))
        plot.grid()
        plot.show()
