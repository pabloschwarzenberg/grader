#Cajero Automático
import sys
Saldocajero = 1000000
Saldo = 100000
Usuario = 10334151
Clave = 1803
Contador = 0
while Contador < 3:
    Contraseña = int(input("Ingrese su clave: "))
    if Contraseña != Clave:
        Contador += 1
        print("Clave inválida")
    while Contraseña == Clave:
        Monto = int(input())
        if Monto > Saldo:
            print("Monto no permitido")
        else:
            Saldo -= Monto
            Saldocajero -= Monto
            print("saldo cuenta={}".format(Saldo))
            print("saldo cajero={}".format(Saldocajero))
            choice = (input(">"))
        if (choice == 'N'):
            sys.exit(0)
        else:
            pass
print("Tarjeta bloqueada")
sys.exit(0)