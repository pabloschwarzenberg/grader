#Cajero Automático
saldocajero=1000000
saldocuenta=100000
while(saldocuenta>0):
  usuario=input("inserte usuario: ")
  if(usuario=="10334151"):
    n=0
    while(n<3):
      clave=input("ingrese clave: ")
      while(clave=="1803"):
        print("clave valida")
        monto=int(input("ingrese monto para retirar: "))
        while(monto>100000):
          print("monto no permitido")
          break
        while(monto<0):
          print("monto no permitido")
          break
        if(0<=monto<=10000):
          saldocajero=saldocajero-monto
          saldocuenta=saldocuenta-monto
          print("el nuevo saldo del cajero es: ",saldocajero)
          print("el nuevo saldo de su cuenta es: ",saldocuenta)
          break
      while(clave!="1803"):
        print("clave invalida")
        n=n+1
        r=3-n
        print("intentos restantes: ",r)
        break
      break
    if(n==3):
      print("tarjeta bloqueada")
  else:
    print("usuario invalido")
if(saldocuenta<=0):
  print("cuenta sin saldo")