from flask import Flask, flash, render_template, request, redirect, url_for
import os
import pandas as pd
import operaciones as op
import operacionesSinExcel as opse

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/teoria')
def teoria():
    return render_template('teoria.html')

@app.route('/sinExcel')
def sinExcel():
    return render_template('sinExcel.html')

@app.route('/subirExcel')
def subirExcel():
    return render_template('subirExcel.html')

@app.route('/datosSinExcel', methods=['POST'])
def datosSinExcel():
    t_muestra = request.form['t_muestra'];
    media = request.form['media'];
    varianza_m = request.form['varianza_m'];
    varianza_p = request.form['varianza_p'];
    alfa = request.form['inlineRadioOptions'];
    print("El alfa fue"+alfa)
    #Primero checo que no esten ambos llenos o vacios, es prioridad esta condicion, solo uno de los dos (el caso de "else") debe estar lleno
    if((opse.vacio(varianza_m)==False and opse.vacio(varianza_p)==False) or (opse.vacio(varianza_m)==True and opse.vacio(varianza_p)==True)):
        return render_template('Error.html')
    else:
        #Verifico que los demas no esten vacios
        if(opse.permiso(t_muestra,media,alfa)==True):
            #hay que convertirlos a numeros, son strings
            resultado = opse.decision(t_muestra,media,varianza_m,varianza_p,alfa)
            return render_template('resultadoSinExcel.html',intervalo=resultado)
        else:
            return render_template('Error.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        

        print("Request files: ", request.files['archivo-subido'])

        nombre_archivo = request.files['archivo-subido'].filename

        if nombre_archivo == "":
            return render_template('subirExcel.html', msg_error="Error: No introdujo archivo", error=True)

        try:
            data = pd.read_excel(nombre_archivo)
        except Exception as e:
            return render_template('subirExcel.html', msg_error="Error con el archivo. Siga las instrucciones", error=True)

        valores = op.obtenerDatos(data)
        n = int(len(valores))

        varianza_poblacional = request.form['varianza']

        if varianza_poblacional == "":
            print("Varianza_poblacional no conocida")
        else:
            varianza_poblacional = float(varianza_poblacional)
            print("Varianza_poblacional: ", varianza_poblacional)

        alfa = float(request.form['inlineRadioOptions'])
        print("Alfa: ", alfa)

        intervalo = op.procedimiento(valores, n, varianza_poblacional, alfa)

        return render_template('resultadoExcel.html', data=data.to_html(), intervalo=intervalo)



if __name__ == '__main__':
    print("Version de pandas: ", pd.__version__)
    app.run(debug=True)