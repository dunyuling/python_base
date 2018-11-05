import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'mysql',
    database = 'python_test'
)

mycursor = mydb.cursor()

#1
#mycursor.execute('create database python_test')

#2
#mycursor.execute('show databases')
#for x in mycursor:
#    print(x)

#3
#mycursor.execute('create table sites (name varchar(255),url varchar(255))')

#4
#mycursor.execute('show tables')
#for x in mycursor:
#    print(x)

#5
#mycursor.execute('alter table sites add column id int auto_increment primary key')

#6
#sql = 'insert into sites(name, url) values(%s, %s)'
#val = ('runoob', 'https://www.runoob.com')
#mycursor.execute(sql, val)
#mydb.commit()

#print(mycursor.rowcount,'记录插入成功')


#7
#sql = 'insert into sites(name, url) values(%s, %s)'
#val = [
#    ('google', 'https://www.google.com'),
#    ('github', 'https://www.github.com'),
#    ('taobao', 'https://www.taobao.com'),
#    ('stackoverflow', 'https://www.stackoverflow.com')
#]

#mycursor.executemany(sql, val)
#mydb.commit()

#print(mycursor.rowcount, '记录插入成功')


#8
#sql = 'insert into sites(name, url) values(%s, %s)'
#val = ('zhihu', 'https://www.zhihu.com')
#mycursor.execute(sql, val)
#mydb.commit()

#print('1 条记录插入成功, ID:', mycursor.lastrowid)


#9
#mycursor.execute('select * from sites')
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)



#10
#mycursor.execute('select name, url  from sites')
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)


#11
#mycursor.execute('select * from sites')
#myresult = mycursor.fetchone()
#print(myresult)


#12
#mycursor.execute("select * from sites where name = 'runoob'")
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)


#13
#mycursor.execute("select * from sites where url like '%oo%'")
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)


#14
#为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义查询的条件：
#sql = "select * from sites where name = %s"
#na = ('runoob',)
#mycursor.execute(sql, na)
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)



#15
#sql = 'select * from sites order by name'
#mycursor.execute(sql)
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)


#16
#sql = 'select * from sites order by name desc' 
#mycursor.execute(sql)
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)


#17
#sql = 'select * from sites limit 3'
#mycursor.execute(sql)
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)


#18
#sql = 'select * from sites limit 3 offset 1'
#mycursor.execute(sql)
#myresult = mycursor.fetchall()

#for x in myresult:
#    print(x)


#19
#sql = "delete from sites where name = 'stackoverflow'"
#mycursor.execute(sql)
#mydb.commit()
#print(mycursor.rowcount, '条记录删除')


#20
#为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义删除语句的条件：
#sql = "delete from sites where name = %s"
#na = ('stackoverflow',) 
#mycursor.execute(sql, na)
#mydb.commit()
#print(mycursor.rowcount, '条记录删除')


#21
#sql = "update sites set name = 'zh' where name = 'zhihu'"
#mycursor.execute(sql)
#mydb.commit()
#print(mycursor.rowcount, '条记录更新')


#22
#为了防止数据库查询发生 SQL 注入的攻击，我们可以使用 %s 占位符来转义更新语句的条件：
#sql = "update sites set name = %s  where name = %s"
#val = ('zh', 'zhihu')
#mycursor.execute(sql, val)
#mydb.commit()
#print(mycursor.rowcount, '条记录更新')


#23
#sql = 'drop table if exists sites'
#mycursor.execute(sql)


mydb.close()
mycursor.close()
