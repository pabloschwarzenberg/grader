#Descomponer un número
n = str(input("introduzca un numero de 4 digitos o menos:\n"))
numero = str(n)

e = numero[0:4]
f = numero[0:3]
g = numero[0:2]
h = numero[0:1]

if n == e  and n != f and n != g and n != h:
    a = numero[0:1]
    b = numero[1:2]
    c = numero[2:3]
    d = numero[3:4]
    print(a, "M +",b,"C +",c,"D +",d,"U")
if n == f and n!= g and n!= h:
    a = numero[0:1]
    b = numero[1:2]
    c = numero[2:3]
    print(a,"C +",b,"D +",c,"U")
if n == g and n != h:
   a = numero[0:1]
   b = numero[1:2]
   print(a,"D +",b,"U")
if n == h:
   a = numero[0:1]
   print(a,"U")






   