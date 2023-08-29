#Descomponer un número

numero = int(input("Ingrese cuatro digitos: "))
#print(numero)
x = numero
#Unidad
u = numero%10
#print(numero, x)
numero //= 10
#Decena
d = numero%10
#print(numero, y)
numero //= 10
#Centena
c = numero%10
#print(numero, z)
numero //= 10
#Unidad de Mil
m = numero%10
#print(numero, w)
numero //= 10

if m != 0:
    print("{}M+{}C+{}D+{}U".format(m,c,d,u))

elif c != 0:
    print("{}C+{}D+{}U".format(c, d, u))

elif d != 0:
    print("{}D+{}U".format(d, u))

elif u != 0:
    print("{}U".format(u))

else:
    print("Error")