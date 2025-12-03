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
