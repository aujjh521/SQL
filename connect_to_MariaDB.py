import mysql.connector
from mysql.connector import Error

'''
mariaDB是MySQL的分支,兩者完全相容且語法基本一樣
'''

# 連線到MySQL資料庫by MySQL connector
try:
    # 連接 MySQL/MariaDB 資料庫
    connection = mysql.connector.connect(
        host='localhost',          # 主機名稱
        database='sakila', # 資料庫名稱
        user='root',        # 帳號
        password='1003')  # 密碼

    if connection.is_connected():

        # 顯示資料庫版本
        db_Info = connection.get_server_info()
        print("資料庫版本：", db_Info)

        # 顯示目前使用的資料庫
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("目前使用的資料庫：", record)

except Error as e:
    print("資料庫連接失敗：", e)


# 查詢資料庫
cursor = connection.cursor()
cursor.execute("SELECT * FROM actor;")

# 取回全部的資料
records = cursor.fetchall()
print("資料筆數：", cursor.rowcount)

# 列出查詢的資料
for row in records:
    print(row)



if (connection.is_connected()):
    cursor.close()
    connection.close()
    print("資料庫連線已關閉")


