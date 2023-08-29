#Ordenar tres números
      a= (float(input("ingrese el primer número: ")))
b= (float(input("ingrese el segundo número: ")))
c= (float(input("ingresa el tercer numero")))
if(a>b) and (b>c):
    print((a),(b),(c))
if(a>b) and (c>b):
    print((a,c,b))

if(b>a) and (a>c):
    print(b,a,c)
if(b>a) and (c>a):
    print((b,c,a))
if(c>a) and (a>b):
    print((c,a,b))
if(c>a) and (b>a):
    print((c),(b),(a))