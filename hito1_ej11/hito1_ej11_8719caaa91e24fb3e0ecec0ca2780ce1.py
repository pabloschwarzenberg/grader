#Cajero Automático
c1=0
c2=0
c3=0
cajero=1000000
saldo=100000
usuario=10334151
clave=1803
contador1=0
x=int(input("Ingrese usuario: "))
if x==usuario:
    while contador1<3:
        y=int(input("Ingrese su clave: "))
        if y==clave:
            monto=int(input("Ingrese monto a retirar: "))
            if monto>saldo:
                print("Monto no permitido!")
            else :
                monto2=monto
                while monto2>=20000:
                    c1+=1
                    monto2-=20000
                while monto2>=10000:
                    c2+=1
                    monto2-=10000
                while monto2>=5000:
                    c3+=1
                    monto2-=5000
                cajero-=monto
                saldo-=monto
                print("saldo cuenta={}\nsaldo cajero={}".format(saldo,cajero))
                print("billetes 20000={}\nbilletes 10000={}\nbilletes 5000={}".format(c1,c2,c3))
                break
        else :
            contador1+=1
            print("Clave Invalida! Intentelo denuevo: ")
    else :
        print("Tarjeta Bloqueada!")
else :
    print("Usuario Invalido!")      