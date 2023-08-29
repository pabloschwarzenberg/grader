numero = int(input("Ingrese cuatro digitos: "))

x = numero

u = numero%10

numero //= 10

d = numero%10

numero //= 10

c = numero%10

numero //= 10

m = numero%10

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