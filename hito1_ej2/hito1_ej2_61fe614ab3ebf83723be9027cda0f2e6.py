telefono=input("Ingrese el numero de 8 digitos: ")
hora=int(input("Ingrese la hora de la llamada en horas de 0 a 23: "))
len(telefono)
if(len(telefono)==8):
    print("Verificando el numero de la llamada...")
else:
    print("Numero incorrecto, vuelva a ingresar el numero")
if(0<=hora<=23):
    print("Redirigiendo la llamada...")
else:
    print("La hora ingresada no es correcta")
if(0<=hora<=7):
    print("CONTESTAR")
elif(7<hora<14 and telefono[5:9]==909):
    print("CONTESTAR")
elif(7<hora<14):
    print("NO CONTESTAR")
elif(14<=hora<17):
    print("CONTESTAR")
elif(17<=hora<=19 and telefono[0:4]==877):
    print("NO CONTESTAR")
elif(17<=hora<=19):
    print("CONTESTAR")
if(19<hora<=23):
    print("NO CONTESTAR")
else:
    print()