#Ing Loreto.

# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "NUMERO FACTORIAL"
 
# Mensajes de Solicitud de Datos
SOLICITUD_TERMINO = ">>> Introduce el numero a calcular: "
 
######################################################################
 
# Declaracion de variables
numero = 0
 
# Formato de Salida Final en Pantalla
Formato_Respuesta = ">>> %d! = %d"
 
######################################################################
 
# Encabezado del Programa
# Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
# Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
######################################################################
 
# Declaracion de funciones
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
 
######################################################################
 
# Inicio del Programa:
numero = int(input(SOLICITUD_TERMINO))
 
# Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
for numero in range(0, numero+ 1):
    print(Formato_Respuesta %(numero, factorial(numero)))
 
######################################################################
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))