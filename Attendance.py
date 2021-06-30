import Exam
import datetime as datetime
import mysql.connector
# Login=input("Enter the time by which you want to take attendance")
def take_attendance():
    now=datetime.datetime.now()
    cur_time = now.strftime("%Y/%D/%m %H:%M:%S")


    cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
    Cursor = cnx.cursor()
    # User_ID = input("Enter User_ID of Student to be searched : ")
    query = ("SELECT * FROM Joinclass WHERE time <= %s ")
    rec_srch = (cur_time,)
    Cursor.execute(query, rec_srch)
    Rec_count = 0
    for(time, User_ID, Email_Address, Name, Roll_Number) in Cursor:
        Rec_count += 1
        print("Name: ", Name)
        print("USER_ID: ",User_ID)
        print("=============================================================")
        # if Rec_count%2 == 0:
        #     input("Press any key continue")
        #     clrscreen()
        #     print(Rec_count, "Record(s) found")
    cnx.commit()
    Cursor.close()
    cnx.close()

    

