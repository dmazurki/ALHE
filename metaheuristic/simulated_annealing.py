import random
import math

#implementation of algorithm
class SimulatedAnnealing:
    def __init__(self, problem, temperature, iterations):
        self.problem = problem
        self.temperature = temperature
        self.iterations = iterations

        x = self.problem.generate_initial_state()
        iteration = 0
        temperature = self.temperature(iteration)
        while iteration < iterations:
            y = x.get_neighbour()
            x_energy = self.problem.energy(x)
            y_energy = self.problem.energy(y)
            tolerance = self.tolerance(x_energy, y_energy, temperature)
            if y_energy < x_energy or random.random() < tolerance:
                x = y
            iteration += 1
            temperature = self.temperature(iteration)
        self.result = x

    def get_result(self):
        return self.result

    @staticmethod
    def tolerance(x_energy, y_energy, temperature):
        return math.exp(-math.fabs(y_energy - x_energy) / temperature)
