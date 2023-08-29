# Cajero Automático
saldo_cajero = 1000000
saldo_cliente = 100000
cliente = 10334151
clave = 1803

intentos = 0
correcto = bool
while intentos < 3:
    entrada1 = int(input("Ingrese su usuario "))
    entrada2 = int(input("Ingrese su clave de 4 digitos "))
    if entrada1 == cliente and entrada2 == clave:
        print("Bienvenido a nuestro Banco")
        correcto = True
        break
    else:
        print("Su clave es inválida")
        intentos = intentos + 1
        correcto = False
else:
    print("Tarjeta bloqueada")

if correcto == True :
    monto = int(input("Ingrese monto a retirar "))
    salir = "a"
    while salir != "N" or salir != "n":
        salir = input("¿Desea continuar? (Para continuar presione N, sino cualquier tecla) ")
        saldoc = saldo_cliente - monto
        saldoca = saldo_cajero - monto
        if monto <= 100000 and saldoc >= 0 :
                print("Saldo retirado")
                print("Saldo cuenta = %d" % (saldoc))
                print("Saldo cajero = %d" % (saldoca))

                if salir != "n" or salir != "N":
                    break
        elif monto > 100000 or saldoc < 0:
                print("Monto no permitido")
                if salir != "n" or salir != "N":
                    break

print("Gracias por usar nuestro servicio")


