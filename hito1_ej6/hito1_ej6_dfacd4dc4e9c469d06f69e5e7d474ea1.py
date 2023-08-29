#Ordenar tres números
a=int(input("ingresa el primer numero: "))
b=int(input("ingresa el segundo numero: "))
c=int(input("ingresa el tercer numero: "))

if a<=b<=c:
    print(a,",",b,",",c)
elif a<=c<=b:
    print(a, ",", c, ",", b)
elif b<=c<=a:
    print(b, ",", a, ",", c)
elif b<=a<=c:
    print(b, ",", a, ",", c)
elif c<=a<=b:
    print(c, ",", a, ",", b)
elif c<=b<=a:
    print(c, ",", b, ",", a)