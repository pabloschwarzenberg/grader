#Ordenar tres números
a = input("Ingrese el primer numero")
b = input("Ingrese el segundo numero")
c = input("Ingrese el tercer numero")


if a <= b <= c:
  print(a,",",b,",",c)
elif b <= a <= c:
  print(b,",",a,",",c)
elif c <= a <= b:
  print(c,",",a,",",b)
elif a <= c <= b:
  print(a,",",c,",",b)
elif b <= c <= a:
  print(b,",",c,",",a)
elif c <= b <= a:
  print(c,",",b,",",a)