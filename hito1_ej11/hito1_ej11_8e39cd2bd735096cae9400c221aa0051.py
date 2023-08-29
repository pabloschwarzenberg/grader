#Cajero Automático
SaldoCajero = 1000000
SaldoCuenta = 100000
bi20mil = 20
bi10mil = 40
bi5mil = 40
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
                retira20mil = 0
                retira10mil = 0
                retira5mil = 0
                while(dineroaretirar > 0):
                    if(dineroaretirar >= 20000 and bi20mil > 0):
                        retira20mil = retira20mil + 1
                        bi20mil = bi20mil - 1
                        dineroaretirar = dineroaretirar - 20000
                    if(dineroaretirar >= 10000 and bi10mil > 0):
                        retira10mil = retira10mil + 1
                        bi10mil = bi10mil - 1
                        dineroaretirar = dineroaretirar - 10000
                    if(dineroaretirar >= 5000 and bi5mil > 0):
                        retira5mil = retira5mil + 1
                        bi5mil = bi5mil - 1
                        dineroaretirar = dineroaretirar - 5000   
                
                print("saldo cuenta =", SaldoCuenta)
                print("saldo cajero =", SaldoCajero)
                print("billetes 20000=", retira20mil)
                print("billetes 10000=", retira10mil)
                print("billetes 5000=", retira5mil)
            else:
                print("monto invalido")
        else:
            print("monto invalido")
        respuesta = input("quiere volver a operar (S/N)")