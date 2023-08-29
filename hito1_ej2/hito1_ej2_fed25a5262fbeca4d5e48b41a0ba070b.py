#Contestador de celular
while True:
    while True:
        telefono=int(input("Ingrese numero telefonico: "))
        temporal=str(telefono)
        if len(temporal)==8:
            print("numero ok")
            break
        else:
            print("ingrese nuevamente")
    while True:
        hora=int(input("Ingrese hora de la llamada: "))
        if(hora>24 or hora<0):
            print("intente nuevamente")
        else:
            break
    temp1=temporal[0:3]
    temp2=temporal[5:8]
    if(hora<7):
        print("Resultado: CONTESTAR")
    elif(hora<=14 and temp2=="909"):
        print("Resultado: CONTESTAR")
    elif(hora>=17 and hora<=19):
        if(temp1=="877"):
            print("Resultado: NO CONTESTAR")
        else:
            print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")