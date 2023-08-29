#Cajero Automático
saldocaja=1000000
saldocuenta=100000
salir="N"
while salir=="N":
    usuario=int(input("Usuario:"))
    clavei=int(input("Clave:"))
    salir="N"
    contador=0
    while (clavei!=1803 and contador<2)and usuario!=11033415:
        print("clave invalida")
        contador = contador + 1
        clavei=int(input("Clave:"))
    if contador>=2:
        print("tarjeta bloqueada")
    else:
        mretirar = int(input("Monto a retirar:"))
        if mretirar>saldocuenta or saldocuenta<=0:
             print("monto no permitido")
        else:
            saldocuenta=saldocuenta-mretirar
            saldocaja=saldocaja-mretirar
            print("saldo cuenta=",saldocuenta)
            print("saldo cajero=",saldocaja)
    salir=input("termianr:")