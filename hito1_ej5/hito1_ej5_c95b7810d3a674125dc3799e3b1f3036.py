#Cálculo del dígito verificador de un rut
# input
x = int(input("ingresa tu rut sin el digito verificador: "))

# descomposicion
q = x//10000000
w = (x - q*10000000) // 1000000
e = (x - q*10000000 - w*1000000) // 100000
r = (x - q*10000000 - w*1000000 - e*100000) // 10000
t = (x - q*10000000 - w*1000000 - e*100000 - r*10000) // 1000
y = (x - q*10000000 - w*1000000 - e*100000 - r*10000 - t*1000) // 100
u = (x - q*10000000 - w*1000000 - e*100000 - r*10000 - t*1000 - y*100) // 10
i = (x % 10)

# multiplicacion
a = 3 * q
s = 2 * w
d = 7 * e
f = 6 * r
g = 5 * t
h = 4 * y
j = 3 * u
k = 2 * i

# suma de la multiplicacion
p = a+s+d+f+g+h+j+k

# calculo de modulo
m = p % 11

#resultado final
n = 11 - m

#Salida
if n == 10:
    print("dv=k")
elif n == 11:
    print("dv=0")
else:
    print("dv={}".format(n))