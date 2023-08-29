#Contestador de celular
  #ENTRADA
nt = int(input("ingrese numero telefonico:"))       
hl = int(input("ingrese hora de la llamda:"))
nt = str(nt)
ntf = str(nt[5:8])

#PROCESAMIENTO
if (hl <= 7 and hl >= 0):
  print("CONTESTAR")
  
else:
    if ntf == str(909) and hl <= 14:
      print("CONTESTAR")
      
    else:
       if hl >=14:
        print("NO CONTESTAR")

       else:
         if(hl <= 19 and hl >= 17 and nt < 87700000 and nt > 87799999):
          print("CONTESTAR")

         else:
           print("NO CONTESTAR")    