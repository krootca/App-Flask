#!/bin/python3
import sqlite3 #sqlite3 como base de datos
import random, re, time
#random para generar numeros aleatorios
#re para usar regex, expresiones regulares
#time para proporcionar al algoritmo información del sistema, fecha, hora

#regex o expresiones regulares
nick_re		= re.compile(r"^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð,.'-]{4,14}$")
age_re		= re.compile(r'^((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])$')
email_re	= re.compile(r"\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b")
password_re	= re.compile(r"^[a-zA-Z0-9\W\w]{7,30}$")
url_re 		= re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")
ip_re		= re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
profile_re	= re.compile(r"^(images)/([a-zA-Z0-9\W]{1,60})+\.(webp|jpeg|png|jpg)$")
tel_peru_re	= re.compile(r"^.+(51)([0-9\w]{9})$")
direction_re= re.compile(r"^[a-zA-Z0-9]{3,30}$")
#---------
#-------------CREATE ALL DB----------
def createDB(): #Crea la primera base de datos
	db_app = sqlite3.connect("database.db", check_same_thread=False) #Crea un archivo database.db
	cursor = db_app.cursor() #sirve para crear algoritmos de bases de datos
	cursor.execute("""CREATE TABLE "accounts" (
						"user_name"	TEXT NOT NULL,
						"user_surname"	TEXT NOT NULL,
						"email"	TEXT NOT NULL UNIQUE,
						"password"	TEXT NOT NULL,
						"phone"	INT NOT NULL UNIQUE,
						"direction"	TEXT NOT NULL,
						"age"	TEXT NOT NULL,
						"user_id"	INT NOT NULL UNIQUE);""")

	db_app.commit()	 # guarda lo creado
	db_app.close()

def computerDB(): #lo mismo que arriba pero con otros datos para crear
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	cursor.execute("""CREATE TABLE "computerDB" (
						"codigo"	TEXT NOT NULL,
						"nombre_equipo"	TEXT NOT NULL,
						"marca"	TEXT NOT NULL,
						"modelo"	TEXT NOT NULL,
						"estado"	TEXT NOT NULL,
						"observacion"	TEXT NOT NULL,
						"transferencia"	TEXT NOT NULL,
						"stock"	TEXT NOT NULL,
						"area" TEXT NOT NULL,
						"user_id" TEXT NOT NULL,
						"producto_id" TEXT NOt NULL);""")

	db_app.commit()	
	db_app.close()

def moveDB():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	cursor.execute("""CREATE TABLE "moveDB" (
						"codigo"	TEXT NOT NULL,
						"marca"	TEXT NOT NULL,
						"nombre_equipo"	TEXT NOT NULL,
						"precio"	TEXT NOT NULL,
						"estado"	TEXT NOT NULL,
						"modelo"	TEXT NOT NULL,
						"observacion"	TEXT NOT NULL,
						"fecha_salida"	TEXT NOT NULL,
						"fecha_ingreso"	TEXT NOT NULL,
						"area" TEXT NOT NULL,
						"user_id" TEXT NOT NULL,
						"producto_id" TEXT NOt NULL);""")

	db_app.commit()	
	db_app.close()

def incidentsDB():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	cursor.execute("""CREATE TABLE "incidentsDB" (
						"codigo"	TEXT NOT NULL,
						"marca"	TEXT NOT NULL,
						"nombre_equipo"	TEXT NOT NULL,
						"precio"	TEXT NOT NULL,
						"estado"	TEXT NOT NULL,
						"modelo"	TEXT NOT NULL,
						"observacion"	TEXT NOT NULL,
						"fecha_compra"	TEXT NOT NULL,
						"tecnico"	TEXT NOT NULL,
						"area" TEXT NOT NULL,
						"user_id" TEXT NOT NULL,
						"producto_id" TEXT NOt NULL);""")

	db_app.commit()	
	db_app.close()

def imagesDB():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	cursor.execute("""CREATE TABLE "imagesDB" (
						"url"	TEXT NOT NULL,
						"marca"	TEXT NOT NULL,
						"nombre_equipo"	TEXT NOT NULL,
						"user_id" TEXT NOT NULL,
						"producto_id" TEXT NOt NULL);""")

	db_app.commit()	
	db_app.close()

def createAllDB(): # esta funcion solo crea todas las bases de datos

	createDB()
	computerDB()
	moveDB()
	incidentsDB()
	imagesDB()
#------------------------------------------------------------
try: # intenta crear las bases de datos, pero si no lo logra no hace nada, sirve para que al momento de correr el archivo, cree la base de datos, si ocurre un error, no dice nada
	createAllDB() 
except Exception as e:
	pass

def return_all(): #retorna todos los datos de la base de datos
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	try:
		datos=cursor.execute('SELECT * FROM accounts').fetchall()
		db_app.close()
		return datos #aqui retorna todo
	except Exception as e: # si no funciona no hace nada
		pass
def account_login(email, password): #sirve para logearse, si el password y el email existe, retorna true, si no, retorna false
	for i in return_all():
		if str(email_re.search(email))!="None" and str(password_re.search(password))!="None":
			if email==i[2] and password == i[3]: #if email is a email
				return True
		else: #email or password is incorrect
			return False 

def cityVerific(direction): # sirve para verificar datos
	try:
		if int(direction)==1: #si la dirección es igual a 1, la dirección toma el valor de "Peru, Lima" siguiendo así con los otros
			direction="Peru, Lima"
			return direction #Luego retorna el valor
		elif int(direction)==2:
			direction="Peru, Cusco"
			return direction
		elif int(direction)==3:
			direction="Peru, Puno"
			return direction
		elif int(direction)==4:
			direction="Peru, Junin"
			return direction
		elif (direction)==5:
			direction="Peru, Piura"
			return direction
		else:
			direction="Peru, Lima"
			return direction #si ninguno coincide, entonces solo retorna Peru, Lima
	except Exception as e:
		return "Peru, Lima" # si el valor introducido es erroneo, como colocar algo extraño, retorna "Peru, Lima"

def account_signup(user_name, user_surname, email, password, telephone, direction, age): #para registrarse
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	#si los valores de un numero es None significa que no existe un numero, lo que es admitible, pues un numero debe ser unico
	# si el email no existe en la base de datos, es admitible, por que debe ser unico
	# luego con ayuda de regex o expresiones regulares, si los otros datos son diferentes de "None", son correctos y admitibles
	#Si todo el condicional retorna True, entra al condicional para insertar los datos a la base de datos

	if numerRETURN(email)==None and nameRETURN(email)==None and str(nick_re.search(user_name))!="None" and str(nick_re.search(user_surname))!="None" and str(email_re.search(email))!="None" and str(password_re.search(password))!="None" and str(tel_peru_re.search(telephone))!="None" and direction!="None" and str(age_re.search(age))!="None":
		user_id=random.randint(99999,99999999) #crea un id con ayuda de un modulo random
		content=[(user_name), (user_surname), (email), (password), (telephone), (cityVerific(direction)), (age), (user_id)]
		cursor.execute("INSERT or IGNORE INTO accounts (user_name,user_surname, email, password, phone, direction, age, user_id) VALUES (?,?,?,?,?,?,?,?)",content)
		db_app.commit() #guarda
		db_app.close() #cierra la conexión
		return True #retorna true
	else:
		db_app.close() #si el condicional no es correcto, por que la persona no ingresó datos correctos, cierra la conexión, y retorna false
		return False

def nameRETURN(correo): #esto solo retorna el nombre
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	account_data=cursor.execute('SELECT * FROM accounts ORDER BY _rowid_').fetchall()
	for i in account_data: #en un bucle recorre los datos para verificar si el email es igual a uno que exisa
		if correo==i[2]: #si existe
			db_app.close() #cierra la base de datos
			return i[0]  #retorna el nombre a la cual el correo esté conectado
		else: #si no, no retorna None
			db_app.close()
			pass

def numerRETURN(correo): #Basicamente es el mismo al de arriba
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	account_data=cursor.execute('SELECT * FROM accounts ORDER BY _rowid_').fetchall()
	for i in account_data:
		if correo==i[2]: # corre el bucle y determina si el correo es igual a uno que exista
			db_app.close()
			return i[4] #retorna el numero
		else:
			db_app.close() #si no existe retorna None y cierra la conexión
			pass


def accountUPDATE(data_update, code_user, data_modific, password): #esto es para actualizar los datos de la cuenta
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	for i in return_all(): #recorre los datos
		if  i[3]==str(password) and str(i[6])==str(code_user): #verifica si el correo y la contraseña son correctos
			cursor.execute("UPDATE accounts set {0}='{1}' where user_id='{2}'".format(data_modific, data_update, code_user)) #modifica los datos
			db_app.commit()
			db_app.close()
			return True

	db_app.close()

def registerComputer(): #recorre los datos de la tabla computerDB
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM computerDB').fetchall()
	db_app.close()
	return datos

def registerIncidents(): #igual que el de arriba pero con incidentsDB
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM incidentsDB').fetchall()
	db_app.close()
	return datos


def showComputer(): #igual que el de arriba
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM computerDB').fetchall()
	db_app.close()
	return datos


def showIncidents(): #igual que el de arriba
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM incidentsDB').fetchall()
	db_app.close()
	return datos


def showMove(): #igual que el de arriba
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM moveDB').fetchall()
	db_app.close()
	return datos

def showImage(): #igual que el de arriba
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM imagesDB').fetchall()
	db_app.close()
	return datos


def deleteAccounts(email, password): # elimina una cuenta
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	for i in return_all():
		if str(email_re.search(email))!="None" and str(password_re.search(password))!="None": #verifica si el correo y el usuario existan
			if email==i[2] and password == i[3]: #if email is a email
				datos=cursor.execute('DELETE FROM accounts WHERE email = "{0}";'.format(email)) # si existe, lo elimina
				db_app.commit()
				db_app.close()
				return True
		else:
			db_app.close()
			return False 
