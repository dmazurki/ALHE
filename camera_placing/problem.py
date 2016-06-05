import camera_placing.state


class Problem:
    def __init__(self, board, camera_angle, camera_range, max_cameras, quality_function):
        self.board = board
        self.camera_vision_angle = camera_angle
        self.camera_vision_range = camera_range
        self.max_cameras = max_cameras
        self.quality_function = quality_function

    def generate_initial_state(self):
        return camera_placing.state.State(self)

    def get_cameras_number(self, state):
        return len(state.cameras)

    def get_not_covered_points(self, state):
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
        return not_covered

    def energy(self, state):
        return self.quality_function(self.get_cameras_number(state), self.get_not_covered_points(state))


