import pandas as pd

student = {
   # "student 1":{"phy":30,"maths":40,"english":50,"hindi":60},
   # "student 2":{"phy":40,"maths":30,"english":45,"hindi":60},
}
while True:
    print("For the specific task enter the following number : ")
    print("1.add ")
    print("2.delete all the data")
    print("3.deleting data from specific student")
    print("4.updating")
    print("5.view all")
    print("6.Quit")
    tasknum = int(input("Enter the number :"))

    if tasknum == 1:
        name = input("Enter the name of the student :")
        marksphy = int(input("enter the marks of physics :"))
        marksm = int(input("enter the marks of maths :"))
        marksen = int(input("enter the marks of english :"))
        markshi = int(input("enter the marks of hindi :"))

        student.update({name: {"phy": marksphy,
                               "maths": marksm,
                               "english": marksen,
                               "hindi": markshi}})
        print("Student added successfully!")

    elif tasknum == 2:
        student.clear()
        print(student)

    elif tasknum == 3:
        name = input("enter the student name who's data you want to delete :")
        if name in student:
            student.pop(name)
            print("student removed successfully")
        else:
            print("Student not found")

    elif tasknum == 4:
        print("1.updating name")
        print("2.updating marks")
        key = int(input("Enter the number:"))
        if key == 1:
            oldname = input("Enter the name :")
            if oldname in student.keys():
                newname = input("Enter the changed name :")
                val = student.pop(oldname)
                student[newname] = val
                print("student name changed successfully")
            else:
                print("student not found")

        elif key == 2:
            name = input("Enter the name :")
            if name in student.keys():
                sub = input("Enter the subject :")
                if sub in student[name]:
                    marksupdate = input("Enter the marks :")
                    student[name].update({sub: marksupdate})
                else:
                    print("Wrong subject")
            else:
                print("wrong name entered")

    elif tasknum == 5:
        stu = pd.DataFrame.from_dict(student)
        print(stu)

    elif tasknum == 6:
        print("Exiting...")
        break
    else:
        print("Wrong key entered")
