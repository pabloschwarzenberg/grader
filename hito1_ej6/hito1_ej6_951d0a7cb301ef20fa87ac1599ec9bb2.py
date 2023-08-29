#Ordenar tres números
a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
c=int(input("ingrese el tercer numero: "))
f=min(a, b, c)
g=max(a, b, c)
h=(a+b+c)-a-c
print("los numeros ordenados son: {}, {}, {}".format(f, h, g))