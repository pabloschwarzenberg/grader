#Contestador de celular
numero=input("Ingrese numero telefonico: ")
hora=int(input("Ingrese hora de la llamada: "))
if (hora>=19):
    print("Resultado: NO CONTESTAR")
elif(hora>=0 and hora<=7):
    print("Resultado: CONTESTAR")
elif((hora>7 and hora<14)):
    if(numero.endswith("909") == True):
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif(hora>=17 and hora<=19):
    if(numero.startswith("877") == True):
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")