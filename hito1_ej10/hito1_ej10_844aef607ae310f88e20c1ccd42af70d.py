#Cajero Automático
n = 0
validadorusuario = 10334151
validadorcontra = 1803
saldocajero = 1000000
saldocuenta = 100000
usuario = eval(input('usuario: '))
while True:
  contra = eval(input('contraseña: '))
  if contra != validadorcontra:
    print('clave invalida')
    n+=1
  else:break
  if n == 3:
    print('tarjeta bloqueda')
    break
while True:
  if n ==3:
    break
  monto = eval(input('monto a retirar: '))
  if monto > saldocajero:
    print('Monto no permitido')
  else:
    saldocajero = saldocajero - monto
    saldocuenta = saldocuenta - monto
    print('saldo cuenta=',saldocuenta)
    print('saldo cajero=',saldocajero)
    break
    