#Ordenar tres números
a=int(input("ingresa el primer numero entero: "))
b=int(input("ingresa el segundo numero entero: "))
c=int(input("ingresa el tercer numero entero: "))
if a>=b>=c:
  print(c,",",b,",",a)
elif b>=a>=c:
  print(c,",",a,",",b)
elif b>=c>=a:
  print(a,",",c,",",b)
elif c>=b>=a:
  print(a,",",b,",",c)
elif a>=c>=b:
  print(b,",",c,",",a)
else:
  print(b,",",a,",",c)
  print(c,",",a,",",b)
 