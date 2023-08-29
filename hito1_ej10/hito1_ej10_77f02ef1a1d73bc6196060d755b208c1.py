si = 1000000
sc = 100000
usuario = 10334151
clave = 1803
intentos = 0

while True:
    usu = int(input("Ingrese Usuario: "))
    if usu == usuario:
        clav = input("Ingrese Clave: ")
        if clav == str(clave):
            montor = int(input("Ingrese monto a retirar: "))
            if montor > sc:
                print("Monto no permitido")
                continue
            if montor <= sc:
                sc -= montor
                si -= montor
                print("Saldo cuenta=", sc)
                print("Saldo cajero=", si)
                pr = input("Desea continuar? N: para salir S: para continuar: ")
                if pr == "N":
                    break
                elif pr == "S":
                    continue
                else:
                    print("Opción inválida. Saliendo del programa.")
                    break
        else:
            print("Clave Incorrecta")
            intentos += 1
        if intentos == 3:
            print("Tarjeta bloqueada")
            break