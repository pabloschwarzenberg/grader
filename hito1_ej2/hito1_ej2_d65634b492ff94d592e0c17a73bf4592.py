#Contestador de celular
telefono = int(input(" Ingrese numero telefonico :"))
hora = int(input(" Ingrese hora de la llamada :"))
ultimosnumeros = telefono % 1000
primerosnumeros = telefono // 1000
horario_tarde = hora <= 19 and hora >=17
if (hora >= 0 and hora <=7):
    print (" Contestar ")
  
    
elif (ultimosnumeros == 909 and hora <= 14):
    print (" Contestar ")

elif (hora > 19):
    print (" No contestar ")

elif (primerosnumeros != 877 and hora == horario_tarde):
    print(" Contestar ")
else:
    print(" No contestar ")
           