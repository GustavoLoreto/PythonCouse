#Loreto

num1 = 0
num2 = 0
aux = 0

num1 = int(input("Introcuce el primer número "))
num2 = int(input("Introcuce el segundo número "))

if num1 > num2:

    aux = num1
    num1 = num2
    num2 = aux

while num1 <= num2:
    print(num1)

    num1 = num1 +1







