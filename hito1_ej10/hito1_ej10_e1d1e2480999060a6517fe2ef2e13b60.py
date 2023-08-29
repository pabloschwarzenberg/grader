saldo_inicial = 1000000  
usuario_valido = "10334151"  
clave_valida = "1803"  
saldo_usuario = 100000 

intentos = 0  
bloqueado = False 

while True:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if usuario == usuario_valido and clave == clave_valida:
        while True:
            monto = float(input("Ingrese el monto a retirar: "))

            if monto <= saldo_usuario:
                saldo_usuario -= monto
                saldo_inicial -= monto

                print("Retiro exitoso")
                print("saldo cuenta=", saldo_usuario)
                print("saldo cajero=", saldo_inicial)
                break
            else:
                print("Monto no permitido")

        break
    else:
        intentos += 1
        print("Clave inválida")
    if intentos >= 3:
        bloqueado = True
        print("Tarjeta bloqueada")
        break

if not bloqueado:
    print("Gracias por utilizar el cajero")