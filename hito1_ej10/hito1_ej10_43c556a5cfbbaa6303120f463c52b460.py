#Cajero Automático
usuario = input("Ingrese el número de cuenta: ")
Saldoin = 1000000
Saldocu = 100000
int(Saldoin)
int(Saldocu)

if int(usuario)!= 10334151:
    print("Usuario incorrecto")

elif int(usuario) == 10334151:
    clave = int(input("Ingrese clave: "))

    for i in range(2):
        if int(clave)!= 1803:
            print("clave invalida")
            print("Ingrese clave nuevamente")
            clave = int(input("Ingrese la clave: "))
             
        
    if clave != 1803:
        print("clave invalida")
        print("tarjeta bloqueada")
        raise SystemExit

    elif clave == 1803:
        print("Su saldo es: ", Saldocu)
        monto = int(input("¿Cuanto dinero desea retirar?: "))
        if 0<= monto <=100000:
            Saldofin = Saldocu - monto
            Saldofincaj = Saldoin - monto
            print("saldo cuenta= ",Saldofin)
            print("saldo cajero= ",Saldofincaj)

        else:
            print("monto no permitido")