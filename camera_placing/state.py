import random
from camera_placing import camera


class State:
    def __init__(self, problem, cameras=None):
        self.problem = problem
        self.xMax = len(self.problem.board) - 1
        self.yMax = len(self.problem.board[0]) - 1
        if not cameras:
            self.cameras = []
        else:
            self.cameras = cameras

    #creates new elemenst according to some specific conditions
    def get_neighbour(self):
        new_cameras = [cam.clone() for cam in self.cameras]

        if len(new_cameras) == self.problem.max_cameras:
            choice = random.randint(1, 2)
        elif len(new_cameras) > 0:
            choice = random.randint(0, 2)
        else:
            choice = 0
        if choice == 0:
            self.generate_additional_camera(new_cameras)
        elif choice == 1:
            self.mutate_cameras_positions(new_cameras)
        else:
            self.remove_camera(new_cameras)

        return State(self.problem, new_cameras)

    def mutate_cameras_positions(self, cameras):
        if len(cameras) == 0:
            return
        for cam in cameras:
            self.mutated_camera(cam)

    def generate_additional_camera(self, cameras):
        cam_x = random.randint(0, self.xMax)
        cam_y = random.randint(0, self.yMax)
        angle = random.randint(0, 7)
        while self.problem.board[cam_x][cam_y]:
            cam_x = random.randint(0, self.xMax)
            cam_y = random.randint(0, self.yMax)
        new_cam = camera.Camera(cam_x, cam_y, angle, self.problem)
        cameras.append(new_cam)

    def remove_camera(self, cameras):
        if len(cameras) > 0:
            del cameras[random.randint(0, len(cameras)-1)]

    #mutates given camera into new example
    def mutated_camera(self, cam):
        old_x = cam.x
        old_y = cam.y
        x_diff = random.randint(-1, 1)
        y_diff = random.randint(-1, 1)
        while not self.point_in_boundaries(old_x + x_diff, old_y + y_diff):
            x_diff = random.randint(-1, 1)
            y_diff = random.randint(-1, 1)
        new_angle = (cam.angle + random.randint(-1, 1)) % 8
        cam.x = old_x + x_diff
        cam.y = old_y + y_diff
        cam.angle = new_angle

    #chekcs if coordinates of given point are inside board
    def point_in_boundaries(self, x, y):
        if x > self.xMax or x < 0:
            return False
        if y > self.yMax or y < 0:
            return False
        if self.problem.board[x][y]:
            return False
        return True

    def __str__(self):
        return str(self.cameras)
