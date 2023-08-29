#Contestador de celular
Telefono = (input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de llamda: "))

Ultimosnumeros = Telefono[-3:]
Primerosnumeros = Telefono[:3]

if hora > 0 and hora <= 7:
    print("contestar")

elif hora > 7 and hora < 14:
    if Ultimosnumeros == "909":
        print("contestar")
    else:
        print("no contestar")
elif hora > 17 and hora < 19:
    if Primerosnumeros == "877":
        print("no contestar")
    else:
        print("contestar")
elif hora > 19:
    print("no contestar")