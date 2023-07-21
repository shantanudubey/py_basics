# Inheritance

# Multiple Inheritance : Deadly Diamond
#   To prevent this python linearises the search order so that
#   left to right creation order is honored.
class Base:
    def display(self):
        print("Base : display")

class Derived1(Base):
    def display(self):
        print("Derived1 : display")

class Derived2(Base):
    def display(self):
        print("Derived2 : display")

# This creation order will result in
#   Der getting a copy of the members from path Base -> Derived1 
class Der(Derived1, Derived2):
    def display(self):
        super().display()
        Derived1.display(self)
        Derived2.display(self)
        print("Der  :", Der.__mro__)
print('-'*79)

d = Der()
d.display()
print('-'*79)

print("isinstance   :", isinstance(d, Der), isinstance(d, Base), isinstance(d, object))
print("issubclass   :", issubclass(Der, Derived1), issubclass(Derived1, Base)
      , issubclass(Derived2, Base), issubclass(Base, Der), issubclass(Der, Base)
      , issubclass(Base, object))
print('-'*79)


print('-'*79)