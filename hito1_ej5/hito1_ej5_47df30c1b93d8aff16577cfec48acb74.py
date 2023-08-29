#Cálculo del dígito verificador de un rut
rut = int(input("ingrese el rut: "))
print("descomponer rut")
print("descomposicion del rut ", rut//10000000)
print("descomposicion del rut ", rut//1000000)
print("descomposicion del rut ", rut//100000)
print("descomposicion del rut ", rut//10000)
print("descomposicion del rut ", rut//1000)
print("descomposicion del rut ", rut//100)
print("descomposicion del rut ", rut//10)
print("descomposicion del rut ", rut//1)

a= (rut//10000000) * 3
print("resultado de a: ",a)

b= ((rut//1000000)%10) * 2
print("resultado de b: ",b)

c= ((rut//100000)%10) * 7
print("resultado de c: ")

d= ((rut//10000)%10) * 6
print("resultado de d: ")

e = ((rut//1000)%10) * 5
print("resultado de e: ")

f = ((rut//100)%10) * 4
print("resultado de f: ")

g = ((rut//10)%10) * 3
print("resultado de g: ")

h = ((rut//1)%10) * 2
print("resultado de h: ")

suma=(a+b+c+d+e+f+g+h)
resto1 = suma // 11
resto2 = suma-(11*resto1)
resta = 11-resto2

if resta == 11:
    print("dv=",end="")
    print(0)
elif resta == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(resta)
