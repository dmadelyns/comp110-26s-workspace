__author__ = "730674804"

class Point: 
    def __init__(self, x_init: "float", y_init: "float"):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        self.x = self.x * factor
        self.y = self.y * factor 

    def scale(self, factor: int) -> "Point":
        new_x = self.x * factor 
        new_y = self.y * factor 
        return Point(new_x, new_y)
