saldo=1000000
saldoc=100000
user="10334151"
pw="1803"
cuenta=input("cuenta: ")
c=0
while True:
    pw1=input("contraseña: ")
    if pw1==pw:
        monto=int(input("monto a retirar: "))
        if monto>saldoc or monto<0:
            print("monto no permitido")
        else:
            saldoc-=monto
            saldo-=monto
            print("saldo cuenta={0}\nsaldo cajero={1}".format(saldoc,saldo))
            break
    elif pw1=="N":
        break
    else:
        c+=1
        print("error")
        if c==3:
            print("tarjeta bloqueada")
            break