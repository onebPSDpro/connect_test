import tkinter
import pymysql

'''
    “host”是自己电脑上的连接名，”user“是用户名，”password“写密码
    这些都是mysql配置的时候进行设置的，”database“是这个库的名称
    ”charset“是用来识别中文的，不是必须的
    
    Translation: "host" is the connection name on your computer
    "user" is the user name, and "password" is the password
     These are set when mysql is configured, "database" is the name of this library
     "Charset", which is not necessary, is used to identify Chinese
    
'''
def connect_mysql():
    conn = pymysql.connect(host="localhost", user="root", password="admin", database="test", charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select * from test_user order by idtest_user')
    D = cursor.fetchone()
    print(D)
    # d = list(D)
    # print(d[1])

if __name__ == '__main__':
    connect_mysql()
