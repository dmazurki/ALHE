from camera_placing import (problem, state, board_utils)
from metaheuristic import simulated_annealing
from temperature import temperatures

b = '''0000000000000;
       0000000000111;
       1111111111111;
       0000000000000
    '''
if __name__ == '__main__':
    board = board_utils.BoardUtils.get_board_from_string(b)
    p = problem.Problem(board, 90, 5)
    t = temperatures.LinearTemperature(5, 0.001)
    alg = simulated_annealing.SimulatedAnnealing(p, t)
    print alg.get_result()
