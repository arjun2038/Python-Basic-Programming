import MySQLdb

db=MySQLdb.connect("192.168.3.188","training","training@123","int_b6")
cursor=db.cursor()
cursor.execute("drop table if exists Employees")
query="""create table emp(
first_Name char(20) not null,
last_name char(20),
age int,
sex char(1),
income float)"""

cursor.execute(query)
db.close()