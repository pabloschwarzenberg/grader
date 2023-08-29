NroTelefono = int(input("Ingrese el número que llama: "))
Hora = int(input("Ingrese hora de la llamada "))

Nro = NroTelefono %1000
NroCom = NroTelefono - (NroTelefono % 100000)
NroCom2 = NroCom/100000

print(NroCom2)
if Hora <= 7 and Hora >= 0:
    print("Contestar")
elif Hora <= 14 and Nro == 909:
    print("Contestar")
elif Hora <= 14:
    print("No contestar")
elif Hora >= 17 and Hora <= 19 and NroCom2 == 877:
    print("No contestar")
elif Hora >= 17 and Hora <= 19:
    print("Contestar")
else:
    print("No contestar")