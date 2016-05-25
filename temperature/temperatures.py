class LinearTemperature:
    def __init__(self, begin_temperature, step):
        self.begin_temperature = begin_temperature
        self.step = step

    def __call__(self, iteration):
        return self.begin_temperature - iteration * self.step
