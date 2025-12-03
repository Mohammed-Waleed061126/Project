class Car():
    def __init__(self,speed):
        self.__speed=speed
    def get__info(self):
        return self.__speed
    def se__info(self):
        return self.__speed
car1=Car("120")
mm=car1.get__info
print(mm())

class person():
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def speak(self):
        return f"my name is {self.__name} and my age is {self.__age}"
    
person_1 = person('Momen', 18)
print(person_1.speak())