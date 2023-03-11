class Car:
    def __init__(self, max_speed, unit):
        self.max_speed = max_speed
        self.unit = unit

    def __str__(self):
        return f('Car with the maximum speed of {str(self.max_speed)} {str(self.unit)}')


class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return f('Boat with the maximum speed of {str(self.max_speed)} knots')
