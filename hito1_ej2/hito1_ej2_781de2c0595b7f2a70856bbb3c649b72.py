#Contestador de celular
while(True):
    numero = int(input("Ingrese el numero de telefono porfavor: "))
    hora = int(input("Ingrese la hora de la llamada: "))
    if 1000000000 <= numero or numero <= 9999999 or hora > 23 or hora < 0:
        print("Datos no validos")
    else:
        break

ultCifras = numero% 1000

primCifras = numero // 100000

if hora <= 7 and hora >= 0:
    print("CONTESTAR")

elif hora >= 8 and hora <= 14:
    if ultCifras == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

elif hora >= 17 and hora <= 19:
    if primCifras == 877:
        print("NO CONTESTAR")
    else: 
        print("CONTESTAR")

elif  hora >= 19:
    print("NO CONTESTAR")

