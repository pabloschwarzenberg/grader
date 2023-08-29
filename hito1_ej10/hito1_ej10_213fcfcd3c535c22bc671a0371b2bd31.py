#Cajero Automático
saldo_cajero=int(1000000)
saldo_cuenta=int(100000)
x=int(3)
usuario=input("ingrese usuario: ")
clave=input("ingrese clave: ")
if usuario =="10334151":
    if clave =="1803":
        print("saldo cajero: ",saldo_cajero)
        print("saldo cuenta: ",saldo_cuenta)
        while x>0:
            print("intentos restantes: ",x)
            clave=input("ingrese clave: ")
            if clave =="1803":
                retirar=input(int(("ingrese monto a retirar: ")
            else:
                x=x-1
    else:
        print("clave no válida")
else:
    print("usuario no válido")
