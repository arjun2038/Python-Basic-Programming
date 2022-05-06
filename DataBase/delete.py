import MySQLdb
db=MySQLdb.connect("192.168.3.188","training","training@123","int_b6")
cursor=db.cursor()
try:
    sql="""DELETE FROM emp WHERE last_name='K';
"""
    cursor.execute(sql)
    db.commit()
    print("delete success")
except:
    db.rollback()
    print("error")