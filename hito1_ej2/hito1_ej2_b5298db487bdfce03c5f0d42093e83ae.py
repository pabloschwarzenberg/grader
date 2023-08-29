#Contestador de celular
numero = str(input("Ingrese el numero: "))

hora = int(input("Hora a la que llama: "))

comienzo = int(numero[0:3])
fin = int(numero[5:9])

if hora >= 0 and hora <=7:
    print("CONTESTAR")
elif hora < 14 and fin != 909:
    print("NO CONTESTAR")
elif hora >= 17 and hora <=19 and comienzo == 877:
    print("NO CONTESTAR")
elif hora > 19:
    print("NO CONTESTAR")
else:
    print("CONTESTAR")      