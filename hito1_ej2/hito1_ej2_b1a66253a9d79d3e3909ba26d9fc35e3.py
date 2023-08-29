#Contestador de celular
number = ""
while len(number) != 8:
    number = (input("Inserte su numero de telefono:"))
    if(len(number) != 8):
        print("Tienes que introducir 8 numeros:")

x = []
for n in number:
    x.append(n)
primeros = x[0] + x[1] + x[2]
ultimos = x[5] + x [6] + x[7]

hora = int(input("Ingrese la hora:"))
while hora >= 24:
    if hora >= 24:
        hora = int(input("Ingrese hora entre 0 y 23"))
    elif hora < 0:
        hora = int(input("Ingrese hora entre 0 y 23"))

if (hora > 19):
    print("NO CONTESTAR")
elif (hora >= 0 and hora <= 7):
    print("CONTESTAR")
elif ((ultimos == "909")):
    print("CONTESTAR")
elif (hora < 14):
    print("NO CONTESTAR")
elif ((primeros == "877")):
    print("NO CONTESTAR")
elif (hora >= 17 and hora <= 19):
    print("CONTESTAR")     