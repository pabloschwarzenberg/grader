#Ordenar tres números
print("Ordenando de menor a mayor los números enteros a, b y c")
a=int(input("Ingrese a= "))
b=int(input("Ingrese b= "))
c=int(input("Ingrese c= "))

if a<b:
    if b<c:
        print(a,", ", b,", ", c)
    else:
        if c<a:
            print(c,", ", a,", ", b)
        else:
            print(a,", ", c,", ", b)

if a>b:
    if b>c:
        print(c,", ", b, ", ", a)
    else:
        if c>a:
            print(b,", ", a, ", ", c)
        else:
            print(b,", ",c, ", ", a)
    
if a==b==c:
    print("Los números ingresados son iguales")
