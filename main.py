import matplotlib.pyplot as pyplot


class Test:
    def __init__(self):
        self.masse = 0
        self.areal = 0


class Graph:
    def draw(self, x, y, title, color):
        plot.title(str(title))
        plot.plot(x, y, color=str(color))
        plot.grid()
        plot.show()
