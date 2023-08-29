#Contestador de celular
t= int(input(" Ingrese numero telefonico: "))
hora= int(input(" Ingrese hora de la llamada: "))
telefono= list(str(t))

if hora >= 0 and hora <= 7:
  print ("CONTESTAR")

if hora < 14 and hora > 8:
    if (telefono[5]== "9") and (telefono[6] == "0" ) and (telefono[7]== "9"):
        print ("CONTESTAR")
        
    else:
        print ("NO CONTESTAR")
      
elif hora < 17 and hora > 14:
  print ("NO CONTESTAR")
  
elif hora >= 17 and hora <=19:
    if (telefono[0]== "8") and (telefono[1] == "7") and (telefono[2]== "7"):
        print ("NO CONTESTAR") 
    else:
      print ("CONTESTAR")

elif hora > 19:
    print ("NO CONTESTAR")

    