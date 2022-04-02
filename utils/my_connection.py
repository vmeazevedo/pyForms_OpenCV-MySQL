import mysql.connector
from mysql.connector import errorcode

def mysql_get_mydb():    
    try:
        cnx = mysql.connector.connect(user='root', password='123456',
                                host='127.0.0.1')
        # print("Conexão estabelecida")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo está errado com seu nome de usuário ou senha")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database não existe")
        else:
            cnx.close()
    return cnx


    
