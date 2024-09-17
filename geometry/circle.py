from geometry.shape import Shape
import math

class Circle(Shape):

    def __init__(self, shape, radius):
        super().__init__(shape)
        self.radius = radius

    def find_area(self):
        area = math.pi * self.radius ** 2
        return f"Area of the circle: {area:.2f} square inches"

    def find_perimeter(self):
        circumference = 2 * math.pi * self.radius
        return f"Circumference of the circle: {circumference:.2f} inches"

    def description(self):
        return f"A circle is a round shape with all points equidistant from the center."
