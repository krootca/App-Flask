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


@app.route("/", methods=["GET","POST"]) #Crea un link
def Index(): # Se ejecuta lo que esta adentro cuando entran al link
	return render_template("index.html") #Se ejecuta para visualizar la página.


@app.route("/login", methods=["GET","POST"])
def login():
	if 'emailXZK' in session:
		usuario=nameRETURN(escape(session["emailXZK"]))
		return render_template("home/home.html", user_name=usuario)
	else:
		if request.method == "POST":
			email=request.form.get('email');
			password=request.form.get('password');
			if password != None or email != None:
				AL=account_login(email=email, password=password)
				print(AL)
				print("-------------------------")
				if AL == None:
					return render_template("login/login.html", style_warning="text-warning text-red", text_warning="La cuenta no existe")
				elif AL == True and AL!=None:
						session['emailXZK']=email

						if "emailXZK" in session:
							return redirect('/home')
						else:
							return render_template("login/login.html", style_warning="text-warning text-red", text_warning="Ocurrió un error con coockies al logearse.")
				elif AL!=True and AL!=None:
					return render_template("login/login.html", style_warning="text-warning text-white", text_warning="Ocurrió un error al logearse.")
		return render_template("login/login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
	if request.method == "POST":

		user_name=request.form.get('user_name');
		user_surname=request.form.get('user_surname');
		email=request.form.get('email');
		password=request.form.get('password');
		telephone=request.form.get('telephone');
		direction=request.form.get('direction');
		age=request.form.get('age');

		if user_name!=None or user_surname!=None or email!=None or password!=None or telephone!=None or direction!=None or age!=None:
			
			signup=account_signup(user_name, user_surname, email, password, telephone, direction, age)
			if signup==True:
				return render_template("login/login.html", style_warning="text-warning text-green", text_warning="¡Gracias por suscribirte!.")
			else:
				return render_template("signup/signup.html", style_warning="text-warning text-red", text_warning="La cuenta no se pudo crear")

	return render_template("signup/signup.html", style_warning="text-warning text-white", text_warning="Registrarse")

@app.route("/home", methods=["GET","POST"])
def home():
	if 'emailXZK' in session:
		usuario=nameRETURN(escape(session["emailXZK"]))
		return render_template("home/home.html", user_name=usuario)
	else:
		return redirect("/login")

@app.route('/home', methods=["GET", "POST"])
def chat():
	if "emailXZK" in session:
		
		return render_template("/home/home.html", usuario=usuario)
	else:
		return redirect('/')


@app.route("/logout")
def logout():
	if "emailXZK" in session:
		session.pop("emailXZK", None)
		return redirect("/login")
	else:
		return redirect("/login")





@socketio.on('messageSER')
def message(msg):
	socketio.emit('messageCLI',msg, broascast=True)

@socketio.on('messageJOIN')
def CLIjoin(msg):
	socketio.emit('CLICREATEuser',msg, broascast=True)



if __name__ == "__main__":

	try:
		#Inicia la aplicación: http://127.0.0.1:2002
		socketio.run(app, host=ip, port=port, debug=True)
	except Exception as e: #Si hay un error, imprime en consola esto:
		print("------------------------------------------------------------")
		print("¡El servidor ha presentado un error!:\nhttp://"+ ip+ ":"+ str(port) )
		print("ERROR: ", e)
		print("------------------------------------------------------------")

