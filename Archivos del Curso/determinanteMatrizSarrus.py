# Ing Loreto.

"""
Determinante de una Matriz (Regla de Sarrus).

Escriba, y ejecute un programa para calcular el determinante de una matriz 3x3.
► Variables:

a11, a12, a13: Elementos de la Primera Fila.

a21, a22, a23: Elementos de la Segunda Fila.

a31, a32, a33: Elementos de la Tercera Fila.

determinante: Determinante de la ecuación.

► Datos de Prueba.

a) a11 = 1 , a12 = 3 , a13 = 9

b) a21 = 2 , a22 = 5 , a23 = 7

c) a31 = 1 , a32 = 2 , a33 = 3


"""
# Valores para Dibujar la Tabla
ANCHO = 45
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
 
######################################################################
 
# Tipo de Mensajes a Mostrar: función imprimir_mensaje(mensaje,tipo)
CABECERA  = 0   # Inicio o seccion de la tabla, con el nombre de 
                # la sección
MENSAJE   = 1   # Mensaje simple en pantalla (Sin variables)
RESULTADO = 2   # Mensaje con formato (Incluye variables)
 
######################################################################
 
# Mensajes a Mostrar
MENSAJE_INICIAL = "DETERMINANTE DE UNA MATRIZ 3x3"
MENSAJE_MATRIZ = '''
            | a11  a12  a13 |
            | a21  a22  a23 | =
            | a31  a32  a33 |
'''
# Mensajes de error
ERROR_FORMATO = "SOLO SE PERMITEN NÚMEROS"
 
######################################################################
 
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
 
def crear_matriz(lista):
    """
    Descripcion : Crea un array o matriz partiendo de una lista 
                  de listas.
    Parametros  : Recibe la Lista de Listas.
    Retorna     : Un array o matriz.
    """
    Matriz = []
 
    for fila in range(len(lista)):
        Matriz.append(lista[fila])
 
    return Matriz
 
def imprimir_matriz(Matriz):
    """
    Descripcion : Se imprime la Matriz Fila por Fila.
    Parametros  : Matriz.
 
    - Matriz: Matriz a imprimir fila por fila.
 
    Retorna     : No devuelve parametros.
    """
    print(">>> MATRIZ: ")
    longitud = len(Matriz)
 
    # Se imprime cada fila de la matriz
    for valor in range(longitud):
        print(">>>", Matriz[valor])
 
    # Separador de la tabla
    # print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
def imprimir_mensaje(mensaje,tipo):
    """
    Descripcion : Imprime 3 tipos de Mensajes.
    Parametros  : mensaje, tipo.
 
    - mensaje: mensaje a imprimir en pantalla
    - tipo: tipo de mensaje (CABEZERA,MENSAJE,RESULTADO)
 
        • CABECERA: Inicio o seccion de la tabla, con el 
                    nombre de la sección.
        • MENSAJE : Mensaje simple en pantalla (Sin variables)
        • RESULTADO : Mensaje con formato (Incluye variables)
 
    Retorna     : Una matriz nula del tamaño indicado
    """
    if tipo == CABECERA:
        print(CADENA_VACIA.center(ANCHO,RELLENO1))
        # Imprime el Inicio o seccion de la tabla, 
        # con el nombre de la sección
        print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
 
    elif tipo == MENSAJE:
        # Imprime un Mensaje simple en pantalla (Sin variables)
        print(mensaje.center(ANCHO,RELLENO2))
 
    elif tipo == RESULTADO:
        # Imprime un Mensaje con formato (Incluye variables)
        print(mensaje)
 
    # Separador de la tabla
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
 
def metodo_sarrus(Matriz):
    """
    Descripcion : Función donde se aplica el Método de 
                  Sarrus.
    Parametros  : Matriz.
 
    - Matriz: Contiene los elementos para calcular el 
              determinante.
 
    Retorna     : No devuelve parametros.
    """
    # Fila 1
    a11 = Matriz[0][0]
    a12 = Matriz[0][1]
    a13 = Matriz[0][2]
 
    # Fila 2
    a21 = Matriz[1][0]
    a22 = Matriz[1][1]
    a23 = Matriz[1][2]
 
    # Fila 3
    a31 = Matriz[2][0]
    a32 = Matriz[2][1]
    a33 = Matriz[2][2]
 
    determinante = a11*(a22 * a33 - a32 * a23) 
    determinante = determinante - a21*(a12 * a33 - a32 *a13)
    determinante = determinante + a31*(a12 * a23 - a22 * a13)
 
    RESPUESTA = ">>> Determinante de la matriz: %4.2f" %(determinante)
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    imprimir_mensaje(RESPUESTA, RESULTADO)
 
######################################################################
 
def main():
    """
    Descripcion : Funcion principal
    Parametros  : Sin parametros
    Retorna     : No devuelve parametros
    """
    # Se crea el array o matriz
    Matriz = crear_matriz([[1, 3, 9],[2, 5, 7], [1, 2, 3]])
 
    imprimir_mensaje(MENSAJE_INICIAL, CABECERA)
    imprimir_mensaje(MENSAJE_MATRIZ, MENSAJE)
    imprimir_matriz(Matriz)
    metodo_sarrus(Matriz)
 
######################################################################
 
# Inicio del Programa:
main()