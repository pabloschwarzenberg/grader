#Cajero Automático

#Definir variables
contador_intentos = 0
saldo_cajero = 1000000
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
      