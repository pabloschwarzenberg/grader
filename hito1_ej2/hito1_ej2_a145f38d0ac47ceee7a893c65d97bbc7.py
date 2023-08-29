#Contestador de celular
numero=(str(input("numero telefonico de 8 digitos ",)))
hora=int(input("ingrese la hora de llamada ",))
if(0<hora<7):
    print("contestar, podria ser una emergencia")
elif(7<=hora<=14) and (int(numero[5:8])==909):
    print("contestar")
elif(17<=hora<=19):

    if(int(numero[0:3])==877):
        print("no contestar")
    else:
        print("contestar")
elif(hora>19):
    print("no contestar")