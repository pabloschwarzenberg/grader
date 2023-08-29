#Descomponer un número
num=int(input("ingrese un numero de 4 digitos:"))

a=num//1000
b=((num//100))%10
c=((num//10))%10
d=((num//1))%10

print(a, "M +", b, "C +", c, "D +", d, "U +")