from camera_placing import (problem, state, board_utils, camera)
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
    board = board_utils.BoardUtils.get_board_from_string(b)
    p = problem.Problem(board, 100, 1)
    cam = camera.Camera(3, 3, 0, p)
    s = state.State(p, [cam])
    board_utils.BoardUtils.show_board_representation(board, s)
