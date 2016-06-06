import matplotlib.pyplot as plt
from metaheuristic import simulated_annealing
from temperature import temperatures
from camera_placing import board_utils, problem, quality_functions

if __name__ == "__main__":
    board = board_utils.BoardUtils.get_board_from_file('board')
    iterations_cases = [50, 100, 200, 400, 700, 1000, 1500, 2000, 3000, 4000]
    p = problem.Problem(board, 60, 8, 1000, quality_functions.LinearQuality(1, 1))
    qualities = []
    for iterations in iterations_cases:
        t = temperatures.GeometricTemperature(0, 900)
        alg = simulated_annealing.SimulatedAnnealing(p, t, iterations)
        res = alg.get_result()
        qualities.append(p.energy(res))
        print iterations

    plt.plot(iterations_cases, qualities, 'ro')
    plt.title("quality of result / number of iterations")
    plt.show()