#Ordenar tres números
a=int(input(" Ingrese el primero número a comparar: "))
b=int(input(" Ingrese el segundo número a comparar: "))
c=int(input(" Ingrese el tercer número a comparar: "))
if((a>=b) & (a>=c)):
    maximo=a
    if(b>=c):
        inter=b
        minimo=c
    else:
        inter=c
        minimo=b
if((b>=a)& (b>=c)):
    maximo=b
    if(a>=c):
        inter=a
        minimo=c
    else:
        inter=c
        minimo=a
if((c>=b)&(c>=a)):
    maximo=c
    if(b>=a):
        inter=b
        minimo=a
    else:
        inter=a
        minimo=b        
print(" El orden creciente de los números es: ", minimo,", ", inter,", ", maximo)

