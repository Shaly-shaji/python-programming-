class Employee:
    def __init__(self,empid,empname,dept,salary):
        self.empid=empid
        self.empname=empname
        self.dept=dept
        self.salary=salary
    def displayEmployee(self):
        print("emp_id",self.empid)
        print("emp_name",self.empname)
        print("dept",self.dept)
        print("salary",self.salary)
emp1=Employee(10,"sam","HR",20000)
emp2=Employee(12,"anu","SE",30000)
emp1.displayEmployee()
emp2.displayEmployee()
