from geometry.shape import Shape

class Square(Shape):

    def __init__(self, shape, side):
        super().__init__(shape)
        self.side = side

    def find_area(self):
        return f"Area of {self.side}in square: {self.side*self.side}in"

    def find_perimeter(self):
        return f"Perimeter of a {self.side}in square: {self.side*4}"

    def description(self):
        return f"A square has 4 sides."