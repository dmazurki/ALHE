import matplotlib.pyplot as plt
import numpy
from metaheuristic import simulated_annealing
from temperature import temperatures
from camera_placing import board_utils, problem, quality_functions

if __name__ == "__main__":
    board = board_utils.BoardUtils.get_board_from_file('board')
    p = problem.Problem(board, 60, 8, 1000, quality_functions.LinearQuality(1, 1))
    t_speeds = []
    cams = []
    not_covered = []
    for t_speed in numpy.arange(0.98, 0.999, 0.001):
        t = temperatures.GeometricTemperature(t_speed, 900)
        alg = simulated_annealing.SimulatedAnnealing(p, t, 1000)
        res = alg.get_result()
        t_speeds.append(t_speed)
        cams.append(p.get_cameras_number(res))
        not_covered.append(p.get_not_covered_points(res))

    plt.plot(t_speeds, cams, 'g^')
    plt.title("cameras / cooling speed")
    plt.show()

    plt.plot(t_speeds, not_covered, 'ro')
    plt.title("not covered points / cooling speed")
    plt.show()
