#Ordenar tres números
a = int(input("Ingrese numero1: "))
b = int(input("Ingrese numero2: "))
c = int(input("Ingrese numero3: "))
if a < b <  c :
    print(a , ",", b, ",", c)
if a <  c <  b : 
  print(a, ",", c, ",", b)
if b <  a <  c :
  print(b, ",", a, ",", c)
if b <  c <  a :
    print(b, ",", c, ",", a)
if c <  a <  b :
    print(c, ",", a, ",", b)
if c <  b <  a :
    print(c, ",", b, ",", a)
if a == c < b :
    print(a, ",", c, ",", b)
if a == c > b :
    print(b, ",", a, ",", c)