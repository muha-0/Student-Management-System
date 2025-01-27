import student
import admin
import faculty
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def login_page():
    print("*"*50)
    print("*"*50)
    print("|", end="")
    print("Welcome To Student Management System".center(48, "_"), end="")
    print("|")
    print("*"*50)
    print("*"*50)
    accountfile = open("accounts.txt", "r")
    lines = accountfile.read().split("\n")
    count = 0
    while count < 3:
        login_id = input("Enter your id : ")
        login_pass = input("Enter your password : ")
        for i in range(len(lines)):
            eachline = lines[i]
            line_details = eachline.split(" ")
            if (line_details[0] == login_id) and (line_details[1] == login_pass):
                count = 4
                if line_details[0].startswith("A"):
                    admin.main()

                elif line_details[0].startswith("S"):
                    student.main(login_id)
                elif line_details[0].startswith("F"):
                    faculty.main(login_id)
                break
        else:
            count += 1
            print("your ID or password is invalid")
    if count >= 3:
        print("Failed...")
        exit(0)


# ----------------------------------------------------

login_page()
