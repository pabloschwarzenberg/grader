import sys
x=0
y=0
saldouser=100000
saldocajero=1000000
while True:
    while x==0:
        user=str(input("Inserte usuario : "))
        if user=="10334151":
            x=1
#aquí tienes que preguntar si user es distinto de N, entonces debes salir
        elif user!="N":
            x=4
    while x==1:
        clave=int(input("Inserte contraseña : "))
        if clave==1803:
            x=3
        else:
            y=y+1
            x=2
    while x==2:
        while y<3:
            print("clave invalida")
            clave=int(input("Inserte contraseña : "))
            if clave==1803:
                y=0
                x=3
                break
            else:
                y=y+1
        while y==3:
            print("tarjeta bloqueada")
            x=9
            sys.exit(0)
    while x==3:
        monto=int(input("Inserte monto a retirar : "))
        if monto<=saldouser:
            saldouser=saldouser-monto
            saldocajero=saldocajero-monto
            print("saldo cuenta=",saldouser)
            print("saldo cajero=",saldocajero)
            x=0
#    while x==4:
    if x==4:
      break
# usas un ciclo solamente cuando quieres repetir algo, si no quieres
# repetir algo debes usar un IF
#    while x==9:
#        sys.exit(0)
    if x==9:
      break
#esto es innecesario
#while False:
#    sys.exit(0)

