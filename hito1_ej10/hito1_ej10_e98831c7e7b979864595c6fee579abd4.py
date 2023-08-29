#Cajero Automático
saldocajero=1000000
saldocuenta=100000
usuario=int(input("ingrese usuario: "))
claveinvalida=True
clave=int(input("ingrese clave: "))
intentos=3
while claveinvalida and intentos>1:
    if usuario==10334151 and clave==1803:
        claveinvalida=False
    else:
        claveinvalida=True
        intentos=intentos-1
        print("clave invalida")
        clave=int(input("ingrese clave: "))
         
if usuario==10334151 and clave==1803:
    monto=int(input("ingrese monto a retirar: "))
    while monto<=saldocuenta:
           saldocajero=saldocajero-monto
           saldocuenta=saldocuenta-monto
           print("saldo cuenta=",saldocuenta)
           print("saldo cajero=",saldocajero)
           salir=str(input())
           if salir!="N":
               break
           monto=int(input("ingrese monto a retirar: "))
           if monto>saldocuenta:
               print("monto no permitido")     
else:
    print("tarjeta bloqueada")
    