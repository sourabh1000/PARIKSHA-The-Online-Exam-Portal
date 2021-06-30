import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
import os
import Exam
import datetime as datetime
from datetime import date
def check_test():
    cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
	# Exam_ID = input("Enter Exam_ID of Exam to be searched : ") 
    # date=datetime 
    dt=date.today()
    Cursor = cnx.cursor()
    query = ("SELECT * FROM Exam WHERE Exam_date > %s ")
    rec_srch = (dt,)
    Cursor.execute(query, rec_srch)
    Rec_count = 0
    for(Exam_ID, User_ID,Subject_ID, Exam_Link,Exam_date,Description) in Cursor:
	    Rec_count += 1
	    print("=============================================================")
	    print("Exam_ID : ", Exam_ID)
	    print("User_ID : ", User_ID)
	    print("Subject_ID : ", Subject_ID)
	    print("Exam_Link: ", Exam_Link)
	    print("Exam_date: ", Exam_date)
	    print("Description: ", Description)
	    print("=============================================================")
	    if Rec_count%2 == 0:
	        input("Press any key continue")
	        clrscreen()
	        print(Rec_count, "Record(s) found")
    cnx.commit()
    Cursor.close()
    cnx.close()

def give_test():
    cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
	# Exam_ID = input("Enter Exam_ID of Exam to be searched : ") 
    # date=datetime 
    dt=date.today()
    Cursor = cnx.cursor()
    query = ("SELECT * FROM Exam WHERE Exam_date = %s ")
    rec_srch = (dt,)
    Cursor.execute(query, rec_srch)
    Rec_count = 0
    for(Exam_ID, User_ID,Subject_ID, Exam_Link,Exam_date,Description) in Cursor:
	    Rec_count += 1
	    print("=============================================================")
	    
	    print("Subject_ID : ", Subject_ID)
	    print("Exam_Link: ", Exam_Link)
	    
	    print("Description: ", Description)
	    print("=============================================================")
	    if Rec_count%2 == 0:
	        input("Press any key continue")
	        clrscreen()
	        print(Rec_count, "Record(s) found")
    cnx.commit()
    Cursor.close()
    cnx.close()	

