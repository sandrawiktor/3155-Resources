from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, shape):
        self.shape = shape
        pass

    def find_area(self):
        pass

    def find_perimeter(self):
        pass

    def description(self):
        pass

    def info(self):
        return f"The shape is a {self.shape}."

