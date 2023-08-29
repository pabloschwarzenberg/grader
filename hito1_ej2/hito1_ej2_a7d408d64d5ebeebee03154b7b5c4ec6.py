#Contestador de celular
telefono=input("Ingrese numero telefonico: ")
hora=int(input("Ingrese hora de la llamada: "))

while len(telefono)==8 and hora<25:
    if hora<7:
        print("CONTESTAR")
    elif 7<hora<14 and telefono[5::]=='909':
        print("CONTESTAR")
    elif 14<hora<17:
        print("NO CONTESTAR")
    elif 17<hora<19 and telefono[0:3]!='877':
        print("CONTESTAR")
    elif 19<hora<24:
        print("NO CONTESTAR")
    elif 24<hora:
        print("Error")
    else:
        print("NO CONTESTAR")
    break
else: print ("Error")