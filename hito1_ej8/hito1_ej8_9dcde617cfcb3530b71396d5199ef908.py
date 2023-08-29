#Descomponer un número
n = eval(input("ingrese numero de 4 digitos: "))
u = n%10
n = n//10
d = n%10
n = n//10
c = n%10
n = n//10
um = n%10

print(um,"M +",c,"C +",d,"D +",u,"U")      