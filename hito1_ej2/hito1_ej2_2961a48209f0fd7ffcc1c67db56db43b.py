#Contestador de celular
numero =int(input("Ingrese numero telefonico:"))
hora =int(input("Ingrese hora de la llamada:"))
if (hora >=0 and hora <=7):
    print ("Contestar")
if(hora >=17 and hora <=19):
    if(numero//100000 == 877):
        print("No contestar")
    else:
        print ("Contestar")
if (hora <14):
    if(numero%1000==909):
        print("Contestar")
    else:
        print("No contestar")
if (hora >19):
    print("No contestar")