class Person:
    def __init__(self, name, age):
        self.age = age  
        self.name = name

    def get_age(self):  
        return self.age

    def get_name(self):  
        return self.name
       
    def set_info(self, name, age):  
        self.age = age
        self.name = name



std1 = Person("mohamed", 20)


std_age = std1.get_age()
std_name = std1.get_name()
print(std_age, std_name)


std1.set_info("amir", 30)
print(std1.get_age(), std1.get_name())
