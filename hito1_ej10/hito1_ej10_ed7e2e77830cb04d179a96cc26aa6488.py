#Cajero Automático

def withdraw(usuario):
    clave = 1803
    intentos = 3
    while intentos > 0:
        x = int(input("Ingrese contraseña: "))
        if x != clave:
            print("clave invalida")
            intentos = intentos - 1
            print(intentos)
        else:
            valor = 2
            return valor
    print("tarjeta bloqueada")


def monto():
    cajero = int(1000000)
    user = int(100000)
    contar = 1
    while contar > 0:
        cuanto = str(input("Ingrese monto a retirar: "))
        if cuanto == "Y":
            contar = 0
        else:
            if 0 <= int(cuanto) <= user:
                cajero = cajero - int(cuanto)
                user = user - int(cuanto)
                print("saldo cuenta =", user)
                print("saldo cajero =", cajero)
                contar = contar + 1
                print("MENSAJE")
                if user == 0:
                    print("No tiene mas dinero en su cuenta, por favor presione N")
            elif int(cuanto) < 0 or int(cuanto) > user:
                print("Monto no permitido")
                contar = contar + 1


usuario = int(input("Ingrese su usuario: "))
if withdraw(usuario) == 2:
    monto()
