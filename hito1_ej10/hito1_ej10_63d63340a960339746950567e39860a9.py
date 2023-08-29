#Cajero Automático
usuario = int(input("ingrese su usuario: "))
clave = int(input("ingrese su clave: "))

cajero=1000000
cuenta=100000

fallos = 0
i=0

while fallos<3 and i<1 :
    if clave != 1803:
        print("clave invalida")
        fallos +=1
        if fallos==3:
            print("tarjeta bloqueada")
        else:
            clave = int(input("ingrese su clave: "))
    else:
        monto = int(input("ingrese su monto: "))
        if monto<=100000:
            print("saldo cuenta=",cuenta-monto)
            print("saldo cajero=",cajero-monto)
            i += 1
            
        else:
            print("monto no permitido")