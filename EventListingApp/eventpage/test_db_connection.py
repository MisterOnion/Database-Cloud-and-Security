import pymysql


endpoint = "replace with your own endpoint"
port = 3306
dbname = "mydb"  # Updated database name
username = "admin"
password = "ADmin987"

connection = None

try:
    connection = pymysql.connect(
        host=endpoint,
        user=username,
        password=password,
        database=dbname,
        port=port
    )

    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()
        print("Database version:", result)
except pymysql.MySQLError as e:
    print(f"Error connecting to database: {e}")
finally:
    if connection:
        connection.close()