from geometry.shape import Shape

class Rectangle(Shape):

    def __init__(self, shape, length, width):
        super().__init__(shape)
        self.length = length
        self.width = width

    def find_area(self):
        return f"Area of the rectangle: {self.length * self.width} square inches"

    def find_perimeter(self):
        return f"Perimeter of the rectangle: {2 * (self.length + self.width)} inches"

    def description(self):
        return f"A rectangle has 4 right angles and opposite sides of equal length."
