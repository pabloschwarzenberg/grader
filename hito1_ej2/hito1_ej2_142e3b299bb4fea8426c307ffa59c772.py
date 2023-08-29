#Contestador de celular
telefono=int(input("Ingrese un numero de telefono: "))
hora=int(input("ingrese un horario entre (0-23) horas: "))

if (hora>=0 and hora<=7):
    print("Resultado: CONTESTAR")
elif (hora<14):
    if str(telefono)[-3:] == "909":
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif (hora>=17 and hora<=19):
    if str(telefono).startswith("877"):
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")