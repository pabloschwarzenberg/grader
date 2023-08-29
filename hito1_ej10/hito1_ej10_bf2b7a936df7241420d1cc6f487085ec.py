#Cajero Automático

cajero = 1000000
saldo = 0
intentos = 0

while True:
    user = int(input("Ingrese su usuario: "))
    clave = int(input("Ingrese su contraseña: "))
    if(user == 10334151 and clave == 1803):
        saldo = 100000
        retiro = int(input("Cuanto dinero va a retirar?: "))
        if (retiro <= saldo and retiro > 0):
            nuevocajero = cajero - retiro
            saldo = saldo - retiro
            print("Ha retirado: ",retiro," pesos del cajero")
            print("saldo cuenta=",saldo)
            print("saldo cajero=",nuevocajero)
            break
        else:
            print("Monto ingresado no válido")
    else: 
        intentos = intentos + 1
        print("Clave ingresada no válida. Intentos realizados: ",intentos)
        if intentos == 3:
            print("Su tarjeta ha sido bloqueada")
            break
            