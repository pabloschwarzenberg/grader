#Ordenar tres números
a=int(input("primer número:"))
b=int(input("segundo número:"))
c=int(input("tercer número:"))
if a>b and a>c:
   if b>c:
      print(str(c)+","+str(b)+","+str(a))
   else:
      print(str(b)+","+str(c)+","+str(a))
if b>a and b>c:
   if a>c:
      print(str(c)+","+str(a)+","+str(b))
   else:
      print(str(a)+","+str(c)+","+str(b))
if c>a and c>b:
   if a>b:
      print(str(b)+","+str(a)+","+str(c))
   else:
      print(str(a)+","+str(b)+","+str(c))
