cajero = 1000000
total_b20 = 20
total_b10 = 40
total_b5 = 40
b5 = 5000
cuenta = 100000
usuario1 = "10334151"
contrasena = "1803"
usuario = input("user: ")
if usuario == usuario1:
    contador = 0
    while contador < 3 :
        clave = input("Ingrese la Contraseña porfavor: ")
        if clave != contrasena:
            contador += 1
            print("La contraseña ingresada no es valida")
            continue
        retiro = eval(input("Cual es el monto a retirar?: "))
        if retiro > 100000:
            print("el monto seleccionado, no correponde")
        else:
            #cuenta de billetes
            sumador = 1
            while True:
                if b5 * sumador == retiro :
                    break
                sumador += 1
            print(sumador)
            total_cajero = cajero - retiro
            total_cuenta = cuenta - retiro
            print("saldo cuenta=", total_cuenta,
            "\nsaldo cajero=", total_cajero, "\nbilletes 20000=", 0, 
            "\nbilletes 10000=", 0, "\nbilletes 5000=", sumador)
            x = input()
            if x != "N" :
                break
            else:
                continue