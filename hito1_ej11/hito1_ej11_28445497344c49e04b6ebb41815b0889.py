b20=20
b10=40
b5=40
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
                    a20 = min(monto // 20000, b20)
                    a10 = min((monto - a20 * 20000) // 10000, b10)
                    a5 = max((monto - a20 * 20000 - a10 * 10000) // 5000,0)
                    if monto==a20*20000+a10*10000+a5*5000 and monto<=saldo_usuario and monto<=b20*20000+b10*10000+b5*5000 :
                        saldo_usuario = saldo_usuario - monto
                        b20=b20-a20
                        b10=b10-a10
                        b5=b5-a5
                        print("saldo cuenta=", saldo_usuario)
                        print("saldo cajero=", b20*20000+b10*10000+b5*5000)
                        print("billetes 20000=", a20)
                        print("billetes 10000=", a10)
                        print("billetes 5000=", a5)
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