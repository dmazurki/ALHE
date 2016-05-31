from camera_placing import (problem, state, board_utils, camera)
from optparse import OptionParser
from metaheuristic import simulated_annealing
from temperature import temperatures

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", action="store", dest="filename", default="board_example")
    parser.add_option("-a", "--angle", action="store", type="int", default=30)
    parser.add_option("-r", "--range", action="store", type="int", default=6)
    parser.add_option("-t", "--temperature", action="store", type="float", default=0.1)
    parser.add_option("-m", "--maxCam", action="store", type="int", default=4)
    (options, args) = parser.parse_args()
    board = board_utils.BoardUtils.get_board_from_file(options.filename)
    p = problem.Problem(board, options.angle, options.range, options.maxCam)
    t = temperatures.LinearTemperature(10, 0.01)
    alg = simulated_annealing.SimulatedAnnealing(p, t)
    board_utils.BoardUtils.show_board_representation(board, alg.get_result())
