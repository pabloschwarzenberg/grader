telefono = int(input('Ingrese numero telefonico: '))
horaLlamada = int(input('Ingrese hora de la llamada: '))


if 10000000 <= telefono <= 99999999 and 0 <= horaLlamada <= 23:
    if 0 <= horaLlamada <= 7:
       if horaLlamada >= 0 and horaLlamada <= 7:
        print('Resultado: CONTESTAR')

    if 8 <= horaLlamada <= 14:
        tresUltimosDigitos = telefono % 1000
        if tresUltimosDigitos == 909:
          print('Resultado: CONTESTAR')
    else:
          print('Resultado: NO CONTESTAR')
else:
    print('ERROR: Teléfono u Hora de Llamada inválidos.')
      