#Ordenar tres números
entero1=int(input("Ingrese un entero: "))
entero2=int(input("Ingrese otro entero: "))
entero3=int(input("Ingrese un último entero: "))
a1=","
if entero1 <= entero2 and entero1 <= entero3:
    if entero2 <= entero3:
        print(entero1,a1,entero2,a1,entero3)
    else:
        print(entero1,a1,entero3,a1,entero2)
elif entero2 <= entero1 and entero2 <= entero3:
    if entero1 <= entero3:
        print(entero2,a1,entero1,a1,entero3)
    else:
        print(entero2,a1,entero3,a1,entero1)
else:
    if entero1 <= entero2:
        print(entero3,a1,entero1,a1,entero2)
    else:
        print(entero3,a1,entero2,a1,entero1)