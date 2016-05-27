from math import sin as sin
from math import cos as cos
from math import sqrt as sqrt


class Camera:

    def __init__(self, x_pos, y_pos, angle, problem):
        self.x = x_pos
        self.y = y_pos
        self.angle = angle
        self.problem = problem

    def is_point_visible(self, x, y):
        x1 = self.x
        y1 = self.y
        distance = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if distance > self.problem.camera_vision_range:
            return False
        half_of_angle = self.radius_to_radian(self.problem.camera_vision_angle / 2)
        angle_base = self.radius_to_radian((self.angle / 8) * 360)
        x2 = x1 + self.problem.camera_vision_range * cos(half_of_angle + angle_base)
        y2 = y1 + self.problem.camera_vision_range * sin(half_of_angle + angle_base)
        x3 = x1 + self.problem.camera_vision_range * cos(angle_base - half_of_angle)
        y3 = y1 + self.problem.camera_vision_range * sin(angle_base - half_of_angle)
        if self.to_the_right_of_line(x1, y1, x2, y2, x, y) and self.to_the_left_of_line(x1, y1, x3, y3, x, y):
            return True
        return False

    def clone(self):
        return Camera(self.x, self.y, self.angle, self.problem)

    @staticmethod
    def to_the_left_of_line(x1, y1, x2, y2, pX, pY):
        v1 = (x2 - x1, y2 - y1)
        v2 = (x2 - pX, y2 - pY)
        xp = v1[0] * v2[1] - v1[1] * v2[0]
        if xp <= 0:
            return True
        else:
            return False

    @staticmethod
    def to_the_right_of_line(x1, y1, x2, y2, pX, pY):
        v1 = (x2 - x1, y2 - y1)
        v2 = (x2 - pX, y2 - pY)
        xp = v1[0] * v2[1] - v1[1] * v2[0]
        if xp >= 0:
            return True
        else:
            return False

    @staticmethod
    def radius_to_radian(angle):
        return (angle / 360) * 2 * 3.14
