import random
from camera_placing import camera


class State:
    def __init__(self, problem):
        self.problem = problem
        self.xMax = len(self.problem.board)
        self.yMax = len(self.problem.board[0])
        self.cameras = []

    def get_neighbour(self):
        new_cameras = [cam.clone() for cam in self.cameras]
        self.mutate_cameras_positions(new_cameras)

        if len(new_cameras) > 0:
            choice = random.randint(0, 2)
        else:
            choice = 0
        if choice == 0:
            self.generate_additional_camera(new_cameras)
        elif choice == 1:
            self.mutate_cameras_positions(new_cameras)
        else:
            self.remove_camera(new_cameras)

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
        new_cam = camera.Camera(cam_x, cam_y, angle)
        cameras.append(new_cam)

    def remove_camera(self, cameras):
        if len(cameras) > 0:
            del cameras[-1]

    def mutated_camera(self, cam):
        old_x = cam.x
        old_y = cam.y
        x_diff = random.randint(-1, 1)
        y_diff = random.randint(-1, 1)
        while not self.point_in_boundaries(old_x + x_diff, old_y + y_diff):
            x_diff = random.randint(-1, 1)
            y_diff = random.randint(-1, 1)
        new_angle = (cam.anglePos + random.randint(-1, 1)) % 8
        cam.x = old_x + x_diff
        cam.y = old_y + y_diff
        cam.angle = new_angle

    def point_in_boundaries(self, x, y):
        if x > self.xMax or x < 0:
            return False
        if y > self.yMax or y < 0:
            return False
        if self.problem.board[x][y]:
            return False
        return True
