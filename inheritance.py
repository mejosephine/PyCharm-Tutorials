class Student:
    def __init__(self,name,age,regno):
        self.name = name
        self.age = age
        self.regno = regno

    def play(self):
        return "I love playing football"

    def discuss(self):

        return "I discuss but not every day"

    def study(self):
        return "I always study on the daily basis"


class NetworkAdmin(Student):

    def __init__self(self):
        Student.__init__(self,"Josephine",43,"S21B13/042")

    def study(self):
        return f'I {self.name}like studying'




student_1 = Student("Josephine", "S21B13/042",45)
print(student_1.play())