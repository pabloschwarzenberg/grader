#Cajero Automático
invalidez = 0
#Configuracion del cajero automatico
while invalidez < 3:
    y = int(input("Ingrese su nombre de usuario: "))
#Nombre de usuario correcto
    if y == 10334151:
        x = int(input("Saludos usuario 10334151 ingrese su clave: "))
#Contraseña correcta
        if x == 1803:
            monto_inicial = 1000000
            saldo_inicial = 100000
            monto_a_retirar = int(input("¿Cual es su monto a retirar?: "))
            if monto_a_retirar > saldo_inicial:
                print("monto no permitido")
            else:
                cuenta = saldo_inicial - monto_a_retirar
                cajero = monto_inicial - monto_a_retirar
                print("saldo cuenta=",cuenta,sep="")
                print("saldo cajero=",cajero,sep="")
#¿Desea repetir?
                z = input("¿Desea repetir el programa?(ingrese n para repetir): ")
                if z != "n":
                    break
                else:
                    pass
#Contraseña incorrecta                
        else:
            print("clave invalida")
            invalidez = invalidez +1
            if invalidez == 3:
                print("tarjeta bloqueada")
                break
#Nombre de usuario incorrecto
    else:
        print("Nombre de usuario no reconocido")