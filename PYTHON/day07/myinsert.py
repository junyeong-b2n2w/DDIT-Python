import pymysql

con=pymysql.connect(host='localhost', user='root', password='java', db='python' ,charset='utf8')

cur = con.cursor()

sql = "Insert into mytable (col02, col03) values ('123','123' )" 

cur.execute(sql)

con.commit()

con.close()