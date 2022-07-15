#Ing Loreto.

"""
Lectura de Matrices: Llenar una Matriz por Teclado
Si deseamos leer una matriz de tamaño determinado, podemos crear una matriz nula como hemos visto anteriormente y, a continuación, rellenar cada uno de sus componentes:

# Pedimos la dimensión de la matriz,
m_filas = int(input("Dime el número de filas: "))
n_columnas = int(input("Dime el número de columnas: "))
 
# Creamos una matriz nula...
M = []
for elemento in range(m_filas):
    M.append ([0] * n_columnas)
 
# ... y leemos su contenido de teclado
for fila in range(m_filas):
    for col in range(n_columnas):
        M[fila][col]=float(input("Dato (%d,%d):" %(fila+1,col+1)))
 
# Se determina el tamaño de la matriz
matriz_longitud = len(M)
 
#Imprime las Filas de la Matriz
for valor in range(matriz_longitud):
    print(M[valor])
► Enunciado:

Haz un programa que permita crear la siguiente matriz:

La matriz cuenta con 3 filas (m) y 4 columnas (n). Los datos se deben solicitar al usuario. Imprime la matriz en pantalla.

► Salida:

>>> MATRIZ M(3x4): [[1.0, 2.0, 3.0, 4.0], [5.0, 6.0, 7.0, 8.0],
[9.0, 0.0, 1.0, 2.0]]
 
[1.0, 2.0, 3.0, 4.0]
[5.0, 6.0, 7.0, 8.0]
[9.0, 0.0, 1.0, 2.0]
"""
# Declaracion de Variables:
M = []
longitud = 0
m_filas = 0
n_columnas = 0
 
######################################################################
 
# Inicio del programa:
# Pedimos la dimensión de la matriz,
m_filas    = int(input(">>> Dime el numero de filas   : "))
n_columnas = int(input(">>> Dime el numero de columnas: "))
 
print()
 
# Creamos una matriz nula...
for elemento in range(m_filas):
    M.append ([0] * n_columnas)
 
# ... y leemos su contenido de teclado
for fila in range(m_filas):
    for col in range(n_columnas):
        M[fila][col] = float(input("Dato (%d,%d):" %(fila+1, col+1)))
 
######################################################################
 
print("\n>>> MATRIZ M(%dx%d): %s\n" %(m_filas,n_columnas,M))
 
longitud = len(M)
 
# Se imprime cada fila de la matriz
for fila in range(longitud):
    print(M[fila])
