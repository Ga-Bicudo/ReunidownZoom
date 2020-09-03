import mysql.connector
import testeapi

sql_user = {
    'user':'Gabriel',
    'password':'Tg@briel10',
    'host':'127.0.0.1',
    'port': '3306',
    'database':'testemysql'
}


cnx = mysql.connector.connect(**sql_user)

cursor = cnx.cursor()



for i in testeapi.lista_subcontas:
    insert_clients = ("insert into clientes(id_cliente,nm_cliente,email_cliente,account_type) values ({0},{1},{2},{3})".format(i['id'],i['account_name'],i['owner_email'],i['account_type']))
    cursor.execute(insert_clients)



