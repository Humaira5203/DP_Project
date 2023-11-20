#decorator pattern
class NOSDecorator:
    def __init__(self, car):
        self._car = car

    def start(self):
        self._car.start()

    def accelerate(self):
        self._car.accelerate()

    def stop(self):
        self._car.stop()

    def apply_nos(self):
        pass
