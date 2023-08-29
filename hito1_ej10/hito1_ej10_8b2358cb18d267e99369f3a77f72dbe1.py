Saldocajero= 1000000
saldocuenta= 100000
usuario= int(input('Ingrese su usuario: '))
while usuario != 10334151:
  usuario = int(input('Error, Ingrese su usuario: '))

clave= int(input('Ingrese su clave: '))
intentos=0
while not(clave == 1803):
  intentos = intentos+1
  print('Intentos:', intentos)
  if intentos ==3:
    print('Tarjeta bloqueada')
    break
  else:
    clave= int(input('Ingrese su clave: '))


if intentos != 3:
               respuesta = 'S'
               while(respuesta == 'S'):
                 montoRetirar= int(input('Ingrese su monto: '))
                 if montoRetirar<= Saldocajero:
                   if montoRetirar<= saldocuenta:
                     Saldocajero = Saldocajero - montoRetirar
                     saldocuenta = saldocuenta - montoRetirar
                     print('saldo cuenta=',saldocuenta,', saldo cajero=',Saldocajero)
                     
                   else:
                     print('monto no permitido')
                     
                 else:
                   print('monto no permitido')
                 
                 respuesta = input('Quiere volver a operar (S/N)')