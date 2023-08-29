#Cajero Automático
saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
clave_invalida=True
usuario=input("usuario:")
clave=input("ingrese clave:")

while clave_invalida and intentos>1:
     if clave=="1803" and usuario=="10334151":
        clave_invalida=False       
     else:
         clave_invalida=True
         print("clave invalida")
         intentos=intentos-1
         clave=input("ingrese clave:")
         
if clave=="1803" and usuario=="10334151":
        monto=input("ingrese monto a retirar:")
        monto=int(monto)
        saldo_cajero=saldo_cajero-monto
        saldo_cuenta=saldo_cuenta-monto
        print("saldo cuenta=",saldo_cuenta)
        print("saldo cajero=",saldo_cajero)
else:
        print("clave invalidada")
