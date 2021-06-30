#PYTHON MODULE: BOOK
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform


def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))


def insertData():
    try:
        cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
        Cursor = cnx.cursor()
        User_ID = input("Enter User_ID : ")
        Password = input("Enter Password : ")
        Email_Address = input("Enter Email_Address : ")
        Name = input("Name : ")
        Roll_Number = input("Enter Roll_Number : ")
        Phone = input("Enter Phone_Number : ")
        Qry = ("INSERT INTO Student VALUES (%s, %s, %s, %s, %s, %s)")
        data = (User_ID, Password, Email_Address, Name, Roll_Number, Phone)
        # if(userid ==format)
        Cursor.execute(Qry,data)  
        # security question
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


def deleteStudent():
    try:
        cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
        Cursor = cnx.cursor()
        User_ID = input("Enter User_ID of Student to be deleted : ")
        Qry = ("""DELETE FROM Student WHERE User_ID = %s""")
        del_rec = (User_ID,)
        Cursor .execute(Qry, del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


def SearchStudentRec():
    try:
        cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
        Cursor = cnx.cursor()
        User_ID = input("Enter User_ID of Student to be searched : ")
        query = ("SELECT * FROM Student WHERE User_ID = %s ")
        rec_srch = (User_ID,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(User_ID, Password, Email_Address, Name, Roll_Number, Phone) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("User_ID : ", User_ID)
            print("Password : ", Password)
            print("Email_Address : ", Email_Address)
            print("Name: ", Name)
            print("Roll_Number : ", Roll_Number)
            print("Phone : ", Phone)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


def UpdateStudent():
    try:
        cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
        Cursor = cnx.cursor()
        User_ID = input("Enter User_ID of the Student to be Updated : ")
        print("Enter new data")
        New_User_ID = input("Enter User_ID : ")
        Password = input("Enter Password : ")
        Email_Address = input("Enter Email_Address : ")
        Name = input("Name : ")
        Roll_Number = input("Enter Roll_Number : ")
        Phone = input("Enter Phone_Number : ")
        Qry = ("UPDATE Student SET User_ID=%s, Password=%s, Email_Address=%s, Name=%s, Roll_Number=%s, Phone=%s WHERE User_ID  = %s")
        data = (New_User_ID, Password, Email_Address, Name, Roll_Number, Phone, User_ID)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.")
    except mysql.connector.ERROR as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()