#cajero
#datos
#--------------------------
saldocajero=1000000
clave =1803
usuario = 103341541
saldocuenta=100000
intentos= 3
#------------------------
usuarioingreado=float(input("ingrese el usuario "))
claveingresada=float(input("ingrese la contraseña"))
int(claveingresada)
int(usuarioingreado)
while usuarioingreado != usuario or claveingresada != clave:
    intentos=intentos-1
    print("Usted ingreso el usuario o y/o la clave invalida""\n""ingrese nuevamente los datos")
    usuarioingreado=float(input(""))
    claveingresada=float(input(""))
    int(claveingresada)
    int(usuarioingreado)
    if intentos == 0:
        print("Su tarjeta a sido bloqueada")
        break

if usuarioingreado == usuario and claveingresada == clave:
    print("Bienvenido")
    print("El saldo de su cuenta es:",saldocuenta)
    saldoretirar=int(input("Ingrese el monto a a retirar"))
    while saldoretirar> saldocuenta:
        print("Monto Invalido")
        saldoretirar=int(input("Ingrese el monto a a retirar"))
    if saldoretirar <= saldocuenta:
        saldofinalcuenta=saldocuenta - saldoretirar
        saldofinalcajero=saldocajero - saldoretirar

        print("Saldo cuenta:",saldofinalcuenta)
        print("Saldo cuenta:",saldofinalcajero)
