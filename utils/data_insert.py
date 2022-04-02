from utils.my_connection import mysql_get_mydb
from pyfiglet import figlet_format
from utils.bypass import bypass

cnx = mysql_get_mydb() 

def logo(titulo):
    print("=" * 80)
    print(figlet_format(text=titulo, font="standard", justify="center"))
    print("=" * 80)

logo("Reconhecimento Facial")

def choose():    
    print("1 - Cadastrar")
    print("2 - Identificar")
    choose = input(str("\nOpção: "))
    return choose

def cadastro(choose):
    if choose == "1":
        cursor = cnx.cursor()
        # input manual dentro do INSERT
        print("\nPor favor, preencha os campos abaixo conforme solicitado.")
        Nome = input(str("Nome: ")).title()
        cpf = input(str("CPF: "))
        Email = input(str("E-mail: ")).lower()
        Telefone = input(str("Tel: "))
        
        cursor.execute("use Formulario")
        sql = "INSERT INTO Pessoas (Nome, CPF, Email, Telefone) VALUES ('%s', '%s', '%s', '%s')" % (Nome, cpf, Email, Telefone)
        cursor.execute(sql)
        cnx.commit()
        print("\nDados inseridos com sucesso")
        return Nome, cpf, Email, Telefone

    elif choose == "2":
        print()
        