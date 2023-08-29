#Contestador de celular
#ENTRADA

valor = str(input("Inserte numero celular: "))

time = eval(input("Inserte hora correspondiente a la llamada: "))

if time > 0 and time <= 7:

    print("CONTESTAR")

elif time > 19 and time <= 23:

    print("NO CONTESTAR")

#Procesamiento
    
else:
    
      if time > 17 and time <= 19 and str(valor [0:1]) == "8" and str(valor [1:2]) == "7" and str(valor [2:3]) == "7":

       print ("NO CONTESTAR")
       
      elif time > 17 and time <= 19 and str(valor [0:1]) != "8" and str(valor [1:2]) != "7" and str(valor [2:3]) != "7":
       
       print ("CONTESTAR")
       
      elif time > 7 and time <= 14 and str(valor[-3]) == "9" and str(valor[-2]) == "0" and str(valor[-1]) == "9":

       print("CONTESTAR")

      if time > 7 and time <= 14 and str(valor[-3]) != "9" and str(valor[-2]) != "0" and str(valor[-1]) != "9":

       print("NO CONTESTAR")

    

    
       
       

   

