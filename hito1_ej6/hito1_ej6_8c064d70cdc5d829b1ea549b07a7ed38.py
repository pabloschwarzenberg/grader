a=int(input("Escriba el primer valor entero: "))
b=int(input("Escriba el segundo valor entero: "))
c=int(input("Escriba el tercer valor entero: "))
if(a>b and b>c):
  print(c, b, a)
elif(a>b and b<c):
  print(b, c, a)
elif(b>a and a>c):
  print (c, a, b)
elif(b>a and c>a):
  print (a, c, b)
elif(c>a and a>b):
  print (b, a, c)
elif(c>b and b>a):
  print (a, b, c)
      