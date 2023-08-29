#Ordenar tres números
a = int(input("Ingrese un numero"))
b = int(input("Ingrese un numero"))
c = int(input("Ingrese un numero"))
if a<=b<=c:
  print(a,",",b,",",c)
elif b<=a<=c:
  print(b,",",a,",",c)
elif c<=a<=b:
  print(c,",",a,",",b)
elif b<=c<=a:
  print(b,",",c,",",a)
elif c<=b<=a:
  print(c,",",b,",",a)
elif a<=c<=b:
  print(a,",",c,",",b)
 
  