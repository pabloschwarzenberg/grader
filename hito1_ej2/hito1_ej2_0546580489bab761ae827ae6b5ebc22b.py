#Contestador de celular
n = int(input("Ingresa el numero de celular: "))
h = int(input("Ingrese hora de la llamada (0-23)"))

if 0 <= h <= 7:
    print("CONTESTAR")
elif 7 < h < 14:
    if int(str(n)[5:]):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 <= h <= 19:
    if int(str(n)[:3]):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif h > 19:
    print("NO CONTESTAR")
