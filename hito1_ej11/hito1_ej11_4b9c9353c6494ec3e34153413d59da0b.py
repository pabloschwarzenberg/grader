dinero_cajero=1000000
dinero_usuario=100000
error=0
while True:
    usuario=input("Ingrese usuario: ")
    clave=input("Ingrese clave: ")
    if usuario!="N" and usuario!="10334151":
        print("Exit")
        break
    if usuario=="10334151" and clave=="1803":
        monto_retira=eval(input("Cuanto monto desea retirar: "))
        if dinero_usuario>=monto_retira and dinero_cajero>=monto_retira:
            dinero_cajero=dinero_cajero-monto_retira
            dinero_usuario=dinero_usuario-monto_retira
            print("saldo cuenta="+str(dinero_usuario))
            print("saldo cajero="+str(dinero_cajero))
            if monto_retira>=10000:
                b10k=monto_retira//10000
                r=monto_retira%10000
                b1k=r//1000
            else:
                b1k=r//1000
            print("billetes 10000="+str(b10k))
            print("billetes 1000="+str(b1k))
            break
        else:
            print("monto no permitido")
    else:
        print("clave invalida")
        error=error+1
        if error==3:
            print("tarjeta bloqueada")
            break
