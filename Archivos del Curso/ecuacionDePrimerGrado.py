#Ing Loreto.
"""
Ecuación de Primer Grado
► Enunciado:

Crear un Algoritmo que permita hallar la solución a una ecuación de primer grado, de la forma: ax + b = 0

El objetivo es despejar la x y validar los posibles datos para arrojar la respuesta.

Al despejar la x tendremos que:

x = -b/a

Por lo tanto tendremos los siguientes escenarios:

1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.

2) Si a es IGUAL a 0 (a == 0) tendremos que:

Si b es DIFERENTE de 0 (b != 0) la ecuación no tiene solución.

Si b es IGUAL a 0 (b == 0) la ecuación tiene Infinitas Soluciones.

___

► Variables:

a: Coeficiente principal.

b: Término Independiente.

x: Incógnita.

___

► Datos de Prueba.

a) a = 2 y b = 6.

b) a = 0 y b = 3.

c) a = 0 y b = 0.

___

► Salida:

----------------------------------------
  ECUACION DE PRIMER GRADO: ax + b = 0  
----------------------------------------
>>> Valor de a: 2
>>> Valor de b: 6
----------------------------------------
ECUACION: 2.0 x + 6.0 = 0
----------------------------------------
>>> SOLUCION: x =  -3.0
----------------------------------------
"""
# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
MENSAJE_INICIAL = "ECUACION DE PRIMER GRADO: ax + b = 0"
 
######################################################################
 
# Declaracion de variables
a = 0 # Coeficiente principal
b = 0 # Termino Independiente
x = 0 # Incognita
 
# Formato de Salida Final en Pantalla
Formato_Ecuacion = "ECUACION: {} x + {} = 0"
 
######################################################################
 
# Encabezado del Programa
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
######################################################################
 
# Inicio del Programa:
a = float(input(">>> Valor de a: "))
b = float(input(">>> Valor de b: "))
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(Formato_Ecuacion.format(a,b))
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
try:
    x = -b/a
    print(">>> SOLUCION: x = ", x)
except:
    if b != 0:
        print("La ECUACION no tiene solucion.")
    else:
        print("La ECUACION tiene infinitas soluciones.")
 
######################################################################
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))

