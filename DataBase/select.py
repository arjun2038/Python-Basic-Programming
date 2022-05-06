import MySQLdb
db=MySQLdb.connect("192.168.3.188","training","training@123","int_b6")
cursor=db.cursor()
try:
    sql="""select * from emp"""
    cursor.execute(sql)
    results=cursor.fetchall()
    for data in results:
        first_name=data[0]
        last_name=data[1]

        print("First Name is {} and Last Name is {}".format(first_name,last_name))
except:
    print("error")
db.close()