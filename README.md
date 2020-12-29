# Registration form with RDS AWS database and facial recognition via OpenCV
The algorithm performs a simple user registration (Name, CPF, E-mail and Telephone) in an Amazon RDS database and also performs the storage, training and facial recognition of the user's face to identify the users already registered in the system in a next time the user is seen.

# Requirements
You will need to install the libraries below:

- numpy
- OpenCV
- mysql-connector

## Creating RDS-MySQL instance on AWS
- Access the "AWS Management Console"
- Open the services menu and select the RDS option
- Select the "Create database" option
- Select MySQL
- Version: MySQL 8.0.11
-> Free tier
- Enter the basic data, username and password:

db instance: "database name"

username: "your username"

password: "your password"

- DB instance size and Storage is default not to mess
- VPC: Default
- Subnet group: default
- Public access: Yes
- VPC security group: Create new

New VPC security group name: <enter_com_the_name>

- Availability Zone: choose where you are connected


# Operation
When the code is run, the menu below will be presented with the options for registration and identification:
![image](https://user-images.githubusercontent.com/40063504/103282211-d6674d80-49b3-11eb-8b8c-84fc54b6c73f.png)

## Option 1
If option 1 is selected, some fields will be presented for filling in the new registration as shown below:
![image](https://user-images.githubusercontent.com/40063504/103282344-3bbb3e80-49b4-11eb-8720-9faa71b78780.png)

After completing the new registration in our database, the face recognition screen will be presented.![image](https://user-images.githubusercontent.com/40063504/103282395-673e2900-49b4-11eb-8db4-0c012b900b25.png)

On this screen we have the option to register a new user photo (space key), perform the training (letter t), or log out (letter q). Pressing the 'space' key on the keyboard, we will capture the photos to perform the training later.
![image](https://user-images.githubusercontent.com/40063504/103282503-c865fc80-49b4-11eb-877b-423246d026ce.png)

By pressing 'space' a folder will be created called 'USER' and inside it will be created a folder with the name previously registered, inside that folder will be stored all the photos of the user that we just registered. In the case of a new registration, another folder will be created automatically with the name registered within the 'USER' folder.
![image](https://user-images.githubusercontent.com/40063504/103282688-4fb37000-49b5-11eb-9497-9a6432d2c241.png)

Now the time has come to carry out the training of our algorithm for it to recognize the registered user through the photos taken. To do this, press the 't' key on the same screen where we took the capture. The algorithm will be trained and the name of the registered user will be presented directly in the facial recognition layer.
![image](https://user-images.githubusercontent.com/40063504/103282855-c2245000-49b5-11eb-90b8-32ddf0cf4381.png)


## Option 2
When the code is run, the menu below will be presented with the options for registration and identification:
![image](https://user-images.githubusercontent.com/40063504/103282211-d6674d80-49b3-11eb-8b8c-84fc54b6c73f.png)

If option 2 is selected, the face recognition screen will be presented to the user.
![image](https://user-images.githubusercontent.com/40063504/103283063-5098d180-49b6-11eb-8bdb-1bf3fbd03b2d.png)

As in this case we already have our user registered in our database in the cloud, it will only be necessary to press the 't' key to run the training algorithm so that he can recognize the user's face and present his name.
![image](https://user-images.githubusercontent.com/40063504/103283159-88a01480-49b6-11eb-943f-748e6b21b0c8.png)

# Validating the registration via MySQL Workbench
We use MySQL Workbench to validate that our registered user was successfully registered
![image](https://user-images.githubusercontent.com/40063504/103283248-c9982900-49b6-11eb-9211-f822b3fbb7fc.png)
