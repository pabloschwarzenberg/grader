usuario = int(input("Ingrese usuario: "))
persona = 100000
cajero  = 1000000
i = 0
while i < 3:
    clave = int(input("Ingrese clave: "))
    if usuario == 10334151 and clave == 1803:
        monto = int(input("Ingrese monto a retirar: "))
        if monto > persona:
            print("Monto invalido")
        else:
            salida = []
            montoP = "Saldo cuenta= " + str(persona - monto)
            montoC = "Saldo cajero= " + str(cajero  - monto)
            salida.append(montoP)
            salida.append(montoC)
            print(salida)
        break
    i += 1
if i == 3:
    print("tarjeta bloqueada")