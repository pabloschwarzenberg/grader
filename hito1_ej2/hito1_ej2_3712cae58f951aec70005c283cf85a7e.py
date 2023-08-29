#Contestador de celular
telefono = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de llegada: "))
 
if (0 <= hora <= 7):
          print("contestar")
         
elif (hora <= 14):
           if(str(telefono)[5] == "9" and str(telefono)[6]=="0" and str(telefono)[7] == "9" ):
           
                  print("contestar")
                  
           else:
                  print("no contestar")
                 
if (17 <= hora <= 19):
           if(str(telefono)[0] == "8" and str(telefono)[1]=="7" and str(telefono)[2]=="7" ):
                  print("no contestar")
           else:
                  print("contestar")
if (19 < hora <= 23):
           print("no contestar")