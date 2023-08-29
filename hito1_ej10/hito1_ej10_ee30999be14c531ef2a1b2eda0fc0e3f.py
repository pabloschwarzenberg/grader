#Cajero Automático
saldoCajero=1000000
usuario=10334151
claveA=1803
saldoUsuario=100000
while True:
  usuario=input()
  if usuario.isalpha() and not usuario=="N":
    break
  clave=int(input())
  vecesEquivocada=0
  while vecesEquivocada!=3:
    if clave==claveA:
      break
    else:
      vecesEquivocada+=1
      print("clave invalida")
      print("ingrese otra clave")
      clave=int(input())
    if vecesEquivocada==3:
      print("Tarjeta Bloqueada")
  if vecesEquivocada==3:
    break
  else:
    print("Monto a retirar:")
    while True:
      monto=int(input())
      if monto>saldoUsuario:
        print("Monto no permitido")
      else:
        break
    nuevoSaldoU=saldoUsuario-monto
    nuevoSaldoC=saldoCajero-monto
    print("saldo cuenta =",end="")
    print(nuevoSaldoU)
    print("saldo cajero =",end="")
    print(nuevoSaldoC)