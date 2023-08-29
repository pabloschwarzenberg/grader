#Cajero Automático
var_Usuario = 10334151
var_Password = 1803
var_MontoCajero = 1000000
var_Billete20 = 20
var_Billete10 = 40
var_Billete05 = 40
var_MontoCuenta = 100000
var_IngresarUsuario = int(input("Ingresar usuario: "))
while (var_IngresarUsuario != var_Usuario):
    var_IngresarUsuario = int(input("Ingresar usuario: "))
for k in range (0, 3):
    var_IngresarPassword = int(input("Ingresar contraseña: "))
    if (var_IngresarPassword != var_Password) and (k == 2):
        print("tarjeta bloqueada")
        break
    elif (var_IngresarPassword != var_Password):
        print("clave invalida")
    elif (var_IngresarPassword == var_Password):
        var_MontoRetiro = int(input("Cuanto dinero desea retirar?: "))
        while (var_MontoRetiro > var_MontoCuenta):
            print("monto no permitido")
            var_MontoRetiro = int(input("Cuanto dinero desea retirar?: "))
        if (var_MontoRetiro <= var_MontoCuenta):
            print("saldo cuenta=", str(var_MontoCuenta - var_MontoRetiro))
            print("saldo cajero=", str(var_MontoCajero - var_MontoRetiro))
            var_Cuenta20 = 0
            var_Cuenta10 = 0
            var_Cuenta05 = 0
            while (var_MontoRetiro > 0):
                if (var_MontoRetiro >= 20000):
                    var_Cuenta20 += 1
                    var_Billete20 -= 1
                    var_MontoRetiro = var_MontoRetiro - 20000
                if (var_MontoRetiro >= 10000):
                    var_Cuenta10 += 1
                    var_Billete10 -= 1
                    var_MontoRetiro = var_MontoRetiro - 10000
                if (var_MontoRetiro >= 5000):
                    var_Cuenta05 += 1
                    var_Billete05 -= 1
                    var_MontoRetiro = var_MontoRetiro - 5000
            print("billetes 20000=", str(var_Cuenta20))
            print("billetes 10000=", str(var_Cuenta10))
            print("billetes 5000=", str(var_Cuenta05))
        break
    break