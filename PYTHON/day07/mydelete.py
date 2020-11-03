import pymysql

con=pymysql.connect(host='localhost', user='root', password='java', db='python' ,charset='utf8')

cur = con.cursor()

sql = "delete from mytable where col01=3" 

cur.execute(sql)

con.commit()
con.close()