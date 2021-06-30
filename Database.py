import mysql.connector as connector

def DatabaseCreate():
    cnx = connector.connect(host = 'localhost', port = 3306, user = 'root',
     password = '')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS online_exam")
    Cursor.execute("")
    Cursor.close()
    cnx.close()


def TablesCreate():
    cnx = connector.connect(host = 'localhost', port = 3306, user = 'root', 
    	password = '', database = 'online_exam')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS Student(User_ID varchar(10) PRIMARY KEY, Password varchar(20), Email_Address varchar(40), Name text(40), Roll_Number varchar(20), Phone varchar(10))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Joinclass(Time varchar(50), User_ID varchar(10) PRIMARY KEY, Email_Address varchar(40), Name text(40), Roll_Number varchar(20))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Subject(Subject_ID varchar(10) PRIMARY KEY, Subject_name text(20), Credits int(2), Teacher text(40))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Exam(Exam_ID varchar(10) PRIMARY KEY, User_ID varchar(10), Subject_ID varchar(10), Exam_Link varchar(50), Exam_date DATE, Description varchar(50))")
    Cursor.close()
    cnx.close()
