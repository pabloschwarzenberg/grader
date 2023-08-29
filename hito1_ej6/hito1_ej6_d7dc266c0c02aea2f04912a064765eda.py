#Ordenar tres números
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

if a >= b and a >= c:
    if b > c:
        print(c,",", b,",", a)
    else:
        print(b,",", c,",", a)
elif b >= a and b >= c:
    if a > c:
        print(c,",", a,",", b)
    else:
        print(a,",", c,",", b)
elif c >= a and c >= b:
    if a > b:
        print(b,",", a,",", c)
    else: 
        print(a,",", b,",", c)