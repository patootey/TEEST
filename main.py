import matplotlib.pyplot as plot
import math


class Test:
    def __init__(self):
        self.MASS = 0.076
        self.AREA = 0.3472
        self.SHAPE = 1.75
        self.height = 12
        self.DRAG_COEFFICIENT = self.SHAPE
        self.GRAVITY = 9.81
        self.DENSITY = 1.293
        self.velocity = 0
        self.drag = 0
        self.acceleration = 0

    # calculates ..
    def dragondznutz(self):
        self.drag = (
            self.DRAG_COEFFICIENT * self.AREA * 0.5 * self.DENSITY * self.velocity
        )
        return self.drag

    # calculates acceleration from the ...
    def accel(self):
        self.acceleration = (self.GRAVITY * self.MASS - self.dragondznutz()) / self.MASS

    # calculates velocity
    def vello(self, time, delta):
        self.velocity = self.acceleration * ((time + delta) - time) + self.velocity

    #
    def heighg(self, delta):
        self.height = self.height - (self.velocity * delta)

    # calculates terminal velocity
    def terminalvelocity(self):
        return math.sqrt(2 * self.MASS * self.GRAVITY) / (
            self.DENSITY * self.AREA * self.DRAG_COEFFICIENT
        )


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
    print(array_acceleration)
    plot.plot(array_time, array_acceleration)
    plot.show()


if __name__ == "__main__":
    main()
