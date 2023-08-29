saldo_cajero = 1000000
usuario_verdadero = 10334151
clave_real = 1803
saldo_inicial = 100000

print("Ingrese nombre de usuario: ")
usuario = int(input())

intentos = 0
while intentos < 3:

    print("Ingrese clave: ")
    clave = int(input())

    if clave == clave_real:
        print("¿Cuanto dinero desea retirar?")
        monto = int(input())

        if monto <= saldo_cajero and monto <= saldo_inicial:
            saldo_restante_usuario = saldo_inicial - monto
            
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
      