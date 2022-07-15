#Ing Loreto.

"""
Distancia entre 2 puntos en el espacio 3D
► Enunciado:

Determine la distancia entre dos puntos en el espacio: (x1,y1, z1) y (x2, y2, z2).
La fórmula para hallar la distancia entre 2 puntos en el espacio es:

raiz (X2-X1)2 + (Y2 - Y1)2 + (Z2 - Z1)2 = d
Donde:

Coordenadas del Punto 1: (x1, y1, z1).

Coordenadas del Punto 2: (x2, y2, z2).

d: Distancia entre los 2 puntos.

___

► Variables:

Distancia: Distancia entre los 2 puntos.

x1: Coordenada X del Punto 1

y1: Coordenada Y del Punto 1

z1: Coordenada Z del Punto 1

x2: Coordenada X del Punto 2

y2: Coordenada Y del Punto 2

z2: Coordenada Z del Punto 2
"""
# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "DISTANCIA ENTRE 2 PUNTOS EN EL ESPACIO"
 
# Mensajes de Solicitud de Datos
SOLICITUD_X1 = ">>> Ingrese la coordenada x1: "
SOLICITUD_Y1 = ">>> Ingrese la coordenada y1: "
SOLICITUD_Z1 = ">>> Ingrese la coordenada z1: "
 
SOLICITUD_X2 = ">>> Ingrese la coordenada x2: "
SOLICITUD_Y2 = ">>> Ingrese la coordenada y2: "
SOLICITUD_Z2 = ">>> Ingrese la coordenada z2: "
 
# Mensajes de error
ERROR_FORMATO = "SOLO SE PERMITEN NUMEROS"
 
######################################################################
 
# Declaracion de variables
x1, y1, z1, x2, y2, z2, distancia = 0.0, 0.0, 0.0 ,0.0, 0.0, 0.0, 0.0
 
# Formato de Salida Final en Pantalla
Formato_Respuesta = "DISTANCIA: %4.2f"
 
######################################################################
 
# Encabezado del Programa
# Parte superior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
# Mensaje Centrado
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
# Separador de la tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
######################################################################
 
# Inicio del Programa:
try:
    x1 = float(input(SOLICITUD_X1)) 
    y1 = float(input(SOLICITUD_Y1)) 
    z1 = float(input(SOLICITUD_Z1)) 
 
    # Separador de la tabla
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    x2 = float(input(SOLICITUD_X2)) 
    y2 = float(input(SOLICITUD_Y2)) 
    z2 = float(input(SOLICITUD_Z2)) 
 
    #Calculo de la Distancia entre dos puntos A y B
    distancia = ((z2-z1)**2 + (y2-y1)**2 + (x2-x1)**2 )**0.5
 
    # Separador de la tabla
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    # Se muestra el mensaje en Pantalla
    print(Formato_Respuesta.center(ANCHO,RELLENO2) %(distancia))
 
except ValueError:
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print(ERROR_FORMATO.center(ANCHO,RELLENO2))
 
######################################################################
 
# Parte Inferior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))