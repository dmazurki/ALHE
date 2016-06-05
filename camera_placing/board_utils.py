from matplotlib import pylab
import matplotlib
import numpy
import random

board_c_dict = {'red': ((0, 1, 1),
                        (0.05, 1, 1),
                        (0.11, 0, 0),
                        (0.66, 1, 1),
                        (0.89, 1, 1),
                        (1, 0, 0)),
                'green': ((0, 1, 1),
                          (0.05, 1, 1),
                          (0.11, 0, 0),
                          (0.375, 1, 1),
                          (0.64, 1, 1),
                          (0.91, 0, 0),
                          (1, 0, 0)),
                'blue': ((0, 1, 1),
                         (0.05, 1, 1),
                         (0.11, 1, 1),
                         (0.34, 1, 1),
                         (0.65, 0, 0),
                         (1, 0, 0))}

board_colormap = matplotlib.colors.LinearSegmentedColormap('board_colormap', board_c_dict, 256)


class BoardUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_board_from_string(board_string):
        result = [[]]
        for character in board_string:
            if character == '0':
                result[-1].append(False)
            elif character == '1':
                result[-1].append(True)
            elif character == ';':
                result.append([])

        return result

    #reads file and loads board
    @staticmethod
    def get_board_from_file(filename):
        f = open(filename, 'r')
        return BoardUtils.get_board_from_string(f.read())

    #Visualize result
    @staticmethod
    def show_board_representation(board, cameras_state=None):
        result_matrix = numpy.zeros((len(board), len(board[0]),))

        for x in range(0, len(board)):
            for y in range(0, len(board[x])):
                if board[x][y] is True:
                    result_matrix[x, y] = 1

        if cameras_state is None:
            return

        for cam in cameras_state.cameras:
            col = ((random.random())%0.6)+0.2
            for x in range(0, len(board)):
                for y in range(0, len(board[x])):
                    if cam.point_visible(x, y) and board[x][y] is False:
                        result_matrix[x, y] = col

        pylab.matshow(result_matrix, fignum=100, cmap=board_colormap, vmin=0, vmax=1)
        pylab.show()
