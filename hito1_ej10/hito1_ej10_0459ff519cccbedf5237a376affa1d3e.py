#Cajero Automático
salcajero= 1000000
user=10334151
clave = 1803
salcuenta = 100000
retiro=0
ingresa_usuario=0
ingresar_clave =0
intento= 0
while True:
    ingresa_usuario=int(input("ingrese usuario:"))
    ingresar_clave = int(input("ingrese su clave:"))
    
    if clave != ingresar_clave:
        print("clave invalida")
        intento + 1
    if intento>3:
        break
    if clave==ingresar_clave:
        retiro=int(input("ingrese monto a retirar:"))
        if retiro>salcuenta:
            print("monto no permitido")
        if retiro<salcuenta:
            break
        
if retiro<salcuenta:
    salfinalcuenta=salcuenta - retiro
    salfinalcajero = salcajero - retiro
    print("saldo cuenta=",salfinalcuenta)
    print("saldo cajero=",salfinalcajero)
    
if intento>3:
    print("tarjeta bloqueada")