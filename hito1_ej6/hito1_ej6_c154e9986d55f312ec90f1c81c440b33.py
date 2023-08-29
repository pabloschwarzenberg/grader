#Ordenar tres números
a = int(input("Ingrese nro 1 ->"))
b = int(input("Ingrese nro 1 ->"))
c = int(input("Ingrese nro 1 ->"))

if ((a <= b) and (a <= c)):
  if(b <= c):
    print(a,",",b,",",c)
  else:
    print(a,",",c,",",b)

if ((b <= a) and (b <= c)):
  if(a <= c):
    print(b,",",a,",",c)
  else:
    print(b,",",c,",",a)

if ((c <= b) and (c <= a)):
  if(b <= a):
    print(c,",",b,",",a)
  else:
    print(c,",",a,",",b)
    
