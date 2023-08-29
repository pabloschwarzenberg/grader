saldo_cajero = {
    20000: 20,
    10000: 40,
    5000: 40
}

saldo_cuenta = {
    10334151: {
        'clave': 1803,
        'saldo': 100000
    }
}

intentos = 0

while True:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))
    
    if usuario in saldo_cuenta and clave == saldo_cuenta[usuario]['clave']:
        print("Bienvenido/a")
        break
    else:
        print("Usuario o clave inválidos")
        intentos += 1
    
    if intentos == 3:
        print("Tarjeta bloqueada")
        exit()

monto_retiro = int(input("Ingrese el monto a retirar: "))

if monto_retiro > saldo_cuenta[usuario]['saldo']:
    print("Monto no permitido")
else:
    for billete in saldo_cajero:
        cantidad_billetes = min(monto_retiro // billete, saldo_cajero[billete])
        monto_retiro -= cantidad_billetes * billete
        saldo_cajero[billete] -= cantidad_billetes
        print("billetes ",billete,"=",cantidad_billetes,sep="")
        
    saldo_cuenta[usuario]['saldo'] -= monto_retiro
    print("saldo cuenta=",saldo_cuenta[usuario]['saldo'],sep="")
    print("saldo cajero=",sum(billete * saldo_cajero[billete] for billete in saldo_cajero),sep="")
