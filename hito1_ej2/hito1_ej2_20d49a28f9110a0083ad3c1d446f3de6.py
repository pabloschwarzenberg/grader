#Contestador de celular
XXXXXXXX = int(input("ingresa numero de telefono: "))
Y = int(input("ingrese hora de la llamada: "))

caso_1 = XXXXXXXX%1000
caso_2 = XXXXXXXX//100000

if 0 <= Y <= 7:
    print("Contestar")
if 7 <= Y < 24:
    if caso_1 == 909:
        print("Contestar")
    else:
        print("No contestar")
if 17 <= Y <=19:
    if caso_2 == 877:
        print("No contestar")
    else:
        print("Contestar")
if 19 <= Y <= 23:
    print("No contestar")      