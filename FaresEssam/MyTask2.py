class Car:
  def __init__(self, speed):
    self.__speed = speed
  
  def get_speed(self):
    return self.__speed
  def set_speed(self, speed):
    self.__speed = speed

car_1 = Car(123)
print(car_1.get_speed())
car_1.set_speed(164)
print(car_1.get_speed())

class Person:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age

  def speak(self):
    return f"My name is: {self.__name} and my age is: {self.__age}"
  

person_1 = Person("Fares", 22)
speak = person_1.speak
print(speak())