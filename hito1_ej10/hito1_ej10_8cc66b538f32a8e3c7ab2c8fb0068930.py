#Cajero Automático

saldo_cajero=1000000
saldo_cuenta=100000

a=True
n=1

while a==True:
    while n<=3:
        usuario=int(input("Usuario: "))
        clave=int(input("Clave: "))
        if clave==1803 and usuario==10334151:
            break
        else:
            n=n+1
            print("clave invalida")
        print("tarjeta bloqueada")
        a=False

    while saldo_cuenta>=0:
        monto=int(input("Monto: "))
        if monto<=saldo_cuenta:
            print("saldo cuenta=" , (saldo_cuenta-monto))
            print("saldo cajero=" , (saldo_cajero-monto))
            saldo_cuenta=saldo_cuenta-monto
            saldo_cajero=saldo_cajero-monto
            continuar=input("Desea continuar? ")
            if continuar!="N":
                a=False
                break
            else:
                print("monto no permitido")
                a=False
                break