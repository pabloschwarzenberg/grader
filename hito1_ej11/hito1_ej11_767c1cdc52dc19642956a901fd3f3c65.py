#Cajero Automático
saldo_cajero=1000000
veinte=True
diez=True
cinco=True
x=0
y=0
z=0
usuario=input("usuario: ")
intentos=2
clave_invalida=True
clave=input("ingresa clave: ")
while clave_invalida and intentos>0:
   if clave=="1803":
    clave_invalida=False
   else:
    clave_invalida=True
    print("clave invalida")
    intentos=intentos-1
    clave=input("ingresa clave: ")

if clave=="1803":
  monto=input("ingrese monto a retirar: ")
  monto=int(monto)
  if monto<=100000 and monto>=0:
    saldo_cuenta=100000-monto     
    saldo_cajero=saldo_cajero-monto
    print("saldo cuenta=",saldo_cuenta)
    print("saldo cajero=",saldo_cajero)
    while veinte:
      if monto-20000>=0:
        monto=monto-20000
        x=x+1
        veinte=True
      else:
        veinte=False
        print("billetes 20000=",x)
    while diez:
      if monto-10000>=0:
        monto=monto-20000
        y=y+1
        diez=True
      else:
        diez=False
        print("billetes 10000=",y)
    while cinco:
      if monto-5000>=0:
        monto=monto-20000
        z=z+1
        cinco=True
      else:
        cinco=False
        print("billetes 5000=",z)   
  else:
      print("monto no permitido")    
else:
  print("tarjeta bloqueada")
