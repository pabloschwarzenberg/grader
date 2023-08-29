# Cajero Automático
saldo_cajero = 1000000
saldo_cliente = 100000
cliente = 10334151
clave = 1803
b1 = 20000
b2 = 10000
b3 = 5000
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
                c1 = monto // b1
                c2 = (monto - c1*b1) // b2
                c3 = (monto - c1*b1 - c2*b2) // b3
                print("Saldo retirado")
                print("Saldo cuenta = %d" % (saldoc))
                print("Saldo cajero = %d" % (saldoca))
                print("Billetes 20000 = %d" %(c1))
                print("Billetes 10000 = %d" %(c2))
                print("Billetes 5000 = %d" %(c3))

                if salir != "n" or salir != "N":
                    break
        elif monto > 100000 or saldoc < 0:
                print("Monto no permitido")
                if salir != "n" or salir != "N":
                    break

print("Gracias por usar nuestro servicio")


