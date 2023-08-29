#Contestador de celular
numero=int(input('ingrese numero telefonico'))
if 10000000<=numero<=99999999:
    hora=int(input('ingrese hora de la llamada'))
    if 0<=hora<=23:
        if 0<=hora<=7:
           print('Resultado: CONTESTAR') 

        if 7<=hora<=14:
            tresUltimosDigitos= numero%1000 
            if tresUltimosDigitos==909:
                print('Resultado: CONTESTAR')
            else:
                 print('Resultado: NO CONTESTAR')
        
        if 15<=hora<=16:
            print('no contestar')
           
        if 17<=hora<=19:
            
            TresPrimerosDigitos= numero//100000
            if TresPrimerosDigitos==877:
                print('Resultado: NO CONTESTAR')
            else:
                print('Resultado: CONTESTAR')
        
        if 20<=hora<=23:
            print('Resultado: NO CONTESTAR')
         

         
    else:
        print('hora incorrecta')
else:
    print('numero telefonico incorrecto')