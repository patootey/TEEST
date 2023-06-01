import matplotlib.pyplot as plt
import math
import Prosjekt_Fritt_Fall_Resultat as result


class FrittFall:
    def __init__(self):
        self.MASS = 0.076 # kg
        self.AREA = 0.3472 # m^2
        self.SHAPE = 0.89
        self.GRAVITY = 9.81 # m/s^2
        self.DENSITY = 1.293 # kg/m^3
        self.height = 12 # m
        self.velocity = 0 # m/s
        self.drag = 0 # N
        self.acceleration = 0 # m/s^2

    def calculate_drag(self):
        self.drag = (
            self.SHAPE * self.AREA * 0.5 * self.DENSITY * self.velocity
        )
        return self.drag

    def calculate_acceleration(self):
        self.acceleration = (self.GRAVITY * self.MASS - self.calculate_drag()) / self.MASS

    def calculate_velocity(self, delta):
        self.velocity += self.acceleration * delta

    def calculate_height(self, delta):
        self.height = self.height - (self.velocity * delta)

    def calculate_terminalvelocity(self):
        return math.sqrt(2 * self.MASS * self.GRAVITY) / (
            self.DENSITY * self.AREA * self.SHAPE
        )


def main():
    Object = FrittFall()
    array_time, array_height, array_velocity, array_acceleration = [], [], [], []
    delta = 0.1
    time = 0

    # Calculate and append object values
    while Object.height > 0:
        array_time.append(time)
        array_height.append(Object.height)
        array_velocity.append(Object.velocity)

        Object.calculate_velocity(delta)
        Object.calculate_acceleration()
        time += delta
        Object.calculate_height(delta)

        array_acceleration.append(Object.acceleration)
    plt.plot(array_time, array_velocity, label="Simulation")
    result.main()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()