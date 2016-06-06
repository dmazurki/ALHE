import matplotlib.pyplot as plt
from metaheuristic import simulated_annealing
from temperature import temperatures
from camera_placing import board_utils, problem, quality_functions

if __name__ == "__main__":
    board = board_utils.BoardUtils.get_board_from_file('board')
    qualities = []
    ranges = []
    for rangeVal in range(2, 20, 2):
        p = problem.Problem(board, 60, rangeVal, 30, quality_functions.LinearQuality(8, 1))
        t = temperatures.GeometricTemperature(0, 900)
        alg = simulated_annealing.SimulatedAnnealing(p, t, 1000)
        res = alg.get_result()
        qualities.append(p.energy(res))
        ranges.append(rangeVal)
        print rangeVal

    plt.plot(ranges, qualities, 'ro')
    plt.title("quality of result / camera vision range")
    plt.show()