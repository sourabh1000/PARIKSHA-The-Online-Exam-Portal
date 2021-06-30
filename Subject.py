#PYTHON MODULE: SUBJECT
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import(connection)
import os

def insertSubject():
    try:
        cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
        Cursor = cnx.cursor()
        Subject_ID  = input("Enter Subject_ID  : ")
        Subject_name = input("Enter Subject Name : ")
        Credits = int(input("Enter Credits : "))
        Teacher = input("Enter Teacher Name : ")
        Qry = ("INSERT INTO Subject VALUES(%s, %s, %s, %s)")
        data = (Subject_ID,Subject_name, Credits,Teacher)
        Cursor.execute(Qry, data)
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


def deleteSubject():
    try:
        cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
        Cursor = cnx.cursor()
        Subject_ID = input("Enter Subject_ID to be deleted : ")
        Qry =("""DELETE FROM Subject WHERE Subject_ID = %s""")
        del_rec = (Subject_ID,)
        Cursor.execute(Qry, del_rec)
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


def SearchSubject():
    try:
        cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
        Cursor = cnx.cursor()
        Subject_ID = input("Enter Subject_ID to be Searched : ")
        query = ("SELECT * FROM Subject where Subject_ID = %s")
        rec_srch = (Subject_ID,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(Subject_ID,Subject_name, Credits,Teacher) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("Subject_ID : ", Subject_ID)
            print("Subject_name : ", Subject_name)
            print("Credits : ", Credits)
            print("Teacher : ", Teacher)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Press any key to continue: ")
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


def UpdateSubject():
    try:
        cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
        Cursor = cnx.cursor()
        Subject_ID = input("Enter Subject_ID of Subject to be Updated : ")
        print("Enter new data")
        New_Subject_ID  = input("Enter Subject_ID  : ")
        Subject_name = input("Enter Subject Name : ")
        Credits = int(input("Enter Credits : "))
        Teacher = input("Enter Teacher Name : ")
        Qry = ("UPDATE Subject SET Subject_ID=%s, Subject_name=%s, Credits=%s, Teacher=%s WHERE Subject_ID=%s")
        data = (New_Subject_ID,Subject_name, Credits,Teacher, Subject_ID)
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