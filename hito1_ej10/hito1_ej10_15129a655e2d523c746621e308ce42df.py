#Cajero Automático
usuario=int(input("Ingrese usuario: "))
saldo_cajero=1000000
saldo_usuario=100000
intentos=3
if usuario==10334151:
    clave=False
    while clave==False and intentos>=1:
        contraseña=int(input("Ingrese clave: "))
        if contraseña==1803:
            clave=True
        else:
            clave=False
            print("Clave incorrecta")
            intentos=intentos-1
            print("Intentos restantes: ",intentos)
    if clave==False and intentos<=1:
        print("Ha superado el maximo de intentos, tarjeta bloqueada")

    else:
        todo_bien="N"
        while todo_bien=="N" and saldo_usuario>0:
            monto=int(input("Ingrese el monto a retirar"))
            if monto<=saldo_usuario:
                saldo_cajero=saldo_cajero-monto
                saldo_usuario=saldo_usuario-monto
                print("Saldo cuenta=",saldo_usuario)
                print("Saldo cajero=",saldo_cajero)
                todo_bien=input("Para continuar presione N: ")
            else:
                print("Ha superado los fondos de su cuenta, intente nuevamente")
                todo_bien=input("Para continuar presione N: ")

else:
    print("Usuario incorrecto")