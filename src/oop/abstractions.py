# Abstract Classes 

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("Rectangle: draw()")
        
class Circle(Shape):
    def draw(self):
        print("Circle   : draw()")

print('-'*79)        
c = Circle()
c.draw()

r = Rectangle()
r.draw()

print('-'*79)
