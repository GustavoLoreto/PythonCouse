#Ing Loreto.

"""
Creación de matrices: Matriz Identidad.

► Teoría:

En álgebra lineal, la matriz identidad es una matriz que cumple la propiedad de ser el elemento neutro del producto de matrices.
 Esto quiere decir que el producto de cualquier matriz por la matriz identidad no tiene ningún efecto.

Como el producto de matrices sólo tiene sentido si sus dimensiones son compatibles, existen infinitas matrices identidad dependiendo de las dimensiones. 
In, la matriz identidad de tamaño n, se define como de las entradas de la diagonal principal:
Los pasos para crear la matriz identidad en Python son los siguientes:

# Pedimos la dimensión de la matriz,
dimension = int(input("Dimension de la matriz: "))
 
# Creamos una matriz nula...
Matriz = []
 
for elemento in range(dimension):
    Matriz.append ([0] * dimension)
 
# ... y leemos su contenido
for fila in range(dimension):
    for columna in range(dimension):
    #si el numero de fila y columna es igual
    if fila == columna:
    # Guarda el número 1 en la posición
    Matriz[fila][columna] = 1
► Enunciado:

Haz un programa que pida un entero positivo n y almacene en una variable M la matriz identidad de n × n (la que tiene unos (1) en la diagonal principal y ceros (0) en el resto de celdas). Imprime la matriz en pantalla.


► Salida:

>>> MATRIZ M(4x4): [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0],
[0, 0, 0, 1]]
 
[1, 0, 0, 0]
[0, 1, 0, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]


"""

# Declaracion de Variables:
M = []
longitud = 0
dimension = 0
 
######################################################################
 
# Inicio del programa:
# Pedimos la dimensión de la matriz,
dimension = int(input(">>> Dimension de la matriz de tamaño nxn: "))
 
# Creamos una matriz nula...
for elemento in range(dimension):
        M.append ([0] * dimension)
 
# ... y leemos su contenido
for fila in range(dimension):
    for columna in range(dimension):
        # Si el numero de fila y columna es igual
        if fila == columna:
             # Guarda el número 1 en la posición
             M[fila][columna] = 1
 
######################################################################
 
print("\n>>> MATRIZ M(%dx%d): %s\n" %(dimension,dimension,M))
 
longitud = len(M)
 
# Se imprime cada fila de la matriz
for valor in range(longitud):
    print(M[valor])