#Ordenar tres números
a = int(input("Número 1: "))
b = int(input("Número 2: "))
c = int(input("Número 3: "))
if a>=b>=c:
    print(c,",",b,",",a)
elif a>=c>=b:
    print(b,",",c,",",a)
elif b>=a>=c:
    print(c,",",a,",",b)
elif b>=c>=a:
    print(a,",",c,",",b)
elif c>=a>=b:
    print(b,",",a,",",c)
elif c>=b>=a:
    print(a,",",b,",",c)
  