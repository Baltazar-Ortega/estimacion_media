from flask import Flask, render_template, request, redirect, url_for
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
    if((vacio(varianza_m)==False and vacio(varianza_p)==False) or (vacio(varianza_m)==True and vacio(varianza_p)==True)):
        return render_template('Error.html')
    else:
        #Verifico que los demas no esten vacios
        if(permiso(t_muestra,media,alfa)==True):
            #hay que convertirlos a numeros, son strings
            resultado=opse.decision(t_muestra,media,varianza_m,varianza_p,alfa)
            return render_template('resultadoSinExcel.html',intervalo=resultado)
        else:
            return render_template('Error.html')

def permiso(t_muestra,media,alfa):
    if(vacio(t_muestra)==True or vacio(media)==True or vacio(alfa)==True):
        return False;
    else:
        return True;

def vacio(string):
    if(string==""):
        return True
    else:
        if(string.isspace()==True):
            return True
        else:
            return False

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['archivo-subido']
        data = pd.read_excel(file)

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

        intervalo = procedimiento(valores, n, varianza_poblacional, alfa)

        return render_template('resultadoExcel.html', data=data.to_html(), intervalo=intervalo)

def procedimiento(valores, n, varianza_poblacional, alfa):
    if (n < 30):
        if varianza_poblacional == "":
            print("Usar t") # Uso el ejemplo del 10 de Febrero
            
            media_muestral = op.mediaMuestral(valores)
            
            valor_tabla_t = op.valorTablaT(alfa, n)
            
            cociente = op.raizCuadrada(op.varianzaMuestral(valores, media_muestral)) / op.raizCuadrada(n)
            
            lado_izquierdo = round(media_muestral - (valor_tabla_t * cociente), 4)
            lado_derecho = round(media_muestral + (valor_tabla_t * cociente), 4)
            
            intervalo = "{izq} < u < {der}".format(izq=lado_izquierdo, der=lado_derecho)
            print(intervalo)
            return intervalo
        else:
            print("Usar z")

            media_muestral = op.mediaMuestral(valores)

            valor_tabla_z = op.valorTablaZ(alfa)

            cociente = op.raizCuadrada(varianza_poblacional) / op.raizCuadrada(n)

            lado_izquierdo = round(media_muestral - (valor_tabla_z * cociente))
            lado_derecho = round(media_muestral + (valor_tabla_z * cociente))

            intervalo = "{izq} < u < {der}".format(izq=lado_izquierdo, der=lado_derecho)
            print(intervalo)
            return intervalo

    else:
        if varianza_poblacional == "":
            print("Usar z estimando varPobl con s^2")

            media_muestral = op.mediaMuestral(valores)

            valor_tabla_z = op.valorTablaZ(alfa)

            cociente = op.raizCuadrada(op.varianzaMuestral(valores, media_muestral)) / op.raizCuadrada(n)

            lado_izquierdo = round(media_muestral - (valor_tabla_z * cociente))
            lado_derecho = round(media_muestral + (valor_tabla_z * cociente))

            intervalo = "{izq} < u < {der}".format(izq=lado_izquierdo, der=lado_derecho)
            print(intervalo)
            return intervalo
        else:
            print("Usar z")

            media_muestral = op.mediaMuestral(valores)

            valor_tabla_z = op.valorTablaZ(alfa)

            cociente = op.raizCuadrada(varianza_poblacional) / op.raizCuadrada(n)

            lado_izquierdo = round(media_muestral - (valor_tabla_z * cociente))
            lado_derecho = round(media_muestral + (valor_tabla_z * cociente))

            intervalo = "{izq} < u < {der}".format(izq=lado_izquierdo, der=lado_derecho)
            print(intervalo)
            return intervalo




if __name__ == '__main__':
    print("Version de pandas: ", pd.__version__)
    app.run(debug=True)