from camera_placing import (problem, state, board_utils, camera)
from optparse import OptionParser
from metaheuristic import simulated_annealing
from temperature import temperatures

b = '''0000000000000;
       0000000000000;
       0000000000000;
       0000000001100;
       0000000000000;
       0000000000000
    '''
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--file", action="store", dest="filename")
    parser.add_option("-a", "--angle", action="store", type="int")
    parser.add_option("-r", "--range", action="store", type="int")
    parser.add_option("-t", "--temperature", action="store", type="float")
    parser.add_option("-m", "--maxCam", action="store", type="int")
    (options, args) = parser.parse_args()
    board = board_utils.BoardUtils.get_board_from_file(options.filename)
    p = problem.Problem(board, options.angle, options.range)
    cam = camera.Camera(3, 3, 0, p)
    s = state.State(p, [cam])
    board_utils.BoardUtils.show_board_representation(board, s)
