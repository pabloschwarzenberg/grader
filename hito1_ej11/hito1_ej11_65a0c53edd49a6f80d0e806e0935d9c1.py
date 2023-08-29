saldocajero = 1000000
saldocliente = 100000
N = "N"
usuario = 0
clave = 0
cont = 0
B20 = 20000
B10 = 10000
B5 = 5000

while usuario != 10334151:
    usuario = int(input("Ingrese usuario: "))
    if usuario != 10334151:
        print("Usuario incorrecto")

while clave != 1803 and cont != 3:
    clave = int(input("Ingrese contraseña: "))
    if clave != 1803:
        print("Contraseña incorrecta")
        cont += 1
    elif cont == 3:
        print("TARJETA BLOQUEADA")
    else:
        while N == "N":
            montoretiro = int(input("Ingrese monto a retirar: "))
            if montoretiro > saldocliente:
                print("Monto no permitido")
                N = input("Desea realizar otra operación? (N): ")
            else:
                nsaldocajero = saldocajero - montoretiro
                nsaldocliente = saldocliente - montoretiro
                print("Saldo cuenta =",nsaldocliente)
                print("Saldo cajero =",nsaldocajero)
                N = input("Desea realizar otra operación? (N): ") 

if montoretiro > 0:
    bill20 = montoretiro // B20
    montoretiro -= bill20 * B20

    bill10 = montoretiro // B10
    montoretiro -= bill10 * B10

    bill5 = montoretiro // B5
    montoretiro -= bill5 * B5

    print("Billetes 20000 =",bill20)
    print("Billetes 20000 =",bill10)
    print("Billetes 20000 =",bill5)
else:
    print("No hay billetes para retirar")