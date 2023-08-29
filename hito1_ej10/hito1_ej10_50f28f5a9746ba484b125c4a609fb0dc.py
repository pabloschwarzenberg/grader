caj=1000000
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
                sald=sald-ret
                caj=caj-ret
                print("saldo cuenta=" ,sald)
                print("saldo cajero=" ,caj)
                break
        else:
            if ret=="N":
                continue
            else:
                print("Terminando programa")
                break