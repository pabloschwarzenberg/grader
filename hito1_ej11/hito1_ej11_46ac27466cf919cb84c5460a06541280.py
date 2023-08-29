#Cajero Automático
import random
saldo_inicial = 1000000
saldo_ci = 100000
usuario = 10334151
clave = int(input('Ingrese clave: '))
intentos = 1
#20 billetes de 20.000
#40 billetes de 10.000
#40 billetes de 5.000

while True:
  if clave == 1803:
    monto = int(input('Que monto desea retirar? '))
    while monto > 100000:
      print('monto no permitido')
      monto = int(input('Que monto desea retirar? '))
    saldo_cajero = saldo_inicial - monto
    saldo_cuenta = saldo_ci - monto
    print('saldo cuenta=', saldo_cuenta,'\nsaldo cajero=', saldo_cajero)
    while True:
      billetes = random.randint(1,20)
      billetes2 = random.randint(1,40)
      billetes3 = random.randint(1,40)
      billetes_suma = billetes*20000 + billetes2*10000 + billetes3*5000
      if billetes_suma != monto:
        billetes = random.randint(1,20)
        billetes2 = random.randint(1,40)
        billetes3 = random.randint(1,40)
        billetes_suma = billetes*20000 + billetes2*10000 + billetes3*5000
      else:
        break
    print('billetes 20000=', billetes,'\nbilletes 10000=', billetes2,'\nbilletes 5000=', billetes3)
    break
  elif intentos == 3:
    print('Tarjeta Bloqueada')
    break
  else: 
    print('clave invalida')
    clave = int(input('Ingrese clave: '))
    intentos += 1      