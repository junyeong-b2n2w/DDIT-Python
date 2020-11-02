import pymysql

con=pymysql.connect(host='localhost', user='root', password='java', db='python' ,charset='utf8')

cur = con.cursor()

sql = "update mytable set col02='up1', col03='up1' where col01=3"

cur.execute(sql)

con.commit()
