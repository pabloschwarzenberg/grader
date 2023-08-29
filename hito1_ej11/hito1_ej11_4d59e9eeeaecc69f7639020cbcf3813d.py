saldo=1000000
saldo1=100000
billetes=[20000,10000,5000,1000]
user="10334151"
pw="1803"
cuenta=input("cuenta: ")
c=0
while True:
    pw1=input("contraseña: ")
    if pw1==pw:
        monto=int(input("monto a retirar: "))
        if monto>saldo1 or monto<0:
            print("monto no permitido")
        else:
            saldo1-=monto
            saldo-=monto
            print("saldo cuenta={0}\nsaldo cajero={1}".format(saldo1,saldo))
            for x in billetes:
                c=0
                pasar=monto//x
                if pasar>0:
                    for a in range(pasar):
                        monto-=x
                        c+=1
                else:
                    continue
                print("billetes",x,"=",c)
                if monto==0:
                    break
            print("faltan: ",monto)
            break
    elif pw1=="N":
        break
    else:
        c+=1
        print("error")
        if c==3:
            print("tarjeta bloqueada")
            break