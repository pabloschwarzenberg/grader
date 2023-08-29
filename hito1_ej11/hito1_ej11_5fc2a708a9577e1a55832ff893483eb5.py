usuario=int(input("Usuario: "))
clave=int(input("Clave: "))
saldo_cajero=1000000
saldo_cuenta=100000
n=1
monto=0
billetes5=40
billetes10=40
billetes20=20
a=str(list(range(1,1000000)))
if usuario==10334151 and clave==1803:
    while True:   
        monto=input("Ingrese monto a retirar: ")
        if (not monto in a) and (monto!="N"):
            print("gracias por preferirnos")
            break
        if monto=="N":
             monto=0
        d20=(int(monto)//20000)
        d10=(int(monto)%20000)//10000
        d5=((int(monto)%20000)%10000)//5000
        if int(monto)<=saldo_cuenta or int(monto)<=saldo_cajero:
            billetes20=int(billetes20-d20)
            billetes10=int(billetes10-d10)
            billetes5=int(billetes5-d5)
        if (int(monto)//5000)!=0:
            saldo_cajero=(saldo_cajero - int(monto))
            saldo_cuenta=(saldo_cuenta - int(monto))
        if d20!=0:
            print("billetes 20000=",d20)
        if d10!=0:
            print("billetes 10000=",d10)
        if d5!=0:
            print("billetes 5000=",d5)
        if (int(monto)//5000)==0:
            print("porfavor, utilice multiplos de 5000")
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
                d20=(int(monto)//20000)
                d10=(int(monto)%20000)//10000
                d5=((int(monto)%20000)%10000)//5000
                if int(monto)<=saldo_cuenta or int(monto)<=saldo_cajero:
                    billetes20=int(billetes20-d20)
                    billetes10=int(billetes10-d10)
                    billetes5=int(billetes5-d5)
                if (int(monto)//5000)!=0:
                    saldo_cajero=(saldo_cajero - int(monto))
                    saldo_cuenta=(saldo_cuenta - int(monto))
                if d20!=0:
                    print("billetes 20000=",d20)
                if d10!=0:
                    print("billetes 10000=",d10)
                if d5!=0:
                    print("billetes 5000=",d5)
                if (int(monto)//5000)==0:
                    print("porfavor, utilice multiplos de 5000")
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