#Cajero Automático
import random
saldo_cajero = 1000000
billetes_20k_cajero = 20
billetes_10k_cajero = 40
billetes_5k_cajero = 40
usuario = 10334151
clave = 1803

sesion = False 
usuario_correcto = False

while usuario_correcto == False:
    usuario_ingresado = int(input("Ingrese su número de usuario: "))
    if (usuario_ingresado == usuario):
        saldo_cuenta = 100000
        usuario_correcto = True
    else:
        print("Número de usuario inválido")
intentos = 0
while sesion == False:
    clave_ingresada = int(input("Ingrese su clave: "))
    intentos += 1
    if (clave_ingresada == clave):
        sesion = True
    if not(clave_ingresada == clave) and (intentos != 3):
        print("clave invalida")
    if intentos == 3:
        print("tarjeta bloqueada")
        break
    
while sesion == True:
    monto = False
    while monto == False:
        retiro = int(input("Ingrese el monto a retirar: "))
        if (retiro <= saldo_cuenta) and (retiro <= saldo_cajero):
            saldo_cuenta = saldo_cuenta - retiro
            saldo_cajero = saldo_cajero - retiro
            cantidad_billetes = False
            while cantidad_billetes == False:
                billetes_20k = random.randint(1, 2)
                billetes_10k = random.randint(1, 4)
                billetes_5k = random.randint(1, 4)
                billetes = (billetes_20k * 20000) + (billetes_10k * 10000) + (billetes_5k * 5000)
                if billetes == retiro:
                    cantidad_billetes = True
                
            print("saldo cuenta=",saldo_cuenta)
            print("saldo cajero=",saldo_cajero)
            print("billetes 20000=", billetes_20k)
            print("billetes 10000=", billetes_10k)
            print("billetes 5000=", billetes_5k) 
            monto = True
        else:
            print("monto no permitido")
    continuar = input("¿Desea hacer otra operación? ")
    continuar = continuar.upper()
    if continuar == "N":
        monto = False
    else:
        sesion = False