#Cajero Automático
usuario = int(input())
clave = int(input())
saldo_cajero = 1000000
saldo_usuario = 100000
if (usuario==10334151) and (clave==1803):
  monto = int(input("Monto a retirar: "))
  if monto<=saldo_cajero:
    saldo_usuario += monto
    saldo_cajero -= monto
    print("saldo cuenta="+str(saldo_usuario))
    print("saldo cajero="+str(saldo_cajero))