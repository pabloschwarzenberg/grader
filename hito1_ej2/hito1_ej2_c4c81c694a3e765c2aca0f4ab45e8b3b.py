#Contestador de celular
# Pedir al usuario que ingrese la hora y el número de teléfono
hora = int(input("Ingrese la hora (entre 0 y 23): "))
numero = input("Ingrese el número de teléfono (8 dígitos): ")

# Verificar si debes contestar o no
if hora >= 0 and hora < 7:
    decision = "CONTESTAR"
elif hora < 14 and numero[-3:] == "909":
    decision = "CONTESTAR"
elif hora >= 17 and hora < 19 and numero[:3] == "877":
    decision = "CONTESTAR"
else:
    decision = "NO CONTESTAR"

# Imprimir la decisión
print(decision)
  