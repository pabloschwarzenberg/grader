def retiro(saldo, cantidad):
  if saldo >= cantidad:
    saldo-=cantidad
    print('Cantidad disponible en billetes:')
    billetes_disponibles = [20000, 10000, 5000]
    for billetes in billetes_disponibles:
      billetes_entregados = cantidad // billetes
      cantidad -= billetes_entregados * billetes
      print('Billetes de $' + str(billetes) + ': ' + str(billetes_entregados))
    return saldo
  else:
    return saldo
saldo = 1000000
cantidad = 45000
retiro(saldo, cantidad)