#Cajero Automático
usuario=int(input("ingrese su número de usuario: "))
while usuario!=10334151:
    usuario = int(input("ingrese su número de usuario: "))
clave=int(input("ingrese su clave: "))
contador=1
cajero= 1000000
saldo=100000
seguir="N"
while contador!=3:
    if clave!=1803:
        print("clave invalida")
        clave = int(input("ingrese su clave: "))
        contador+=1
    if contador==3:
        print("tarjeta bloqueada")
    if clave==1803:
        retirodinero=int(input("monto a retirar: "))
        while retirodinero >saldo:
            print("Monto Invalido")
            retirodinero = int(input("monto a retirar: "))
        if retirodinero < saldo:
            saldocajero=cajero-retirodinero
            saldocuenta=saldo-retirodinero
            print("saldo cuenta=",saldocuenta)
            print("saldo cajero=", saldocajero)
            saldo=saldo-retirodinero
            cajero=cajero-retirodinero
            seguir = str(input("desea hacer otro movimiento: "))
            seguir.upper()
        if seguir != "N":
            break