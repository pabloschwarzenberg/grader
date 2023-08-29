#Cajero Automático
saldo_cuenta = 100000
saldo_cajero = 1000000
N = "N"
while N == "N":
    user = input("Ingrese su nombre de usuario :")
    if user == "10334151":
        #Asigna 2 intentos porque toma en cuenta el intento antes de entrar al ciclo
        intentos = 2
        password = input("Ingrese su clave :")
        while password != "1803" and intentos > 0:
            print("clave inválida")
            intentos -= 1
            password = input("Ingrese su clave :")
        if intentos == 0:
            print("tarjeta bloqueada")
            N = "deiauwfueiwbf"
        if password == "1803":
            monto = int(input("Ingrese el monto a retirar :"))
            while monto < 0 or monto > saldo_cuenta:
                print("monto no permitido")
                monto = int(input("Ingrese el monto a retirar :"))
            saldo_cuenta -= monto
            saldo_cajero -= monto
            print("saldo cuenta =",saldo_cuenta)
            print("saldo cajero =",saldo_cajero)
            print("Si desea continuar presione 'N'")
            N = input(">>> ")