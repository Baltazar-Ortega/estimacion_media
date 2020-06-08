import pandas as pd
from scipy import stats
import functools
import math

def vacio(string):
    if(string == ""):
        return True
    else:
        if(string.isspace()==True):
            return True
        else:
            return False

def valorTablaZ(alfa):
    aux = alfa / 2
    return stats.norm.ppf(1 - aux)

def valorTablaT(alfa, n):
    aux = alfa / 2
    return stats.t.ppf(1 - aux, n - 1)

def decision(t_muestra,media,varianza_m,varianza_p,alfa):
	t_muestra = float(t_muestra)
	media = float(media)
	alfa = float(alfa)
	if(varianza_p):
		s = math.sqrt(float(varianza_p))
	else:
		s = math.sqrt(float(varianza_m))
	if(t_muestra<30):
		if(varianza_p):
			#usar z
			print("Caso 1")
			tabla = valorTablaZ(alfa);
			s_raiz_n = s/math.sqrt(t_muestra)
		else:
			#usar t
			print("Caso 2")
			tabla = valorTablaT(alfa, t_muestra)
			s_raiz_n = s/math.sqrt(t_muestra)
	else:
		if(varianza_p):
			#usar z
			print("Caso 3")
			tabla=valorTablaZ(alfa);
			s_raiz_n=s/math.sqrt(t_muestra)
		else:
			#usar z estimando q2 con s2
			print("Caso 4")
			tabla=valorTablaZ(alfa);
			s_raiz_n = s/math.sqrt(t_muestra)
	resultado = operacion(media,tabla,s_raiz_n);
	return resultado;

def operacion(media,tabla,s_raiz_n):
	print(str(media) + " " + str(tabla) + " " + str(s_raiz_n))
	l_i = round(media - (tabla*s_raiz_n), 4)
	l_d = round(media + (tabla*s_raiz_n), 4)
	return str(l_i)+"<μ<"+str(l_d);

def permiso(t_muestra,media,alfa):
    if(vacio(t_muestra) == True or vacio(media) == True or vacio(alfa) == True):
        return False;
    else:
        return True;

def vacio(string):
    if(string==""):
        return True
    else:
        if(string.isspace() == True):
            return True
        else:
            return False