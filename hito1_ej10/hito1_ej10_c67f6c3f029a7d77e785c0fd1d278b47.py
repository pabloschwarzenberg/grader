saldo_cajero=1000000
saldo_cuenta=100000
intentos=3
continuar=True

while continuar==True and intentos>0:
    usuario=input("ingrese su usuario: ")
    clave=input("ingresar clave: ")
    while continuar==True and usuario=="10334151":
        if clave=="1803":
            while continuar==True and saldo_cuenta>0:
                monto=input("ingresar monto a retirar: ")
                monto=int(monto)
                if monto<=100000:
                    saldo_cajero=saldo_cajero-monto
                    saldo_cuenta=saldo_cuenta-monto
                    print("saldo cuenta=",str(saldo_cuenta))
                    print("saldo cajero=",str(saldo_cajero))
                    salir=input()
                    if salir!="N":
                        continuar=False
                    else:
                        pass
                else:
                    print("monto no permitido")
        else:
            intentos=intentos-1
            print("clave invalida")
print("tarjeta bloqueada")
