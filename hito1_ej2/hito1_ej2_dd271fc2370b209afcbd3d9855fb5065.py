#Contestador de celular
n = int(input("Ingrese numero telefonico: "))
h = int(input("Ingrese la hora de llamada: "))

if h < 0 and h > 23:
    print("Numero no valido")
elif h >= 0 and h <= 7:
    print("CONTESTAR")
elif h >= 7 and h < 14:
    utd = str(n)[-3:]
    if utd == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif h >= 17 and h <= 19:
    ptd = str(n)[:3]
    if ptd == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")