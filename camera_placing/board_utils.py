import StringIO

class BoardUtils:
    def __init__(self):
        pass

    def get_board_from_file(self, filename):
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

    @staticmethod
    def board_representation(board_string, cameras_state = None):
        result = StringIO.StringIO()
        for x in range(0, len(board_string)):
            for y in board_string[x]:
                if y == True:
                    result.write('x')
                if y == False:
                    result.write(' ')
            result.write('\n')
        return result.getvalue()

