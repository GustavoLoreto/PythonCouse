
# 1) Programa que solicite al usuario los datos para
# calcular el area de un Cuadrado

#VARIABLES

int_Lado = 0
int_Area = 0

#Inicio de Programa

print("CALCULAR EL AREA DEL CUADRADO")

# SOLICITUD de Datos en PYTHON 2.7
# int_Lado = int(raw_input('Introduzca el valor del lado del cuadrado: '))

# SOLICITUD de Datos en PYTHON 3.x
int_Lado = int(input('Introduzca el valor del lado del cuadrado: '))

# AREA DEL CUADRADO
# Area = Lado ** 2
int_Area = int_Lado**2

print("El area del cuadrado es:  %d"%(int_Area))

