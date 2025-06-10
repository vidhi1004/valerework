class Employee:

    def __init__(self, eid, name, age, level, salary, phone):
        self.eid = eid
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        self.phone = phone

    def display(self):
        print("Employee's id :", self.eid)
        print("Employess's name :", self.name)
        print("Employee's age :", self.age)
        print("Employee's Level :", self.level)
        print("Employee's salary:", self.salary)
        print("Employee's phone number:", self.phone)


class Employee_management_system(Employee):

    def __init__(self):
        pass

    employee = []

    @staticmethod
    def add_employee():

        eid = int(input("Enter Employee id:"))
        name = input("Enter the employees name:")
        age = abs(int(input("Enter the employee's age:")))
        Level = input("Enter the employees level:")
        salary = abs(int(input("Enter the employee salary:")))
        phone = abs(int(input("enter your phone number:")))

        for emp in Employee_management_system.employee:
            if emp.eid is not Employee_management_system.employee:
                print("User already exists")
                return
        name = Employee(eid, name, age, Level, salary, phone)
        Employee_management_system.employee.append(name)
        print("user addded successfully ")

    def display_emp(self):
        if self.employee == []:
            print("No Employee preset")
        else:
            for emp in self.employee:
                emp.display()

    def search_employee(self, name):
        for emp in self.employee:
            if emp.name.lower() == name.lower():
                emp.display()
            else:
                print("Employee not found")

    def remove(self, name):
        for emp in self.employee:
            if emp.name.casefold() == name:
                self.employee.remove(emp)
                print(f"{name} is successfully removed")
            else:
                print(f"{name} not present")

    def remove_all(self):
        if self.employee == []:
            print("Nothing is present to remove!!!")
        else:
            self.employee.clear()

    def update(self):
        name = input("Enter the name in which you want to update :")
        for emp in self.employee:
            if emp.name.casefold() == name:
                eid = input("Enter the id:")
                age = input("Enter the age:")
                level = input("Enter the level:")
                salary = input("Enter the salary:")
                phone = input("Enter the phone_no:")
                newname = input("Enter the name:")

                if eid != '':
                    emp.id = eid
                if age != '':
                    emp.age = age
                if level != '':
                    emp.level = level
                if salary != '':
                    emp.salary = salary
                if phone != '':
                    emp.phone = phone
                if name != newname:
                    emp.name = newname

    def run(self):
        while True:
            key = int(input("Enter the number to select the operation you want to perform\n"
                            "1)ADD Employee\n"
                            "2)Search Employee\n"
                            "3)Delete Employee\n"
                            "4)Delete All Employee\n"
                            "5)Display Employee\n"
                            "6)Update\n"
                            "7)EXIT\n"))

            if key == 1:
                Employee_management_system.add_employee()
            elif key == 2:
                name = input("Enter the name of the employee")
                self.search_employee(name)
            elif key == 3:
                name = input(
                    "Enter the name of the employee you want to remove")
                self.remove(name)
            elif key == 4:
                self.remove_all()
            elif key == 5:
                self.display_emp()
            elif key == 6:
                self.update()
            elif key == 7:
                print("Exiting")
                break


if __name__ == '__main__':
    Employee_management_system().run()
