#Contestador de celular
numero_telefono = (input("ingrese el numero telefonico: "))
numero_hora = int(input("ingrese la hora de llamada: "))

Ultimosnumeros = numero_telefono[-3:]
Primerosnumeros = numero_telefono[:3]

if numero_hora > 0 and numero_hora <= 7:
    print("CONTESTAR")

elif numero_hora > 7 and numero_hora < 14:
    if Ultimosnumeros == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif numero_hora > 17 and numero_hora < 19:
    if Primerosnumeros == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif numero_hora > 19:
    print("NO CONTESTAR")      