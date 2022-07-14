import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',passwd='123456',database='storeresult',autocommit=True)
cursor=mydb.cursor()
cursor.execute("select * from sem1rec1")
x=cursor.fetchall()
print(x)
