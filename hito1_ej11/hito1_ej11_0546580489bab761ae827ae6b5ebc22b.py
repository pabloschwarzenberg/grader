
#Definir variables
contador_intentos = 0
cantidad_billetes_v = 20
cantidad_billetes_d = 40
cantidad_billetes_c = 40
billetes_v = 20000
billetes_d = 10000
billetes_c = 5000
darv = 0
dard = 0
darc = 0
saldo_cajero = billetes_c * cantidad_billetes_c + billetes_d * cantidad_billetes_d + billetes_v * cantidad_billetes_v
saldo_usuario = 100000
clave_usuario = 1803
usuario = 10334151
usuario_ingresado = int(input("Ingrese su numero de usuario: "))
clave_ingresada = 0

#chequear que el usuario ingresado existe

while usuario_ingresado != usuario:
    print("usuario no existe, volver a intentarlo")
    usuario_ingresado = int(input("Ingrese su numero de usuario: "))

#chequear que la clave ingresada sea la correcta, si no, entrar a bucle que se cierra si se llegan a los 3 intentos fallidos

while clave_ingresada != clave_usuario:
    contador_intentos += 1
    clave_ingresada = int(input("Ingrese su clave nuevamente (Intento {0} de 3): "))
    if contador_intentos == 3:
        break

if clave_ingresada == clave_usuario:
    retiro = int(input("Ingrese el dinero a retirar: "))
    if retiro > saldo_usuario:
        print("Usted no cuenta con este dinero")
    elif retiro > saldo_cajero:
        print("El cajero no cuenta con esta cantidad de dinero")
    else:
        saldo_cajero -= retiro
        saldo_usuario -= retiro
        print("saldo cuenta={0}".format(saldo_usuario))
        print("saldo cajero={0}".format(saldo_cajero))
        darv = int(retiro / billetes_v)
        cantidad_billetes_v -= darv
        retiro -= darv * billetes_v
        dard = int(retiro / billetes_d)
        cantidad_billetes_d -= dard
        retiro -= dard * billetes_d
        darc = int(retiro / billetes_c)
        cantidad_billetes_c -= darc
        print("billetes 20000={0}".format(darv))
        print("billetes 10000={0}".format(dard))
        print("billetes 5000={0}".format(darc))
 