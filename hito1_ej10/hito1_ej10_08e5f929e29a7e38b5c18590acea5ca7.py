#Cajero Automático
import sys

SaldoIni = 1000000
intentos = 0 
Saldo = 100000
while intentos <3:  
    usuario = int(input("Ingrese usuario: "))
    clave = int(input("Ingrese clave: "))
    if usuario == 10334151 and clave == 1803:        
        print("clave valida")
        break
    if not usuario == 10334151 or not clave ==1803:
        intentos = intentos + 1
        print("clave invalida")
if intentos == 3:
    print("tarjeta bloqueada")
    sys.exit()
while True:
    if intentos <3:
        print("Saldo actual:", Saldo)
        print("Cuanto desea retirar?")
        retiro = int(input())    
    if retiro > Saldo:
        print("Monto no permitido")
    if retiro <= Saldo:
        print("Monto valido, retirando")
        SaldoIni = SaldoIni - retiro
        Saldo = Saldo - retiro
        print("saldo cuenta=", Saldo)
        print("saldo cajero=", SaldoIni)
    print("Para otra operacion aprete `N`, para salir aprete cualquier otra tecla")
    respuesta = input()
    if respuesta != "N" or respuesta != "n":
        break 
      