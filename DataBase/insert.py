import MySQLdb
db=MySQLdb.connect("192.168.3.188","training","training@123","int_b6")
cursor=db.cursor()
try:
    # query="""insert into emp values('Arjun','VP',22,'M','15000')"""
    query="""insert into emp values("bramman",'K',24,'M','723684')"""


    cursor.execute(query)
    db.commit()
    print("success")
except:
    db.rollback()