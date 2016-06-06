import matplotlib.pyplot as plt
from metaheuristic import simulated_annealing
from temperature import temperatures
from camera_placing import board_utils, problem, quality_functions

if __name__ == "__main__":
    board = board_utils.BoardUtils.get_board_from_file('board')
    qualities = []
    angles = []
    for angle in range(10, 360, 50):
        p = problem.Problem(board, angle, 8, 30, quality_functions.LinearQuality(8, 1))
        t = temperatures.GeometricTemperature(0, 900)
        alg = simulated_annealing.SimulatedAnnealing(p, t, 1000)
        res = alg.get_result()
        qualities.append(p.energy(res))
        angles.append(angle)
        print angle

    plt.plot(angles, qualities, 'ro')
    plt.title("quality of result / camera vision angle")
    plt.show()