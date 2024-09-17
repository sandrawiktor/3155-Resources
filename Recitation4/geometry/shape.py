from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, shape):
        self.shape = shape

    @abstractmethod
    def find_area(self):
        """Method to compute the area of the shape."""
        pass

    @abstractmethod
    def find_perimeter(self):
        """Method to compute the perimeter of the shape."""
        pass

    @abstractmethod
    def description(self):
        """Method to provide a description of the shape."""
        pass

    def info(self):
        return f"The shape is a {self.shape}."
