n = int(input("ingrese el rut: "))

n1 = n//10000000
n2 = n%10000000//1000000
n3 = n%1000000//100000
n4 = n%100000//10000
n5 = n%10000//1000
n6 = n%1000//100
n7 = n%100//10
n8 = n%10

suma = (n8*2) + (n7*3) + (n6*4) + (n5*5) + (n4*6) + (n3*7) + (n2*2) + (n1*3)
a = suma%11
codigo = 11 - a

if codigo == 11:
    codigo = 0
if codigo == 10:
    codigo = "k"
else:
    codigo = codigo

print("dv =",codigo)