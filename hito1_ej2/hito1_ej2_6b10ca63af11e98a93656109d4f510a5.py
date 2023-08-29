#Contestador de celular
Telefono = str(input("numero telefonico: "))
hora = int(input("hora de llamada: "))

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