#Cajero Automático
#Cajero Automático
saldo = 100000
saldocajero = 1000000
i = 1
usuario = input('Usuario: ')
clave = input('Clave: ')
if (int(usuario) == 10334151) and (int(clave) == 1803):
  monto= int(input('Monto a Retirar: '))
  if monto >= saldo:
      print('Monto no permitido ')
  else:
          saldo = saldo - monto
          saldocajero = saldocajero - monto
          print('saldo cuenta = ',saldo)
          print ('saldo cajero = ', saldocajero)
elif i == 3:
    print('tarjeta bloqueada ')
elif (int(usuario) != 10334151) or (int(clave) != 1803):
    i = i+1
    print('clave inválida ')