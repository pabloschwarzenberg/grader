usuario = 10334151
clave = 1803
saldoInicial = 1000000
saldoIncialUsuario = 100000
salir = False
contadorClaveIncorrecta = 0
if __name__ == "__main__":
    while salir != True:
        if contadorClaveIncorrecta == 2:
            print("tarjeta bloqueada")
            salir = True
        usuarioingresado = int(input("Ingrese su usuario: "))
        claveIngresada = int(input("Ingrese la clave de 4 digitos: "))
        if (claveIngresada == clave) and (usuario == usuarioingresado):
            montoRetirar = int(input("Ingrese el monto a retirar: "))
            if montoRetirar <= saldoIncialUsuario:
                saldoIncialUsuario -= montoRetirar
                saldoInicial -= montoRetirar
                print("saldo cuenta={}".format(saldoIncialUsuario))
                print("saldo cajero={}".format(saldoInicial))
                deseaSalir = input("N: ")
            else:
                print("monto no permitido")
        else:
            print("clave invalida")
            contadorClaveIncorrecta += 1
        if not deseaSalir.upper() == "N":
            salir = True