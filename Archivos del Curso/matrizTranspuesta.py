# Ing Loreto.

"""
Matriz Transpuesta

La traspuesta de una matriz A de dimensión m × n es una matriz AT de dimensión n × m tal que ATi,j = Aj,i.


► Enunciado:

Diseña un programa que lea una matriz y muestre su traspuesta.

► Salida:

>>> MATRIZ ORIGINAL:
 
[1.0, 2.0, 3.0, 4.0]
[5.0, 6.0, 7.0, 8.0]
[9.0, 0.0, 1.0, 2.0]
 
>>> MATRIZ TRANSPUESTA:
 
[1.0, 5.0, 9.0]
[2.0, 6.0, 0.0]
[3.0, 7.0, 1.0]
[4.0, 8.0, 2.0]
"""
# Declaracion de Variables:
longitud = 0
m_filas = 0
n_columnas = 0
# Matriz transpuesta
 
######################################################################
 
# Inicio del Programa:
# Pedimos la dimensión de la matriz,
m_filas    = int(input(">>> Dime el numero de filas: "))
n_columnas = int(input(">>> Dime el numero de columnas: "))
 
# Se crean las matrices nulas
Matriz = []
Transpuesta = []
 
print()
 
# Se crea la Matriz nula para la matriz original
for elemento in range(m_filas):
    Matriz.append ([0] * n_columnas)
 
# Se crea la matriz nula para la matriz Transpuesta
for elemento in range(n_columnas):
    Transpuesta.append ([0] * m_filas)
 
# Se crea la Matriz y su Transpuesta
for fila in range(m_filas):
    for col in range(n_columnas):
        Matriz[fila][col]=float(input("Dato(%d,%d): "%(fila+1,col+1)))
        Transpuesta[col][fila] = Matriz[fila][col]
 
######################################################################
 
print("\n>>> MATRIZ ORIGINAL:\n")
#Tamaño de la Matriz original
longitud = len(Matriz)
 
# Se imprimen las Filas de la matriz Original
for fila in range(longitud):
    print(Matriz[fila])
 
print("\n>>> MATRIZ TRANSPUESTA:\n")
#Tamaño de la matriz transpuesta
longitud = len(Transpuesta)
 
#Se imprimen las filas de la matriz Transpuesta
for fila in range(longitud):
    print(Transpuesta[fila])
