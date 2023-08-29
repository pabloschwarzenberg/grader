#Cajero Automático
usuario = 10334151
clave = 1803
saldo = 100000
res = "F"
intentos = 0
monto_cajero = 1000000

usu = int(input("Ingrese su usuario", ))

if usuario == usu:
    while intentos < 3:
        pas = int(input("Ingrese su clave", ))
        intentos = intentos + 1
        if pas == clave:
            print("El saldo de la cuennta es", saldo)
            while res != "N":
                din = int(input("ingrese el dinero deseado",))
                while din > saldo:
                        print("Monto no permitido")
                        din = int(input("ingrese el dinero deseado", ))
                else:
                        saldo = saldo - din
                        monto_cajero = monto_cajero - din
                        print("saldo cuenta=", saldo, ",", "saldo cajero=", monto_cajero)
                        res = input("¿Desea retirar más dinero?",)
                break
            break
        else:
            print("Clave invalida")
    if intentos >= 3:
        print("Tarjeta bloqueada")
else:
    print("Usuario invalido")

print("Finalizo su sesión")