#Cajero Automático
cajero = 1000000
saldo = 100000
usuario = int(input("Ingrese el usuario: "))
codigo = int(input("Ingrese la contraseña: "))
while True:
    if usuario == 10334151 and codigo == 1803:
        print("Usuario y codigo correctos")
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > saldo and monto > cajero:
            print("monto no permitido")
            break
        if monto < saldo and monto < cajero:
            usuario_final = saldo - monto
            cajero_final = cajero - monto
            print("saldo cuenta=", usuario_final)
            print("saldo cajero=", cajero_final)
            ##Billetes*
            lukas20 = int(monto / 20000)
            monto = monto % 20000
            lukas10 = int(monto / 10000)
            monto = monto % 10000
            lukas5 = int(monto / 5000)
            monto = monto % 5000
            ##Billetes
            print("billetes 20000= ", lukas20)
            print("billetes 10000= ", lukas10)
            print("billetes 5000= ", lukas5)
        if monto != "N":
            break
  
    if usuario != 10334151 or codigo != 1803:
        print("clave invalida")
        print("INTENTO N°2")
        codigo = int(input("Ingrese la codigo denuevo: "))
        if usuario != 10334151 or codigo != 1803:
            print("clave invalida")
            print("INTENTO N°3")
            codigo = str(int(input("Ingrese la codigo denuevo: "))
            if usuario != 10334151 or codigo != 1803:
              print("tarjeta bloqueada")
              break      