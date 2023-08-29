#Ordenar tres números
a = int(input("incerte n 1: "))
b = int(input("incerte n 2: "))
c = int(input("incerte n 3: "))
if a<b<c:
  print(a,b,c)
elif b<a<c:
  print(b,a,c)
elif c<a<b:
   print(c,a,b)
elif a<c<b:
  print(a,c,b)
elif b<c<a:
  print(b,c,a)
elif c<b<a:
  print(c,b,a)
 
      