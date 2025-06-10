import csv
import json
import logging
import os


def csv_parsing():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler('csv_logging.log')
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("user selected csv parsing mode")
    print("Select the mode: ")
    print("r. For read mode")
    print("w. For write mode")
    print("d. delete the file")
    mode = input("Enter the mode you want to access in :")
    mode = mode.casefold()
    logger.info(f"User selected {mode} to access the file in.")
    try:
        file_path = input("Enter the path of the file :")
        if mode == "r" or mode == "w":
            with open(file_path, mode) as f:

                if mode == "r":
                    logger.info(f"User selected {file_path} to access "
                                "it in reading mode")
                    data = csv.reader(f)
                    for row in data:
                        print(row)
                elif mode == 'w':
                    logger.info(f"User selected {file_path} to "
                                "access it in writing mode")
                    data = csv.writer(f)
                    print("Please a key")
                    print("1.Adding single row")
                    print("2.Adding multiple rows")
                    key = int(input("Enter the key:"))
                    if key == 1:
                        logger.info("User is inserting single row")
                        row = input("Enter the data you want to insert:")
                        logger.info(f"The data user inserted is {row}")
                        data.writerow([f"{row}"])
                    elif key == 2:
                        logger.info("User is inserting multiple rows")
                        rows = input("Enter the rows you want to insert:")
                        logger.info(f"The data user inserted is {rows}")
                        data.writerows([f"{rows}"])
                    else:
                        logger.warning("Wrong key entered")
                        print("Wrong key entered")
        elif mode == 'd':
            logger.warning("User is deleting the file")
            try:
                os.remove(file_path)
                print("file deleted")
            except FileNotFoundError:
                logger.error("File not found")
                print("No such file exists")
    except FileNotFoundError:
        logger.error("NO file found.Path entered is wrong")
        print("No such file present")


def txt_parsing():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler('txt_logging.log')
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("user selected txt parsing mode")
    print("Select the mode you want to open file in:")
    print("r.read file")
    print("w.write file")
    print("d.delete file")
    mode = input("Enter the key for the mode you want to access the file in:")
    mode.casefold()

    try:
        file_path = input("Enter the file path:")
        if mode == 'r':
            with open(file_path, mode) as file:
                logger.info(f"User wants to access file at"
                            f" {file_path} to read.")
                print("How do you want to read the file")
                print("1.read full file")
                print("2.read first 5 lines")
                mode = int(input("Enter the key:"))
                if mode == 1:
                    logger.info("User is reading full file")
                    data = file.read()
                    print(data)
                elif mode == 2:
                    logger.info("User is reading only first five lines")
                    data = file.readline(5)
                    print(data)
                else:
                    logger.error("Wrong key entered")
                    print("Wrong key entered")
        elif mode == 'w':
            with open(file_path, mode) as file:
                logger.warning(f"User is accessing the file in write mode")
                data = input("Enter the data you want to write in the file:")
                logger.info(f"User inserted this :{data}")
                file.writelines(f"{data}")

        elif mode == 'd':
            logger.warning("User is deleting the file")
            try:
                os.remove(file_path)
            except FileNotFoundError:
                logger.error("File not found")
                print("No file exists")
    except FileNotFoundError:
        logger.error("File not found")
        print("No such file present")


def json_parsing():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler('txt_logging.log')
    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("user selected json parsing mode")
    print("Select the key for the task you want to perform:")
    print("1.read file")
    print("2.Converting any data structure to json")
    key = int(input("Enter the key:"))
    if key == 1:
        logger.info("User wants to access the json file in reading mode")
        try:
            file_path = input("Enter the file path:")
            logger.info(f"User is accessing the file at {file_path}")
            with open(file_path, "r") as file:
                data = json.load(file)
                print(data)
        except FileNotFoundError as f:
            logger.error("No such file found")
            print("Error !!!! No Such File Found")

    elif key == 2:
        logger.warning("User is accessing the file in write mode")
        mydata = str(input("Enter the data:"))
        file_path = input("Enter the file path:")
        with open(file_path, "w") as file:
            data = json.dump(mydata, file)
            logger.info(f"User inserted this in the file:{data}")
            print(data)


print("Select the file you want to work on using key:")
print("1.txt")
print("2.csv")
print("3.json")
number = int(input("Enter the key:"))
if number == 1:
    txt_parsing()
elif number == 2:
    csv_parsing()
elif number == 3:
    json_parsing()
else:
    print("Incorrect key selected")
