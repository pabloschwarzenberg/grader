#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese su rut sin codigo verificador: "))

#Descomposicion

q = rut//10000000
w = (rut - q*10000000) // 1000000
e = (rut - q*10000000 - w*1000000) // 100000
r = (rut - q*10000000 - w*1000000 - e*100000) // 10000
t = (rut - q*10000000 - w*1000000 - e*100000 - r*10000) // 1000
y = (rut - q*10000000 - w*1000000 - e*100000 - r*10000 - t*1000) // 100
u = (rut - q*10000000 - w*1000000 - e*100000 - r*10000 - t*1000 - y*100) // 10
i = (rut % 10)

#Multiplicacion

a = 3 * q
s = 2 * w
d = 7 * e
f = 6 * r
g = 5 * t
h = 4 * y
j = 3 * u
k = 2 * i

#Suma

p = a+s+d+f+g+h+j+k

#Modulo

m = p % 11

#Resultado

n = 11 - m

#Salida

if n == 10:
    print("dv=k")
elif n == 11:
    print("dv=0")
else:
    print("dv={}".format(n))