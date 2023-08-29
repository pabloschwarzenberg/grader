#Cajero Automático
usuario=int(input("Ingrese ususario: "))
saldo_caja=1000000
saldo_us=100000

if usuario==10334151:
    cant=1
    claveok=False
    while claveok==False and cant<=3:
        clave=int(input("Ingrese clave: "))
        if clave==1803:
            claveok=True
        else:
            print("clave invalida")
            cant=cant+1
        
    if claveok==False and cant>3:
        print("tarjeta bloqueada")

    else:
        continuar="N"
        while continuar=="N" and saldo_us>0:
            monto=int(input("Ingrese el monto: "))
            if monto>saldo_us:
                print("monto no permitido")
                continuar=input("Para intentar de nuevo ponga N: ")
            else:
                saldo_caja=saldo_caja-monto
                saldo_us=saldo_us-monto
                print("saldo cuenta=", saldo_us)
                print("saldo cajero=", saldo_caja)
                continuar=input("Para intentar de nuevo ponga N: ")
else:
    print("usuario incorrecto")    