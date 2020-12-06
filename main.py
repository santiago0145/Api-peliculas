# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


usuariosregistrados = [{"nombres": "eddy", "documento": "100", "correo": "admin","password":"123"}]

@app.route ('/')
def index ():
    return render_template( 'index.html' )

@app.route('/usuarios', methods=['GET'])
def usuarios():
    return jsonify({"datos": usuariosregistrados}), 200
    
@app.route('/consultarusuario', methods=['POST'])
def usuariosdatos():
    #id = request.args.get('id')
    content = request.get_json()
    #
    correo = content["correo"]
    password = content["password"]
    n=len(usuariosregistrados)
    validor=0
    print(correo)
    print(password)
    for i in range(n):
        if(correo == usuariosregistrados[i]['correo'] and password==usuariosregistrados[i]['password']):
            validor = 1
            #return jsonify({"datos": "correcto"}), 200
    if(validor == 1):
        validor=0
        return jsonify({"datos": "Datos ingresados correctamente"}), 200
        #print("datos ingresados correctamente")
    else:
        validor=0
        #print("datos ingresados incorrectamente")
        return jsonify({"datos":"Datos ingresados incorrectamente"}), 200



@app.route('/registro', methods=['POST'])
def formulario():
    content = request.get_json()
    nombres = content['nombres']
    documento = content['documento']
    correo = content['correo']
    passwordd = content['password']
    usuariosregistrados.append({"nombres": nombres, "documento": documento, "correo": correo, "password": passwordd})
    return jsonify({"status": "Registro Exitoso"}), 200
    
app.run(debug = True, port=5000)