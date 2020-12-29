import mysql.connector
from mysql.connector import errorcode
from mysql.connector import cursor

###############################################################################################################
# Conexão da instância RDS - Amazon Web Service
###############################################################################################################
# Preencher os campos de conexão abaixo
host = ''    # Endpoint da instância RDS na cloud da AWS
user = ''                                               # Username criado na hora de realizar a instância RDS
password = '"                                         # Password criado na hora de realizar a instância RDS

# host = 'localhost'    # Endpoint da instância RDS na cloud da AWS
# user = 'root'                                               # Username criado na hora de realizar a instância RDS
# password = ''                                           # Password criado na hora de realizar a instância RDS

try:
	db_connection = mysql.connector.connect(host = host, user = user, password = password)
	print("\nConexão com a base de dados realizada!\n")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("\nA base de dados não existe.")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("\nUsername ou o password está errado.")
	else:
		print(error)

cursor = db_connection.cursor()
# Criando a database e a tabela
cursor.execute("CREATE DATABASE IF NOT EXISTS Formulario")
cursor.execute("use Formulario")
cursor.execute("CREATE TABLE IF NOT EXISTS Pessoas (ID int auto_increment, Nome varchar(50) not null, cpf varchar(50) not null, Email varchar(200) not null, Telefone varchar(20) not null, Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, primary key (id))")
###############################################################################################################

# Inserir registros no formulario
def inserir():
    # Declaração de variável
    cursor = db_connection.cursor()
    # input manual dentro do INSERT
    print("Por favor, preencha os campos abaixo conforme solicitado.")
    Nome = input(str("Nome: ")).title()
    cpf = input(str("CPF: "))
    Email = input(str("E-mail: ")).lower()
    Telefone = input(str("Tel: "))
    
    sql = "INSERT INTO Pessoas (Nome, CPF, Email, Telefone) VALUES ('%s', '%s', '%s', '%s')" % (Nome, cpf, Email, Telefone)
    cursor.execute(sql)
    db_connection.commit()
    print("\nDados inseridos com sucesso")



# Consultar a base de dados
def consulta_base():
    cursor = db_connection.cursor()
    # Apresentando o header da base de dados
    sql = ("SELECT * FROM Pessoas")
    cursor.execute(sql)
    print(cursor.column_names)
    rows = cursor.fetchall()
    
    # Apresentando a base de dados completa
    sql = ("SELECT CONCAT_WS('  ||  ', ID, Nome, CPF, Email, Telefone) FROM Pessoas")
    cursor.execute(sql)
    for (x) in cursor:
        print(x)
    print("\n")

# inserir()
consulta_base()
