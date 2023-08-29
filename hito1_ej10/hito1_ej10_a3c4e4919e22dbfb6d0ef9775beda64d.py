salInicialCajero = 1000000
salCuentaUser = 100000

user =  int(input("Ingrese USER: ")) #10334151
pw = int(input("Ingrese PASSWORD: ")) #1803

intento = 1

while pw != 1803:

    if intento == 3:

        print("tarjeta bloqueada")
        break

    print("clave invalida")
    intento += 1

    pw = int(input("Ingrese PASSWORD: ")) #1803

giro = int(input("Ingrese el monto a retirar: $"))

while giro < 0 or giro > 100000:

    if giro < 0:

        print("Ingrese un giro mayor a 0.")
        giro = int(input("Ingrese el monto a retirar: $"))

    else:

        print("monto no permitido")
        giro = int(input("Ingrese el monto a retirar: $"))

while salCuentaUser < giro:

    print("monto no permitido")
    giro = int(input("Ingrese el monto a retirar: $"))


salCuentaUser = salCuentaUser - giro
salInicialCajero = salInicialCajero - giro

print("saldo cuenta=", salCuentaUser)
print("saldo cajero=", salInicialCajero)