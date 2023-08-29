#Cajero Automático
usuario=int(input("Ingrese su usuario: "))
clave=int(input("Ingrese su clave: "))
saldocajero=1000000
saldocuenta=100000
contador=0
while True:
    if contador>3:
        print("tarjeta bloqueada")
    if usuario==10334151 and clave==1803:
        plata=int(input("Monto a retirar: "))
        if plata<=100000:
            nuevosaldocajero=saldocajero-plata
            nuevosaldocuenta=saldocuenta-plata
            print("saldo cuenta="+str(nuevosaldocuenta)+","+"saldo cajero="+str(nuevosaldocajero))
        else:
            print("monto no permitido")
    else:
        print("clave invalida")
    contador=contador+1
    salir=input("¿Desea salir?: ")
    if salir!="N":
        break
  