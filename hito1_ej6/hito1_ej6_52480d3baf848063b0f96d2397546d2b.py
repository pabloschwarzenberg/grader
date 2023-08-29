#Ordenar tres números
print("Introduce el primer numero")
a = int(input())
print("Introduce el segundo numero")
b = int(input())
print("Introduce el tercer numero")
c = int(input())

if(a < b and b < c):
  print(a,",",b,",",c)
elif(a < c and c < b):
  print(a,",",c,",",b)
elif(b < a and a < c):
  print(b,",",a,",",c)
elif(b < c and c < a):
  print(b,",",c,",",a)
elif(c < a and a < b):
  print(c,",",a,",",b)
elif(c < b and b < a):
  print(c,",",b,",",a)
elif(a == b and b < c):
  print(a,",",b,",",c)
elif(a == c and c < b):
  print(a,",",c,",",b)
elif(b == c and c < a):
  print(b,",",c,",",a)
elif(a == b and b > c):
  print(c,",",a,",",b)
elif(a == c and c > b):
  print(b,",",a,",",c)
elif(c == b and a < c):
  print(a,",",b,",",c)
elif(a == b and b == c):
  print(a,",",b,",",c)