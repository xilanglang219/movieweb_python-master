import sqlite3

# 连接到SQLite数据库（如果文件不存在，会自动创建）
conn = sqlite3.connect('D:\website\movieweb_python-master\movieweb_python-master\movieweb\movieweb.db')
cursor = conn.cursor()

# SQL="SELECT sql FROM sqlite_master WHERE type='table' AND name='videoplay_movie';"
SQL="SELECT sql FROM sqlite_master WHERE type='table' AND name='videoplay_usercomment';"
SQL1="SELECT * FROM videoplay_movie ;"
cursor.execute(SQL1)
tables = cursor.fetchall()
for table in tables:
    print(table)



# print(tables)
"""
('django_migrations',)
('sqlite_sequence',)
('auth_group_permissions',)
('auth_user_groups',)
('auth_user_user_permissions',)
('django_content_type',)
('auth_permission',)
('django_session',)
('videoplay_movie',)
('videoplay_moviepay',)
('videoplay_user',)
('videoplay_usercomment',)
('django_admin_log',)
('auth_group',)
('auth_user',)
"""

# 创建一个表
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# 插入数据
# cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
# cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# 提交事务
# conn.commit()

# 查询数据
# cursor.execute("SELECT * FROM users")
# results = cursor.fetchall()
# for row in results:
#     print(row)  # 输出： (1, 'Alice', 30), (2, 'Bob', 25)

# 关闭游标和连接以释放资源
cursor.close()
conn.close()