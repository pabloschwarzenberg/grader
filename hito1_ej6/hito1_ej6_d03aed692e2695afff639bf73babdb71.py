# Ordenar tres números
a = int(input("ingrese un numero:"))
b = int(input("ingrese un numero:"))
c = int(input("ingrese un numero:"))
if a <= b and a < c and b <= c:  # abc
    print(a, ",", b, ",", c)
if a < b and a <= c and b >= c:  # acb
    print(a, ",", c, ",", b)
if a >= b and a <= c and b > c:  # bac
    print(b, ",", a, ",", c)
if a >= b and a > c and b <= c:  # bca
    print(b, ",", c, ",", a)
if a <= b and a >= c and b > c:  # cab
    print(c, ",", a, ",", b)
if a >= b and a > c and b >= c:  # cba
    print(c, ",", b, ",", a)


      