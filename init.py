from flask import Flask, flash, render_template, request, redirect, url_for, abort, session, escape, make_response, send_from_directory #el modulo de Flask

from flask_socketio import SocketIO, send, emit #Usaremos socket.io

import random,time,os #El modulo random, para obtener numeros aleatorios, time
# para obtener las horas, y os, para ejecutar código en el SO
from database import *
#-------------
#lo de arriba son módulos.
#-------------
#lo de abajo es el algoritmo en si.
#---------
ip="127.0.0.1" #la ip
port=2021 #el puerto
#---------


app=Flask(__name__) #la aplicación
socketio = SocketIO(app) #socketio
app.secret_key="secret_key" #un código secreto, para realizar peticiones GET, POST


@app.route("/", methods=["GET","POST"]) #Crea un link y admite los metodos get y post
def Index(): # Se ejecuta lo que esta adentro cuando entran al link
	return render_template("index.html") #Se ejecuta para visualizar la página.


@app.route("/login", methods=["GET","POST"])#Crea un link y admite los metodos get y post
def login(): #si entran al link /login ejecuta el contenido de la función 
	if 'emailXZK' in session: #verifica si existe un coockie
		usuario=nameRETURN(escape(session["emailXZK"])) #si existe, usuario toma valor del coockie que es un nombre de usuario
		return render_template("home/home.html", user_name=usuario) #muestra la pagina html y envía una variable en el html
	else:
		if request.method == "POST": # si no existe el coockie, este condicional espera a que se envien metodos http post
			email=request.form.get('email'); #si se envian entra al condicional, obteniendo datos del <form>
			password=request.form.get('password'); #obtiene datos del email y password
			if password != None or email != None: #este condicional verifica si password y email son diferentes de None, si lo son, entra al condicional
				AL=account_login(email=email, password=password) #envía datos a la base de datos, la función account_login en database.py para logearse
				if AL == None: # si la función retorna None simplemente renderiza nuevamente la pagina del login con un mensaje que dice la cuenta no existe
					return render_template("login/login.html", style_warning="text-warning text-red", text_warning="La cuenta no existe")
				elif AL == True and AL!=None: #si es correcto, crea un coockie que es como una variable que toma valor el email
						session['emailXZK']=email

						if "emailXZK" in session: #si el coockie existe, osea que si se ha creado, nos envía a la función home redireccionandonos al link
							return redirect('/home')
						else: #si no existe el coockie renderiza nuevamente el login con otro mensaje
							return render_template("login/login.html", style_warning="text-warning text-red", text_warning="Ocurrió un error con coockies al logearse.")
				elif AL!=True and AL!=None: #si al es diferente de True o None renderiza el login por que ha ocurrido un error inesperado
					return render_template("login/login.html", style_warning="text-warning text-white", text_warning="Ocurrió un error al logearse.")
		return render_template("login/login.html") #saliendo fuera del condicional de los metodos http, renderiza el login

@app.route("/signup", methods=["GET","POST"])#Crea un link y admite los metodos get y post
def signup(): 
	if request.method == "POST": #espera a que se envíe el metodo http post

		user_name=request.form.get('user_name'); #obtiene valor de los formularios, en este caso  el name del input del form que tiene como valor user_name
		user_surname=request.form.get('user_surname'); #lo mismo para los otros
		email=request.form.get('email');
		password=request.form.get('password');
		telephone=request.form.get('telephone');
		direction=request.form.get('direction');
		age=request.form.get('age');

		#este condicional solo verifica que los datos no estén vacios, si no lo están, retorna True y accede al condicional
		#Si crees que esto solo se resuelve con js, estás equivocado, por que el js, se puede bloquear o simplemente cambiar valores

		if user_name!=None or user_surname!=None or email!=None or password!=None or telephone!=None or direction!=None or age!=None:
			
			signup=account_signup(user_name, user_surname, email, password, telephone, direction, age) #envía los datos a la función account_signup en database.py
			if signup==True: #si signup  la función retorna True, accede a este condicional
				#renderiza el login con un mensaje
				return render_template("login/login.html", style_warning="text-warning text-green", text_warning="¡Gracias por suscribirte!.")
			else: #si signup retorna False o None, renderiza el signup
				return render_template("signup/signup.html", style_warning="text-warning text-red", text_warning="La cuenta no se pudo crear")

	return render_template("signup/signup.html", style_warning="text-warning text-white", text_warning="Registrarse")
	#fuera del condicional del metodo http, GET POST, renderiza signup

@app.route("/home", methods=["GET","POST"])#Crea un link y admite los metodos get y post
def home(): 
	if 'emailXZK' in session: #comprueba si existe un coockie
		usuario=nameRETURN(escape(session["emailXZK"])) # obtiene el nombre del usuario utilizando la coockie y una función
		return render_template("home/home.html", user_name=usuario) #renderiza home con el nombre de usuario 
	else:
		return redirect("/login") #si no existe coockie, nos envía al login para logearnos


@app.route("/logout")#si acceden a este link ejecuta la función logout eliminando los coockies
def logout():
	if "emailXZK" in session:
		session.pop("emailXZK", None)
		return redirect("/login")
	else:
		return redirect("/login")



if __name__ == "__main__":

	try:
		#Inicia la aplicación: http://127.0.0.1:2002
		socketio.run(app, host=ip, port=port, debug=True)
	except Exception as e: #Si hay un error, imprime en consola esto:
		print("------------------------------------------------------------")
		print("¡El servidor ha presentado un error!:\nhttp://"+ ip+ ":"+ str(port) )
		print("ERROR: ", e)
		print("------------------------------------------------------------")

