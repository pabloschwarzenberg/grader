#Ordenar tres números
a=int(input("Ingrese primer numero: "))
b=int(input("Ingrese segundo numero: "))
c=int(input("Ingrese tercer  numero: "))
d=0

while d <= 0 :
    if b < a :
        aux = b
        b = a
        a = aux
    elif c < a :
        aux = c
        c = a
        a = aux
    elif c < b :
        aux = b
        b = c
        c = aux
    else:
        d = 1

print(a,",",b,",",c)
      