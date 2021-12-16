import  sqlite3


conn=sqlite3.connect('users.db')
cursor=conn.cursor()
cursor.execute("CREATE TABLE user(username text, email text, password text, confirm text)")
conn.commit()