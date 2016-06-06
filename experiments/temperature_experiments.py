import matplotlib.pyplot as plt
import numpy
from metaheuristic import simulated_annealing
from temperature import temperatures
from camera_placing import board_utils, problem, quality_functions

if __name__ == "__main__":
    board = board_utils.BoardUtils.get_board_from_file('board')
    p = problem.Problem(board, 60, 8, 1000, quality_functions.LinearQuality(1, 1))
    t_speeds = []
    qualities = []
    for t_speed in numpy.arange(0.0, 0.7, 0.1):
        t = temperatures.GeometricTemperature(t_speed, 900)
        alg = simulated_annealing.SimulatedAnnealing(p, t, 1000)
        res = alg.get_result()
        t_speeds.append(t_speed)
        qualities.append(p.energy(res))
        print t_speed

    plt.plot(t_speeds, qualities, 'ro')
    plt.title("quality of result / cooling speed")
    plt.show()


