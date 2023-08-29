#Contestador de celular
TELEFONO = (input("Ingresa un numero de telefono: "))
HORA = int(input("Ingrese la hora de la llamada: "))

Ultimos_Numeros_Del_Telefono = TELEFONO[-3:]
Primeros_Numeros_Del_Telefono = TELEFONO[:3]

if HORA > 0 and HORA <= 7:
    print("CONTESTAR")

elif HORA > 7 and HORA < 14:
    if Ultimos_Numeros_Del_Telefono == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif HORA > 17 and HORA < 19:
    if Primeros_Numeros_Del_Telefono == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif HORA > 19:
    print("NO CONTESTAR")