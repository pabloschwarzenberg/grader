#Contestador de celular
# Pide al usuario que ingrese el número de teléfono y la hora de la llamada
telefono = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

# Verifica las reglas para determinar si se debe contestar la llamada
if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14 and telefono % 100 == 9:
    print("CONTESTAR")
elif hora >= 17 and hora < 19 and telefono // 1000000 == 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
