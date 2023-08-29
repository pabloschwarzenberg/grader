#Cajero Automático
sc=1000000
su=100000
intentos=3
username=int(input())
clave=int(1803)
if username==10334151:
    while intentos>0:
        claveu=int(input("Ingrese su clave porfavor "))
        if claveu==clave:
            print("clave correcta")
            break
        else:
            print("clave incorrecta intente nuevamente ")
        intentos-=1
if intentos==0:
    print("Tarjeta Bloqueada")
else:
    monto=int(input("ingrese monto por favor "))
    if monto<=su:
        su-=monto
        sc-=monto
        print("saldo cuenta= ",su)
        print("saldo cajero= ",sc)
    elif monto>su:
        print("monto no permitido")    