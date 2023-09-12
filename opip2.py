from datetime import date
from typing import Literal,Optional

class Person:
    def __init__(self,name,birth_date):
        self.name = name
        self.birth_date = birth_date 


    @property
    def age(self):
        diff = date.today() - self.birth_date
        return diff.days // 365
    
    def __len__(self):
        return self.age 

class Teacher(Person):
    def __init__(self,name,birth_date):
        super().__init__(name,birth_date)
        pass


class Student(Person):
    def __init__(self,name,birth_date):
        super().__init__(name,birth_date)
        self.marks = []
        self.group :Optional['Group'] = None

    def add_mark(self,*args):
        self.marks.extend(args)   

    def get_average_marks(self):
        return sum(self.marks) / len(self.marks)   

    def set_group(self,group):
        self.group = group 



class Group:
    def __init__(self,grade):
        self.students = []
        self.teachers = []
        self.grade = grade

    def add_students(self,*args):
        for student in args:
            self.check_student_age(student)
        self.students.extend(args)

    def add_teachers(self,*args):
        self.teachers.extend(args)

    def check_student_age(self,student):
        age_norm = self.grade + 5
        age_diff = abs(student.age - age_norm)
        if age_diff > 1:
            raise  self.WrongAgeException(f'{student.name} yasi {self.grade}.sinif ucun duz gelmir')

    class WrongAgeException(Exception):
        pass    

class School:
    def __init__(self):
        pass


husniyye = Student('Husniyye',date(1999,9,9))    
cavid = Student('Cavid',date(1998,8,9))    
ucal = Student('Ucal',date(1994,11,9))    
behram = Student('Behram',date(1989,9,9))    
fuad = Student('Fuad',date(1990,9,9))    
orxan = Student('Orxan',date(1980,9,9))    
cavad = Student('Cavad',date(1994,2,3))    

k111 = Group(10)
k211 = Group(8)
k211 = Group(7)


k211.add_students(behram,fuad,ucal)

