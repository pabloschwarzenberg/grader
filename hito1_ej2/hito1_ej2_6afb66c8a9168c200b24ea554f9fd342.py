print("llamada")
hora=int(input("Hora de llamada:"))
telefono=(input("Numero de telefono:"))
i=1
if(hora>=0)and(hora<7):
    print("Resultado: CONTESTAR")
while(hora>=7)and(hora<14):
    telefono= str(telefono)
    celular= telefono[5:8]
    llamada= int(celular)
    
    if (llamada == 909)>=i:
        print("Resultado: CONTESTAR")
        i=i+1
        
    elif (llamada != 909)>=i:
        
        print("Resultado: NO CONTESTAR")
        i=i+1
i=1
if (hora>14)and(hora<17):
      print("Resultado: CONTESTAR")
        
while(hora>17)and(hora<19):
     telefono= str(telefono)
     celular= telefono[5:8]
     llamada= int(celular)
  
     if (llamada== 877)>=i:
         
         print("Resultado: NO CONTESTAR")
         i=i+1
     if (llamada != 877)>=i:
         print("Resultado: CONTESTAR")
         i=i+1
if(hora>19)and(hora>23):
     print("Resultado: NO CONTESTAR")



