#Cajero Automático
usuario = int(input('Ingresa el usuario: '))
clave = int(input('Ingresa tu clave: '))
contador = 0
if usuario == 10334151 and clave == 1803:
  print('Saldo disponible en la cuenta : $100.000')
  retiro = int(input('¿Cuál es el monto a retirar?: $'))
  if retiro > 0 and retiro < 100000:
    saldo_cuenta = 100000 - retiro
    saldo_cajero = 1000000 - retiro
    print('Saldo cuenta: $', saldo_cuenta)
    print('Saldo cajero: $', saldo_cajero)
  else:
    print('Monto no permitido')
else:
  while True:
    print('Clave inválida')
    int(input('Ingresa el usuario: '))
    int(input('Ingresa la clave: '))
    contador += 1
    if contador == 2:
      print('Tarjeta bloqueada')
      break   