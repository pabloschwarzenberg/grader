#Cajero Automático

saldo_cajero = 1000000
clave = 1803
contador_intentos = 3
validador_clave = False
usuario = input("Ingrese rut de usuario: ")
while contador_intentos != 0 and not validador_clave:
    clave = int(input("Ingrese su clave secreta: "))
    if clave//1000 < 1 or clave//1000 > 9:
        print("---Ingrese su clave de 4 digitos---")
        continue
    if clave != clave:
        print("---Clave ingresada invalida---")
        contador_intentos = contador_intentos - 1
    else:
        print("Bienvenido", usuario)
        validador_clave = True
        saldo_cuenta = 100000
        monto = int(input("¿Cuanto desea girar?: "))
        if monto > saldo_cuenta:
            print("---Monto invalido---")
        else:
            saldo_cuenta = saldo_cuenta - monto
            saldo_cajero = saldo_cajero - monto

if contador_intentos == 0:
    print("---Su tarjeta ha sido broqueada---")
print("saldo cuenta= ", saldo_cuenta)
print("saldo cajero= ", saldo_cajero)