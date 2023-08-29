celular= int(input("Ingrese numero de celular"))
hora= int(input("Ingrese hora de la llamada"))

#divido el numero para obtener los 3 ultimos y los 3 primeros del celular que ingrese
exception1= celular%1000
print(exception1) #Hago print para ver si quedo bien hecho el "corte"
exception2= celular//100000
print(exception2) #Hago print para ver si quedo bien hecho el "corte"


if hora >=0 and hora==7:
    print("CONTESTAR")

  #entre 7 y 14 solo le contesto a 909
elif hora > 7 and hora < 14 and exception1==909:
    print("CONTESTAR")
    
 #entre 17 y 19 le contesto a todos excepto a los que empiecen por 877

elif hora >=17 and hora <=19 and exception2!=877:
    print("CONTESTAR")
    
else:
    print("NO CONTESTAR")
     

#Ejemplo 1
#>>> Ingrese numero telefonico: 77389909
#>>> Ingrese hora de la llamada: 13
#>>> Resultado: CONTESTAR
#Ejemplo 2
#>>> Ingrese numero telefonico: 98927674
#>>> Ingrese hora de la llamada: 20
#>>> Resultado: NO CONTESTAR
#Ejemplo 3
#>>> Ingrese numero telefonico: 87765545
#>>> Ingrese hora de la llamada: 18
#>>> Resultado: NO CONTESTAR

