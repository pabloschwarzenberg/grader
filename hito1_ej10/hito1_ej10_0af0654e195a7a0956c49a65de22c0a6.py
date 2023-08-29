saldo_cajero=1000000
intentos = 3
clave_invalida=True
monto_posible = True
salida = "N"
while salida == "N":
    usuario = input("Ingresa Usuario:")
    if usuario == "10334151":    
        clave=input("Ingresa clave: ")
        saldo_usuario = 100000
        while clave_invalida and intentos>1:
            if clave == "1803":
                clave_invalida=False
            else:
                clave_invalida=True
                print("Clave invalida, intente nuevamente ")
                intentos = intentos - 1
                clave=input("Ingreso clave: ")
        if clave_invalida == False:
            while monto_posible:
                monto=int(input("Ingrese monto a retirar: "))
                if monto > saldo_cajero and monto > saldo_usuario:
                    print("Este monto excede el maximo del cajero o del usuario")
                    monto_posible = True
                else:
                    saldo_cajero=saldo_cajero-monto
                    saldo_usuario = saldo_usuario - monto
                    print("saldo cuenta="+str(saldo_usuario)+", saldo cajero="+str(saldo_cajero))
                    monto_posible = False
        else:
            print("Tarjeta bloqueada, favor deje de robar.")

    else:
        print("Ese no es el usuario de este cajero, procedere a autodestruirme")

    salida = input("Ingrese N para otra operacion")
