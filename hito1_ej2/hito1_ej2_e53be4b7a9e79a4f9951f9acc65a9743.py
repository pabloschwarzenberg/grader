telefono = int(input('Ingrese  el numero telefonico: '))
horaLlamada = int(input('Ingrese  la hora de la llamada : '))


if 10000000 <= telefono <= 99999999 and 0 <= horaLlamada <= 23:

# Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
    if 0 <= horaLlamada <= 7:
        print('CONTESTAR')

# Si ocurre antes de las 14:00 no la contestas,excepto si el número termina en 909.
    if 8 <= horaLlamada <= 14:
        TresUltimosDigitos = telefono % 1000
        if TresUltimosDigitos == 909:
            print('CONTESTAR')
        else:
            print('NO CONTESTAR')

# Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
    if 15 <= horaLlamada <= 16:
        print('NO CONTESTAR')
        
    if 17 <= horaLlamada <= 19:
        TresPrimerosDigitos = telefono // 100000
        if TresPrimerosDigitos == 877:
            print('NO CONTESTAR')
        else:
            print('CONTESTAR')

# Después de las 19:00, no contestas el celular.
    if 20 <= horaLlamada <= 23:
        print('NO CONTESTAR') 

else:
    print('Uno o más de los datos ingresados son inválidos.')