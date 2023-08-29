#Cajero Automático
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
            if monto > 100000 :
                print("monto invalido")
                break
            else:
                if monto < 100000 and monto % 5000 == 0:
                    carga_de_5 = 40
                    carga_de_10 = 40
                    carga_de_20 = 20
                    billetes_de_20 = monto // 20000
                    resto = monto % 20000
                    billetes_de_10 = resto // 10000
                    resto = resto % 10000
                    billetes_de_5 = resto // 5000
                    cajero = 1000000 - monto
                    usuario = 100000 - monto
                    print("billetes de 20000="+str(billetes_de_20))
                    print("billeres de 10000="+str(billetes_de_10))
                    print("billetes de 5000="+str(billetes_de_5))
                    print("saldo cajero="+str(cajero))
                    print("saldo cuenta="+str(usuario))
                    break
else:
    if intentos == 3:
        print("Tarjeta bloqueada")