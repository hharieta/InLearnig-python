# super() alone returns a temporary object of the superclass 
# that then allows you to call that superclass’s methods.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self) -> int | float:
        return self.length * self.width

    def perimeter(self) -> int | float:
        return 2 * self.length + 2 * self.width
    

# Here we declare that the Square class inherits
# from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# class Cube that inherits from Square and extends 
# the functionality of .area() (inherited from the Rectangle
# class through Square)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.length    


square = Square(5)
cube = Cube(3)
print(square.area())
print(f"cube perimeter: {cube.surface_area()}\ncube volume: {cube.volume()}")
