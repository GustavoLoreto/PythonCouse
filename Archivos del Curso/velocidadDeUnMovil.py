#Ing Loreto.

# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "VELOCIDAD DE UN MOVIL"
 
# Mensajes de Solicitud de Datos
SOLICITAR_DISTANCIA  = ">>> Ingrese la Distancia : "
SOLICITAR_TIEMPO  = ">>> Ingrese el Tiempo    : "
 
# Mensajes de error
ERROR_FORMATO = "SOLO SE PERMITEN NUMEROS"
ERROR_ZERO_DIVISION = "NO SE PERMITE LA DIVISION ENTRE 0."
 
######################################################################
 
# Declaración de variables
f_velocidad = 0.0
f_distancia = 0.0
i_tiempo = 1
 
# Formato de Salida Final en Pantalla
s_formato_respuesta = "VELOCIDAD: %0.1f (m/s)"
 
######################################################################
 
# Encabezado del Programa
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
######################################################################
 
# Inicio del Programa:
try:
    #SOLICITUD de Datos en PYTHON 2.7
    # f_velocidad = float(raw_input("Ingrese la Velocidad : ") )
    # i_tiempo = int(raw_input("Ingrese el Tiempo    : ") )
 
    #SOLICITUD de Datos en PYTHON 3
    f_distancia= float(input(SOLICITAR_DISTANCIA))
    i_tiempo = int(input(SOLICITAR_TIEMPO))
 
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    # Formula para calcular Distancia
    # Distancia = Velocidad x Tiempo
 
    f_velocidad = f_distancia / i_tiempo
 
    # Se muestra el mensaje en Pantalla
    print(s_formato_respuesta.center(ANCHO,RELLENO2) %(f_velocidad))
 
except ZeroDivisionError:
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print(ERROR_ZERO_DIVISION)
 
except ValueError:
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print(ERROR_FORMATO)
 
######################################################################
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))
