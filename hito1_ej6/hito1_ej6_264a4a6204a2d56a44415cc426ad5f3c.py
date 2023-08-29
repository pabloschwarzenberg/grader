n1 = eval(input("Por favor ingrese un numero entero: "))
n2 = eval(input("Por favor ingrese un numero entero: "))
n3 = eval(input("Por favor ingrese un numero entero: "))

if(n1 < n2 < n3):
    print(n1, ",", n2, ",", n3)
if(n1 < n3 < n2):
    print(n1, ",", n3, ",", n2)
if(n2 < n1 < n3):
    print(n2, ",", n1, ",", n3)
if(n2 < n3 < n1):
    print(n2, ",", n3, ",", n1)
if(n3 < n1 < n2):
    print(n3, ",", n1, ",", n2)
if(n3 < n2 < n1):
    print(n3, ",", n2, ",", n1)

if(n1 == n2 < n3):
    print(n1, ",", n2, ",", n3)
if(n1 == n2 > n3):
    print(n3, ",", n1, ",", n2)

if(n1 == n3 < n2):
    print(n1, ",", n3, ",", n2)
if(n1 == n3 > n2):
    print(n2, ",", n1, ",", n3)

if(n2 == n3 < n1):
    print(n2, ",", n3, ",", n1)
if(n2 == n3 > n1):
    print(n1, ",", n3, ",", n2)





