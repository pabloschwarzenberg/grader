#Cajero Automático 1

saldoCajero = 1000000
usuario = 10334151
clave = 1803
saldoUsuario =  100000

def retirar(saldoU,saldoC):
  validar  = False
  contador = 0
  ingresoUsuario = int(input("Ingrese su usuario:"))
  ingresoClave = int(input("Ingrese su clave:"))
  while validar == False:
    if clave != ingresoClave:
      contador += 1
      ingresoClave = int(input("Clave invalida:"))
      if contador == 2:
        return (print("Tarjeta bloqueada"))
    else:
      montoRetirar = int(input("Indique el monto a retirar:"))
      if montoRetirar <= 0 or montoRetirar > saldoU:
        return print("Monto no permitido")
      else:
        saldoC -= montoRetirar
        saldoU -= montoRetirar
        return print("saldo cuenta={}\nsaldocajero={}".format(saldoU, saldoC))      
        
retirar(saldoUsuario,saldoCajero)