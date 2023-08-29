#Contestador de celular
telefono=int(input('ingresa un numero de telefono: '))
horadellamada=int(input('ingresa una hora de llamada: '))

if 10000000<=telefono<=99999999 and 0<=horadellamada<=23:

     if 0<=horadellamada<=7:
        print('resultado: contestar')
        
     if 7<horadellamada<=14:
        tresultimosdigitos=telefono%1000
        if tresultimosdigitos==909:
            print('resultado: contestar')
        else:
            print('resultado: no contestar')
                
     if 14<horadellamada<17:
       print('resultado: no contestar')
        
     if 17<=horadellamada<=19:
        tresprimerosdigitos=telefono//100000 
        if tresprimerosdigitos==877:
           print('Resultado: no contestar')
        else:
            print('Resultado: contestar') 
            
     if 19<horadellamada<=23:
       print('Resultado: no contestar')

else:
    print('al menos uno de los datos ingresados no es valido!')

               
            