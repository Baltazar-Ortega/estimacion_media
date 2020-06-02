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