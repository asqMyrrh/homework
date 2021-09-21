class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name = new_name
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        self.__age = new_age

st=Person("ya",18)
print(st.get_name())
print(st.get_age())