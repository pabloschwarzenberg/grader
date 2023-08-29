#Cajero Automático
saldo_cajero = 10**6
saldo_cuenta = 10**5

intentos = 0

user = -1
pw = -1

while user != 10334151 or pw != 1803:
    if intentos >= 3:
        print("[!] Has pasado el limite de intentos.")
        break
    try:
        user = int(input("\nIngrese usuario: "))
        pw = int(input("Ingrese clave: "))
    except Exception as errorMsg:
        print("\n[!] Error: %s\n[!] Ingresa solo numeros enteros!!!" % (errorMsg))
        continue
    intentos += 1

else:

    print("\nBienvenido <%d>" % (user))
    print("Su saldo es de: %d" % (saldo_cuenta))
    monto = -1
    while monto > saldo_cuenta or monto % 5000 != 0 :

        try:
            monto = int(input("\n[!]Solo multiplos de 5000\nIngrese monto a retirar: "))
        except Exception as errorMsg:
            print("\n[!] Error: %s\n[!] Ingresa solo numeros enteros!!!" % (errorMsg))
            continue

        if monto > saldo_cuenta:
            print("\n[!] Saldo insuficiente\n")
        elif monto % 5000 != 0:
            print("\n[!] Monto incorrecto\n")
        else:
            print("\n[!] Monto retirado exitosamente!\n")
    else:
        saldo_cuenta -= monto
        saldo_cajero -= monto

        print("[!] Su saldo es de: %d" % (saldo_cuenta))
        print("[!] Saldo cajero de: %d" % (saldo_cajero))
