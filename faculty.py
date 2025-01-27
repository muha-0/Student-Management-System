import csv
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main(id):
    Faculty_file = open("faculty.txt", "r")
    fdata_list = Faculty_file.read().split("\n")

    faculty_data = {
        "first names": [],
        "last names": [],
        "ids": [],
        "courses taught": []
    }

    for i in range(len(fdata_list)):
        attribute = fdata_list[i].split(":")
        if attribute[0] == "-First name":
            faculty_data["first names"].append(attribute[1])
        elif attribute[0] == "-Last name":
            faculty_data["last names"].append(attribute[1])
        elif attribute[0] == "-ID":
            faculty_data["ids"].append(attribute[1])
        elif attribute[0] == "-Courses taught":
            faculty_data["courses taught"].append(attribute[1])
        else:
            continue
    Faculty_file.close()

    print("Welcome Back!")
    ID_Identifier(faculty_data, id)


def ID_Identifier(faculty, FID):

    index = faculty["ids"].index(FID)
    Courses = faculty['courses taught'][index].split()
    print(f'which course do you want to explore more? \n')
    for i in range(len(Courses)):
        print(f'{Courses[i]}')

    Course_in = input("Enter your choice: \n")
    while Course_in not in Courses:
        Course_in = input("Enter a valid course! : \n")
    CourseFN(Course_in, faculty, FID)


def good_bye():
    print("See you soon!")
    time.sleep(1)
    exit(0)


def putin():

    task = input("How can we help you? \n"
                 "Enter 1 for Grades Avarege \n"
                 "Enter 2 for Highest Grade \n"
                 "Enter 3 for Lowest Grade \n"
                 "Enter 4 for Failed Students \n"
                 "Enter 5 for Registered Students \n"
                 "Enter 6 for Students In Specfic Range \n"
                 "Enter 7 to Update Grades \n"
                 "Enter 8 to Search For Students Details \n"
                 "Enter 9 to see The success percentage in your course \n"
                 "Enter 10 to exit\n")

    while task != "1" and task != "2" and task != '3' and task != '4' and task != "5" and task != '6' and task != '7' and task != "8" and task != '9' and task != "10":
        print('please choose a correct number! \n')
        task = input("How can we help you? \n"
                     "Enter 1 for Grades Avarege \n"
                     "Enter 2 for Highest Grade \n"
                     "Enter 3 for Lowest Grade \n"
                     "Enter 4 for Failed Students \n"
                     "Enter 5 for Registered Students \n"
                     "Enter 6 for Students In Specfic Range \n"
                     "Enter 7 to Update Grades \n"
                     "Enter 8 to Search For Students Details \n"
                     "Enter 9 to see The success percentage in your course \n"
                     "Enter 10 to exit\n")
    if task == "10":
        good_bye()
    return task


def CourseFN(which, faculty, FID):
    students_csv = open('studs.csv', 'r')
    read = csv.DictReader(students_csv)

    FName = []
    LName = []
    Id = []
    Grade = []

    for i in read:
        if i[which] != 'None':
            FName.append(i['First'])
            LName.append(i['Last'])
            Id.append(i['ID'])
            Grade.append(i[which])

    Needed = putin()
    if Needed == "1":
        AVR(Grade)

    elif Needed == "2":
        Maxima(FName, LName, Id, Grade)

    elif Needed == "3":
        Minima(FName, LName, Id, Grade)

    elif Needed == "4":
        Failed(FName, LName, Id, Grade)

    elif Needed == "5":
        Registered(FName, LName, Id)

    elif Needed == "6":
        GWR(FName, LName, Id, Grade)

    elif Needed == "7":
        Update(FName, LName, Id, Grade, which)

    elif Needed == "8":
        Search(FName, LName, Id, Grade)

    elif Needed == "9":
        Success_Percentage(Grade)
    ID_Identifier(faculty, FID)


def AVR(Grade):
    average = 0

    for mark in Grade:
        average += int(mark)

    else:
        average = average/len(Grade)

    print(f'The Grades Average in this course is equal to: {average:.2f}')
    return


def Maxima(FName, LName, Id, Grade):
    MaxGrade = max(Grade)
    print(f'The Maximum Grade in your class is for the student {FName[Grade.index(MaxGrade)]} {LName[Grade.index(MaxGrade)]}'
          F', ID: {Id[Grade.index(MaxGrade)]} ,and his grade is {MaxGrade}')
    return


def Minima(FName, LName, Id, Grade):
    MinGrade = min(Grade)
    print(f'The Minimum Grade in your class is for the student {FName[Grade.index(MinGrade)]} {LName[Grade.index(MinGrade)]}'
          F', ID: {Id[Grade.index(MinGrade)]} ,and his grade is {MinGrade}')
    return


def Failed(FName, LName, Id, Grade):
    success = 60

    failed_fnames = []
    failed_lnames = []
    failed_ids = []
    failed_grades = []

    for mark in Grade:
        if int(mark) < success:
            failed_fnames.append(FName[Grade.index(mark)])
            failed_lnames.append(LName[Grade.index(mark)])
            failed_ids.append(Id[Grade.index(mark)])
            failed_grades.append(mark)

    print(f'The following students failed this course:\n')
    for prints in range(len(failed_grades)):
        print(
            f"{failed_fnames[prints]} {failed_lnames[prints]}, ID: {failed_ids[prints]}, Grade: {failed_grades[prints]}")
    return putin()


def Registered(FName, LName, Id):
    for n in range(1, len(Id)+1):
        print(f"{n}-{FName[n-1]} {LName[n-1]}, ID: {Id[n-1]}")
    return


def GWR(FName, LName, Id, Grade):
    LO, HI = input('Enter ther range of grades you want displayed. \n'
                   '(Enter the lower grade limit followed by a space then the upper grade limit) \n').split(' ')
    while not int(LO) < int(HI) and not int(HI) < 101 and not int(LO) > -1:
        print('Enter a valid range!')
        LO, HI = input('Re-enter ther range of grades you want displayed. \n'
                       '(Enter the lower grade limit followed by a space then the upper grade limit) \n').split(' ')

    InRange_grades = []
    InRange_fnames = []
    InRange_lnames = []
    InRange_ids = []

    for mark in Grade:
        if int(mark) > int(LO) and int(mark) < int(HI):
            InRange_fnames.append(FName[Grade.index(mark)])
            InRange_lnames.append(LName[Grade.index(mark)])
            InRange_ids.append(Id[Grade.index(mark)])
            InRange_grades.append(mark)

    print(
        f'The following students have a grade in the grade range of {LO} to {HI}: \n')
    for students in range(len(InRange_grades)):
        print(
            f"-{InRange_fnames[students]} {InRange_lnames[students]}, ID: {InRange_ids[students]}, Grade: {InRange_grades[students]}")
    return


def Success_Percentage(Grade):
    failure = 59
    percentage = 0
    for mark in Grade:
        if int(mark) > failure:
            percentage += 1

    else:
        percentage = (percentage/len(Grade))*100
        print(
            f'The percentage of succeeded students in this course is {percentage:.2f}%')
    return


def Search(FName, LName, Id, Grade):

    how = input('Search for the student using (enter 1 or 2): \n'

                '1-Their first name or last name \n'

                '2-Their ID \n'

                '(If you are searching by the name, the first letter should be capitalized): \n'
                )

    while how != "1" and how != "2":

        print('Choose only 1 or 2!')
        how = input('Search for the student using (enter 1 or 2): \n'

                    '1-Their first name or last name \n'

                    '2-Their ID \n'

                    '(If you are searching by the name, the first letter should be capitalized): \n'
                    )

    searchKEY = input("Search with the type you chose here: \n")
    if how == '1':
        while (searchKEY not in FName) and (searchKEY not in LName):
            print(
                'The name you entered is wrong or is not in your course, please try again')
            searchKEY = input("Write the name again: \n")

        first_found = []
        last_found = []
        mark = []
        name_id = []

        for first in FName:
            if searchKEY == first:
                first_found.append(searchKEY)
                last_found.append(LName[FName.index(searchKEY)])
                mark.append(Grade[FName.index(searchKEY)])
                name_id.append(Id[FName.index(searchKEY)])

        for last in LName:
            if searchKEY == last:
                first_found.append(FName[LName.index(searchKEY)])
                last_found.append(searchKEY)
                mark.append(Grade[LName.index(searchKEY)])
                name_id.append(Id[LName.index(searchKEY)])

        for i in range(len(first_found)):
            print(f'Here is what we found with that name: \n'

                  f'Name: {first_found[i]} {last_found[i]} \n'

                  f'ID: {name_id[i]} \n'

                  f'Grade: {mark[i]} \n \n \n'
                  )

    if how == '2':

        while searchKEY not in Id:
            print('The ID you have entered is not correct! please try again.')
            searchKEY = input("Write the ID again: \n")

        id_found = []
        for id in Id:
            if searchKEY == id:
                id_found.append(id)
                break

        print(f'Here is what we found with that ID: \n'

              f'Name: {FName[Id.index(searchKEY)]} {LName[Id.index(searchKEY)]} \n'

              f'ID: {searchKEY} \n'

              f'Grade: {Grade[Id.index(searchKEY)]}'
              )
    return


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

    return


def Update(f, l, Id, g, crs_name):
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    # ---------------------------------------------------------
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
        Students_file.close()
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    searchKEY = input(
        "Search for the student you want their grade changed by their ID: \n")

    while searchKEY not in Id:
        print('The ID you have entered is not correct! please try again.')
        searchKEY = input(
            "Search for the student you want their grade changed by their ID: \n")
    id_index = students_data["ids"].index(searchKEY)
    student_courses = students_data["registered courses"][id_index].split()
    student_grades = students_data["grades"][id_index].split()
    id_found = []
    for id in Id:
        if searchKEY == id:
            id_found.append(id)
            break

    print(f'Here is what we found with that ID: \n'

          f'Name: {f[Id.index(searchKEY)]} {l[Id.index(id)]} \n'

          f'ID: {id} \n'

          f'Grade: {g[Id.index(id)]}'
          )

    change = input('What is their new grade? \n')
    for c in change:
        if c not in list("0123456789"):
            print("Failed...Invalid grade")
            return
    if int(change) < 0 or int(change) > 100:
        print("Failed...Invalid grade")
        return
    crs_index = student_courses.index(crs_name)
    student_grades[crs_index] = change
    students_data["grades"][id_index] = " ".join(student_grades)
    write_data(students_data, "students.txt")
    studs = open('studs.csv', 'r')
    studs_read = csv.reader(studs)

    studs_read = list(studs_read)

    for i in studs_read:
        if id in i:
            for j in i:
                if j == g[Id.index(id)]:
                    break
            break
    studs.close()

    studs_read[studs_read.index(i)][i.index(j)] = change

    studs = open('studs.csv', 'w')

    w = csv.writer(studs)
    w.writerows(studs_read)
    studs.close()
    return
