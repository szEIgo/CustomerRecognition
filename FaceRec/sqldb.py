import sqlite3
import mysql.connector

def insertOrUpdate(Id, Name):
    # conn = sqlite3.connect("FaceTest.db")
    conn = mysql.connector.connect(host='localhost',
                                   database='python_mysql',
                                   user='root',
                                   password='allunite')
    cmd = "SELECT * FROM People WHERE ID=" + str(Id)
    cursor = conn.cursor()
    cursor.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if (isRecordExist == 1):
        cmd = "UPDATE People SET Name='" + str(Name) + "'WHERE ID =" + str(Id)
    else:
        cmd = "INSERT INTO People(ID, Name) Values(" + str(Id) + ",'" + str(Name) + "')"
    cursor.execute(cmd)
    conn.commit()
    conn.close()


def getProfile(id):
    conn = mysql.connector.connect(host='localhost',
                                   database='python_mysql',
                                   user='root',
                                   password='allunite')
    cmd = "SELECT Name FROM People WHERE ID=" + str(id)
    cursor = conn.cursor()
    cursor.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


def getNewID():
    conn = mysql.connector.connect(host='localhost',
                                   database='python_mysql',
                                   user='root',
                                   password='allunite')
    cmd = "SELECT count(ID) FROM People"
    cursor = conn.cursor()
    cursor.execute(cmd)
    LastID = cursor.fetchone()
    return int(LastID[0] + 1)



profile = getProfile(1)

print(profile)