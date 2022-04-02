import mysql.connector
from utils.my_connection import mysql_get_mydb

cnx = mysql_get_mydb()
cursor = cnx.cursor()

def create_table(cnx):
    cursor = cnx.cursor()
    try:
        # cursor.execute("DROP DATABASE Formulario")
        cursor.execute("CREATE DATABASE IF NOT EXISTS Formulario")
        cursor.execute("use Formulario")
        cursor.execute("CREATE TABLE IF NOT EXISTS Pessoas (ID int auto_increment, Nome varchar(50) not null, cpf varchar(50) not null, Email varchar(200) not null, Telefone varchar(20) not null, Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, primary key (id))")        
    except mysql.connector.Error as err:
        print("Algo está errado com sua tabela")
        print(err)
    else:
        print("Tabela criada com sucesso")