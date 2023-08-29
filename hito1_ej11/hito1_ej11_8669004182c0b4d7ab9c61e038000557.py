#Cajero Automático
 usuario = int(input("Ingrese el usuario: "))
clave = int(input("Ingrese su clave: "))

intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
user = 10334151
passw = 1803

while clave != passw:
    intentos += 1

    if clave == passw:
        print("clave incorrecta")
        break

    if intentos > 3:
        break

    clave = int(input("Ingrese de nuevo su clave: "))


if intentos > 3:
    print("tarjeta bloqueada")     