telefono=0
hora=0
telefono=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese  hora de la llamada: "))

fin=(str(telefono)[-3])
inicio=(str(telefono)[1:3])

if (hora>=0) and (hora<=7):
    print("CONTESTAR")
elif (hora<=14) and ((fin)!='909'):
    print("CONTESTAR")
elif (hora>=17) and (hora<=19) and ((inicio)!='877'):
    print("NO CONTESTAR")
elif (hora>19):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
