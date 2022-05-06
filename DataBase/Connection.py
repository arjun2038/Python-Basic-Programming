import MySQLdb
try:
    db=MySQLdb.connect("192.168.3.188","training","training@123","int_b6")
    # print("success")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data=cursor.fetchall()
    print(data)
    db.close()
except:
    print("error")
