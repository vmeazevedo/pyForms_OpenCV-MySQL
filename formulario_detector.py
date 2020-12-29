import numpy as np
import cv2
import os
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import cursor
from numpy.core.fromnumeric import choose

##############################################################################################################
# Conexão da instância RDS - Amazon Web Service
###############################################################################################################
# Preencher os campos de conexão abaixo
host = 'localhost'                                          # Endpoint da instância RDS na cloud da AWS
user = 'root'                                               # Username criado na hora de realizar a instância RDS
password = ''                                               # Password criado na hora de realizar a instância RDS

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
cursor.execute("DROP DATABASE Formulario")
cursor.execute("CREATE DATABASE IF NOT EXISTS Formulario")
cursor.execute("use Formulario")
cursor.execute("CREATE TABLE IF NOT EXISTS Pessoas (ID int auto_increment, Nome varchar(50) not null, cpf varchar(50) not null, Email varchar(200) not null, Telefone varchar(20) not null, Data TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP, primary key (id))")
###############################################################################################################

def creatDir(name, path=''):
    # verifica se tem um diretorio, se não tem ele cria
    if not os.path.exists(f'{path}/{name}'):  
        os.makedirs(f'{path}/{name}')  

def saveFace():
    # criando a pasta de treino e a pasta do usuário
    global saveface  
    global lastName
    saveface = True  
    creatDir('USUARIO')  
    print("CADASTRANDO..")  
    name = Nome  
    lastName = name  
    creatDir(name, 'USUARIO')  

def saveImg(img):
    # salvando as fotos na pasta do usuário e nomeando elas
    global lastName  
    qtd = os.listdir(f'USUARIO/{lastName}')  
    cv2.imwrite(f'USUARIO/{lastName}/{str(len(qtd))}.jpg', img)  

def trainData():
    # realizando o treinamento das fotos
    global recognizer  
    global trained
    global persons
    trained = True  
    persons = os.listdir('USUARIO')  
    ids = []  
    faces = []  
    for i, p in enumerate(persons):  
        i += 1  
        for f in os.listdir(f'USUARIO/{p}'):  
            img = cv2.imread(f'USUARIO/{p}/{f}', 0)  
            faces.append(img) 
            ids.append(i)  
    recognizer.train(faces, np.array(ids))  



print("=================================================")
print("             Formulário de Cadastro              ")
print("=================================================")
print("Selecione:")
print("1 - Cadastrar")
print("2 - Identificar")
choose = input(str("\nOpção: "))

if choose == "1":
    cursor = db_connection.cursor()
    # input manual dentro do INSERT
    print("\nPor favor, preencha os campos abaixo conforme solicitado.")
    Nome = input(str("Nome: ")).title()
    cpf = input(str("CPF: "))
    Email = input(str("E-mail: ")).lower()
    Telefone = input(str("Tel: "))
    
    sql = "INSERT INTO Pessoas (Nome, CPF, Email, Telefone) VALUES ('%s', '%s', '%s', '%s')" % (Nome, cpf, Email, Telefone)
    cursor.execute(sql)
    db_connection.commit()
    print("\nDados inseridos com sucesso")

elif choose == "2":
    print("")
    

# Variáveis
lastName = ''
saveface = False
savefaceC = 0
trained = False
persons = []

# Inicia a leitura do video
cap = cv2.VideoCapture(0)
# Carrega o classificador Haar Cascade
face_cascade = cv2.CascadeClassifier('C:\\Users\\pqcir\\Desktop\\Projetos\\exercicio4\\haarcascade_frontalface_default.xml')
# Carrega o recognizer - "pip install opencv_contrib_python"
recognizer = cv2.face.LBPHFaceRecognizer_create()


# Criando um loop
while(True):
    # Realizando a leitura do frame
    _, frame = cap.read()
    # Frame em cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detectando rostos no frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 6)
    
    for i, (x,y,w,h) in enumerate(faces):
        # Desenhando um quadrado nos rostos
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        # Cortando o rosto
        roi_gray = gray[y:y+h, x:x+w]
        # Ajustando a foto para 50x50
        resize = cv2.resize(roi_gray, (400, 400)) 
        # Verificando se o recognizer está treinado
        if trained:
            # Prevendo o rosto
            idf, conf = recognizer.predict(resize)
            # Obter o nome da pessoa
            nameP = persons[idf-1]
            # Se a confidenci for menor que 100, imprimir o nome em verde
            if conf < 40:
                cv2.putText(frame,nameP,(x+5,y+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0),1,cv2.LINE_AA)
               
            # Se for maior que 100 imprimir em vermelho
            else:
                cv2.putText(frame,nameP,(x+5,y+25), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1,cv2.LINE_AA)
            # Mostrar um texto indicando se está treinado ou não
            cv2.putText(frame,'TREINADO',(10,65), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0),1,cv2.LINE_AA)
        else:
            cv2.putText(frame,'NAO TREINADA',(10,65), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),1,cv2.LINE_AA)
        # Se a função "save" for pressionada
        if saveface:
            # Desenhe o texto de "save"
            cv2.putText(frame,str(savefaceC),(10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,255),1,cv2.LINE_AA)
            # Incrementando a id
            savefaceC += 1
            # Salvando os rostos
            saveImg(resize)
        # Se chegar em 50 fotos deve parar
        if savefaceC > 100:
            # Retorna o contador pra 0
            savefaceC = 0
            # Desativa a variavel 
            saveface = False


    # Escrevendo na tela
    cv2.putText(frame, "Pressione a tecla 'space' para cadastrar um novo perfil.", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    # DRAW TEXT 2
    cv2.putText(frame, "Pressione a tecla 't' para realizar o reconhecimento facial.", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, "Pressione a tecla 'q' para fechar.", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    # Apresentando o frame
    cv2.imshow('frame',frame)
    # Esperando a chave de comando
    key = cv2.waitKey(10) 
    # Pressionar T para treinar
    if key == 116:
        trainData()
    # Pressionar "espaço" para salvar
    if key == 32:
        saveFace()
    # Pressionar o "q" para o loop
    if key & 0xFF == ord('q'):
        break
      

# RELEASE CAP
cap.release()
# DESTROY ALL WINDOWS
cv2.destroyAllWindows()