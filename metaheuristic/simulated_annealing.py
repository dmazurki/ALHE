import random
import math


class SimulatedAnnealing:
    def __init__(self, problem, temperature):
        self.problem = problem
        self.temperature = temperature

        x = self.problem.generate_initial_state()
        iteration = 0
        temperature = self.temperature(iteration)
        while temperature > 0.01:
            y = x.get_neighbour()
            x_energy = self.problem.energy(x)
            y_energy = self.problem.energy(y)
            tolerance = self.tolerance(x_energy, y_energy, temperature)
            if y_energy < x_energy or random.random() < tolerance:
                x = y
            iteration += 1
            temperature = self.temperature(iteration)
            print x_energy, tolerance
        self.result = x

    def get_result(self):
        en = self.problem.energy(self.result)
        print 'ENERGY',en
        return self.result

    @staticmethod
    def tolerance(x_energy, y_energy, temperature):
        return math.exp(-math.fabs(y_energy - x_energy) / temperature)
