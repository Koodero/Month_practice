# Class to store the user's points
class Scores:
    def __init__(self) -> None:
        self.points = 0
        self.attempts = 0

    # Method to easily add points and attempts
    def add_points(self, points: int, attempts: int):
        self.points += points
        self.attempts += attempts
