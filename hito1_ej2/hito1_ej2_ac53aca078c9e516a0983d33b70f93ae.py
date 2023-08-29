#Contestador de celular
numero=int(input("ingrese su numero de telefono:   "))
hora=int(input("ingrese hora de llamada: "))
numero=str(numero)

 


if 0<hora and hora<7:
   
    print("contestar")
      
elif hora>7 and hora<14 and str(numero[5])=="9" and str(numero[6])=="0" and str(numero[7])=="9":
   
    print("contestar")

elif hora>7 and hora<14:
  
    print("no contestar")

elif hora>17 and hora<19 and str(numero[5])=="8" and str(numero[6])=="7" and str(numero[7])=="7":
    
    print("no contestar")

elif hora>17 and hora<19:

    print("no contestar")
    
elif hora>19:
    
    print("no contestar")
 
    

