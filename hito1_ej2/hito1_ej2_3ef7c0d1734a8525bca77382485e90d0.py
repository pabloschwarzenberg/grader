#Contestador de celular
telefono = int(input("ingrese un numero telefonico:"))
hora = int(input("ingrese hora de llamada:"))

if (0 <= hora <= 7):
           print("CONTESTAR")

elif (hora <= 14):
           if(str(telefono)[5]=="9" and str(telefono)[6]=="0" and str(telefono)[7]=="9" ):

                 print("CONTESTAR")

           else:
                 print("NO CONTESTAR")
                 
if (15<= hora <= 16):
    print("CONTESTAR")

if (17 <= hora <= 19):
           if(str(telefono)[0]=="8" and str(telefono)[1]=="7" and str(telefono)[2]=="7" ):

                 print("NO CONTESTAR")

           else:
                 print("CONTESTAR")
                 

if (19 < hora <= 23):
           print("NO CONTESTAR")     