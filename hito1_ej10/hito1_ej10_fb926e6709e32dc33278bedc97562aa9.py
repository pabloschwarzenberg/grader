#Cajero Automático
saldo_cajero= 1000000
saldo_usuario= 100000
usuario=10334151
clave=1803
salida="N"
intentos=0
while salida=="N":
    ingresousuario=int(input("ingrese su numero de usuario:"))
    if ingresousuario==usuario :
        ingresovalido = False
        while intentos<3 and ingresovalido==False :
            ingresoclave = int(input("Ingrese su clave:"))
            if ingresoclave==clave:
                ingresovalido=True
                opcorrecta=False
                while opcorrecta==False:
                    monto=int(input("Ingrese monto a retirar:"))
                    if monto<=saldo_usuario and monto<=saldo_cajero:
                        saldo_cajero=saldo_cajero-monto
                        saldo_usuario=saldo_usuario-monto
                        print("saldo cuenta=", saldo_usuario)
                        print("saldo cajero=",saldo_cajero)
                        opcorrecta=True
                    else:
                        print("monto invalido")
                    salida=str(input("si desea realizar otra operación ingrese N"))
            else:
                print("clave invalida")
                intentos=intentos+1
        if intentos==3:
            print("tarjeta bloqueada")
            salida="Y"
    else :
        print("Usuario incorrecto")