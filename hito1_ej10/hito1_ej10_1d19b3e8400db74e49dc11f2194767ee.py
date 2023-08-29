#Cajero Automático
saldo_inicial=1000000
saldo_usuario=100000
intentos=0

while True:
    usuario=input("Ingrese su usuario: ")
    clave=input("Ingrese su clave: ")

    if usuario=="10334151" and clave=="1803":
        print("Ingreso exitoso")
        break
    else:
        intentos=intentos+1
        print("Clave invalida")
    if intentos==3:
        print("Tarjeta bloqueada")
        exit()
while True:
    monto=int(input("Ingrese el monto a retirar: "))
    if monto<=0 or monto>saldo_usuario:
        print("Monto no permitido")
    else:
        saldo_usuario=saldo_usuario-monto
        saldo_inicial=saldo_inicial-monto
        print("Retiro exitoso")
        print("Saldo cuenta=",saldo_usuario)
        print("Saldo cajero=",saldo_inicial)
        print()

    respuesta=input("¿Desea realizar otro retiro? (S/N): ")
    if respuesta.upper()!="S":
        break     