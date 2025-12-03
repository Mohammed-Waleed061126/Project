class Car:
    def __init__(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed
    
    def set_speed(self,speed):
        self.speed = speed

c1 = Car(40)
c1_speed = c1.get_speed()
print(c1_speed)
c1.set_speed(70)
print(c1.get_speed())

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f"Hello, my name is {self.name}, and I'm {self.age} years old.")

p1 = Person("Waleed", 19)
p1.speak()