#Contestador de celular
numero = int(input('Ingrese numero telefonico: '))

while len(str(numero)) != 8:
    print('El numero ingresado es invalido, intentelo nuevamente: ')
    numero = int(input('Ingrese numero telefonico: '))

hora = int(input(' Ingrese la hora de la llamada:'))
if hora < 0 and hora > 23:
    int(input('Hora invalida, intentelo nuevamente: '))
    hora = int(input(' Ingrese la hora de la llamada:'))
   
else:
    while hora >= 0 and hora <= 23:
        
        #Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
        
        if hora >= 0 and hora < 7:
            print('CONTESTAR')
            break
        
        #Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
        elif hora >= 7 and hora < 14:
            fin_num = int(str(numero)[5:8])
            if fin_num == 909:
                print('CONTESTAR')
                break
            else:
                print('NO CONTESTAR')
                break
        
        

        elif hora >= 14 and hora <= 17:
            print('NO CONTESTAR')
            break

        #Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
        elif hora > 17 and hora < 19:
            inicio_num = int(str(numero)[0:3])
    
            if inicio_num == 877:
                print('NO CONTESTAR')
                break
            else:
                print('CONTESTAR')
                break

        #Después de las 19:00, no contestas el celular.
        elif hora >= 19 and hora > 0:
            print('NO CONTESTAR')
            break
                
if hora < 0 and hora > 23:
    int(input('Hora invalida, intentelo nuevamente: '))
    hora = int(input(' Ingrese la hora de la llamada:'))