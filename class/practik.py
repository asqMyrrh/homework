class Person():
    def __init__(self,name):
        self.name = name
class Student(Person):
    homework = 0
    kn = 0
    def get_kn(self):
        self.kn +=1
    def get_homework(self, n):
        self.homework += n
    def do_homework(self):
        if self.homework > 0:
            self.homework-=1
        else:
            print("Ну вот и все")
