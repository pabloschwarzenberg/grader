cajero = 1000000
billetes_20 = 20
billetes_10 = 40
billetes_5 = 40
billete5 = 5000
cuenta = 100000
usuario = "10334151"
contraseña = "1803"
n_cuenta = eval(input("Ingrese su N° de cuenta: "))
if usuario == n_cuenta:
    contador = 0
    while contador < 3:
        clave = eval(input("Ingrese su clave: "))
        if clave != contraseña:
            contador += 1
            print("Clave invalida")
            if contador == 3:
                print("Tarjeta bloqueada")
            continue

        retiro = eval(input("Cuanto dinero desea retirar: "))
        if retiro > 100000:
            print("monto no permitido")
        else:
            suma = 1
            while True:
                if billete5 * suma == retiro:
                    break
                suma += 1
            print(suma)
            saldo_cajero = cajero - retiro
            saldo_cuenta = cuenta - retiro
            print("saldo cuenta=", saldo_cuenta)
            print("saldo cajero=", saldo_cajero)
            print("billetes 20000=", 0)
            print("billetes 10000=", 0)
            print("billetes 5000=", suma)