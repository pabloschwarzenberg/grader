#Cajero Automático
UsuarioCajero = 10334151 
ClaveCajero = 1803
cajero= 1000000
cuentacorriente = 100000
intentos = 1
while True:
    if intentos != 4:
        Usuario = int(input("Ingrese el usuario: "))
        Clave = int(input("Ingrese la contraseña: "))
    elif intentos == 4:
        print('Tarjeta bloqueada')
        break
    if Usuario == UsuarioCajero and Clave == ClaveCajero:
        retiro = int(input("Cuanto dinero desea retirar: "))
        if retiro > cuentacorriente:
            print("Monto no permitido")
        else:
            cuentacorriente -= retiro
            print("Saldo cuenta=" + str(cuentacorriente))
            cajero-=retiro
            print("Saldo cajero=" +str(cajero))
        opcion = input()
        if opcion != 'N':
            break
    else:
        print('Usuario y/o clave incorrecta, intento numero: ' + str(intentos))
        intentos += 1