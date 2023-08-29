
saldoCajero = 1000000
usuario = 10334151
clave = 1803
saldoUsuario =  100000
montoRetirar = 0
validar  = False
contador = 0
ingresoUsuario = int(input("Ingrese su usuario:"))
ingresoClave = int(input("Ingrese su clave:"))
while validar == False:
  if clave != ingresoClave:
    contador += 1
    ingresoClave = int(input("Clave invalida:"))
    if contador == 2:
      (print("Tarjeta bloqueada"))
      validar = True
  else:
    montoRetirar = int(input("Indique el monto a retirar:"))
    if montoRetirar <= 0 or montoRetirar > saldoUsuario:
      print("Monto no permitido")
      validar = True
    else:
      saldoCajero -= montoRetirar
      saldoUsuario -= montoRetirar
      print("saldo cuenta={}\nsaldo cajero={}".format(saldoUsuario, saldoCajero))   
      validar = True 
def billetes(saldoRetirar):
  billetes_20000 = 0
  billetes_10000 = 0
  billetes_5000= 0
  while saldoRetirar != 0: 
    if (saldoRetirar - 20000) > 0:
      saldoRetirar -= 20000
      print(saldoRetirar)
      billetes_20000 += 1  
    elif  (saldoRetirar - 10000) > 0:
      saldoRetirar -= 10000
      print(saldoRetirar)
      billetes_10000 += 1  
    elif  (saldoRetirar - 5000) >= 0:
      saldoRetirar -= 5000
      print(saldoRetirar)
      billetes_5000 += 1  
  return (print("billetes 20000={}\nbilletes 10000={}\nbilletes 5000={}".format(billetes_20000,billetes_10000,billetes_5000)))    

billetes(montoRetirar)