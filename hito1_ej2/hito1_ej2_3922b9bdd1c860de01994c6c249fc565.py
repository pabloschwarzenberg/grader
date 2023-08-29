#Contestador de celular
telefono = int(input('Ingrese numero telefonico:'))
horaLlamada  = int(input('Ingrese hora de la llamada:'))

if 10000000 <= telefono <= 99999999 and 0 <= horaLlamada <=23:

   if 0<= horaLlamada <=7:
      print('CONTESTAR')
      
   if 8 <= horaLlamada <=14:
       tresUltimosDigitos = telefono%1000
       if tresUltimosDigitos == 909:
           print('CONTESTAR')
       else:
           print('NO CONTESTAR')
          
           
if 15 <= horaLlamada <= 16:
    print('NO CONTESTAR')
    
    if 17 <= horaLlamada <= 19:
        tresPrimerosDigitos = telefono//100000
        if tresPrimerosDigitos == 877:
           print('NO CONTESTAR')
        else:
           print('CONTESTAR')
      
   if 20<= horaLlamada <=23:
       print('NO CONTESTAR')
else:
   print('Uno o más de los datos ingresados son inválidos.')