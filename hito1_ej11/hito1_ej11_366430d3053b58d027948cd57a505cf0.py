# Cajero automatico 2
# Entrada
cajero = 1000000
user = int(input("Ingrese usuario: "))

# Variables
intentos = 0
i = 0
clave = 1803
clave_ingresada = 0
saldo_user = 100000

# Desgloce de billetes
# Billetes 20,000
billete_20 = 20000
resto_20 = 0
# Billetes 10,000
billete_10 = 10000
resto_10 = 0
# Billetes 5,000
billete_5 =  5000

# Proceso
# Validacion de la clave
while i < 3 and clave_ingresada != clave:
    clave_ingresada = int(input("Ingrese clave: "))
    if clave_ingresada == clave:
        retiro = int(input("Ingrese monto a retirar: "))
        if 0 <= retiro <= saldo_user:
            saldo_user = saldo_user - retiro
            cajero = cajero - retiro
            # Billete 20,000
            billete_20 = retiro // 20000
            resto_20 = retiro % 20000
            # Billete 10,000
            billete_10 = resto_20 // 10000
            resto_10 = resto_20 % 10000
            # Billete 5,000
            billete_5 = resto_10 // 5000
        else:
            print("** Monto invalido **")
            retiro = int(input("Ingrese monto a retirar nuevamente: "))
            if 0 <= retiro <= saldo_user:
                saldo_user = saldo_user - retiro
                cajero = cajero - retiro
                # Billete 20,000
                billete_20 = retiro // 20000
                resto_20 = retiro % 20000
                # Billete 10,000
                billete_10 = resto_20 // 10000
                resto_10 = resto_20 % 10000
                # Billete 5,000
                billete_5 = resto_10 // 5000

    else:
        if clave_ingresada != clave:
            print("** Clave invalida ** ")
            intentos += 1
        if intentos == 3:
            print("** Tarjeta bloqueada **")
    i += 1
# Salida
print("**************************")
print("Saldo cuenta", "=", saldo_user)
print("Saldo cajero", "=", cajero)
print("Billetes 20000", "=", billete_20)
print("Billetes 10000", "=", billete_10)
print("Billetes 5000", "=", billete_5)
print("**************************")