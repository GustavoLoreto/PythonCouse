#EJERCICIOS (Mostrar el resultado en pantalla)

# 1) Programa que solicite al usuario los datos para calcular el area de un Cuadrado 

# int_Nombre_variable = tipo_dato       ;   Variables del tipo entero  
# Pseudocódigo:

# nombre_variable = tipo_dato
# introducir nombre_variable
# imprime comentario
from ctypes.wintypes import INT


print ("El área de un cuadrado")

#Declaracion de variables
#int_Lado = 0
#int_Area = 0
#Inicio del programa


int_Lado       = int  (input("Introduce la longitud de un aldo del cuadrado: "))
print("")

int_Area = int_Lado  **2

print ("El área del cuadrado es:    %d" %(int_Area))
print("")


print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
# 2) Programa que solicite al usuario los datos para calcular el area de un Triangulo
print("")
int_Base         = int  (input("Introduce la base del Triangulo: "))
int_Altura       = int  (input("Introduce la altura del Triangulo: "))

int_AreaT = (int_Base * int_Altura)/2

print ("El área del Truangulo es: %d" %(int_AreaT))
print("")

print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
# 3) Programa que solicite al usuario los datos para calcular el area de un Circulo
# AREA DE UN CIRCULO
# A = PI*(Radio**2)
print("")
int_Pi = 3.1416

int_Radio         = int  (input("Introduce el radio del círculo: "))
int_AreaC         = int_Pi*(int_Radio**2)

print ("El área del Círculo es: %d" %(int_AreaC))
print("")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("")


# 4) Programa que solicite al usuario los datos para llevar Grados farenheit a Grados Celcius
#celcius = (fahrenheit - 32.0) * 5.0 / 9.0

float_Far       = float  (input("Introduce los grados en Farenheit: "))
float_Cel       = (float_Far - 32.5) * 5.0 / 9.0

print ("Los grados celcius ingresados son igual a %d"%(float_Cel) + (" grados Farenheit"))

print("")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("")

# 5) Sumar 4 Tramas de datos(Stings) que contengan el precio de un producto.

#    Consideraciones:

#    Trama = 6E + 3D
#    La suma no debe exceder el numero 999999999

print("Sumar tramas")



str_Valor1 = "58236986"

str_Valor2 = "69547957"

str_Valor3 = "76898688"

str_Valor4 = "98979869"

int_Suma=0

print("********************************")

print("*       PRIMERA TRAMA          *")

print("********************************")

print("* Primer  valor $%s"%(str_Valor1), "     *")

print("* Segundo valor $%s"%(str_Valor2), "     *")

print("* Tercer  valor $%s"%(str_Valor3), "     *")

print("* Cuarto  valor $%s"%(str_Valor4), "     *")

print("********************************")

print("********************************")

print("*    SEGUNDA TRAMA SUMA        *")

print("********************************")



int_Suma=int (str_Valor1)+ int (str_Valor2)+ int (str_Valor3)+ int (str_Valor4)



print("********************************")

print("*VALOR DEL PRODUCTO $%d"%(int_Suma),"*")

print("********************************")

print("********************************")

print("*  TERCER TRAMA PARTE DECIMAL  *")

print("********************************")



int_Part_entera = int_Suma/1000

int_Part_decimal = int_Suma%1000



print("* VALOR TOTAL  $%d.%d"%(int_Part_entera,int_Part_decimal), "    *")




# FORMULAS

# AREA DEL CUADRADO
# A = Lado ** 2

# AREA DEL TRIANGULO
# A = (Base*Altura)/2

# AREA DE UN CIRCULO
# A = PI*(Radio**2)

# FAHRENHEIT A CELCIUS
# celcius = (fahrenheit - 32.0) * 5.0 / 9.0


