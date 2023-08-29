#Cajero Automático
usuario=str(input("Ingrese su usuario: "))
clave="1803"
x=0
while x<3:
    saldo_cajero=1000000
    saldo=100000
    clave_ing=str(input("Ingrese su contraseña: "))
    if clave_ing==clave:
        monto=int(input("Ingrese monto a realizar"))
        if monto<=saldo_cajero and monto<=saldo:
            saldo=saldo-monto
            saldo_cajero=saldo_cajero-monto
            saldo=str(saldo)
            saldo_cajero=str(saldo_cajero)
            print("Saldo cuenta="+saldo)
            print("saldo cajero="+saldo_cajero)
            x=x+4
    else:
        print("clave invalida")
        x=x+1
if (x==3):
    print("Tarjeta bloqueada")
      