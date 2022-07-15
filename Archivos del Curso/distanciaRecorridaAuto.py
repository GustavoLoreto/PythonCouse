#Ing Loreto.


# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "DISTANCIA DE UN MOVIL"
 
# Mensajes de solicitud de Datos
SOLICITAR_VELOCIDAD = ">>> Ingrese la Velocidad : "
SOLICITAR_TIEMPO = ">>> Ingrese el Tiempo    : "
 
# Mensajes de Error
ERROR_FORMATO = "SOLO SE PERMITEN NUMEROS"
 
######################################################################
 
# Declaracion de variables
f_velocidad, f_distancia  = 0.0, 0.0
i_tiempo = 0
 
# Formato de Salida Final en Pantalla
s_formato_respuesta = "DISTANCIA: %0.1f Metros"
 
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
    f_velocidad = float(input(SOLICITAR_VELOCIDAD))
    i_tiempo = int(input(SOLICITAR_TIEMPO))
 
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    # Formula para calcular Distancia
    # Distancia = Velocidad x Tiempo
 
    f_distancia = f_velocidad * i_tiempo
 
    # Se muestra el mensaje en Pantalla
    print(s_formato_respuesta.center(ANCHO,RELLENO2) %(f_distancia))
 
except ValueError:
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print(ERROR_FORMATO.center(ANCHO,RELLENO2))
 
######################################################################
 
print(CADENA_VACIA.center(ANCHO,RELLENO1))