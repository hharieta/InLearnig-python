class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self) -> int | float:
        return self.length * self.width
    

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class VolumeMixin:
    def volume(self) -> int | float:
        return self.area() * self.heigth


class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.heigth = length
    
    def face_area(self):
        return super().area()
    
    def surface_area(self):
        return super().area() * 6


cube = Cube(2)

print(cube.surface_area())
print(cube.volume())