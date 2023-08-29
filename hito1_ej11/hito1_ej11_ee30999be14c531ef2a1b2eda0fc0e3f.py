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
    billetes20=0
    billetes10=0
    billetes5=0
    division5=monto//5000
    division10=monto//10000
    division20=monto//20000
    billetes20+=division20
    billetes10+=division10-(2*division20)
    billetes5+= division5-((4*division20)+(2*billetes10))
    print("billetes 20000=",end="")
    print(billetes20)
    print("billetes 10000=",end="")
    print(billetes10)
    print("billetes 5000=",end="")
    print(billetes5)