i=0
a=0
b=0
c=0
while i<3:
    saldo_cajero=1000000
    saldo_cuenta=100000
    usuario=int(input("usuario:"))
    clave=int(input("clave:"))
    if usuario==10334151 and clave==1803:
        monto=int(input("Indique monto a sacar: "))
        if monto>100000:
            print("monto no permitido")
            continue
        elif monto<=100000:
            saldo_cajero=saldo_cajero-monto
            saldo_cuenta=saldo_cuenta-monto
            monto1=monto%20000
            a=(monto-monto1)/20000
            monto2=monto1%10000
            b=(monto1-monto2)/10000
            monto3=monto2%5000
            c=(monto2-monto3)/5000
            a1=str(a).split(".")[0]
            b1=str(b).split(".")[0]
            c1=str(c).split(".")[0]
            if monto3!=0:
                print("el cajero no tiene billetes para completar el giro")
                continue
            print("saldo cuenta=",saldo_cuenta)
            print("saldo cajero=",saldo_cajero)
            print("billetes 20000=",a1)
            print("billetes 10000=",b1)
            print("billetes 5000=",c1)
            continuidad=input("continudad:")
            if continuidad=="N":
                continue
            else:
                break
    else:
        print("clave inválida")
        i+=1
if i==3:
    print("clave bloqueada")

