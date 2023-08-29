#Cajero Automático
x=int(input("introdusca su usuario"))
y=int(input("introdusca su clave"))

if x==10334151 and y ==1803:
    z=int(input("monto a retirar"))
    if z<=100000:
        a= 100000-z
        b= 1000000-z
        print("saldo cuenta=",a)
        print("saldo cajero=",b)
    else:
        print("monto no permitido")
else:
    print("clave invalida")
    x=int(input("introdusca al usuario"))
    y=int(input("introdusca su clave"))
    if x==10334151 and y ==1803:
        z=int(input("monto a retirar"))
        if z<=100000:
            a= 100000-z
            b= 1000000-z
            print("saldo cuenta=",a)
            print("saldo cajero=",b)
        else:
            print("monto no permitido")
    else:
        print("clave invalida")
        x=int(input("introdusca al usuario"))
        y=int(input("introdusca su clave"))
        if x==10334151 and y ==1803:
            z=int(input("monto a retirar"))
            if z<=100000:
                a= 100000-z
                b= 1000000-z
                print("saldo cuenta=",a)
                print("saldo cajero=",b)
            else:
                print("monto no permitido")
        else:
            print("tarjeta bloqueada")      