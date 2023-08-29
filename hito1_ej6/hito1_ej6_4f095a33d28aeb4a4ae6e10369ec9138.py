#Ordenar tres números
a=int(input("ingrese un numero a"))
b=int(input("ingrese un numero b"))
c=int(input("ingrese un numero c"))
if int(a)>=int(b)>=int(c):
  print(c,",",b,",",a)
  
if int(c)>=int(b)>=int(a):
  print(a,",",b,",",c)
  
if int(b)>=int(a)>=int(c):
  print(c,",",a,",",b)
  
if int(c)>=int(a)>=int(b):
  print(b,",",a,",",c)

if int(b)>=int(c)>=int(a):
  print(a,",",c,",",b)
  
if int(a)>=int(c)>=int(b):
  print(b,",",c,",",a)
  