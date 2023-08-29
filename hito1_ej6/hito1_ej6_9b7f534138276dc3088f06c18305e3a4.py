#Ordenar tres números
a=input("ingrese primer valor:")
b=input("ingrese segundo valor:")
c=input("ingrese tercer valor:")
c=int(c)
b=int(b)
a=int(a)
if a>=b:
    if b>=c:
        print(c,",",b,",",a)
    else:
        if a>=c:
            print(b,",",c,",",a)
        else:
            print(b,",",a,",",c)
else:
    if a>=c:
        print(c,",",a,",",b)
    else:
        if b>=c:
            print(a,",",c,",",b)
        else:
            print(a,",",b,",",c)
      