from flask import Flask, request, make_response
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask_ipban import IpBan
import MySQLdb

# Now you can use MySQLdb.cursors and other functionalities of MySQLdb
import MySQLdb.cursors as cur

app=Flask(__name__)

cors=CORS(app)
mysql=MySQL(app)
ipban=IpBan(app=app,ban_count=5)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'fis'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'fis'
app.config['JSON_SORT_KEYS'] = False

@app.get('/')
def welcome():
    return make_response({'message':'welcome'})

@app.post('/login')
@cross_origin()
def login():
    x=request.get_json()
    cursor = mysql.connection.cursor(cur.DictCursor)
    if ' ' in x['password']:
        ipban.add()
        return make_response({'message':'Login failed'})
    else:
        com="select exists(select users.User_Name from users,password where password.Password=%s) as login"
        cursor.execute(com,(x['password']))
        # a=f"select exists(select from users, password where users.User_Name={x['user_name']} and password.Password={x['password']})"
        # print(a)
        a=cursor.fetchone()['login']
        if a:
            return make_response({'message':'Login successfull'})
        else:
            return make_response({'message':'Login failed'})

@app.post('/register')
@cross_origin()
def register():
    x=request.get_json()
    cursor=mysql.connection.cursor(cur.DictCursor)
    if ' ' in x['password']:
        ipban.add()
        return make_response({'message':'Registration failed, password can not contain space'})
    com="insert into users (User_Name,Email) values (%s,%s)"
    value=(x['user_name'],x['email'])
    cursor.execute(com,value)
    mysql.connection.commit()
    com="insert into password (User_Name,Password) values (%s,%s)"
    value=(x['user_name'],x['password'])
    cursor.execute(com,value)
    mysql.connection.commit()
    com="insert into level (User_Name,Level) values (%s,%s)"
    value=(x['user_name'],'basic')
    cursor.execute(com,value)
    mysql.connection.commit()
    try:
        a=cursor.fetchone()
    except:
        a=None
    return make_response({'message':a if a else "done"})

if __name__=='__main__':
    app.run(debug=True)