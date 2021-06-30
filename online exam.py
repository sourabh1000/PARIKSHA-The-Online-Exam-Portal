2#Project on Online Exam Management
#--------------------------------------------------------------------------------
#MODULE : Online Exam Management
import Database
import Menulib
import Student
import Subject
import Exam
import joinclass
import tests
import menulibstudent
import Attendance
Database.DatabaseCreate()
Database.TablesCreate()


while True:

    print("To login as a professor kindly press 2 and to login as student press 1")
    ch=int(input("Enter choice: "))

    if ch == 2:
        print("\t\t\t Online Exam Management\n")
        print("=====================================================================")
        print("1. Student Management")
        print("2. Subject Management")
        print("3. Exam Management")
        print("4. Take attendance")
        print("5. Exit")
        choice = int(input("Enter Choice between 1 to 4 -------> : "))
        if choice == 1:
            Menulib.MenuStudent()
        elif choice == 2:
            Menulib.MenuSubject()
        elif choice == 3:
            Menulib.MenuExam()
        elif choice == 4:
            Attendance.take_attendance()
        elif choice == 5:
            break    
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Press any key to continue")
    else:
        print("\t\t\t Student Account\n")
        print("=========================================================================")
        print("1. Join The class ")
        print("2. Check the upcoming test ")
        print("3. Attempt the test ")
        print("4. Exit")

        ch= int(input("Enter Choice between 1 to 3 -------> : "))
        if ch == 1:
            joinclass.join()
        elif ch == 2:
            tests.check_test()
        elif ch == 3:
            tests.give_test()    
        elif ch ==4:
            break    
        else:
            print("Wrong Choice.....Enter Your Choice again")
            # break


