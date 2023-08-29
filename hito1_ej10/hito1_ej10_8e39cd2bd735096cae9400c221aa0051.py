#Cajero Automático
SaldoCajero = 1000000
SaldoCuenta = 100000
usuario  = int(input("ingrese el usuario: "))
while(usuario != 10334151):
    print("usuarion equivocado")
    usuario  = int(input("vuelva a ingresar su usuario: "))
clave = int(input("ingrese su clave: "))
intentos = 0
while not (clave == 1803):
    intentos = intentos + 1
    print("Clave invalida")
    if(intentos == 3):
        print("Trajeta bloqueada")
        break
    else:    
         clave = int(input("ingrese su clave: "))
if(intentos != 3):
    respuesta = "S"
    while(respuesta == "S"):
        dineroaretirar = int(input("monto a retirar: "))
        if(dineroaretirar <= SaldoCajero):
            if(dineroaretirar <= SaldoCuenta):
                SaldoCajero = SaldoCajero - dineroaretirar
                SaldoCuenta = SaldoCuenta - dineroaretirar
                print("saldo cuenta=",SaldoCuenta)
                print("saldo cajero=",SaldoCajero)
            else:
                print("monto invalido")
        else:
            print("monto invalido")
        respuesta = input("quiere volver a operar (S/N)")      