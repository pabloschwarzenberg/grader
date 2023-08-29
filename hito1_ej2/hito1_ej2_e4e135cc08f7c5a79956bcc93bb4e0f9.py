#Contestador de celular
telefono = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
if (0<hora<7):
  print ("CONTESTAR")
elif(hora<14):
    numero_termino=str(telefono)
    Numero_termino=numero_termino[5:8]
    if(Numero_termino=="909"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif(hora<17):
    print("NO CONTESTAR")
elif(17<=hora<=19):
    numero_inicio=str(telefono)
    Numero_inicio=numero_inicio[0:3]
    if(Numero_inicio=="877"):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif(hora>19):
    print("NO CONTESTAR")
    