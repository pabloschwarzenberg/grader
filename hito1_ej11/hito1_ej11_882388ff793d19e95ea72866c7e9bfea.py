#Cajero Automático
usuario=input("ingrese su nombre")
clave=eval(input("ingrese su clave"))
cuenta=100000
saldo=1000000
if clave==1803:
  monto=eval(input("ingrese el monto a retirar"))
  if saldo-monto>0:
    saldo=saldo-monto
    cuenta=cuenta-monto
    print("saldo cuenta=",cuenta)
    print("saldo cajero=",saldo)
  else:
    print("monto no permitido")
else:
  print("clave invalida")
