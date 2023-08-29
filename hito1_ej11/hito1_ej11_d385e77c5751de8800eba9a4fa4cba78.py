#Cajero Automático
cajero=1000000
saldo=100000
usuario=10334151
clave=1803
contador1=0
print("\t.:MENÚ ACCESO CAJERO AUTOMATICO:.")
x=int(input(".:Ingrese usuario: "))
if x==usuario:
    while contador1<3:
        y=int(input(".:Ingrese su clave: "))
        if y==clave:
            monto=int(input(".:Ingrese monto a retirar: "))
            if monto>saldo:
                print(".:MONTO NO PERMITIDO!:.")
            else :
                cajero-=monto
                saldo-=monto
                print(".:Saldo cuenta= {}\n.:Saldo cajero= {}".format(saldo,cajero))
                break
        else :
            contador1+=1
            print(".:ERROR:Clave Invalida! Intentelo nuevamente:. ")
    else :
        print(".:TARJETA BLOQUEADA:.")
else :
    print(".:ERROR: Usuario Invalido!:.")