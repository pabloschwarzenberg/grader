#Descomponer un número
s = int(input("ingrese un numero de 4 digitos como maximo: "))
pdigito = s//1000
sdigito = (s//100)%10
tdigito = (s%100)//10
cdigito = s%10

print(pdigito,"M", "+", sdigito, "C", "+", tdigito, "D", "+", cdigito, "U")