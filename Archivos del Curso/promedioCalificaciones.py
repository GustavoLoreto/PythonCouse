#Ing Loreto.

# Declaracion de variables
datos = [
            {"nombre": "Taylor C.","promedio": 9.51,},
            {"nombre": "John G."  ,"promedio": 8.96,},
            {"nombre": "Maria S." ,"promedio": 9.22,},
            {"nombre": "Juan C."  ,"promedio": 9.99,},
            {"nombre": "Anna A."  ,"promedio": 8.99,},
            {"nombre": "Mike T."  ,"promedio": 9.50,},
            {"nombre": "Pedro F." ,"promedio": 9.99,},
            {"nombre": "Julia F." ,"promedio": 8.99,},
            {"nombre": "Delia F." ,"promedio": 9.89,},
            {"nombre": "Julio A." ,"promedio": 7.50,},
        ]
 
encabezado = '''
+--------------------+----------+"
|       NOMBRE       | PROMEDIO |
+--------------------+----------+ '''
 
######################################################################
 
# Inicio del Programa:
print(encabezado)
 
for dato in datos:
    nombre = dato["nombre"]
    promedio = dato["promedio"]
    cadena = "|{:<20}|{:>10.2f}|".format(nombre, promedio)
    print(cadena)
    print("+--------------------+----------+")