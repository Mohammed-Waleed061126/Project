class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name = name
    
    def get_age(self):
        return self.age
    
    def set_age(self,age):
        self.age = age
    

p1 = Person("Mohammed",20)
p1_name = p1.get_name()
p1_age = p1.get_age()
print(p1_name, p1_age)
p1.set_name("Waleed")
p1.set_age(30)
print(p1.get_name(), p1.get_age())

