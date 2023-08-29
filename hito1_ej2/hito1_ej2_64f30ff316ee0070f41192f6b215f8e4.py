numero_telefono=input("Ingresa Numero Telefonico: ")
Emergencia=int(numero_telefono[:3])
Emergencia2=int(numero_telefono[5:])

Numero_Final=int(numero_telefono[:5])
Hora=int(input("Ingresa Hora llamado: "))
##print(Emergencia)
##print(Emergencia2)



if Hora >= 0 and Hora <= 7:
    print("CONTESTAR")

elif Hora < 14 and Emergencia2 != 909:
    print("NO CONTESTAR")

elif Hora < 14 and Emergencia2 == 909:
    print("CONTESTAR")

elif Hora >= 17 and Hora <= 19 and Emergencia != 877:
    print("CONTESTAR")

elif Hora >= 17 and Hora <= 19 and Emergencia == 877:
    print("NO CONTESTAR")

elif Hora > 19:
    print("NO CONTESTAR")
