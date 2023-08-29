#Cajero Automático
saldocajero=1000000
saldousuario=100000
contador=0
while contador<3:
    usuario=input("usuario: ")
    clave=input("clave: ")
    if usuario=="10334151" and clave=="1803":
        montoaretirar=int(input("monto a retirar: "))
        if montoaretirar>100000:
            print("monto no permitido")
        else:
            print("saldo cuenta=", saldousuario-montoaretirar)
            print("saldo cajero=", saldocajero-montoaretirar)
            salida=input("ingresa algo distinto de n para salir")
            if salida!="n":
                break
    else:
        print("clave invalida")
    contador=contador+1
    print("tarjeta bloqueada")

