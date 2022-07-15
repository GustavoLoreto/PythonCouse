# Ing Loreto.

"""
Función para transformar una lista en una Matriz.

Desarrolla una función llamada “crear_matriz” que reciba tres parámetros:

Fila: Número de filas para la matriz.

Columna: Número de columnas para la matriz.

Lista: Lista a transformar en Msatriz.

La función debe permitir transformar los elementos de una lista simple en elementos de una matriz agrupándolos en filas y columnas. la función debe devolver la nueva lista y guardarla en una variable llamada “matriz”.

► Entrada:

fila = 4
columna = 4
nueva_lista = [
                'a','b','c','d','e',
                'f','g','h','i','j',
                'k','l','m','n','o',
                'p','q','r','s','t',
                'u','v','w','x','y',
              ]
matriz = crear_matriz (fila, columna, nueva_lista)
print(matriz)
► Salida:

[['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h'], ['i', 'j', 'k', 'l'], ['m', 'n', 'o', 'p']]

"""

# Declaración de Funciones:
def crear_matriz(fila, columna, lista):
    """
    Descripcion : Crea una Matriz con los elementos de una lista 
                  simple.
    Parametros  : filas, columnas, lista.
 
    - filas: Cantidad de filas que tendrá la matriz.
    - columnas: Cantidad de Columnas que tendrá la matriz.
    - lista: Lista a transformar en matriz.
 
    Retorna     : Una matriz con los elementos de la lista separados
                  en filas y columnas.                 
    """
    matriz = []
 
    for m in range(fila):
        lista_fila = []
        for n in range(columna):
            # Se necesita incrementar la posicion para guardar los
            # valores de la lista desde 0 hasta el indice del ultimo
            # elemento.
            lista_fila.append(lista[fila * m + n])
        matriz.append(lista_fila)
    return matriz
 
######################################################################
 
def main():
    """
    Descripcion : Funcion principal.
    Parametros  : Sin parametros.
    Retorna     : No devuelve parametros.
    """
    fila = 4
    columna = 4
    nueva_lista =   [
                     'a','b','c','d','e',
                     'f','g','h','i','j',
                     'k','l','m','n','o',
                     'p','q','r','s','t',
                     'u','v','w','x','y',
                    ]
 
    matriz = crear_matriz (fila,columna,nueva_lista)
    print(matriz)
 
######################################################################
 
# Inicio del Programa:
main()