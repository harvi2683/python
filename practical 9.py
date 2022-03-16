#20CE136_harvi sheth
'''Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members
 such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing
 the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program
to model this relationship.'''

class student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def studen_info(self):
        print('Name is',self.name)
        print('Id is',self.id)


class Exam(student):
    def __init__(self,name,id,m1,m2,m3,m4,m5,m6):
        student.__init__(self, name, id)
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
        self.m5=m5
        self.m6=m6

    def marks_info(self):
        print('m1 =',self.m1)
        print('m2 =', self.m2)
        print('m3 =', self.m3)
        print('m4 =', self.m4)
        print('m5 =', self.m5)
        print('m6 =', self.m6)


class result(Exam):
    def __init__(self, name, id, m1, m2, m3, m4, m5, m6):
        Exam.__init__(self, name, id, m1, m2, m3, m4, m5, m6)
        self.total_marks=m1+m2+m3+m4+m5+m6

    def final_result(self):
        return self.total_marks
print('How many record of student you want to print :')
n=int(input())
for i in range(1,n):
    print('Enter Name of the student :')
    Name=str(input())
    print('Enter id of the student :')
    Id=str(input())
    print('enter m1')
    m1=int(input())
    print('enter m2')
    m2=int(input())
    print('enter m3')
    m3=int(input())
    print('enter m4')
    m4=int(input())
    print('enter m5')
    m5=int(input())
    print('enter m6')
    m6=int(input())
    result=result(Name,Id,m1,m2,m3,m4,m5,m6)
    result.studen_info()
    result.marks_info()
    print('total marks is :',result.final_result())
