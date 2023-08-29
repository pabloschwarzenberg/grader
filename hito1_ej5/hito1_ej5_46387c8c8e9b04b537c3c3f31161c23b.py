#Cálculo del dígito verificador de un rut
Numero = int(input("Ingrese rut: "))
Numero = str(Numero)
a = int(Numero[0])
b = int(Numero[1])
c = int(Numero[2])
d = int(Numero[3])
e = int(Numero[4])
f = int(Numero[5])
g = int(Numero[6])
h = g*2
i = f*3
j = e*4
k = d*5
l = c*6
m = b*7
n = a*2
suma = h+i+j+k+l+m+n
resto = suma%11
res = 11-resto
if res == 5:
    print("dv=k")
elif res == 11:
    print("dv=0")
else:
    print("dv=",res)
