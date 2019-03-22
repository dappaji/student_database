from college import *
from department import *
from dep_application import *
from student import *
from stu_application import *

def main():
    print("college database ")
    while True:
        print("1:Department 2:student 3:Exit ")
        choice = input("Enter your choice ->")
        if choice == '1':
            Department()
        elif choice == '2':
            Student()
        elif choice == '3':
            Exit()
        else:
            print("Invalid Input ")

def Department():
    dep_main()
def Student():
    stu_main()

def Exit():
    exit()

main()