#Contestador de celular
tel = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if 0 < hora < 7:
    print ("CONTESTAR")

elif hora > 19:
    print ("NO CONTESTAR")

elif hora < 14 and (tel - 909)%100 == 0:
    print ("CONTESTAR")
    
elif hora < 14 and (tel - 909)%100 != 0:
    print ("NO CONTESTAR")
    
elif 17 < hora < 19 and (tel - 877)%100 == 0:
    print ("CONTESTAR")

elif 17 < hora < 19 and (tel - 877)%100 != 0:
    print ("NO CONTESTAR")
      