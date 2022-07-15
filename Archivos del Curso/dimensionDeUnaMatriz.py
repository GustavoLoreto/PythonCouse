#Ing Loreto.

"""
Dimensión de una Matriz
Cuando deseábamos saber cuál era la longitud de una lista utilizábamos la función len(). ¿Funcionará también sobre matrices? Hagamos la prueba.

► Entrada:

Matriz = [[1, 0], [0, 1], [0, 0]]
­len(Matriz)
► Salida:

3

___

No funciona correctamente: solo nos devuelve el número de filas (que es el número de componentes de la lista de listas que es la matriz). ¿Cómo averiguar el número de columnas?

► Entrada:

Matriz = [[1, 0], [0, 1], [0, 0]]
­len(Matriz[0])
► Salida:

2

___

Enunciado:

Crea una matriz 3x3 que almacene los valores del 1 al 9. El tamaño de la matriz indica la cantidad de filas. Imprime cada fila de la matriz en pantalla.

► Salida:

>>> MATRIZ: [[7, 8, 9], [4, 5, 6], [7, 8, 9]]
>>> FILA 1: [7, 8, 9]
>>> FILA 2: [4, 5, 6]
>>> FILA 3: [7, 8, 9]
"""

# Declaracion de Variables:
Matriz = []
Longitud = 0
 
######################################################################
 
# Inicio del Programa:
# Creacion de la matriz del teclado Matricial 4x4
Matriz = [[7, 8, 9], [4, 5, 6,], [7, 8, 9]]
 
#Longitud de la Matriz
Longitud = len(Matriz)
 
######################################################################
 
print(">>> MATRIZ: %s" %(Matriz))
 
# Se imprime cada fila de la matriz
for fila in range(Longitud):
    print(">>> FILA %d: %s" %(fila+1, Matriz[fila]))