import matplotlib.pyplot as plt
from metaheuristic import simulated_annealing
from temperature import temperatures
from camera_placing import board_utils, problem, quality_functions

if __name__ == "__main__":
    board = board_utils.BoardUtils.get_board_from_file('board')
    input_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    qualities = []
    for inputVal in input_data:
        values = []
        p = problem.Problem(board, 60, 8, 40, quality_functions.LinearQuality(inputVal, 1))
        t = temperatures.GeometricTemperature(0, 900)
        for i in range(0, 3):
            alg = simulated_annealing.SimulatedAnnealing(p, t, 1000)
            res = alg.get_result()
            values.append(p.get_not_covered_points(res))
            print inputVal
        qualities.append((values[0] + values[1] + values[2])/3.0)
    plt.plot(input_data, qualities, 'ro')
    plt.title("not covered points / quality function parameters ratio(number of cameras/number of uncovered points)")
    plt.show()
