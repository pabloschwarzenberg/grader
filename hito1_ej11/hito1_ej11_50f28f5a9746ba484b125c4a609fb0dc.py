caj=1000000
bill20k=20
b20k=20000
c20k=0
bill10k=40
b10k=10000
c10k=0
b5k=5000
bill5k=40
c5k=0
tarj=1
while True:
    for i in range (3):
        usu=input("Ingrese usuario: ")
        con=int(input("Ingrese contraseña: "))
        if usu=="10334151" and con==1803:
            sald=100000
            break
        else:
            print("clave invalida")
    if usu=="10334151" and con==1803:
        break
    else:
        print("Tarjeta Bloqueada")
        tarj=0
        break

while True:
    if tarj==0:
        break
    else:
        print("Saldo= " ,sald)
        ret=input("Ingrese monto a retirar: ")
        if ret.isdigit():
            ret=int(ret)
            if sald<ret or caj<ret:
                print("Monto no permitido")
            else:
                while True:
                    if ret>=b20k:
                        c20k=ret//b20k
                        bill20k-=c20k
                        sald=sald-(b20k*c20k)
                        caj=caj-(b20k*c20k)
                        ret=ret-(b20k*c20k)
                    elif ret>=b10k:
                        c10k=ret//b10k
                        bill10k-=c10k
                        sald=sald-(b10k*c10k)
                        caj=caj-(b10k*c10k)
                        ret=ret-(b10k*c10k)
                    elif ret>=b5k:
                        c5k=ret//b5k
                        bill5k-=c5k
                        sald-=(b5k*c5k)
                        caj-=(b5k*c5k)
                        ret-=(b5k*c5k)
                    else:
                        if ret==0:
                            print("saldo cuenta=" ,sald)
                            print("saldo cajero=" ,caj)
                            print("billetes 20000=" ,c20k)
                            print("billetes 10000=" ,c10k)                   
                            print("billetes 5000=" ,c5k)
                            break
        else:
            if ret=="N":
                continue
            else:
                print("Terminando programa")
                break