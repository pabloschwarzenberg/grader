clave=1803
usuario=10334151
while True:
  usuario1=int(input("Ingrese Usuario: "))
  clave1=int(input("Ingrese Clave: "))
  saldot=1000000
  if (usuario1==usuario and clave1==clave):
    saldo1=100000
    for i in range(0,3):
      dinerillo=int(input("cuanto dinero quiere retirar"))
      if dinerillo>0 and dinerillo<=100000:
        saldonuevo=saldo1-dinerillo
        saldocajero=saldot-dinerillo
        print("saldo cuenta="+str(saldonuevo))
        print("saldo cajero="+str(saldocajero))
        break
      else:
        print("monto no permitido")
        break
  else:
    print("clave invalida")
  salir=input("Desea salir")
  if salir!="N":
    break
      