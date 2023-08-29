import sys
intentos = 0 
Saldo = 100000
billete20 = 20000
billete10 = 10000
billete5 = 5000
conteo20= 20
conteo10= 40
conteo5= 40
total20= conteo20*billete20
total10= conteo10*billete10
total5= conteo5*billete5
SaldoIni = total20+total10+total5
billeteR20 = 0
billeteR10 = 0
billeteR5 = 0
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
        SaldoIni = SaldoIni-retiro
        Saldo = Saldo-retiro
        while retiro>0:
            if retiro>=billete20 and conteo20>0:
                retiro = retiro - billete20
                billeteR20 = billeteR20 + 1
                conteo20 = conteo20 - 1
            if retiro>=billete10 and conteo10>0:
                retiro = retiro - billete10
                billeteR10 = billeteR10 + 1
                conteo10 = conteo10 - 1
            if retiro>=billete5 and conteo5>0:
                retiro = retiro - billete5
                billeteR5 = billeteR5 + 1
                conteo5 = conteo5 - 1    
        print("saldo cuenta=", Saldo)
        print("saldo cajero=", SaldoIni)
        print("billetes 20000=", billeteR20)
        print("billetes 10000=", billeteR10)
        print("billetes 5000=", billeteR5)
        print("Para otra operacion aprete `N`, para salir aprete cualquier otra tecla")
        respuesta = input()
        if respuesta != "N" or respuesta != "n":
            break 