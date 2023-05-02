import matplotlib.pyplot as plot
import math

def draw(x, y, title, color):
    plot.title(str(title))
    plot.plot(x, y, color)
    plot.grid()
    plot.show()


class Test:
    def __init__(self):
        self.MASS = 30
        self.AREA = 100
        self.SHAPE = 0.3
        self.height = 50
        self.DRAG_COEFFICIENT = self.SHAPE
        self.GRAVITY = 9.81
        self.DENSITY = 1.1
        self.velocity = 0
        self.drag = 0
        self.acceleration = 0

    def dragondznutz(self):
        self.drag = self.DRAG_COEFFICIENT * self.AREA * 0.5 * self.DENSITY * self.velocity**2
        return self.drag
    def accel(self):
        self.acceleration = (self.GRAVITY*self.MASS - self.dragondznutz())/self.MASS
    def vello(self, time, delta):
        self.velocity = self.acceleration * ((time + delta)-time) + self.velocity
    def heighg(self, delta):
        self.height = self.height - (self.velocity*delta)
    def terminalvelocity(self):
        return (math.sqrt(2*self.MASS*self.GRAVITY)/(self.DENSITY*self.AREA*self.DRAG_COEFFICIENT))
def main():
    Object = Test()
    array_time, array_height, array_velocity, array_acceleration = [], [], [], []
    delta = 0.1
    time = 0
    while Object.height > 0:
        array_time.append(time)
        array_height.append(Object.height)
        array_velocity.append(Object.velocity)

        Object.vello(time, delta)
        Object.accel()
        time += delta
        Object.heighg(delta)

        array_acceleration.append(Object.acceleration)
    print(array_velocity)
    print(Object.terminalvelocity())
    draw(array_time, array_velocity, "fart", (255,0,0))


if __name__ == "__main__":
    main()