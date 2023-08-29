#Contestador de celular
# Por Matías Henríquez Gómez

num = int(input("Ingrese número telefónico: "))
hrs = int(input("Ingrese la hora de llamada: "))


if hrs < 7:
    print("CONTESTAR")
if hrs < 14:
    if num%1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if hrs > 17:
    if hrs < 19:
        if num//10 == 877:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
if hrs > 19:
    print("NO CONTESTAR")