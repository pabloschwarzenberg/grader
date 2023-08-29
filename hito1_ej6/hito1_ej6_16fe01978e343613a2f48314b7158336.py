#Ordenar tres números
a = int(input("Ingrese su primer número:"))
b = int(input("Ingrese su segundo número:"))
c = int(input("Ingrese su tercer número:"))
if a<b and b<c:
      print(a,b,c)
if a<c and c<b:
      print(a,c,b)
if b<a and a<c:
      print(b,a,c)
if b<c and c<a:
      print(b,c,a)
if c<a and a<b:
      print(c,a,b)
if c<b and b<a:
      print(c,b,a)
if a<b and b==c:
      print(a,b,c)
if b<a and a==c:
      print(b,a,c)
if c<b and a==b:
      print(c,b,a)
if a==b and b<c:
      print(a,b,c)
if a==c and c<b:
      print(a,c,b)
if b==c and c<a:
      print(b,c,a)
if a==b==c:
      print(a,b,c)