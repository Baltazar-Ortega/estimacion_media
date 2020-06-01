from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/teoria')
def teoria():
    return render_template('teoria.html')

@app.route('/subirExcel')
def subirExcel():
    return render_template('subirExcel.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['archivo-subido']
        data = pd.read_excel(file)
        
        # Preguntar alfa (usar un select con 0.01 y 0.05)
        # Obtener n
        # Preguntar si se conoce varianza de la poblacion

        # Obtener xBarra, s, lo que se necesite
        return render_template('data.html', data=data.to_html())


if __name__ == '__main__':
    print("Version de pandas: ", pd.__version__)
    app.run(debug=True)