import time
import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
POINT_MAPPING = {

    "A": 4.0,

    "B": 3.0,

    "C": 2.0,

    "D": 1.0,
    "F": 0.0,
}


def main(id):
    students_data = {
        "first names": [],
        "last names": [],
        "ids": [],
        "mobiles": [],
        "emails": [],
        "c_gpas": [],
        "levels": [],
        "registered courses": [],
        "completed courses": [],
        "credit hours": [],
        "grades": []
    }

    Students_file = open("students.txt", "r")

    sdata_list = Students_file.read().split("\n")

    # read students data
    for i in range(len(sdata_list)):
        attribute = sdata_list[i].split(":")
        if attribute[0] == "-First name":
            students_data["first names"].append(attribute[1])
        elif attribute[0] == "-Last name":
            students_data["last names"].append(attribute[1])
        elif attribute[0] == "-ID":
            students_data["ids"].append(attribute[1])
        elif attribute[0] == "-Mobile":
            students_data["mobiles"].append(attribute[1])
        elif attribute[0] == "-Email":
            students_data["emails"].append(attribute[1])
        elif attribute[0] == "-C-GPA":
            students_data["c_gpas"].append(attribute[1])
        elif attribute[0] == "-Academic level":
            students_data["levels"].append(attribute[1])
        elif attribute[0] == "-Registered courses":
            students_data["registered courses"].append(attribute[1])
        elif attribute[0] == "-Fullfilled credit hours":
            students_data["credit hours"].append(attribute[1])
        elif attribute[0] == "-Grades":
            students_data["grades"].append(attribute[1])
        elif attribute[0] == "-Completed courses":
            students_data["completed courses"].append(attribute[1])
        else:
            continue

    # read faculty data

    Students_file.close()
    index = students_data["ids"].index(id)
    welcome_student()
    menu(students_data, index)


def write_data(data, filename):
    # open the file and write the data in the same file format
    if filename == "students.txt":

        Students_file = open("students.txt", "w")

        for i in range(len(data["ids"])):
            for key in data:
                if key == "first names":
                    word = "First name"
                elif key == "last names":
                    word = "Last name"
                elif key == "ids":
                    word = "ID"
                elif key == "mobiles":
                    word = "Mobile"
                elif key == "emails":
                    word = "Email"
                elif key == "c_gpas":
                    word = "C-GPA"
                elif key == "levels":
                    word = "Academic level"
                elif key == "registered courses":
                    word = "Registered courses"
                elif key == "credit hours":
                    word = "Fullfilled credit hours"
                elif key == "grades":
                    word = "Grades"
                elif key == "completed courses":
                    word = "Completed courses"
                Students_file.write(
                    "-"+word+":"+data[key][i]+"\n")
            Students_file.write("_"*50 + "\n")
        Students_file.close()
        write_csv(data)

    return


def write_csv(students_data):
    myfile = open("studs.csv", "w")
    myfile.write("First,Last,ID")
    all_courses = read_courses()
    codes = all_courses["code"]
    for code in codes:
        myfile.write(","+code)
    myfile.write("\n")
    ids = students_data["ids"]
    studs = []
    for i in range(len(ids)):
        mylist = []
        mylist.append(students_data["first names"][i])
        mylist.append(students_data["last names"][i])
        mylist.append(students_data["ids"][i])
        for course in codes:
            if course in students_data["registered courses"][i].split():
                index = (students_data["registered courses"]
                         [i].split()).index(course)
                grades = students_data["grades"][i].split()
                mylist.append(grades[index])
            else:
                mylist.append("None")

        studs.append(mylist)
    w = csv.writer(myfile)
    w.writerows(studs)
    myfile.close()


def welcome_student():

    print("*"*50)
    print("*"*50)
    print("|", end="")
    print("Welcome Student".center(48, "_"), end="")
    print("|")
    print("*"*50)
    print("*"*50)
    return


def menu(students_data, index):
    print("1]Display academic record\n2]Register course\n3]Drop course\n4]Calculate gpa\n5]Exit\n")
    choice = input("Enter your choice (1,2,3,4,5): ").strip()
    while choice not in ["1", "2", "3", "4", "5"]:
        choice = input("Enter a valid choice (1,2,3,4,5): ").strip()
    if choice == "1":
        display(students_data, index)
    elif choice == "2":
        register(students_data, index)
    elif choice == "3":
        drop(students_data, index)
    elif choice == "4":
        calc_gpa(students_data, index)
    else:
        good_bye_student()
    return


def read_courses():
    # read the course data and return a dict of it
    courses_data = {
        "code": [],
        "name": [],
        "description": [],
        "credit hours": [],
        "preq": []
    }
    Courses_file = open("courses.txt", "r")
    cdata_list = Courses_file.read().split("\n")
    for i in range(len(cdata_list)):
        attribute = cdata_list[i].split(":")
        if attribute[0] == "-Code":
            courses_data["code"].append(attribute[1])
        elif attribute[0] == "-Name":
            courses_data["name"].append(attribute[1])
        elif attribute[0] == "-Description":
            courses_data["description"].append(attribute[1])
        elif attribute[0] == "-Credit hours":
            courses_data["credit hours"].append(attribute[1])
        elif attribute[0] == "-Prerequisites":
            courses_data["preq"].append(attribute[1])
        else:
            continue
    Courses_file.close()
    return courses_data


def calc_letter_grade(grade):
    if grade >= 90:
        letter = "A"
    elif grade >= 80 and grade < 90:
        letter = "B"
    elif grade >= 70 and grade < 80:
        letter = "C"
    elif grade >= 60 and grade < 70:
        letter = "D"
    else:
        letter = "F"
    return letter


def question(students_data, index):
    # asking user if he wants to do another operation or not
    answer = input(
        "Do you want to perform another operation?(y/n): ").strip().lower()
    while answer not in ["y", "n"]:
        answer = input("Enter a valid choice please(y/n): ").strip().lower()
    if answer == "y":
        return menu(students_data, index)
    else:
        return good_bye_student()


def good_bye_student():
    # terminating the program
    print("*"*50)
    print("*"*50)
    print("|", end="")
    print("Good Bye Student".center(48, "_"), end="")
    print("|")
    print("*"*50)
    print("*"*50)
    time.sleep(1)
    exit(0)


def display(students_data, index):

    def display_all(students_data, index):
        print('Your academic record: ')
        courses = students_data["registered courses"][index].split()
        grades = students_data["grades"][index].split()
        for i in range(len(courses)):
            print(f"{courses[i]}:", calc_letter_grade(int(grades[i])))
        return

    def display_specefic(students_data, index):
        courses = students_data["registered courses"][index].split()
        grades = students_data["grades"][index].split()
        for i in range(1, len(courses)+1):
            print(f"{i}]{courses[i-1]}")
        answer = input('Enter the number course to display: ').strip()
        while answer not in list("123456789"):
            answer = input(
                'Enter a valid number of the course to display: ').strip()
        while int(answer) > len(courses) or int(answer) <= 0:
            answer = input(
                'Enter a valid number of the course to display: ').strip()
        ind = int(answer)-1
        print(f"{courses[ind]}:", calc_letter_grade(int(grades[ind])))
        return
    print("1]Display all courses\n2]Display specefic course\n")
    choice = input('Your choice: ').strip()
    while choice not in ["1", "2"]:
        choice = input('Enter a valid choice: ').strip()
    if choice == "1":
        display_all(students_data, index)
    else:
        display_specefic(students_data, index)
    return question(students_data, index)


def register(students_data, index):
    courses = students_data["registered courses"][index].split()
    grades = students_data["grades"][index].split()
    f = read_courses()
    all_courses = f["code"]

    crs = input("Enter course to register: ").strip()
    if crs not in f["code"]:
        print("Failed...Invalid course")
        return question(students_data, index)
    indx = all_courses.index(crs)
    preq_courses = f["preq"][indx].split()
    comp_courses = students_data["completed courses"][index].split()
    if crs in comp_courses:
        print("Failed...You already completed this course")
        return question(students_data, index)
    if crs in courses:
        print("Failed...You are already registered for this course")
        return question(students_data, index)
    for item in preq_courses:
        if item == "None":
            continue
        if item not in comp_courses:
            print("Failed...You need to complete course prequisites first")
            return question(students_data, index)
    courses.append(crs)
    grades.append("0")
    students_data["registered courses"][index] = " ".join(courses)
    students_data["grades"][index] = " ".join(grades)
    write_data(students_data, "students.txt")
    return question(students_data, index)


def drop(students_data, index):
    courses = students_data["registered courses"][index].split()
    grades = students_data["grades"][index].split()
    crs = input("Enter course to drop: ").strip()
    if crs not in courses:
        print("Failed...Invalid course")
        return question(students_data, index)
    i = courses.index(crs)
    courses.remove(crs)

    grades.remove(grades[i])
    students_data["registered courses"][index] = " ".join(courses)
    students_data["grades"][index] = " ".join(grades)
    write_data(students_data, "students.txt")
    return question(students_data, index)


def calc_gpa(students_data, index):
    grades = students_data["grades"][index].split()
    courses = students_data["registered courses"][index].split()
    all_courses = read_courses()
    credit_hours = []
    for item in courses:
        credit_hours.append(
            all_courses["credit hours"][all_courses["code"].index(item)])
    total_points = 0
    total_hours = 0
    for item in credit_hours:
        total_hours += int(item)
    for i in range(len(grades)):
        grade = float(grades[i])
        if grade >= 90:
            total_points += 4*int(credit_hours[i])
        elif grade >= 80:
            total_points += 3*int(credit_hours[i])
        elif grade >= 70:
            total_points += 2*int(credit_hours[i])
        elif grade >= 60:
            total_points += 1*int(credit_hours[i])

    if int(total_hours) == 0:
        print("Failed...")
        return question(students_data, index)

    gpa = float(total_points) / float(total_hours)
    print(f'Your GPA is: {gpa:.1f}')
    return question(students_data, index)
