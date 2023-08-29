#Ordenar tres números
print("le ordenare 3 numeros enteros de menor a mayor")
a = int(input("escriba el primer numero entero"))
b = int(input("escriba el segundo numero entero"))
c = int(input("escriba el tercer numero entero"))
if(a>b and b>c):
  print("el orden seria",c,",",b,",",a)
if(a>c and c>b):
  print("el orden seria",b,",",c,",",a)
if(b>a and a>c):
  print("el orden seria",c,",",a,",",b)
if(b>c and c>a):
  print("el orden seria",a,",",c,",",b)
if(c>a and a>b):
  print("el orden seria",b,",",a,",",c)
if(c>b and b>a):
  print("el orden seria",a,",",b,",",c)