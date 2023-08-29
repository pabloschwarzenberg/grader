usuario = input('Ingrese su usuario: ')
saldo_banco = 1000000
saldo_cuenta = 100000
contraseña = 1803

for var in range(1,4):
  print('Intento', var)
  contraseña2 = int(input('Ingrese su contraseña: '))
  if contraseña == contraseña2:
    print('Contraseña correcta')
    break
  else:
    print('Su contraseña es incorrecta')  
  if var >= 3:
    print('Su tarjeta ha sido bloqueada')
N = str
while contraseña == contraseña2:
    monto_retiro = input('Ingrese el monto que desea retirar: ')
    if monto_retiro == 'N':
      print('El programa se ha cerrado')
      break
    elif int(monto_retiro) >= 1000000 or int(monto_retiro) <=0:
      print('Monto no permitido')
    else:
      saldo_banco -= int(monto_retiro)
      saldo_cuenta -= int(monto_retiro)
      print('El saldo del banco es: ',saldo_banco)
      print('El saldo de su cuenta es: ', saldo_cuenta)