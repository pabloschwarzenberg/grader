#Contestador de celular
fono = int(input("Ingrese su numero telefonico de solo 8 caracterers : "))
if fono >= 10000000 and fono < 99999999:
   hora = int(input("Ingrese la hora de la llamada : "))
   if hora >= 0 and hora <= 7 :
      print("Contestar")

   elif hora > 7 and hora <= 14 :
      if fono == 77389909:
         print("contestar")
      else: print("No contestar")

   elif hora >= 17 and hora <= 19:    
       if fono == 87765545:
           print("No contestar")
       else : print("No contestar")

   elif hora > 19 and hora <= 23:
    print("No contestar ")

else: print("Ingrese un numero valido")                            
