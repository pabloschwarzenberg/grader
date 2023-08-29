#Cajero Automático
user=int(input("Ingrese su usuario: "))
while True:
    clave=int(input("Ingrese su clave: "))
    fallos=0
    saldoC = 1000000
    saldoU = 100000
    if clave!=1803 and user==10334151:
        if fallos==0:
            print("clave invalida")
            fallos=fallos+1
        elif fallos==1:
            print("clave invalida")
            fallos = fallos + 1
        elif fallos==2:
            print("tarjeta bloqueada")
            break
    elif user!=10334151:
        print("usuario invalido")
    else:
        print("Su saldo es de", saldoU)
        print("¿Cuanto desea retirar?")
        while True:
            retiro=int(input(""))
            if retiro<2000 or 200000<retiro:
                print("monto no permitido")
            else:
                saldoU=saldoU-retiro
                saldoC=saldoC-retiro
                print("El saldo actual del cajero es", saldoC,"y su saldo actual es",saldoU)
                break