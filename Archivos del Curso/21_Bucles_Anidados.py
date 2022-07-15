
#Loreto

# Ejercicios con estructuras repetitivas.

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

## Pseudocodigo:

##    Hacer_1 mientras condicion1
##
##        Hacer_2 mientras condicion2
##
##            Hacer_3 mientras condicion3
##
##            Fin del Hacer_3
##
##         Fin del Hacer_2
##
##    Fin del Hacer_1

################################################################################

## ENUNCIADO 1:

##  Imprimir diez veces la serie de numeros del 1 al 10. Los numeros deben
## aparecer cada 1 segundo

################################################################################

## Estudio previo:
##
##    La secuencia de numeros del 1 al 10 se realiza mediante un ciclo que
##    vaya del 1 al 10 y un contador para generarlos.
##
##    Esta secuencia se debe realizar 10 veces por lo tanto se requiere otro
##    ciclo que cuente las veces que se ha impreso el bucle interno. Este ciclo
##    aumentará en una unidad cuando se hayan visualizado los numeros
##    del 1 al 10.

##    El bucle exterior controla que se imprima 10 veces el bucle interno.


################################################################################

## Variables

##  numero = contador interno para generar los numeros del 1 al 10
##  serie = contador de series externo del 1 al 10

#   Pseudocodigo:

##    numero = 0
##    serie = 1
##
##    Hacer_1 mientras serie <= 10
##
##        numero = 1
##
##        Hacer_2 mientras numero <= 10
##            imprime numero
##            numero = numero + 1
##            espera(1)
##        Fin del Hacer_2
##
##        serie = serie  + 1
##
##    Fin del Hacer_1
##    Fin del programa


################################################################################

import time

# Declaracion de variables:

int_Numero = 0
int_Serie = 1

################################################################################

# Inicio del programa:

print("\nSerie numero: %d \n" %(int_Serie))

while int_Serie <= 10:

    int_Numero = 1

    while int_Numero <= 10:
        print(int_Numero)
        int_Numero = int_Numero + 1
        time.sleep(1)

    int_Serie = int_Serie + 1
##    print("")

    if int_Serie <= 10:
        print("\nSerie numero: %d \n"%(int_Serie))

################################################################################

#