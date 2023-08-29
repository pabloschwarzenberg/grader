#Cajero Automático
#cajero automatico
saldo = 1000000
usuario_valido = 10334151
clave_usuario_valido = 1803
saldo_usuario_valido = 100000
usuario =int(input("Ingrese usuario: "))
while usuario != usuario_valido:
    usuario = int(input("Ingrese usuario nuevamente: "))

clave = int(input("Ingrese clave: "))
intentos = 0
while clave != clave_usuario_valido:
    intentos = intentos + 1
    clave = int(input("Clave invalida , Ingrese nuevamente: "))
    if intentos == 3:
        print("Usted ha intentado erroneamente muchas veces el ingreso a su cuenta, esta ha sido bloqueada por motivos de seguridad")
        break
if intentos != 3: 
    monto_retirado = int(input("Ingrese monto a retirar: "))
    if monto_retirado >= saldo or monto_retirado >= saldo_usuario_valido:
        print("monto no permitido")
    else:
        saldo = saldo - monto_retirado
        saldo_usuario_valido = saldo_usuario_valido - monto_retirado
        print("saldo cuenta =", saldo_usuario_valido)
        print("saldo cajero =", saldo)
