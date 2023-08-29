#Cálculo del dígito verificador de un rut
print("calculadora de diito verificador")
run = int(input("ingrese el run sin puntos ni digito verificador : "))
a = (run//10000000)
b = (run//1000000) % 10
c = (run//100000) % 10
d = (run//10000) % 10
e = (run//1000) % 10
f = (run//100) % 10
g = (run//10) % 10
h = (run//1) % 10
a1 = h * 2
b1 = g * 3
c1 = f * 4
d1 = e * 5
e1 = d * 6
f1 = c * 7
g1 = b * 2
h1 = a * 3
suma = (a1+b1+c1+d1+e1+f1+g1+h1)
mod = suma % 11
digito = 11 - mod
if digito == 11 :
    print("dv=0")
else:
    if digito == 10:
        print("dv=k")
    else:
        print("dv=", digito)