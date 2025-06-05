import logging
import pandas as pd

logging.basicConfig(level=logging.DEBUG, filename=r"day5\trial.log",
                    filemode="w",
                    format="%(asctime)s: %(levelname)s: %(message)s")

student = {}
logging.info("The Starting of system")

while True:
    print("For the specific task enter the following number : ")
    print("1.add ")
    print("2.delete all the data")
    print("3.deleting data from specific student")
    print("4.updating")
    print("5.view all")
    print("6.Quit")
    tasknum = int(input("Enter the number :"))
    logging.info(f"User entered key {tasknum}")

    if tasknum == 1:
        logging.info("User is adding the student")
        name = input("Enter the name of the student :")
        logging.debug(f"User added name :{name}")
        marksphy = int(input("enter the marks of physics :"))
        marksm = int(input("enter the marks of maths :"))
        marksen = int(input("enter the marks of english :"))
        markshi = int(input("enter the marks of hindi :"))
        logging.info(f"{name}'s marks are phy: {marksphy}, Maths: {marksm},"
                     f"English: {marksen}, Hindi: {markshi}")

        student.update({name: {"phy": marksphy,
                               "maths": marksm,
                               "english": marksen,
                               "hindi": markshi}})
        print("Student added successfully!")
        logging.info("Student added successfully")

    elif tasknum == 2:
        logging.critical("User deleted whole record")
        student.clear()
        print(student)

    elif tasknum == 3:
        logging.warning("User is removing a particular student")
        name = input("enter the student name who's data you want to delete :")
        if name in student:
            student.pop(name)
            logging.info(f"Student named {name} is removed")
            print("student removed successfully")
        else:
            logging.error("Student not found")
            print("Student not found")

    elif tasknum == 4:
        print("1.updating name")
        print("2.updating marks")
        key = int(input("Enter the number:"))
        if key == 1:
            logging.info("User is updating name")
            oldname = input("Enter the name :")
            if oldname in student.keys():
                newname = input("Enter the changed name :")
                val = student.pop(oldname)
                student[newname] = val
                logging.warnig(f"User update {oldname} to {newname}")
                print("student name changed successfully")
            else:
                logging.error("Student not found")
                print("student not found")

        elif key == 2:
            logging.warning("User wants to change the marks")
            name = input("Enter the name :")
            if name in student.keys():
                sub = input("Enter the subject :")
                logging.warning(f"user is changing {name}'s marks of {sub}")
                if sub in student[name]:
                    marksupdate = input("Enter the marks :")
                    logging.info(f"{name}'s {sub} marks changed {marksupdate}")
                    student[name].update({sub: marksupdate})
                else:
                    logging.error("Wrong subject name enterd")
                    print("Wrong subject")
            else:
                logging.error("Name entered is not found")
                print("wrong name entered")

    elif tasknum == 5:
        stu = pd.DataFrame.from_dict(student)
        logging.info("User is viewing all the entries")
        print(stu)

    elif tasknum == 6:
        logging.warning("Exiting")
        print("Exiting...")
        break
    else:
        logging.error("Wrong key entered")
        print("Wrong key entered")
