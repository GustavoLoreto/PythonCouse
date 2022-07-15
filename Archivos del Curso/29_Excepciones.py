
#Ing Loreto 

# Manejo de excepciones

# ESTILO WCODE

# Variables
# int_Nombre_variable = tipo_dato       ;   Variables del tipo entero
# float_Nombre_variable = tipo_dato     ;   Variables con decimales
# str_Nombre_variable = tipo_dato       ;   variables con Cadenas o caracteres
# bool_Nombre_variable = tipo_dato      ;   variables booleanas

# Constantes
# const_NOMBRE_CONSTANTE = tipo_dato    ;   Constante de cualquier tipo de datos
# NOMBRE_CONSTANTE = tipo_dato

# Colecciones
# list_Nombre_Lista = [dato1,dato2,...]         ;   Elementos de una lista
# tuple_Nombre_tupla = (dato1,dato2,...)        ;   Elementos de una tupla
# dic_Nombre_diccionario = {'clave':dato2,...}  ;   Elementos de un diccionario
#
################################################################################

def edad():
    
    try:
        int_edad = int(input("Intrioduce tu edad: "))
        print("Tuedad es: %d\n"%(int_edad))

    except:
        print("\nNo has introducido valores numéricos. Intenta de nuevo\n")
        edad()
edad()

