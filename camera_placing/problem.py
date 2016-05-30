import camera_placing.state


class Problem:
    def __init__(self, board, camera_angle, camera_range):
        self.board = board
        self.camera_vision_angle = camera_angle
        self.camera_vision_range = camera_range

    def generate_initial_state(self):
        return camera_placing.state.State(self)

    def energy(self, state):
        not_covered = 0
        for x in range(0, len(self.board)):
            for y in range(0, len(self.board[x])):
                if self.board[x][y] is True:
                    continue
                if len(state.cameras) == 0:
                    not_covered += 1
                else:
                    covering = [cam for cam in state.cameras if cam.point_visible(x, y)]
                    if len(covering) == 0:
                        not_covered += 1

        return self.__goal_function(len(state.cameras), not_covered)

    def __goal_function(self, cameras, not_covered_points):
        print 'cams, not_covered:',cameras, not_covered_points
        return cameras + not_covered_points
