usuario = int(input("ingrese usuario: "))
clave = int(input("ingrese su clave: "))
retirar = int(input("ingrese el monto a sacar"))
sueldo = 1000000
cajero = 100000
if((usuario == 10334151) and (clave == 1803)):
    print("a ingresado correctamente los datos")
    saldo_actual_usuario = (sueldo - retirar)
    saldo_actual_cajero = (cajero - retirar)
    print("saldo cuenta=",saldo_actual_usuario)
    print("saldo cajero=",saldo_actual_cajero)
if(clave != 1803):
    veces += 1

    while veces <= 3:
        print("intentelo nuevamente", veces + 1)
        while (veces == 3):
            print("tarjeta bloqueada")