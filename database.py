#!/bin/python3
import sqlite3 #sqlite3 como base de datos
import random, re, time
#random para generar numeros aleatorios
#re para usar regex, expresiones regulares
#time para proporcionar al algoritmo información del sistema, fecha, hora

#regex o expresiones regulares
nick_re		= re.compile(r"^[a-zA-Z0-9]{4,12}$")
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
def createDB():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	cursor.execute("""CREATE TABLE "accounts" (
						"user_name"	TEXT NOT NULL,
						"user_surname"	TEXT NOT NULL,
						"email"	TEXT NOT NULL UNIQUE,
						"password"	TEXT NOT NULL,
						"phone"	INT NOT NULL UNIQUE,
						"direction"	TEXT NOT NULL,
						"age"	TEXT NOT NULL,
						"user_id"	INT NOT NULL UNIQUE);""")

	db_app.commit()	
	db_app.close()

def computerDB():
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

def createAllDB():

	createDB()
	computerDB()
	moveDB()
	incidentsDB()
	imagesDB()
#------------------------------------------------------------
try:
	createAllDB()
except Exception as e:
	pass

def return_all():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	try:
		datos=cursor.execute('SELECT * FROM accounts').fetchall()
		db_app.close()
		return datos
	except Exception as e:
		pass
def account_login(email, password): #true is ok # false is error with regular expretion # None is login failed
	for i in return_all():
		if str(email_re.search(email))!="None" and str(password_re.search(password))!="None":
			if email==i[2] and password == i[3]: #if email is a email
				return True
		else: #email or password is incorrect
			return False 



def account_signup(user_name, user_surname, email, password, telephone, direction, age):
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	if nameRETURN(email)==None and str(nick_re.search(user_name))!=None and str(nick_re.search(user_surname))!=None and str(email_re.search(email))!="None" and str(password_re.search(password))!="None" and str(tel_peru_re.search(telephone))!="None" and direction!=None and str(age_re.search(age)):
		user_id=random.randint(99999,99999999)
		content=[(user_name), (user_surname), (email), (password), (telephone), (direction), (age), (user_id)]
		cursor.execute("INSERT or IGNORE INTO accounts (user_name,user_surname, email, password, phone, direction, age, user_id) VALUES (?,?,?,?,?,?,?,?)",content)
		db_app.commit()
		db_app.close()
		return True
	else:
		db_app.close()
		return False

try:
	def nameRETURN(correo):
		db_app = sqlite3.connect("database.db", check_same_thread=False)
		cursor = db_app.cursor()
		account_data=cursor.execute('SELECT * FROM accounts ORDER BY _rowid_').fetchall()
		for i in account_data:
			if correo==i[2]:
				db_app.close()
				return i[0]
			elif correo==i[0]:
				db_app.close()
				return i[0]
		db_app.close()
except Exception as e:
	pass

def accountUPDATE(data_update, code_user, data_modific, password): #return True or None
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	for i in return_all():
		if  i[3]==str(password) and str(i[6])==str(code_user):
			cursor.execute("UPDATE accounts set {0}='{1}' where user_id='{2}'".format(data_modific, data_update, code_user))
			db_app.commit()
			db_app.close()
			return True

	db_app.close()

def registerComputer():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM computerDB').fetchall()
	db_app.close()
	return datos

def registerIncidents():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM incidentsDB').fetchall()
	db_app.close()
	return datos


def showComputer():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM computerDB').fetchall()
	db_app.close()
	return datos


def showIncidents():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM incidentsDB').fetchall()
	db_app.close()
	return datos


def showMove():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM moveDB').fetchall()
	db_app.close()
	return datos

def showImage():
	db_app = sqlite3.connect("database.db", check_same_thread=False)
	cursor = db_app.cursor()
	datos=cursor.execute('SELECT * FROM imagesDB').fetchall()
	db_app.close()
	return datos

#--- example ----
THENAME="Mark"
THESURNAME="Akernan"
EMAIL="markaker@example.com"
PASSWORD="passsword"
TEL="+51568368475"
DIRECTION="EEUU, New York"
FECHA = time.localtime()
#----------------
