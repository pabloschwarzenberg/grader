#Cajero Automático
usuario=int(input("Ingrese ususario: "))
saldo_caja=1000000
saldo_us=100000
cant20m=20
cant10m=40
cant5m=40

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
            out20=0
            out10=0
            out5=0
            monto=int(input("Ingrese el monto: "))
            if monto>saldo_us:
                print("monto no permitido")
                continuar=input("Para intentar de nuevo ponga N: ")
            else:
                saldo_caja=saldo_caja-monto
                saldo_us=saldo_us-monto
                print("saldo cuenta=", saldo_us)
                print("saldo cajero=", saldo_caja)

                if monto>=20000:
                    out20=int(monto/20000)
                    monto=monto-(out20*20000)
                if monto>=10000:
                    out10=int(monto/10000)
                    monto=monto-(out10*10000)
                if monto>=5000:
                    out5=int(monto/5000)
                    monto=monto-(out5*5000)
                print("billetes 20000=", out20)
                print("billetes 10000=", out10)
                print("billetes 5000=", out5)
                
                continuar=input("Para intentar de nuevo ponga N: ")
else:
    print("usuario incorrecto")     