##Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue la descomposición en Unidades, Decenas, Centenas y Miles. Ejemplos
##Entrada de datos

num = int(input("ingrese un numero que tenga como maximo 4 digitos: "))

uni = (num%10)
dec = (num%100-num%10)//10
cen = (num%1000-num%100)//100
miles = (num%10000-num%1000)//1000


print(miles)
print(cen)
print(dec)
print(uni)