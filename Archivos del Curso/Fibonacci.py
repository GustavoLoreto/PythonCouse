#Ing Loreto.

# Valores para Dibujar la Tabla
ANCHO = 45
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "SUCESION DE FIBONACCI"
 
# Mensajes de Solicitud de Datos
SOLICITUD_TERMINO = ">>> Introduce el valor deL termino 'n': "
 
######################################################################
 
# Declaracion de variables
termino_n = 0
 
# Formato de Salida Final en Pantalla
Formato_Respuesta = ">>> F(%02d) = %02d"
 
######################################################################
 
# Encabezado del Programa
# Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
# Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
######################################################################
 
# Declaracion de funciones:
def fibonacci(numero):
    if(numero == 0):
        return 0
    elif(numero == 1):
        return 1
    else:
        # Retorna la suma de los dos terminos anteriores
        return (fibonacci(numero - 2) + fibonacci(numero - 1))
 
######################################################################
 
# Inicio del Programa:
# Solicitud de Datos en PYTHON 2.7
# termino_n = int(raw_input(SOLICITUD_TERMINO))
 
# Solicitud de Datos en PYTHON 3
termino = int(input(SOLICITUD_TERMINO))
 
# Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
for termino in range(0, termino + 1):
    # Se muestra el mensaje en Pantalla
    print(Formato_Respuesta %(termino,fibonacci(termino)))
 
######################################################################
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))