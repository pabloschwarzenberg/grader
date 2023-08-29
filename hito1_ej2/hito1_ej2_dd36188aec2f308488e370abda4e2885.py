#Contestador de celular
numero = str(input("Ingrese numero de telefono:")) 

horario = int(input("Ingrese a que horario es la llamada:")) 

if horario > 0 and horario < 7: 

  print("contestar") 

if horario > 19 and horario <= 23: 

  print("no contestar") 

else: 

  if horario > 7 and horario < 14 and str(numero[-3]) == "9" and str(numero[-2]) == "0" and str(numero[-1]) == "9": 

    print("contestar") 

  if horario > 7 and horario < 14 and str(numero[-3]) != "9" and str(numero[-2]) != "0" and str(numero[-1]) != "9": 

    print("no contestar") 

  if horario > 17 and horario < 19 and str(numero[0:1]) == "8" and str(numero[1:2]) == "7" and str(numero[2:3]) == "7": 

    print("no contestar") 

  if horario > 17 and horario < 19 and str(numero[0:1]) != "8" and str(numero[1:2]) != "7" and str(numero[2:3]) != "7": 

    print("contestar") 
      