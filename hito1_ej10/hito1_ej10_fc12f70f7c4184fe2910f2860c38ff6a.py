usuario=10334151
clave=1803
saldo_cajero=1000000
saldo_usuario=100000
contador=0
u=int(input("ingrese el usuario: "))
c=int(input("ingrese su clave: "))
if u==usuario and c==clave:
    print("Su saldo actual es de $100.000")
    retiro=int(input("¿Cuanto desea retirar?: "))
    if retiro>saldo_usuario:
            print("Monto no válido")
    else:
        saldo_restante_usuario=saldo_usuario-retiro
        saldo_restante_cajero=saldo_cajero-retiro
        print("saldo cuenta=",saldo_restante_usuario)
        print("saldo cajero=",saldo_restante_cajero)
        v=20000
        d=10000
        c=5000
else:
    while True:
        contador+=1
        clave2=int(input("CLAVE INVALIDA. Ingrese su clave: "))
        if clave2==clave:
                print("Su saldo actual es de $100.000")
                retiro=int(input("¿Cuanto desea retirar?: "))
                if retiro>saldo_usuario:
                    print("Monto no válido")
                else:
                    saldo_restante_usuario=saldo_usuario-retiro
                    saldo_restante_cajero=saldo_cajero-retiro
                    print("saldo cuenta=",saldo_restante_usuario)
                    print("saldo cajero=",saldo_restante_cajero)
                    v=20000
                    d=10000
                    c=5000
                    cantidad_v=retiro/v
                    cantidad_d=retiro/d
                    cantidad_c=retiro/c
        if contador==2:
            print("TARJETA BLOQUEADA")
            break
    