# se definen las variables
a = int(input("ingrese un primer valor:"))
b = int(input("ingrese un segundo valor:"))
c = int(input("ingrese un tercer valor:"))

#se analizan las variables para dar orden
if (a < b) and (b < c):
    print(a ,",", b ,",", c)
if (a < c) and (c < b):
    print(a, ",", c, ",", b)
if (b < a) and (a < c):
    print(b, ",", a, ",", c)
if (b < c) and (c < a):
    print(b, ",", c, ",", a)
if (c < a) and (a < b):
    print(c, ",", a, ",", b)
if (c < b) and ( b < a):
    print(c, ",", b, ",", a)
#en caso de que dos numeros sean iguales
if (a == b) and (a < c):
    print(a, ",", b, ",", c)
if (a == b) and (a > c):
    print(c, ",", a, ",", b)
if (b == c) and (b < a):
    print(b, ",", a, ",", c)
if (b == c) and (b > a):
    print(a, ",", b, ",", c)
if (c == a) and (c < b):
    print(c, ",", b, ",", a)
if (c == a) and (c > b):
    print(b, ",", a, ",", c)