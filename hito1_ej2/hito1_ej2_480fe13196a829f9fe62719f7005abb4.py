numero=input("Ingrese numero telefonico")  
hora=input("Ingrese hora de la llamada")
hora=int(hora)
if len(numero)==8:
    if 0<hora<7:
        print("CONTESTAR")
    elif (7<hora<14)and (numero[5:]=="909"):  
        print("CONTESTAR")
    elif 7<hora<14:
        print("NO CONTESTAR") 
    elif 14<hora<17:
        print("NO CONTESTAR")
    elif (17<hora<19)and (numero[:3]=="877"): 
        print("NO CONTESTAR")
    elif 17<hora<19:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("numero no valido")
        
      