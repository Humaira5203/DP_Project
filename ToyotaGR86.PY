
class ToyotaGR86:
    def __init__(self, engine_behavior, turbocharger_behavior):
        self._engine_behavior = engine_behavior
        self._turbocharger_behavior = turbocharger_behavior

    def start(self):
        print("Starting Toyota GR86")

    def accelerate(self):
        print("Accelerating Toyota GR86")

    def stop(self):
        print("Stopping Toyota GR86")

    def car_info(self):
        return f"Toyota GR86 with {self._engine_behavior.engine_info()} and {self._turbocharger_behavior.turbocharger_info()}"