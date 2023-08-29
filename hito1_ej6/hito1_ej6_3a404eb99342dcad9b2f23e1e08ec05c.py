#Ordenar tres números

a=int(input("introduzca un numero"))
b=int(input("introduzca un numero"))
c=int(input("introduzca un numero"))
if a<=b<=c:
  print(a,b,c,sep=",")
if a<=c<=b:
  print(a,c,b,sep=",")
if b<=a<=c:
  print(b,a,c,sep=",")
if b<=c<=a:
  print(b,c,a,sep=",")
if c<=b<=a:
  print(c,b,a,sep=",")
if c<=a<=b:
  print(c,a,b,sep=",")