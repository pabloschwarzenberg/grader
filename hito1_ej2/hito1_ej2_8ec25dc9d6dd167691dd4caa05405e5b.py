numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora < 7:
    resultado = ("CONTESTAR")
elif hora < 14 and numero % 1000 == 909:
    resultado = ("CONTESTAR")
elif hora >= 17 and hora < 19 and numero // 1000000 == 877:
    resultado = ("CONTESTAR")
else:
    resultado = ("NO CONTESTAR")

print("Resultado:", resultado)