class Student:
    def __init__(self, name, ID):
        self.ID = ID  
        self.name = name

    def get_ID(self):  
        return self.ID

    def get_name(self):  
        return self.name
       
    def set_info(self, name, ID):  
        self.ID = ID
        self.name = name



std1 = Student("mohamed", 509)
std_ID = std1.get_ID()
std_name = std1.get_name()
print(std_ID, std_name)   
std1.set_info("amir", 777)
print(std1.get_ID(), std1.get_name())  