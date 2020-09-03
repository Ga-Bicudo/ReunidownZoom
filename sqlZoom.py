import mysql.connector


sql_user = {
    'user':'Gabriel',
    'password':'Tg@briel10',
    'host':'127.0.0.1',
    'port': '3306',
    'database':'Sakila'
}


cnx = mysql.connector.connect(**sql_user)

cursor = cnx.cursor()

cursor.execute()

