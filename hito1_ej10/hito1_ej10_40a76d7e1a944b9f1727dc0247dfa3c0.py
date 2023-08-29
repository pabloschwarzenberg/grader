#Cajero Automático
saldo_cajero=1000000
usuario=10334151
clave=1803
saldo_usuario=100000

clave_bloqueada=0
while True:
    cliente=int(input("ingrese su codigo de usuario: "))
    if cliente!=usuario:
        print("usuario invalido ingrese otra vez")
    elif cliente==usuario:
        for i in range(0,3):
            contraseña=int(input("ingrese su clave: "))
            if contraseña!=clave:
                print("clave invalida")
                clave_bloqueada=clave_bloqueada+1
            else:
                break
        if clave_bloqueada==3:
            print("tarjeta bloqueada")
            break
        else:
            salida='N'
            while salida=='N':
                monto=int(input("ingrese monto: "))
                if monto<=saldo_usuario and monto>0:
                    saldo_usuario=saldo_usuario-monto
                    saldo_cajero=saldo_cajero-monto
                    print("saldo cuenta=",saldo_usuario)
                    print("saldo cajero=",saldo_cajero,'\n')
                    print("para salir debe ingresar algo distinto a la letra N")
                    salida=str(input("quiere hacer otra operacion?: "))
                else:
                    print("monto no permitido")
                
            break