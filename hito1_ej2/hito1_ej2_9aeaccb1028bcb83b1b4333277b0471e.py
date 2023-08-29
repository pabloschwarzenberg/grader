#Contestador de celular
number=(input("Ingrese su numero de telefono: "))

hora=int(input("Ingrese la hora de la llamada: "))

last = number[-3:]
first = number[:3]

if (hora > 0 and hora <= 7):
    print("CONTESTAR")

elif (hora > 7 and hora < 14 ):
    if last == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif (hora > 17 and hora < 19):
    if first == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif (hora > 19):
      print("NO CONTESTAR")      