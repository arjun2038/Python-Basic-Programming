import MySQLdb
db=MySQLdb.connect("192.168.3.188","training","training@123","int_b6")
cursor=db.cursor()
try:
    sql="""UPDATE emp
SET last_name = 'Pankajakshan'
WHERE first_name='Arjun'"""
    cursor.execute(sql)
    db.commit()
    print("Update Success")
except:
    db.rollback()
    print('error')
db.close()