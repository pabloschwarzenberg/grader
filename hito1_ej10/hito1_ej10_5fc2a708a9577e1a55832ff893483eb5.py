usuario=int(input("Usuario: "))
clave=int(input("Clave: "))
saldo_cajero=1000000
saldo_cuenta=100000
n=1
monto=0
a=str(list(range(1,1000000)))
if usuario==10334151 and clave==1803:
    while True:   
        monto=input("Ingrese monto a retirar: ")
        if (not monto in a) and (monto!="N"):
            print("gracias por preferirnos")
            break
        if monto=="N":
             monto=0
        saldo_cajero=(saldo_cajero - int(monto))
        saldo_cuenta=(saldo_cuenta - int(monto))
        if(saldo_cuenta)<0 or (saldo_cajero)<0:
            print("monto no permitido")
            saldo_cajero=(saldo_cajero + int(monto))
            saldo_cuenta=(saldo_cuenta + int(monto))
        print("saldo cuenta=",saldo_cuenta)
        print("saldo cajero=",saldo_cajero)    
elif usuario==10334151 and clave!=1803:
    while n<=2 and clave!=1803:
        print("clave invalida")
        clave=int(input("Clave: "))
        n=n+1
        if clave==1803:
            while True:   
                monto=input("Ingrese monto a retirar: ")
                if (not monto in a) and (monto!="N"):
                    print("gracias por preferirnos")
                    break
                if monto=="N":
                    monto=0
                saldo_cajero=(saldo_cajero - int(monto))
                saldo_cuenta=(saldo_cuenta - int(monto))
                if(saldo_cuenta)<0 or (saldo_cajero)<0:
                    print("monto no permitido")
                    saldo_cajero=(saldo_cajero + int(monto))
                    saldo_cuenta=(saldo_cuenta + int(monto))
                print("saldo cuenta=",saldo_cuenta)
                print("saldo cajero=",saldo_cajero)
        elif n==3:
            print("tarjeta bloqueada")
            break
else:
    print("Usuario invalido")