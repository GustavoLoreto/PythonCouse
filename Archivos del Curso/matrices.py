#Ing Loreto.

"""
Matrices

► Teoría:

Las matrices son disposiciones bidimensionales de valores. En notación matemática, una matriz se denota encerrando entre paréntesis los valores, que se disponen en filas y columnas. He aquí una matriz M :

     1  2  3
     2 12  6 
M =  1  0 -3
     0 -1  0

     Las listas permiten representar series de datos en una sola dimensión. Con una lista de números no se puede representar directamente una matriz, pero sı con una lista de listas.

# Creación de una Lista de Listas
M = [ [1, 2, 3], [2, 12, 6], [1, 0, -3], [0, -1, 0] ] 
En la notación matemática el elemento que ocupa la fila i-ésima y la columna j-ésima de una matriz M se representa con Mi,j .

Por ejemplo, el elemento de una matriz que ocupa la celda de la fila 1 y la columna 2 se denota con M1,2. Pero si deseamos acceder a ese elemento en la matriz Python M , hemos de tener en cuenta que Python siempre cuenta desde cero, así que la fila tendrá ́índice 0 y la columna tendrá ́índice 1:

# Acceso acceso a un elemento de la Lista M.
M [0][1]
► Salida:

2

___

► Enunciado:

Crea una Matriz 4x4 que almacene los valores de un teclado matricial. Imprime la matriz, la cuarta fila y el asterisco (*) en pantalla.

► Salida:

>>> IMPRIMIR MATRIZ  : [['1','2','3','A'], ['4','5','6', 'B'],
['7','8','9', 'C'], ['*', 0, '#', 'D']]
>>> FILA A IMPRIMIR  : ['*', '0', '#', 'D']
>>> DATO A IMPRIMIR  : *

"""

# Declaracion de Variables:
Matriz = []
Fila = 3
Columna = 0
 
######################################################################
 
# Inicio del Programa:
# Creacion de la matriz del teclado Matricial 4x4
Matriz = [['1', '2', '3', 'A'],
          ['4', '5', '6', 'B'],
          ['7', '8', '9', 'C'],
          ['*', '0', '#', 'D']]
 
# Se imprime la matriz en pantalla
print(">>> IMPRIMIR MATRIZ  : %s" %(Matriz))
print(">>> FILA A IMPRIMIR  : %s" %(Matriz[Fila]))
print(">>> DATO A IMPRIMIR  : %s" %(Matriz[Fila][Columna]))