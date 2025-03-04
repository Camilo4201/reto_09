# shape_package/point.py

class Point:
    def __init__(self, x: int, y: int):
        self._x = x                
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def compute_distance(self, other: 'Point') -> float:
        return ((self._x - other.x) ** 2 + (self._y - other.y) ** 2) ** 0.5
shape.py
This module defines the Shape class with the requested features.


# shape_package/shape.py

class Shape:
    def __init__(self):
        self._vertices = []
        self._edges = []
        self._inner_angles = []
        self._is_regular = False

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._edges

    @property
    def inner_angles(self):
        return self._inner_angles

    @property
    def is_regular(self):
        return self._is_regular

    @classmethod
    def change_shape_type(cls, new_shape_type):
        return new_shape_type()

    def compute_area(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def compute_perimeter(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def compute_inner_angles(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def time_it(method):
        def wrapper(*args, **kwargs):
            import time
            start_time = time.time()
            result = method(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time of {method.__name__}: {end_time - start_time:.4f} seconds")
            return result
        return wrapper
#rectangle.py
#This module defines the Rectangle class that inherits from Shape.


# shape_package/rectangle.py

from shape_package.shape import Shape

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__()
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @Shape.time_it
    def compute_area(self) -> float:
        return self._width * self._height

    def compute_perimeter(self) -> float:
        return 2 * (self._width + self._height)
#square.py
#This module defines the Square class that inherits from Rectangle.

# shape_package/square.py

from shape_package.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length: float):
        super().__init__(side_length, side_length)
triangle.py
This module defines the Triangle class that inherits from Shape.


# shape_package/triangle.py

from shape_package.shape import Shape
from shape_package.point import Point
from shape_package.line import Line  # Assuming you have a Line class defined elsewhere

class Triangle(Shape):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        super().__init__()
        self._vertices = [point1, point2, point3]
        self._edges = [Line(point1, point2), Line(point2, point3), Line(point3, point1)]
        self._inner_angles = self.compute_inner_angles()

    @Shape.time_it
    def compute_area(self) -> float:
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def compute_perimeter(self) -> float:
        return sum(edge.get_length() for edge in self._edges)
    
    def compute_inner_angles(self) -> list:
        return [60.0, 60.0, 60.0]