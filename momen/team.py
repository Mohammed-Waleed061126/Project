class student():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_info(self):
       return self.__name,self.__age
    
    
    def set_name(self, name):
        self.__name = name


std2 = student("fares", 22)
mm = std2.get_info
print(mm())



def function_(name, *args, **kwargs):
    return [name, args, kwargs]
new_var = function_("momen", 1,2,3, age=18)
print(new_var)







