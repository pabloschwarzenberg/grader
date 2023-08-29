#Cajero Automático
salir="N"
cajero=1000000
cuenta=100000
i=1
while salir =="N":
    usuario = int(input("ingrese su numero de usuario:"))
    while usuario != 10334151:
        usuario = int(input("ingrese su numero de usuario:"))
    clave = int(input("Ingrese clave:"))
    while clave != 1803:
        print("Clave invalida")
        clave = int(input("Ingrese clave:"))
        i = i + 1
        if i > 2:
            break
    if i > 2:
        print("Tarjeta bloqueada")
        break
    monto = int(input("Monto a retirar:"))
    while monto > cuenta:
        print("Monto no permitido")
        monto = int(input("Monto a retirar:"))
    cajero = cajero - monto
    cuenta = cuenta - monto
    print("saldo cuenta=", cuenta)
    print("saldo cajero=", cajero)
    salir=input("Quiere salir(Y= si, N=no):")