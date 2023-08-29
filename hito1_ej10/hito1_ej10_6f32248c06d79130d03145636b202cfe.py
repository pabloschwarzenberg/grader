nombre = int(input("Ingrese su usuario: "))
intentos = 0
while intentos < 3:
    intentos += 1
    contra = int(input("Ingrese su contraseña: "))
    if contra != 1803:
        print("clave invalida")
        
    else:
        if contra == 1803:
            monto = int(input("Ingrese el monto a retirar: "))
            if monto > 100000:
                print("monto invalido")
                break
            else:
                if monto < 100000:
                    cajero = 1000000 - monto
                    usuario = 100000 - monto
                    print("saldo cajero="+str(cajero))
                    print("saldo cuenta="+str(usuario))
                    break
else:
    if intentos == 3:
        print("Tarjeta bloqueada")