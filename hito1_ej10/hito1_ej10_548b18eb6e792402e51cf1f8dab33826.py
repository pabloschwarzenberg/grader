saldo_cuenta = 100000
saldo_cajero = 1000000
i = 0

user = eval(input("Ingrese nombre de usuario: "))
while True:
    password = eval(input("Ingrese su contraseña: "))
    
    if password == 1803:
        retiro = eval(input("Ingrese el monto que desea retirar: "))
        if retiro <= saldo_cuenta:
            saldo_cuenta = saldo_cuenta - retiro
            saldo_cajero = saldo_cajero - retiro
        else:
            print("monto no permitido")
        break
    else:
        i += 1
        print("clave invalida")
        if i == 3:
            print("tarjeta bloqueada")
            break
print("saldo cuenta=",saldo_cuenta)
print("saldo cajero=",saldo_cajero)