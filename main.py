from camera_placing import (problem, state, board_utils, camera)
from optparse import OptionParser
from metaheuristic import simulated_annealing
from temperature import temperatures

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", action="store", dest="filename", default="board_example")
    parser.add_option("-a", "--angle", action="store", type="int", default=60)
    parser.add_option("-r", "--range", action="store", type="int", default=8)
    parser.add_option("-t", "--iterations", action="store", type="int", default=1600)
    parser.add_option("-m", "--maxCam", action="store", type="int", default=1000)
    (options, args) = parser.parse_args()
    board = board_utils.BoardUtils.get_board_from_file(options.filename)
    p = problem.Problem(board, options.angle, options.range, options.maxCam)
    t = temperatures.GeometricTemperature(0.993, 500)
    alg = simulated_annealing.SimulatedAnnealing(p, t, options.iterations)
    board_utils.BoardUtils.show_board_representation(board, alg.get_result())
