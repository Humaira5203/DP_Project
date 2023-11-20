#factory pattern
class TrackFactory:
    @staticmethod
    def create_track(track_type):
        if track_type == "USA":
            return "Blue Moon Bay Speedway (USA)"
        elif track_type == "Japan":
            return "BB Raceway (Japan)"
        elif track_type == "Germany":
            return "Circuit de Spa-Francorchamps (Germany)"
        else:
            return "Unknown Track"