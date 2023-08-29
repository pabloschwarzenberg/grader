saldo_inicial = 1000000
saldo_usuario = 100000
intentos = 0

usuario_correcto = 10334151
clave_correcta = 1803


usuario = int(input("Ingrese su usuario: "))
clave = int(input("Ingrese su clave: "))

if usuario == usuario_correcto and clave == clave_correcta:
    print("Acceso permitido")
else:
    print("Usuario o clave incorrectos")
    exit()

while True:
    monto = int(input("Ingrese el monto a retirar: "))


    if monto <= 0 or monto > saldo_usuario:
        print("Monto no permitido")
        continue


    saldo_usuario -= monto
    saldo_inicial -= monto


    print("saldo cuenta =", saldo_usuario)
    print("saldo cajero =", saldo_inicial)


    break