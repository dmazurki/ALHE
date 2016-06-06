from math import sin as sin
from math import cos as cos
from math import sqrt as sqrt
from camera_placing.geometrical_utils import GeometricalUtils

#class represents one camera with its state and has methods to check if some point is in its range of vision
class Camera:
    def __init__(self, x_pos, y_pos, angle, problem):
        self.x = x_pos
        self.y = y_pos
        self.angle = angle
        self.problem = problem

    #checks if point is in range and angle of vision
    def point_visible(self, x, y):
        if not self.point_in_range(x, y):
            return False
        points_to_check = GeometricalUtils.get_points_between(self.x, self.y, x, y)
        for i in range(0, len(points_to_check)):
            if self.problem.board[points_to_check[i].x][points_to_check[i].y]:
                return False
        return True

    def point_in_range(self, x, y):
        x1 = self.x
        y1 = self.y
        distance = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        #checks if point is in range of vision
        if distance > self.problem.camera_vision_range:
            return False
        half_of_angle = self.radius_to_radian(self.problem.camera_vision_angle / 2.0)
        angle_base = self.radius_to_radian((self.angle/8.0) * 360)
        #calculates angle arms endpoints
        x2 = x1 + self.problem.camera_vision_range * cos(half_of_angle + angle_base)
        y2 = y1 + self.problem.camera_vision_range * sin(half_of_angle + angle_base)
        x3 = x1 + self.problem.camera_vision_range * cos(angle_base - half_of_angle)
        y3 = y1 + self.problem.camera_vision_range * sin(angle_base - half_of_angle)
        #checks if point is between arms
        if self.problem.camera_vision_angle <= 180:
            if self.to_the_right_of_line(x1, y1, x2, y2, x, y) and self.to_the_left_of_line(x1, y1, x3, y3, x, y):
                return True
            return False
        else:
            if self.to_the_right_of_line(x1, y1, x2, y2, x, y) or self.to_the_left_of_line(x1, y1, x3, y3, x, y):
                return True
            return False

    def clone(self):
        return Camera(self.x, self.y, self.angle, self.problem)

    #checks if point is to the left of given line
    @staticmethod
    def to_the_left_of_line(x1, y1, x2, y2, pX, pY):
        v1 = (x2 - x1, y2 - y1)
        v2 = (x2 - pX, y2 - pY)
        xp = v1[0] * v2[1] - v1[1] * v2[0]
        if xp <= 0:
            return True
        else:
            return False

    #checks if point is to the right of given line
    @staticmethod
    def to_the_right_of_line(x1, y1, x2, y2, pX, pY):
        v1 = (x2 - x1, y2 - y1)
        v2 = (x2 - pX, y2 - pY)
        xp = v1[0] * v2[1] - v1[1] * v2[0]
        if xp >= 0:
            return True
        else:
            return False

    #transforms angle measure in degrees to radians
    @staticmethod
    def radius_to_radian(angle):
        return (angle / 360.0) * 2 * 3.14

    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ', ' + str(self.angle) + ')'
