#Contestador de celular
telefono1=int(input("ingrese numero telefonico: "))
telefono=[int(a) for a in str(telefono1)]
#es para convertir un numero en una lista con todos los numeros de ese numero
hora=int(input("ingrese hora de llamada: "))


if hora>=0 and hora <=7:
    print("RESULTADO: CONTESTAR")
    
if hora<14:
    if telefono[5]==9 and telefono[6]==0 and telefono[7]==9:
        print("RESULTADO: CONTESTAR")
    else:
        print("RESULTADO: NO CONTESTAR")
        
if hora>=17 and hora<=19:
    if telefono[0]==8 and telefono[1]==7 and telefono[2]==7:
        print("RESULTADO: NO CONTESTAR")
    else:
        print("RESULTADO: CONTESTAR")
        
if hora>19:
    print("RESULTADO: NO CONTESTAR")
     