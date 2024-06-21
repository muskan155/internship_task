from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# Concrete subclass Circle
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Concrete subclass Rectangle
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Create instances of concrete classes
circle = Circle("Circle", 5)
rectangle = Rectangle("Rectangle", 3, 4)

# Print details of each shape
print(f"{circle.name}:")
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

print(f"\n{rectangle.name}:")
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())