#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if a<=b<=c:
  print(str(a)+","+str(b)+","+str(c))
elif b<=a<=c:
  print(str(b)+","+str(a)+","+str(c))
elif b<=c<=a:
  print(str(b)+","+str(c)+","+str(a))
elif c<=a<=b:
  print(str(c)+","+str(a)+","+str(b))
elif c<=b<=a:
  print(str(c)+","+str(b)+","+str(a))
elif a<=c<=b:
  print(str(a)+","+str(c)+","+str(b))
  