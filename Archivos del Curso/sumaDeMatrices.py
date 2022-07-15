# Ing Loreto.

"""
Suma de Matrices.

► Enunciado:

Diseñar un programa que sume dos matrices. 
Recuerda que solo es posible sumar matrices con la misma dimensión, 
con la misma cantidad de Filas y Columnas.

Hemos de tener claro cómo se calcula C = A + B. Si la dimensión de A y de B es m × n, 
la matriz resultante será de esa misma dimensión, y su elemento de coordenadas (i, j), 
es decir, Ci,j , se calcula así: Ci,j = Ai,j + Bi,j

Para 1 ≤ i ≤ m y 1 ≤ j ≤ n. 
Recuerda que la convención adoptada en la notación matemática hace que los índices de las matrices empiecen en 1, 
pero que en Python todo empieza en 0.

"""

# Declaración de Funciones:
def matriz_nula(filas, columnas):
    """
    Descripcion : Crea una Matriz Nula.
    Parametros  : filas, columnas.
 
    - filas: Cantidad de filas de la matriz.
    - columnas: cantidad de Columnas de la matriz.
 
    Retorna     : Una matriz nula del tamaño indicado.
    """
    matriz = []
 
    # Se agregan los elementos a la Matriz
    for elemento in range(filas):
        matriz.append ([0] * columnas)
    return matriz
 
def crear_array(lista):
    """
    Descripcion : Crea un array o matriz partiendo de una lista de 
                  listas.
    Parametros  : Recibe la Lista de Listas.
    Retorna     : Un array o matriz.
    """
    array = []
 
    for fila in range(len(lista)):
        array.append(lista[fila])
 
    return array
 
def sumar_matrices(Matriz_A, Matriz_B):
    """
    Descripcion : Suma Dos matrices.
    Parametros  : Matriz A , Matriz_B.
 
    - Matriz_A: Primera Matriz.
    - Matriz_B: Segunda Matriz.
 
    Retorna     : El resultado de la Suma de la Matriz_A y 
                  la Matriz_B.
    """
    filas = len(Matriz_A)
    columnas = len(Matriz_B[0])
 
    Matriz_C = matriz_nula(filas,columnas)
 
    for i in range(filas):
        for j in range(columnas):
            Matriz_C[i][j] = Matriz_A[i][j] + Matriz_B[i][j]
 
    return Matriz_C
 
def imprimir_matriz(Matriz):
    """
    Descripcion : Se imprime la Matriz Fila por Fila.
    Parametros  : Matriz.
 
    - Matriz: Matriz a imprimir fila por fila.
 
    Retorna     : No devuelve parametros.
    """
    print("\n>>> MATRIZ: %s\n" %(Matriz))
 
    longitud = len(Matriz)
 
    # Se imprime cada fila de la matriz
    for valor in range(longitud):
        print(">>>",Matriz[valor])
 
######################################################################
 
def main():
    """
    Descripcion : Funcion principal.
    Parametros  : Sin parametros.
    Retorna     : No devuelve parametros.
    """
    # Se crean los Arrays o Matrices
    A = crear_array([[0, 1, 2],[3, 4, 5], [6, 7, 8]])
    B = crear_array([[1, 1, 1],[1, 1, 1], [1, 1, 1]])
 
    # Se muestran las matrices en pantalla
    imprimir_matriz(A)
    imprimir_matriz(B)
 
    # Se suman las Matrices A y B
    C = sumar_matrices(A, B)
 
    # Se muestra el resultado en pantalla
    imprimir_matriz(C)
 
######################################################################
 
# Inicio del Programa:
main()