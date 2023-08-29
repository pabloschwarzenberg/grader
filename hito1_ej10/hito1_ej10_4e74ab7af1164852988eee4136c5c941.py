saldo_inicial = 1000000
saldo_cuenta = 100000
intentos = 0

while intentos < 3:
    usuario = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su clave: "))

    if usuario == 10334151 and clave == 1803:
        print("Clave correcta")
        opcion = "S"
        while opcion == "S":
            monto = int(input("Ingrese el monto a retirar: "))
            if monto <= saldo_cuenta:
                saldo_cuenta -= monto
                saldo_inicial -= monto
                print(f"Saldo cuenta = {saldo_cuenta}")
                print(f"Saldo cajero = {saldo_inicial}")
            else:
                print("Monto no permitido")
            opcion = input("¿Desea realizar otro retiro? (S/N): ")
            opcion = opcion.upper()
        break
    else:
        print("Clave inválida")
        intentos += 1

if intentos == 3:
    print("Tarjeta bloqueada")
