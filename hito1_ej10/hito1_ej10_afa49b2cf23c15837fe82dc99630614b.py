#Cajero Automático
saldo_cajero=1000000
u=10334151
c="1803"
cont=0
saldo = 100000
clave="0"
cajero=False

while cajero==False:
 clave=input("ingrese clave:")
 if clave == "n":
     cajero=True
     break
 for n in range(3):    
    if clave!=c:
        cont+=1
        print("clave incorrecta")
        clave=input("ingrese clave:")
    if cont==3:
      print("tarjeta bloqueada")
      break
    if clave ==c:
      monto=int(input("monto a retirar :"))
      if monto > int(saldo):
        print("monto no permitido")
        break
      else:
        saldo=saldo-monto
        saldo_cajero = saldo_cajero-monto
        print("saldo cuenta",saldo-monto)
        print("saldo cajero",saldo_cajero-monto)
        break
