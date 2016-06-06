#class represents quality function - problem objective function
class LinearQuality:
    def __init__(self, cameras_number_weight, uncovered_points_weight):
        self.cameras_number_weight = cameras_number_weight
        self.uncovered_points_weight = uncovered_points_weight

    def __call__(self, cameras, uncovered_points):
        return self.uncovered_points_weight * uncovered_points + self.cameras_number_weight * cameras
