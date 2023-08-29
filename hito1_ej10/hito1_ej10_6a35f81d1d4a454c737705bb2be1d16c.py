#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = 10334151
clave = 1803
intentos = 0

def validar_clave():
    global intentos
    clave_ingresada = int(input("Ingrese su clave: "))
    if clave_ingresada == clave:
        return True
    else:
        intentos += 1
        if intentos < 3:
            print("Clave inválida")
            return validar_clave()
        else:
            print("Tarjeta bloqueada")
            return False


def retirar_dinero():
    global saldo_cajero, saldo_cuenta
    monto = int(input("Ingrese el monto a retirar: "))
    if monto > saldo_cuenta or monto > saldo_cajero:
        print("Monto no permitido")
        retirar_dinero()
    else:
        saldo_cajero -= monto
        saldo_cuenta -= monto
        print("Saldo cuenta: ",saldo_cuenta)
        print("Saldo cajero: ", saldo_cajero)

def main():
    usuario_ingresado = int(input("Ingrese su usuario: "))
    if usuario_ingresado == usuario:
        if validar_clave():
            retirar_dinero()
            opcion = input("¿Desea realizar otra operación? (N para salir): ")
            if opcion.upper() != "N":
                main()
            else:
                print("Gracias por usar nuestro servicio")
                return
        else:
            return
    else:
        print("Usuario inválido")
        main()

main()