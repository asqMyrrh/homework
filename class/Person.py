class Person():
    def __init__(self,name):
        self.name=name
    def exclaim(self):
        print("Я человек вообще-то и звать меня ",self.name)
class Student(Person):
    def exclaim(self):
        print("Ну а я студент емае, звали меня ",self.name," спать хочу кааааааааааапец")
p = Person("pussydestroer3000")
s = Student("Ваня")
p.exclaim()
s.exclaim()
isinstance(s, Student)
issubclass(Student, Person)
print()
