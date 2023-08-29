#Cajero Automático
saldo_cajero = 1000000
saldo_usuario = 100000
billete1 = 20000
billete2 = 10000
billete3 = 5000
usuario = "10334151"
clave = "1803"

intentos = 0

while intentos < 3:
    ingreso_usuario = input("Ingrese su usuario: ")
    ingreso_clave = input("Ingrese su clave: ")

    if ingreso_usuario == usuario and ingreso_clave == clave:
        monto_retiro = float(input("Ingrese el monto a retirar: "))

        if monto_retiro <= saldo_usuario and monto_retiro <= saldo_cajero:
            saldo_usuario -= monto_retiro
            saldo_cajero -= monto_retiro

            print("Retiro exitoso")
            print("Saldo cuenta:", saldo_usuario)
            print("Saldo cajero:", saldo_cajero)
        else:
            print("Monto no permitido")
        
        break
    else:
        intentos += 1
        print("Clave inválida")

if intentos == 3:
    print("Tarjeta bloqueada")
      