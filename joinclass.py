import datetime as datetime
import Database
import mysql.connector
# Login=input("Enter the time by which you want to take attendance")
def join():
    cnx = mysql.connector.connect(host = 'localhost', port = 3306, user = 'root', password = '',database = 'online_exam')
    Cursor = cnx.cursor()
    print("------------------Join the class------------------")
    now=datetime.datetime.now()
    time = now.strftime("%Y/%D/%m %H:%M:%S")
    User_ID = input("Enter User_ID : ")
    # Password = input("Enter Password : ")
    Email_Address = input("Enter Email_Address : ")
    Name = input("Name : ")
    Roll_Number = input("Enter Roll_Number : ")
    Qry = ("INSERT INTO Joinclass VALUES (%s, %s, %s, %s, %s)")
    data = (time,User_ID, Email_Address, Name, Roll_Number)
    # if(userid ==format)
    Cursor.execute(Qry,data)  
    # security question
    cnx.commit()
    Cursor.close()
    cnx.close()
    print("Class joined")


