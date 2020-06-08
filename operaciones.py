import pandas as pd
from scipy import stats
import functools
import math

def obtenerDatos(data):
    valores = []
    for _, columnData in data.iteritems():
        print("Column Contents: ", columnData.values)
    valores = columnData.values
    return valores

def cantidadDatos(data):
    return data.size

def mediaMuestral(lista):
    suma = functools.reduce(lambda a, b: a + b, lista)
    print("Suma: ", suma)
    print(type(suma))
    return float(suma / len(lista))

def varianzaMuestral(lista, media):
    sumatoria = 0
    for valor in lista:
        sumatoria += (valor - media) ** 2
    return sumatoria / (len(lista) - 1)

def raizCuadrada(varianza):
    return math.sqrt(varianza)

def valorTablaZ(alfa):
    aux = alfa / 2
    return stats.norm.ppf(1 - aux)

def valorTablaT(alfa, n):
    aux = alfa / 2
    return stats.t.ppf(1 - aux, n - 1)

def procedimiento(valores, n, varianza_poblacional, alfa):
    if (n < 30):
        if varianza_poblacional == "":
            print("Usar t") # Uso el ejemplo del 10 de Febrero
            
            media_muestral = mediaMuestral(valores)
            
            valor_tabla_t = valorTablaT(alfa, n)
            
            cociente = raizCuadrada(varianzaMuestral(valores, media_muestral)) / raizCuadrada(n)
            
            lado_izquierdo = round(media_muestral - (valor_tabla_t * cociente), 4)
            lado_derecho = round(media_muestral + (valor_tabla_t * cociente), 4)
            
            intervalo = "{izq} < u < {der}".format(izq=lado_izquierdo, der=lado_derecho)
            return intervalo
        else:
            print("Usar z")

            media_muestral = mediaMuestral(valores)

            valor_tabla_z = valorTablaZ(alfa)

            cociente = raizCuadrada(varianza_poblacional) / raizCuadrada(n)

            lado_izquierdo = round(media_muestral - (valor_tabla_z * cociente))
            lado_derecho = round(media_muestral + (valor_tabla_z * cociente))

            intervalo = "{izq} < u < {der}".format(izq=lado_izquierdo, der=lado_derecho)
            return intervalo

    else:
        if varianza_poblacional == "":
            print("Usar z estimando varPobl con s^2")

            media_muestral = mediaMuestral(valores)

            valor_tabla_z = valorTablaZ(alfa)

            cociente = raizCuadrada(varianzaMuestral(valores, media_muestral)) / raizCuadrada(n)

            lado_izquierdo = round(media_muestral - (valor_tabla_z * cociente))
            lado_derecho = round(media_muestral + (valor_tabla_z * cociente))

            intervalo = "{izq} < u < {der}".format(izq=lado_izquierdo, der=lado_derecho)
            return intervalo
        else:
            print("Usar z")

            media_muestral = mediaMuestral(valores)

            valor_tabla_z = valorTablaZ(alfa)

            cociente = raizCuadrada(varianza_poblacional) / raizCuadrada(n)

            lado_izquierdo = round(media_muestral - (valor_tabla_z * cociente))
            lado_derecho = round(media_muestral + (valor_tabla_z * cociente))

            intervalo = "{izq} < u < {der}".format(izq=lado_izquierdo, der=lado_derecho)
            return intervalo

