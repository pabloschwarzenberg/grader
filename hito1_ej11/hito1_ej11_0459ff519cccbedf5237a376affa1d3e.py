#Cajero Automático
salcajero= 1000000
user=10334151
clave = 1803
salcuenta = 100000
retiro=0
ingresar_usuario=0
ingrese_clave =0
intentos= 0
billetes_de_20 =20
billetes_de_10 =40
billetes_de_5 =40
while True:
    ingresar_usuario=int(input("ingrese usuario:"))
    ingrese_clave = int(input("ingrese su clave:"))
    
    if clave != ingrese_clave:
        print("clave invalida")
        intentos + 1
    if intentos>3:
        break
    if clave==ingrese_clave:
        retiro=int(input("ingrese monto a retirar:"))
        if retiro>salcuenta:
            print("monto no permitido")
        if retiro<=salcuenta:
            break
        
if retiro<salcuenta:
    sfinalcuenta=salcuenta - retiro
    sfinalcajero = salcajero - retiro
    print("saldo cuenta=",sfinalcuenta)
    print("saldo cajero=",sfinalcajero)
if retiro>=20000:
    division = retiro//20000
    billetes_de_20 = division
    resto = retiro%20000
    division2 = resto//10000
    billetes_de_10 = division2
    resto2 = resto%10000
    division3 = resto2//5000
    billetes_de_5 = division3
if retiro<20000 and retiro>=10000:
    division = retiro//10000
    billetes_de_10 = division
    resto = retiro % 10000
    division2 = resto//5000
    billetes_de_5 = division2
    billetes_de_20 = 0
if retiro<10000 and retiro>=5000:
    division = retiro//5000
    billetes_de_5 = division
    billetes_de_20=0
    billetes_de_10 =0

print("billetes 20000=",billetes_de_20)
print("billetes 10000=",billetes_de_10)
print("billetes 5000=",billetes_de_5)

    
if intentos>3:
    print("tarjeta bloqueada")     