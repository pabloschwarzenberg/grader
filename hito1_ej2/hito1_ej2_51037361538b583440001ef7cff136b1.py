#Contestador

cadena = input("Ingrese numero de telefono que llama: ")
numero = int(cadena)
#12345678
print(">")
print(cadena[5:8])
print("<")

#numero = int(input("Ingrese numero de telefono que llama: "))
hora = int(input("Ingrese hora de llamada (sin minutos): "))
if numero >= 100000000 or numero < 1:
    print("Numero ingresado es inválido")
elif hora > 23 or hora < 0:
    print("Hora ingresada es inválida")
elif hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora > 7 and hora < 14 and cadena[5:8] == "909":
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and cadena[1:3] == "877*":
    print("CONTESTAR")
elif hora > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
