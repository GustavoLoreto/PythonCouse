# Ing Loreto.

"""
Función para generar una Matriz.

► Enunciado:

Desarrolla una función llamada “crear_array” que reciba un parámetro llamado "lista" que va a almacenar los elementos contenidos en la lista  para ser  trasformados en un array o matriz.

La función debe permitir transformar los elementos de una lista de listas y devolver los mismos valores para ser guardados en una variable llamada “array” la cual será una lista vacía hasta recibir los elementos de la función “crear array”.

___

►Entrada:

array = crear_array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
print(array)
► Salida:

[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""

# Declaracion de Funciones:
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
 
def main():
    """
    Descripcion : Funcion principal.
    Parametros  : Sin parametros.
    Retorna     : No devuelve parametros.
    """
    array = crear_array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
    print(array)
 
######################################################################
 
# Inicio del Programa:
main()