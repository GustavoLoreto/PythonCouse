# Ing Loreto.

"""
Sistema de Ecuaciones (Método de Cramer).

► Teoria:

El conjunto de ecuaciones lineales que se muestra a continuación:
a11X1 + a12X2 = C1
a21X1 + a22X2 = C2


Puede resolverse usando la regla de Cramer:


► Enunciado:

Usando estas ecuaciones, escriba, y ejecute un programa para encontrar

los valores x1 y x2 que satisfagan las siguientes ecuaciones:

3X1 + 4X2 = 40
5X1 + 2X2 = 34


►  Variables:

a11: Coeficiente principal de la primera ecuación.

a12: Coeficiente secundario de la primera ecuación.

c1  : Término independiente de la primera ecuación.

a21: Coeficiente principal de la segunda ecuación.

a22: Coeficiente secundario de la segunda ecuación.

c2  : Término independiente de la segunda ecuación.

x1  : Incógnita 1.

x2  : Incógnita 2.

"""

# Tipo de Mensajes a Mostrar: función imprimir_mensaje(mensaje,tipo)
CABECERA  = 0   # Inicio o seccion de la tabla, con el nombre de la
                # sección.
MENSAJE   = 1   # Mensaje simple en pantalla (Sin variables).
RESULTADO = 2   # Mensaje con formato (Incluye variables).
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "METODO DE CRAMER"
MENSAJE_SOLUCION = "SOLUCIONES"
 
MENSAJE_ECUACION = '''
         a11(x1) + a12(x2) = c1
         a21(x1) + a22(x2) = c2
'''
# Mensajes de error
ERROR_FORMATO = "SOLO SE PERMITEN NÚMEROS"
 
######################################################################
 
# Declaracion de funciones:
def matriz_nula(filas, columnas):
    """
    Descripcion : Crea una Matriz Nula.
    Parametros  : filas, columnas.
 
    - filas: Cantidad de filas de la matriz.
    - columnas: cantidad de Columnas de la matriz.
 
    Retorna     : Una matriz nula del tamaño indicado.
    """
    Matriz = []
 
    # Se agregan los elementos a la Matriz
    for elemento in range(filas):
        Matriz.append ([0] * columnas)
    return Matriz
 
def imprimir_mensaje(mensaje,tipo):
    """
    Descripcion : Imprime 3 tipos de Mensajes.
    Parametros  : mensaje, tipo.
 
    - mensaje: mensaje a imprimir en pantalla.
    - tipo: tipo de mensaje (CABEZERA,MENSAJE,RESULTADO).
 
        • CABECERA: Inicio o seccion de la tabla, con el nombre
                    de la sección.
        • MENSAJE : Mensaje simple en pantalla (Sin variables).
        • RESULTADO : Mensaje con formato (Incluye variables).
 
    Retorna     : Una matriz nula del tamaño indicado.
    """
    
   
   
   # Tipo de Mensajes a Mostrar: función imprimir_mensaje(mensaje,tipo)
CABECERA  = 0   # Inicio o seccion de la tabla, con el nombre de la
                # sección.
MENSAJE   = 1   # Mensaje simple en pantalla (Sin variables).
RESULTADO = 2   # Mensaje con formato (Incluye variables).
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "METODO DE CRAMER"
MENSAJE_SOLUCION = "SOLUCIONES"
 
MENSAJE_ECUACION = '''
         a11(x1) + a12(x2) = c1
         a21(x1) + a22(x2) = c2
'''
# Mensajes de error
ERROR_FORMATO = "SOLO SE PERMITEN NÚMEROS"
 
######################################################################
 
# Declaracion de funciones:
def matriz_nula(filas, columnas):
    """
    Descripcion : Crea una Matriz Nula.
    Parametros  : filas, columnas.
 
    - filas: Cantidad de filas de la matriz.
    - columnas: cantidad de Columnas de la matriz.
 
    Retorna     : Una matriz nula del tamaño indicado.
    """
    Matriz = []
 
    # Se agregan los elementos a la Matriz
    for elemento in range(filas):
        Matriz.append ([0] * columnas)
    return Matriz
 
def imprimir_mensaje(mensaje,tipo):
    """
    Descripcion : Imprime 3 tipos de Mensajes.
    Parametros  : mensaje, tipo.
 
    - mensaje: mensaje a imprimir en pantalla.
    - tipo: tipo de mensaje (CABEZERA,MENSAJE,RESULTADO).
 
        • CABECERA: Inicio o seccion de la tabla, con el nombre
                    de la sección.
        • MENSAJE : Mensaje simple en pantalla (Sin variables).
        • RESULTADO : Mensaje con formato (Incluye variables).
 
    Retorna     : Una matriz nula del tamaño indicado.
    """
    if tipo == CABECERA:
        print("CADENA_VACIA".center("ANCHO,RELLENO1"))
        # Imprime el Inicio o seccion de la tabla, con el nombre 
        # de la sección.
        print(MENSAJE_INICIAL.center("ANCHO,RELLENO2"))
 
    elif tipo == MENSAJE:
        # Imprime un Mensaje simple en pantalla (Sin variables)
        print(mensaje.center("ANCHO,RELLENO2"))
 
    elif tipo == RESULTADO:
        # Imrprime un Mensaje con formato (Incluye variables)
        print(mensaje)
 
    # Separador de la tabla
    print("CADENA_VACIA".center("ANCHO,RELLENO1"))
 
def metodo_cramer():
   """
   Descripcion : Función donde se aplica el Método de Cramer.
   Parametros  : Sin parametros.
   Retorna     : No devuelve parametros.
   """
   filas, columnas = 2, 2
 
   M = matriz_nula(filas, columnas)
 
   # ... y leemos su contenido de teclado
   for fila in range(filas):
        for col in range(columnas):
            M[fila][col]=float(input("Dato a%d%d: " %(fila+1,col+1)))
        #Se agregan Los terminos independientes C1 y C2
        M[fila].append(float(input("Dato c%d : " %(fila+1))))
        print("CADENA_VACIA".center("ANCHO,RELLENO1"))
 
   # Se almacenan las posiciones de la Matriz en las variables 
   # correspondientes
 
   # Ecuacion 1
   a11 = M[0][0]
   a12 = M[0][1]
   c1  = M[0][2]
 
   # Ecuacion 2
   a21 = M[1][0]
   a22 = M[1][1]
   c2  = M[1][2]
 
   # Puede resolverse usando la regla de Cramer:
 
   x1 = (c1*a22 - c2*a12)/(a11*a22 - a12*a21)
   x2 = (c2*a11 - c1*a21)/(a11*a22 - a12*a21)
 
   RESPUESTA = ">>> x1 = %4.2f y x2 = %4.2f" %(x1, x2)
 
   imprimir_mensaje(MENSAJE_SOLUCION, MENSAJE)
   imprimir_mensaje(RESPUESTA, RESULTADO)
 
######################################################################
 
def main():
    """
    Descripcion : Funcion principal
    Parametros  : Sin parametros
    Retorna     : No devuelve parametros
    """
    imprimir_mensaje(MENSAJE_INICIAL , CABECERA)
    imprimir_mensaje(MENSAJE_ECUACION, MENSAJE)
    metodo_cramer()
 
######################################################################
 
# Inicio del programa:
main()