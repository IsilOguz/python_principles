from student import Student
from schoolDB import sdb1

print ("Welcome To School Database OOP")

while True:
    choice = int(input("""
    1-List all students.
    2-Save a new student.

    Type your choice:"""))

    if choice == 1:
        sdb1.listStu()

    elif choice == 2:
        sdb1.saveStu()