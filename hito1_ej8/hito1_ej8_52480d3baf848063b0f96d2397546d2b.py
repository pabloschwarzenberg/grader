#Descomponer un número
num1 = int(input("Ingresar un numero de cuatro digitos para descomponerlo.\n"))
uni = num1 % 10
num1 = num1 // 10

dec = num1 % 10
num1 = num1 // 10

cen = num1 % 10
num1 = num1 // 10

mil = num1 % 10
num1 = num1 // 10

print("descomposicion\n",mil,"M +",cen,"C +",dec,"D +",uni,"U")