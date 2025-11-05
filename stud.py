class Student:
    def __init__(self,rollno,name,course):
        self.rollno=rollno
        self.name=name
        self.course=course
    def displayStudent(self):
        print("rollno",self.rollno)
        print("name",self.name)
        print("course",self.course)
stud1=Student(10,"Anu","MCA")
stud2=Student(12,"ANNA","MBA")
stud1.displayStudent()
stud2.displayStudent()
