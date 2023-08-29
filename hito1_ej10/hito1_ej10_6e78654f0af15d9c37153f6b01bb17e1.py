#Cajero Automático
#Ingreso de usuario
Usuario = int(input('Ingrese su rut sin puntos ni guión: '))

#Ingreso de contraseña, con sus intentos
i = 0
while i < 3:
    i = i+1

    #Si introduce la contraseña correcta
    Clave = int(input("Ingrese su clave: "))
    if Clave==1803:
        print('Contraseña valida')
        break
   #Si la contraseña no es 1803
    if Clave !=1803:
        print('Contraseña invalida')
   #Si intentó 3 veces y la contraseña es invalida
    else:
        if i==3:
            print ("Tarjeta bloqueada")
            break
            exit()

#Una vez ingresado al cajero
DineroEnCuentaDelUsuario= 100000
DineroEnCajero= 1000000
RetirarDinero= int(input('Cuanto dinero quiere extraer de su cuenta?: '))
if (RetirarDinero) > (DineroEnCuentaDelUsuario):
    print('Monto no permitido')
if (RetirarDinero) > (DineroEnCajero):
    print('Monto no permitido')
else:
    print("Saldo cuenta=",(DineroEnCuentaDelUsuario-RetirarDinero))
    print("Saldo Cajero=",(DineroEnCajero-RetirarDinero))