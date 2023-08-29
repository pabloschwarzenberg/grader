a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))
a=min(a,b,c)
c=max(a,b,c)
b=(a + b + c) - a - c
print(a,b,c)