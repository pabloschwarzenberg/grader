#Contestador de celular
t = int(input("Ingrese número telefónico: "))
h = int(input("Ingrese la hora: "))

primero = int(t/100000)
ultimo = t - int(t/1000)*1000

if 0 <= h <= 7:
    print("CONTESTAR")
elif h < 14:
    if ultimo == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 <= h <= 19:
    if primero == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")