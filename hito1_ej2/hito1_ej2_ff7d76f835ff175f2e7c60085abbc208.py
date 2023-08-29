#Contestador automático

n = int(input("Ingrese número de teléfono >>> "))
h = int(input("Ingrese hora de llamada (formato 24h) >>> "))

primer = int(n/100000)
ultimo = n - int(n/1000)*1000

if 0 <= h <= 7:
    print("CONTESTAR")
elif h < 14:
    if ultimo == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17 <= h <= 19:
    if primer == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
