#Contestador de celular
hora = int(input("Ingrese la hora de la llamada (en formato 24 horas): "))
telefono = int(input("Ingrese el número de teléfono (de 8 cifras): "))

# Se comprueba si se debe contestar o no
if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14 and telefono % 1000 == 909:
    print("CONTESTAR")
elif hora >= 17 and hora < 19 and telefono // 1000000 == 877:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
