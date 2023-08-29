#Contestador de celular
telefono = (input("Ingrese Numero Telefonico: "))
Hora = int(input("ingrese Hora de llamda: "))

Ultimosnumeros = telefono[-3:]
Primerosnumeros = telefono[:3]

if Hora > 0 and Hora <= 7:
    print("Contestar")

elif Hora > 7 and Hora < 14:
    if Ultimosnumeros == "909":
        print("Contestar")
    else:
        print("no Contestar")
elif Hora > 17 and Hora < 19:
    if Primerosnumeros == "877":
        print("no Contestar")
    else:
        print("Contestar")
elif Hora > 19:
    print("no Contestar")