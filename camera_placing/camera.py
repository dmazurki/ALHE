from math import sin as sin
from math import cos as cos
from math import sqrt as sqrt


class Camera:
    visionRange = 10
    visionAngle = 60

    def __init__(self, xPos, yPos, anglePos):
        self.xPos = xPos
        self.yPos = yPos
        self.anglePos = anglePos

    def is_point_visible(self, x, y):
        x1 = self.xPos
        y1 = self.yPos
        distance = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
        if distance > self.visionRange:
            return False
        halfOfAngle = self.radius_to_radian(self.visionAngle / 2)
        angleBase = self.radius_to_radian((self.anglePos / 8) * 360)
        x2 = x1 + self.visionRange * cos(halfOfAngle + angleBase)
        y2 = y1 + self.visionRange * sin(halfOfAngle + angleBase)
        x3 = x1 + self.visionRange * cos(angleBase - halfOfAngle)
        y3 = y1 + self.visionRange * sin(angleBase - halfOfAngle)
        if self.to_the_right_of_line(x1, y1, x2, y2, x, y) and self.to_the_left_of_line(x1, y1, x3, y3, x, y):
            return True
        return False

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
