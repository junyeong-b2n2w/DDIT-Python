import pymysql

con=pymysql.connect(host='localhost', user='root', password='java', db='python' ,charset='utf8')

cur = con.cursor()

sql = 'select * from mytable'

cur.execute(sql)

for i in cur:
    print(i)
    
con.close()
    