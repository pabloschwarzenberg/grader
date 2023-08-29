#Contestador de celular
cel = int(input("Ingrese el numero telefonico: "))
hora = int(input("Ingrese la hora de la llamada: "))

if hora >= 0 and hora <=6:
    print("Resultado: CONTESTAR")

if hora >= 7 and hora <=13 and cel % 1000 == 909:
    print("Resultado: CONTESTAR")
elif hora >= 7 and hora <=13 and cel % 1000 != 909:
    print("Resultado: NO CONTESTAR")

if hora >=17 and hora <=18 and cel//100000 == 877:
    print("Resultado: NO CONTESTAR")
elif hora >=17 and hora <=18 and cel//100000 != 877:
    print("Resultado: CONTESTAR")

if hora >=19 and hora <=23:
    print("Resultado: NO CONTESTAR")