# Entrada
tel = int(input("ingrese numero telefónico: "))
hora = int(input("ingrese hora de la llamada: "))

# Procesamiento del problema
tel_909 = int(tel % 1000)
tel_877 = int(tel // 100000)

if 0 <= hora <= 7:
    print("CONTESTAR")

elif (hora <= 14) and (tel_909 == 909):
    print("CONTESTAR")

elif (17 <= hora <= 19 and tel_877 != 877):
    print("CONTESTAR")

elif (hora > 19):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")

