# Overriding functions in inherited classes :

# To prevent functions from being overridden, start with __<fname>
class Base:
    def __method(self):
        print("Base : __method()")

    def func(self):
        print("Base : func()")
        self.__method()


class Derived(Base):
    def __method(self):
        print("Derived : __method()")


print('-'*79)
b = Base()
b.func()
d = Derived()
d.func()
print("addr :", id(b.func()), id(d.func()), Derived.__mro__)

print("Base     :", dir(b))
print("Derived  :", dir(d))

print('-'*79)