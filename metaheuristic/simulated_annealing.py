import random


class SimulatedAnnealing:
    def __init__(self, problem, temperature):
        self.problem = problem
        self.temperature = temperature
        self.log = []

        self.log.append(self.problem.generate_initial_state())
        x = self.log[0]
        iteration = 0
        while self.temperature(iteration) > 0:
            y = x.get_neighbour()
            x_energy = self.problem.energy(x)
            y_energy = self.problem.energy(y)
            if y_energy > x_energy or random.random() < self.__tolerance(x_energy, y_energy):
                x = y
            self.log.append(y)
            iteration += iteration

    def get_runtime(self):
        pass

    def __tolerance(self, x_energy, y_energy):
        pass
