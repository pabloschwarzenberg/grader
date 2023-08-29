#Cajero Automático
cuenta_activada = True
saldo_cajero = 1000000
saldo_cuenta = 100000
contador = 0
usuario = int(input('Ingresar numero de usuario: '))

while cuenta_activada == True:
  if usuario == 10334151:
    clave_usario1 = int(input('Ingresar clave usuario: '))

    if clave_usario1 == 1803:
      while cuenta_activada == True:
        monto_a_retirar = int(input('Monto a retirar: '))
        if monto_a_retirar > saldo_cuenta:
          print('Monto no permitido')
        else:
          saldo_cuenta = saldo_cuenta - monto_a_retirar
          saldo_cajero = saldo_cajero - monto_a_retirar
          print('saldo cuenta=' +str(saldo_cuenta)+ ',saldo cajero=' +str(saldo_cajero))
        break
      break
    else:
      contador = contador + 1
      if contador == 1:
        print('Clave invalida, quedan dos intentos')
      elif contador == 2:
        print('Clave invalida, queda un intento')
      elif contador == 3:
        print('Fin de los intentos')
        print('CUENTA BLOQUEADA')
        break      