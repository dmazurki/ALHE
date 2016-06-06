import math

#represents temperature used by simulated annealing algorithm
class GeometricTemperature:
    def __init__(self, base, parameter):
        self.base = base
        self.parameter = parameter
        self.last_iteration = None
        self.last_temperature = None

    def __call__(self, iteration):
        if self.last_iteration is not None and self.last_iteration == iteration - 1:
            self.last_iteration = iteration
            self.last_temperature = self.last_temperature * self.base
            return self.last_temperature
        else:
            self.last_iteration = iteration
            self.last_temperature = self.parameter * (self.base**iteration)
            return self.last_temperature

