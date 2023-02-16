class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)
    
    def area(self) -> int | float:
        return self.length * self.width

    def perimeter(self) -> int | float:
        return 2 * self.length + 2 * self.width


class Triangle:
    def __init__(self, base, heigth, **kwargs):
        self.base = base
        self.heigth = heigth
        super().__init__(**kwargs)
    
    def triangle_area(self) -> float:
        return 0.5 * self.base * self.heigth
    

# Here we declare that the Square class inherits
# from the Rectangle class
class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)


class Cube(Square):
    def surface_area(self) -> int | float:
        face_area = super().area()
        return face_area * 6
    
    def volume(self) -> int | float:
        face_area = super().area()
        return face_area * self.length

# a pyramid with a square base
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_heigth, **kwargs):
        self.base = base
        self.slant_heigth = slant_heigth
        kwargs["heigth"] = slant_heigth
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)
    
    def area(self) -> float:
        base_area = super().area()
        perimeter = super().perimeter()

        return 0.5 * perimeter *self.slant_heigth + base_area
    
    def area_2(self) -> int | float:
        base_area = super().area()
        triangle_area = super().triangle_area()
        return triangle_area * 4 + base_area


pyramid = RightPyramid(base=2, slant_heigth=4)
print(pyramid.area())
print(pyramid.area_2())

print(RightPyramid.__mro__)