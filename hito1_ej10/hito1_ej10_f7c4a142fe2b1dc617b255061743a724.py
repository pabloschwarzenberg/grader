saldo_cajero = 1000000
# nombre Real tratado como numero, o sea, int()
usuario_verdadero = 10334151
# clave Real tratar como numero int()
clave_real = 1803
# saldo inicial usuario $100.000
saldo_inicial = 100000

# pedir usuario
print("Ingrese nombre de usuario: ")
usuario = int(input())


# contador para intentos
intentos = 0
while intentos < 3:
    # tratar todos los input como numeros int()

    # pedir clave
    print("Ingrese clave: ")
    clave = int(input())

    # Validar clave y Monto a retirar
    if clave == clave_real:
        print("¿Cuanto dinero desea retirar?")
        monto = int(input())

        # Validar monto del cajero vs monto pedido
        if monto <= saldo_cajero and monto <= saldo_inicial:
        # Validar el monto pedido vs monto en mi cuenta

            # Operacion matematicas
            # Descontar plata del usuario
            saldo_restante_usuario = saldo_inicial - monto

            # Descontar dinero retirado a saldo del cajero
            saldo_cajero_final = saldo_cajero - monto

            print("Saldo Cuenta= ", saldo_restante_usuario )
            print("Saldo Cajero= ", saldo_cajero_final)
            break
        else:
            print("Monto no permitido")
            break

    else:
        print("Clave Incorrecta, intente nuevamente")
        intentos = intentos + 1  #  otroa forma de escribir -> intentos += 1

if intentos == 3:
    print("Tarjeta Bloqueada")

print("Muchas gracias!!")