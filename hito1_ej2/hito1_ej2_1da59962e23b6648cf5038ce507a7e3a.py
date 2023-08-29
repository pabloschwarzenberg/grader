#Contestador de celular
while True:
    while True:
        numero=int(input("Ingrese número de 8 digitos: "))
        temporal=str(numero)
        if len(temporal)==8:
            break
        else:
            print("ingrese nuevamente")
    while True:
        hora=int(input("Ingrese la hora de la llamada: "))
        if(hora>23 and hora<0):
            print("intente nuevamente")
        else:
            break
    temp1=temporal[0:3]
    temp2=temporal[5:8]
    if(hora<7):
        print("Contestar")
        break
    elif(hora<=14 and temp2=="909"):
        print("Contestar")
        break
    elif(hora>=17 and hora<=19):
        if(temp1=="877"):
            print("No contestar")
            break
        else:
            print("contestar")
            break
    else:
        print("No contestar")
        break   