import random
from camera_placing import camera


class State:
    def __init__(self, problem):
        self.board = problem.board
        self.xMax = len(self.board)
        self.yMax = len(self.board[0])
        self.cameras = []

    def get_neighbour(self):
        if len(self.cameras) > 0:
            choice = random.randint(0, 2)
        else:
            choice = 0
        if choice == 0:
            self.generate_additional_camera()
        elif choice == 1:
            self.permutate_cameras_positions()
        else:
            self.remove_camera()

    def permutate_cameras_positions(self):
        if len(self.cameras) == 0:
            return
        for cam in self.cameras:
            self.permutate_positions_of_one_camera(cam)

    def generate_additional_camera(self):
        camX = random.randint(0, self.xMax)
        camY = random.randint(0, self.yMax)
        angle = random.randint(0, 7)
        while self.board[camX][camY]:
            camX = random.randint(0, self.xMax)
            camY = random.randint(0, self.yMax)
        newCam = camera.Camera(camX, camY, angle)
        self.cameras.append(newCam)

    def remove_camera(self):
        if len(self.cameras) > 0:
            del self.cameras[-1]

    def permutate_positions_of_one_camera(self, camera):
        oldX = camera.xPos
        oldY = camera.yPos
        xDiff = random.randint(-1, 1)
        yDiff = random.randint(-1, 1)
        while not self.isValidPoint(oldX + xDiff, oldY + yDiff):
            xDiff = random.randint(-1, 1)
            yDiff = random.randint(-1, 1)
        newAngle = (camera.anglePos + random.randint(-1, 1)) % 8
        camera.xPos = oldX + xDiff
        camera.yPos = oldY + yDiff
        camera.anglePos = newAngle

    def isValidPoint(self, x, y):
        if x > self.xMax or x < 0:
            return False
        if y > self.yMax or y < 0:
            return False
        if self.board[x][y]:
            return False
        return True
