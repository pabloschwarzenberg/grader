#Cajero Automático
var_Usuario = 10334151
var_Password = 1803
var_MontoCajero = 1000000
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
        break
    break