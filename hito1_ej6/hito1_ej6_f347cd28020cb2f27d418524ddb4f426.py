#Ordenar tres números
a= int(input("Ingrese primer numero: "))
b= int(input("Ingrese segundo numero: "))
c= int(input("Ingrese tercer numero: "))
if a<b<c and b==c:
    print(a, end=",")
    print(b, end=",")
    print(c)
elif a<b<c:
    print(a, end=",")
    print(b, end=",")
    print(c)
elif b<a<c and a==c:
    print(b, end=",")
    print(a, end=",")
    print(c)
elif b<c<a and a==c:
    print(b, end=",")
    print(c, end=",")
    print(a)
elif c<a<b and a==b:
    print(c, end=",")
    print(a, end=",")
    print(b)
elif c<b<a or b==a:
    print(c, end=",")
    print(b, end=",")
    print(a)
elif b>a and a==c:
    print(a, end=",")
    print(c, end=",")
    print(b)
elif b>a and a==c:
    print(a, end=",")
    print(c, end=",")
    print(b)
elif a<b and a==c:
    print(a, end=",")
    print(c, end=",")
    print(b)
elif a<b and b>c:
    print(a, end=",")
    print(c, end=",")
    print(b)
elif a==c and a>b:
    print(b, end=",")
    print(a, end=",")
    print(c)
elif a>b and b<c and a>c:
    print(b, end=",")
    print(c, end=",")
    print(a)