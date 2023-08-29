saldo_cajero = 1000000
saldo_usuario = 100000
decision = ""
intentos = 0

print("Bienvenido al cajero automatico. Ingrese el numero de usuario.")
num_usuario = int(input(""))
while (num_usuario != 10334151):
    print("Numero de usuario incorrecto, ingrese nuevamente.")
    num_usuario = int(input(""))
print("Ingrese la clave")
clave = int(input())
while (clave == 1803):
    while saldo_cajero <= 1000000:
        while (decision != "N") and (decision != "n"):
            print("Unica accion permitida es el retiro del dinero, ¿cuanto desea retirar?")
            print("Hay actualmente",saldo_cajero,"disponible")
            try:
                retiro = float(int(input()))
            except EOFError:
                break

            while (retiro > saldo_cajero):
                print("Retiro invalido, ingrese la cantidad nuevamente")
                try:
                    retiro = float(int(input()))
                except EOFError:
                    break
            saldo_usuario = saldo_usuario - retiro
            saldo_cajero = saldo_cajero - retiro
            print("saldo cuenta=",saldo_usuario)
            print("saldo cajero=",saldo_cajero)
            print("¿Desea seguir retirando dinero? S - N")
            decision = input("")
        break
    break
print("Gracias por utilizar este cajero.")
while (clave != 1803):
    intentos =+ 1
    clave = int(input("Te has equivocado, te quedan",intentos,"intentos."))
    while intentos == 3:
        print("Tarjeta bloqueada")
        break
    break