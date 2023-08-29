#Ordenar tres números
a=int(input("coloque un numero"))
b=int(input("coloque otro numero"))
c=int(input("y el ultimo numero"))
if(a<b<c):
  print(a,b,c)
elif(a>c>b):
  print(b,c,a)
elif(c>a>b):
  print(b,a,c)
elif(b>c>a):
  print(a,c,b)
elif(b>a>c):
  print(c,a,b)
elif(c>b>a):
  print(a,b,c)