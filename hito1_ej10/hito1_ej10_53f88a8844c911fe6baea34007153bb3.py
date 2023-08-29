#Cajero Automático
usuario=int(input("Usuario: "))
clave=int(input("Clave: "))

money_cajero=1000000
money_user=100000
monto=0
p=0
while p<3:
    if usuario==10334151 and clave!=1803:
        print("clave invalida")
        clave=int(input("Clave: "))

    if usuario==10334151 and clave==1803:
        monto=input("Monto a retirar:")
        if monto!="N":
          SystemExit()
        else:
            monto=int(monto)
            if monto>money_user:
                print("monto no permitido")
            else:
                a=money_user - monto
                b=money_cajero-monto
                print("saldo cuenta:",a)
                print("saldo cajero:",b)
                SystemExit()
    p=p+1

if p==3:
    print("tarjeta bloqueada")
    SystemExit()
