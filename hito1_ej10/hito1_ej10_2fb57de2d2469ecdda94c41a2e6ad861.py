import sys

u=10334151
c=1803
caja=1000000
saldo=100000
usuario=int(input("Ingrese usuario: "))
clave=int(input("Ingrese clave: "))
while usuario==u or usuario!=u:
    if usuario==u and clave==c:
        monto=int(input("Monto a retirar: "))
        while monto>100000:
            print("monto no permitido")
            monto=int(input("Monto a retirar: "))
        else:
            print("saldo cuenta= ", saldo-monto)
            print("saldo cajero= ", caja-monto)
        break
    contador=0
    if usuario==u and clave!=c and contador<3:
        while clave!=c:
            print("clave invalida")
            contador+=1
            cl=int(input("Ingrese clave: "))
            if cl==c:
                monto=int(input("Monto a retirar: "))
                while monto>100000:
                    print("monto no permitido")
                    monto=int(input("Monto a retirar: "))
                else:
                    print("saldo cuenta= ", saldo-monto)
                    print("saldo cajero= ", caja-monto)
                break
            if contador==2 and cl!=c:
                print("tarjeta bloqueada")
                sys.exit(1)
        break
    if usuario!=u:
        usuario=int(input("Ingrese usuario: "))
        clave=int(input("Ingrese clave: "))