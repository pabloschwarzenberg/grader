#Cajero Automático
saldocajero=1000000
saldousuario=100000
contador=0
billete20000=20
billete10000=40
billete5000=40
while contador<3:
    usuario=input("usuario: ")
    clave=input("clave: ")
    if usuario=="10334151" and clave=="1803":
        montoaretirar=int(input("monto a retirar: "))
        a=montoaretirar%20000
        b=montoaretirar%10000
        c=montoaretirar%5000
        if montoaretirar>100000:
            print("monto no permitido")
        else:
            if montoaretirar==100000:
                print("billete 20 = 5")
            elif a==0:
                print("billetes 20000=", montoaretirar//20000)
            elif a!=0 and b==0:
                print("billetes 10000=", montoaretirar//10000)
            elif c==0:
                print("billetes 5000=", montoaretirar//5000)
            print("saldo cuenta=", saldousuario-montoaretirar)
            print("saldo cajero=", saldocajero-montoaretirar)
            salida=input("ingresa algo distinto de n para salir")
            if salida!="n":
                break
    else:
        print("clave invalida")
    contador=contador+1
    print("tarjeta bloqueada")
  