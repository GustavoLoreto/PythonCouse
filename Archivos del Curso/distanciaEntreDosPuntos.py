#Ing Loreto.
"""
Distancia entre 2 Puntos en el Plano

Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano, elabore el algoritmo que permita obtener la distancia entre A y B.
Un punto en el plano tiene dos coordenadas (X ,Y), entonces el punto A tendrá sus coordenadas (AX, AY) y el punto B de manera similar (BX, BY).
► Variables:

D  : Distancia entre los 2 puntos.

Ax: Coordenada X del Punto A.

Ay: Coordenada Y del Punto A.

Bx: Coordenada X del Punto B.

By: Coordenada X del Punto B.
"""





# Valores para Dibujar la Tabla
ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "DISTANCIA ENTRE 2 PUNTOS EN EL PLANO"
 
# Mensajes de Solicitud de Datos
SOLICITUD_AX = ">>> Ingrese la coordenada Ax: "
SOLICITUD_AY = ">>> Ingrese la coordenada Ay: "
 
SOLICITUD_BX = ">>> Ingrese la coordenada Bx: "
SOLICITUD_BY = ">>> Ingrese la coordenada By: "
 
# Mensajes de error
ERROR_FORMATO = "SOLO SE PERMITEN NUMEROS"
 
######################################################################
 
# Declaracion de variables
Ax, Ay , Bx, By , Distancia = 0.0, 0.0, 0.0 ,0.0, 0.0
 
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
    Ax = float(input(SOLICITUD_AX)) 
    Ay = float(input(SOLICITUD_AY)) 
 
    # Separador de la tabla
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    Bx = float(input(SOLICITUD_BX)) 
    By = float(input(SOLICITUD_BY)) 
 
    # Calculo de la Distancia entre dos puntos A y B
    # Distancia = ((AX-BX)^2 + (AY-BY)^2)^0.5
 
    Distancia = ((Ax-Bx)**2 + (Ay-By)**2 )**0.5
 
    # Separador de la tabla
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
    # Se muestra el mensaje en Pantalla
    print(Formato_Respuesta.center(ANCHO,RELLENO2) %(Distancia))
 
except ValueError:
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print(ERROR_FORMATO.center(ANCHO,RELLENO2))
 
######################################################################
 
# Parte Inferior de la Tabla
print(CADENA_VACIA.center(ANCHO,RELLENO1))