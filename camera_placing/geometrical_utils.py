from camera_placing.point import Point

class GeometricalUtils:

    def __init__(self):
        pass

    #returns list of points match line between given pair of points
    @staticmethod
    def get_points_between(x_a, y_a, x_b, y_b):
        if x_a > x_b:
            a = Point(x_b, y_b)
            b = Point(x_a, y_a)
        else:
            a = Point(x_a, y_a)
            b = Point(x_b, y_b)
        if a.x == b.x and a.y == b.y:
            return [Point(a.x, b.y)]
        if a.x == b.x:
            result = []
            start = min(a.y, b.y)
            end = max(a.y, b.y) + 1
            for i in range(start, end):
                result.append(Point(a.x, i))
            return result
        if a.y == b.y:
            result = []
            start = min(a.x, b.x)
            end = max(a.x, b.x) + 1
            for i in range(start, end):
                result.append(Point(i, a.y))
            return result
        return GeometricalUtils.bresenham_points(a.x, a.y, b.x, b.y)

    #returns list of points they lay
    @staticmethod
    def bresenham_points(x1, y1, x2, y2):
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        slope = dy/float(dx)
        result = []

        x, y = x1, y1

        if slope > 1:
            dx, dy = dy, dx
            x, y = y, x
            x2, y2 = y2, x2

        p = 2 * dy - dx

        for k in range(1, dx):
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
            x = x + 1 if x < x2 else x - 1
            if slope <= 1:
                result.append(Point(x, y))
            else:
                result.append(Point(y, x))
        return result
