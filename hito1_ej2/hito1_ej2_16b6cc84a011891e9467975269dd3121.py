telefono = int(input('Ingrese numero telefonico: '))
hora = int(input('Ingrese hora de la llamada: '))

if 10000000 <= telefono <= 99999999 and 0 <= hora <= 23:
  
    if 0 <= hora <= 7:
        print('Resultado: CONTESTAR')


    if 7 < hora < 14:
        
        tresUltimosDigitos = telefono%1000       
        
        if tresUltimosDigitos == 909:
            print('Resultado: CONTESTAR')
        else: 
            print('Resultado: NO CONTESTAR')
  
  
    if 14 <= hora < 17:
        print('Resultado: NO CONTESTAR')

    if 17 <= hora <= 19:

        tresPrimerosDigitos = telefono//100000 
        
        if tresPrimerosDigitos == 877:
            print('Resultado: NO CONTESTAR')
        else:
            print('Resultado: CONTESTAR')
        
   
    if 19 < hora < 23:
        print('Resultado: NO CONTESTAR')    

    else:
      print('Alguno de los valores ingresados')
