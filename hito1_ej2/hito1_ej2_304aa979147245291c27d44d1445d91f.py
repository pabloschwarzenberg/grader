#Contestador de celular
print("\nContestador automatico\n")
numero=int(input("\nIndique el numero que está llamando: "))
hora= int(input("Indique la hora actual (en formato de 0 a las 23 Hrs): "))


ultimosdecimal= numero*0.001 #chamullo para obtener los ultimos 3 digitos del numero de telefono
parteentera= int(numero*0.001)#chamullo para obtener los ultimos 3 digitos del numero de telefono

ultimosdigistos= round(((ultimosdecimal-parteentera)*1000),0)

primerosfigitos= int(numero*0.00001)

print("")#para dejar un espacio de una linea 

print(ultimosdigistos)
if (hora>=0 and hora<=7):
    print("CONTESTAR")

elif(hora <14 and ultimosdigistos==909):
    print ("CONTESTAR")

elif (hora>=17 and hora <=19):
    if (primerosfigitos == 877):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
    