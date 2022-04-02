import cv2
import numpy as np
import os
from utils.my_connection import mysql_get_mydb
from utils.create_table import create_table
from utils.data_insert import cadastro, choose


# Conectando com o MySQL e criando a tabela
cnx = mysql_get_mydb() 
create_table(cnx)

#################################################################
# Inicializando o reconhecimento facial
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
#################################################################

# Selecionador de opções
choose = choose()
response = cadastro(choose)
if choose == '1':
    Nome = response[0]
    cpf = response[1]
elif choose == '2':
    print("Vamos iniciar o reconhecimento facial")


# Variáveis globais
lastName = ''
saveface = False
savefaceC = 0
trained = False
persons = []

# Inicia a leitura do video
cap = cv2.VideoCapture(0)
# Carrega o classificador Haar Cascade
face_cascade = cv2.CascadeClassifier('C:\\Users\\pqcir\\Desktop\\Formulario_Cadastro_RDS_OpenCV\\haarcascade_frontalface_default.xml')
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
      
# Liberando a captura
cap.release()
# Destruindo as janelas
cv2.destroyAllWindows()
