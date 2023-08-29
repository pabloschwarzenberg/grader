#Cajero Automático
N = list(range(40))
A = []
R = []
ciclo = 0
dinero = 1000000
saldo = 100000
intentos = 3
n2 = 0



while ciclo == 0:
    y = int(input("digite usuario"))
    x = int(input("digite clave"))
    
    if intentos <= 0 and y == 33:
        print("cuenta bloqueada")
        continue

    if x != 22 or y != 33:
        intentos = intentos-1
        print("usuario o clave inconrrecto, tiene",intentos,"intentos")
        if intentos <= 0:
            print("tarjeta bloqueada")
        continue
        

    retiro = int(input("monto a retirar"))
    while retiro > saldo:
        print("monto invalido")
        retiro = int(input("monto a retirar"))

    if retiro%10000 == 0
        billetes = retiro//1000
        
    nuevoSaldo = saldo - retiro
    nuevoDinero = dinero - retiro
    print("su saldo es",nuevoSaldo)
    print("saldo cajero",nuevoDinero)
    
