#Ordenar tres números
a=0
b=0
c=0
n1=int(input("Ingrese un número entero "))
n2=int(input("Ingrese un segundo número entero "))
n3=int(input("Ingrese un tercer número entero "))
if(n1>=n2 and n1>=n3):
    a=n1
    if(n2>=n3):
        b=n2
        c=n3
    else:
        b=n3
        c=n2
if(n2>=n1 and n2>=n3):
        a=n2
        if(n1>=n3):
            b=n1
            c=n3
        else:
            b=n3
            c=n1
if(n3>=n1 and n3>=n2):
    a=n3
    if(n1>=n2):
        b=n1
        c=n2
    else:
        b=n2
        c=n1
print(c,",",b,",",a)