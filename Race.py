# Pattern: Template Pattern
class Race:
    def race(self, car, track, racing_strategy):
        print("Race Start:")
        car.run()
        print(f"Car: {car.car_info()}")
        print(f"Track: {track}")
        print(f"Racing Strategy: {racing_strategy.race_strategy()}")
        print("Finish Line:")
        print(f"Lap Time: {self.lap_time()}")

    @staticmethod
    def lap_time():
        hours = (0, 23)
        minutes = (0, 59)
        seconds = (0, 59)
        lap_time = (f"{hours:02d}:{minutes:02d}:{seconds:02d}", "%H:%M:%S")
        return lap_time.strftime("%H:%M:%S")
