telefono = input("Ingrese numero telefonico: ")
hora = int(input("Ingrese hora de la llamada: "))

print(telefono[len(telefono)-1])

if(hora <= 7):
    print("CONTESTAR")

if(hora > 7 and hora < 14):
    if(telefono[len(telefono)-3] == "9" and telefono[len(telefono)-2] == "0" and telefono[len(telefono)-1] == "9"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
    # contesto solo si termina en 909

if(hora >= 14 and hora < 17):
    print("NO CONTESTAR")

if(hora >= 17 and hora <= 19):
    if(telefono[0] == "8" and telefono[1] == "7" and telefono[2] == "7"):
        #no conetesto si comienza en 877
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if(hora > 19):
    print("NO CONTESTAR")      