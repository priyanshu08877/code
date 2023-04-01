import pymysql


def doConnection():
    #sglobal conn, cursor
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="2023",
        db="sys"
    )
    cursor = conn.cursor()
    cursor.execute("select @@version")
    output = cursor.fetchall()


    print("sacchai ka rakhwala -bhosdiwala",output)
    conn.close()
doConnection()

# def viewRecords():
#     count = 0
#     cursor.execute("SELECT * FROM empdata")

# (var,let,cons)