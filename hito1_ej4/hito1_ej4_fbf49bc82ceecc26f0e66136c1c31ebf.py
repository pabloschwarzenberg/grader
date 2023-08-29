numero = int(input("ingrese su numero:"))



binario = ""


while numero >=1:
    x = numero % 2
    xstr = str(x)
    binario = binario + xstr
    numero //= 2

longOriginal = len(binario)

w = int(binario)



r = w

a = r//1000000
r = r%1000000
b = r//100000
r = r%100000
c = r//10000
r = r%10000
d = r//1000
r = r%1000
e = r//100
r = r%100
f = r//10
g = r%10


y = 10 *(10 *(10 *(10 * (10 *(10 * g + f)+ e) + d) + c) + b) + a

ystr = str(y)

print("resultado=",ystr[0:longOriginal])


