#calculadora
print("ingresa una cantidad de numeros y el numero final debe -1")
print("-1 indica el termino del programa")
suma=0
n=1
z=0
while n>0:
    m=float(input("ingresa un numero:"))

    if m!=-1:
        z=z+1
        suma=suma+m
       

    elif m==-1 :
        n=n-1

    if z==0:
        print("cantidad:",0)
        print("promrdio: nd")
        print("minimo: nd")
        break

print("cantidad:",z)
if z!=0:
    print("el promedio es:", (suma)/z)
