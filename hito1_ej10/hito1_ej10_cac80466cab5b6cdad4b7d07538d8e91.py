#Cajero Automático
saldocajero=1000000
saldocuenta=100000
x=0
a=0
while x==0:
        usuario=int(input("Ingrese su numero de cuenta: "))
        clave=int(input("Ingrese su clave: "))

        if usuario==10334151 and clave==1803:
            print("clave valida")
            monto=int(input("Monto a retirar: "))
            if monto>saldocajero:
                print("monto no permitido")
            if saldocajero>monto:
                print("saldo cuenta=",saldocuenta-monto)
                print("saldo cajero=",saldocajero-monto)
        else:
            print("clave invalida")
            a=a+1
            if a==3:
                print("tarjeta bloqueada")
                break
        salir=input("Si desea salir presione cualquier tecla menos N: ")
        if salir=="N":
            continue
        else:
            break