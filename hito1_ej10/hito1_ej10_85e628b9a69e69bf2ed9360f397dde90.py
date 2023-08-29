#Cajero Automático
a=int(input("Ingrese usuario: "))
b=input("Ingrese clave: ")
if b!="1803":
    print("clave invalida")
    b=input("Ingrese clave: ")
    if b!="1803":
        print("clave invalida")
        b=input("Ingrese clave: ")
        if b!="1803":
            print("tarjeta bloqueada")
        else:
            c=int(input("Monto a retirar: "))
    else:
        c=int(input("Monto a retirar: "))
else:
    c=int(input("Monto a retirar: "))
if c>100000:
    print("Monto no permitido")
else:
    cajero=1000000-c
    cuenta=100000-c
    print("saldo cuenta=",cuenta)
    print("saldo cajero=",cajero)
input("")
