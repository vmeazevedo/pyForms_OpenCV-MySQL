# Formulário de Cadastro com database RDS AWS e reconhecimento facial via OpenCV
O algoritmo realiza um cadastro de usuário simples (Nome, CPF, E-mail e Telefone) em uma database RDS da Amazon e também realiza o armazenamento, treinamento e o reconhecimento facial do rosto do usuário para identificar os usuários já cadastrados no sistema em uma próxima vez que o usuário for visto.

# Requirements
Será necessário instalar as bibliotecas abaixo:

- numpy
- OpenCV
- mysql-connector

## Criando instancia RDS-MySQL na AWS
- Acessar o "Console de gerenciamento da AWS"
- Abra o menu de serviços e selecione a opção RDS
- Selecione a opção de "Create database"
- Selecione MySQL
- Version: MySQL 8.0.11
-> Free tier
- Entre com os dados de base, username e password:

db instance: "nome da base de dados"

username: "seu usuário"

password: "sua senha"

- DB instance size e Storage é default não mexer
- VPC: Default
- Subnet group: default
- Public acess: Yes
- VPC security group: Create new

New VPC security group name: <entrar_com_o_nome>

- Availability Zone: escolher onde você ta conectado

# Funcionamento
Ao rodar o código será apresentado no terminal o menu abaixo com as opções de cadastro e identificação:
![image](https://user-images.githubusercontent.com/40063504/103282211-d6674d80-49b3-11eb-8b8c-84fc54b6c73f.png)

## Opção 1
Se a opção 1 for selecionada, será apresentado alguns campos para preenchimento do novo cadastro conforme mostrado abaixo:
![image](https://user-images.githubusercontent.com/40063504/103282344-3bbb3e80-49b4-11eb-8720-9faa71b78780.png)

Após realizarmos o preenchimento do novo cadastro em nossa base de dados a tela do reconhecimento fácial será apresentada.
![image](https://user-images.githubusercontent.com/40063504/103282395-673e2900-49b4-11eb-8db4-0c012b900b25.png)

Nessa tela temos a opção de cadastrar uma nova foto de usuário (tecla espaço), realizar o treinamento (letra t), ou sair (letra q). 
Pressionando a tecla 'espaço' do teclado iremos realizar a captura das fotos para realização do treinamento posteriormente.
![image](https://user-images.githubusercontent.com/40063504/103282503-c865fc80-49b4-11eb-877b-423246d026ce.png)

Ao pressionarmos 'espaço' uma pasta será criada chamada 'USUARIO' e dentro dela será criado uma pasta com o nome cadastrado anteriormente, dentro dessa pasta será armazenada todas as fotos do usuário que acabamos de cadastrar. Em um caso de novo cadastro, será criado outra pasta automaticamente com o nome cadastrado dentro da pasta 'USUARIO'.
![image](https://user-images.githubusercontent.com/40063504/103282688-4fb37000-49b5-11eb-9497-9a6432d2c241.png)

Agora chegou o momento de realizarmos o treinamento de nosso algoritmo para ele reconhecer o usuário cadastrado através das fotos tiradas. Para isso pressionamos a tecla 't' na mesma tela onde realizamos a captura. O algoritmo será treinado e será apresentado o nome do usuário cadastrado diretamente no layer do reconhecimento facial.
![image](https://user-images.githubusercontent.com/40063504/103282855-c2245000-49b5-11eb-90b8-32ddf0cf4381.png)


## Opção 2
Ao rodar o código será apresentado no terminal o menu abaixo com as opções de cadastro e identificação:
![image](https://user-images.githubusercontent.com/40063504/103282211-d6674d80-49b3-11eb-8b8c-84fc54b6c73f.png)

Se a opção 2 for selecionada, a tela do reconhecimento facial será apresentada para o usuário.
![image](https://user-images.githubusercontent.com/40063504/103283063-5098d180-49b6-11eb-8bdb-1bf3fbd03b2d.png)

Como nesse caso já temos o nosso usuário cadastrado em nossa database na cloud, será necessário somente pressionar a tecla 't' para rodar o algoritmo de treinamento para que ele possa reconhecer o rosto do usuário e apresentar o seu nome.
![image](https://user-images.githubusercontent.com/40063504/103283159-88a01480-49b6-11eb-943f-748e6b21b0c8.png)


# Validando o cadastro via MySQL Workbench
Utilizamos o MySQL Workbench para validar que nosso usuário cadastrado foi realmente cadastrado com sucesso
![image](https://user-images.githubusercontent.com/40063504/103283248-c9982900-49b6-11eb-9211-f822b3fbb7fc.png)
