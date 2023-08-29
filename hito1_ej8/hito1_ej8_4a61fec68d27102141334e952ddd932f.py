#Descomponer un número
num = int(input("menciona un numero de 4 digitos/n"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 10**2 % 10
m = num // 10**3 % 10
print("{}M+{}C+{}D+{}U".format(m,c,d,u))