#Ordenar tres números
print("Ingrese números")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))


if a<=b<=c:
    print(a,",",b,",",c)
elif b<=a<=c:
    print(b,",",a,",",c)
elif b<=c<=a:
    print(b,",",c,",",a)
elif a<=c<=b:
    print(a,",",c,",",b)
elif c<=b<=a:
    print(c,",",b,",",a)
elif c<=a<=b:
    print(c,",",a,",",b)
