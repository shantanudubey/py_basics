# OOPS

class Employee:

    count = 0   # clas variable : same as static

    # Constructor : default values are needed if e1 = Employee() has to work
    def __init__(self, name='', age=0, salary=0.0) -> None:
        self.__name = name
        self.__age = age
        self.__salary = salary
        Employee.count += 1
        print("Employee : initalized:", self.__name)

    
    # Data Access : set
    def set_data(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        print("Employee : data is set:", name)

    # Data Access : get
    def get_data(self):
        return (self.__name, self.__age, self.__salary)

    # # Data Display
    def display_data(self):
        print("Employee :", self.__name, self.__age, self.__salary)

    def display_count():
        print("Employee : count:", Employee.count)


    # Destructor
    def __del__(self):
        print("Employee : deleted:", self.__name)

print('-'*79)

e1 = Employee()
e1.set_data("Suresh", 25, 30000)
e1.display_data()

e2 = Employee("Ramesh", 23, 20000)
e2.display_data()

# Do this explcitly as good practice to mark objects for deletion
e1 = None
e2 = None
print('-'*79)


# Built-ins : 
#   - vars(<scope>) : returns a dictionary of attributes and values
#        of the specified scope, default is local : result is same as locals()
#   - dir(<scope>) : returns a list of attributes of the specified scope,
#        default is local
print("vars()       :", vars())
print("dir()        :", dir())
print('-'*79)

print("class vars() :", vars(Employee))
print("class dir()  :", dir(Employee))
print('-'*79)

# In itialize the object again as the previous one would've been deleted
e1 = Employee("Yash", 32, 61593)
print("obj vars()   :", vars(e1))
print("obj dir()    :", dir(e1))
e1.display_data()
# e1.display_count() will fail because 
#   the instance get implicitely passed to a class method
Employee.display_count()
print('-'*79)




print('-'*79)