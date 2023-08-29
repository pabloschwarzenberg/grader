#Contestador de celular
num = int(input("Ingresa el numero: "))
hora = int(input("Ingresa la hora:"))
if(len(str(num)) != 8):
    print("Numero erroneo, intente de nuevo.")
elif(hora > 23 or hora < 0):
    print("Hora erronea, intente nuevamente.")
else:
    if(hora >= 0 and hora <= 7):
        print("CONTESTAR")
    elif(hora == 14):
        if(str(num)[-3:] == "909"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif(hora >= 17 and hora <= 19):
        if(str(num)[:3] == "877"):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    elif(hora >= 19 and hora >= 0):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")