#Cajero Automático
saldo_cajero = 1000000
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
            print("saldo cuenta=",saldo_cuenta)
            print("saldo cajero=",saldo_cajero)
            monto = True
        else:
            print("monto no permitido")
    continuar = input("¿Desea hacer otra operación? ")
    continuar = continuar.upper()
    if continuar == "N":
        monto = False
    else:
        sesion = False

