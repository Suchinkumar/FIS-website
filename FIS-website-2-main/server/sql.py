from mysql.connector import connect as con
mysql=con(host='localhost',user='fis',password='password',database='fis')
cur=mysql.cursor(dictionary=True)
cur.execute(f'select * from users where User_Name={input()}')
print(cur.fetchall())
