class Employee:
    emp_name = input("enter your name : ")
    emp_id = int(input("enter your id : "))
    dept = input("enter your department : ")
    basic_pay = int(input("enter your basic pay : "))
    print("***************************DETAILS OF EMPLOYEE************************************")

    def total_salary(self):
        self.HRA = Employee.basic_pay * 20/100
        self.DA = Employee.basic_pay * 120/100
        self.MA = Employee.basic_pay * 5/100
        total_sal = self.HRA + self.DA +self.MA
        print("Total salary of employee : ",total_sal)
        

        
    def emp_details(self):
        print("Employee Name :" , Employee.emp_name)
        print("Employee ID :",Employee.emp_id)
        print("Employee Depatrment : ",Employee.dept)
        
obj1 = Employee()
obj1.emp_details()
obj1.total_salary()

