class Student:
    def __init__(self, nameP, ageP):
        self.__name  = nameP
        self.__age = ageP

    def get_info(self):
        return self.__name, self.__age
    
    def set_name(self, namePS):
        self.__name = namePS
studentOne = Student("Fares", 22)

studentOne.set_name("Essam")
newName = studentOne.get_info,
#print(newName())
studentOne.__name

studentTwo = Student("Momen", 18)
get_info = studentTwo.get_info
print(get_info())

def function_(name, *args, **kwargs, ):
    return name, args, kwargs, list

new_var = function_("Fares", 1,2,3, age=23)
print(new_var)
