class Teacher(Person):
    work = 0
    def give_kn(self,*pupils):
        for pupil in pupils:
            pupil.get_kn()
            self.work+=1
    def give_homework(self, * pupils, n):
        for pupil in pupils:
            pupil.get_homework()
            work +=1
class Student(Person):
    t = Teacher("Владимир")
p = [Student("уважаемый")
    for i in range(n)]

t.give_kn(p)
print(p.kn)