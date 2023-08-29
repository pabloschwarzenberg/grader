billetes20 = 20000
cbi20 = 20
br20 = 0
billetes10 = 10000
cbi10 = 40
br10 = 0
billetes5 = 5000
cbi5 = 40
br5 = 0
cajero = (billetes20*cbi20) + (billetes10*cbi10) + (billetes5*cbi5)
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
            retirar = retiro
            while(retirar!=0):
                if(retirar >= 20000):
                    br20 = br20 + 1
                    retirar = retirar - 20000
                elif(retirar >= 10000 and retirar < 20000):
                    br10 = br10 + 1
                    retirar = retirar - 10000
                else:
                    br5 = br5 + 1   
                    retirar = retirar - 5000

            print("Ha retirado: ",retiro," pesos del cajero")
            print("billetes 20000=",br20)
            print("billetes 10000=",br10)
            print("billetes 5000=",br5)
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