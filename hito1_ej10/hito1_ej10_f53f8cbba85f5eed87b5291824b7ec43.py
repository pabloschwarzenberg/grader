#Cajero Automático
intentos=0
saldocajero=1000000
saldocuenta=100000
retiro = 0
while intentos<3:
    user=input("Ingrese Codigo de usuario:")
    clave=input("Ingrese clave numerica")
    if clave==" " or len(clave)<4 or len(clave)>4 :
        print("Clave invalida")
        intentos+=1
    else:
        pass
    while retiro ==0:
        retiro=int(input("Monto a retirar"))
        if retiro > saldocuenta:
            print("Monto no permitido")
            retiro=0
        elif retiro> saldocajero:
            print("Monto no permitido")
            retiro=0
        saldocajero=saldocajero-retiro
        saldocuenta=saldocuenta-retiro
        print("saldo cuenta=",saldocuenta)
        print("saldo cajero=",saldocajero)
    break
if intentos==3:
    print("Tarjeta bloqueada")
     