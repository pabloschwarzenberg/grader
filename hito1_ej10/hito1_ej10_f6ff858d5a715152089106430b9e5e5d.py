intentos = 3
salida = "N"

saldo_cajero =  1000000

saldo_cuenta = 100000


while ((intentos > 0) and (salida == "N")):
    
    usuario = input("Ingrese usuario: ")
    psw = input("Ingrese contraseña: ")

    if (psw != "1803"):
        intentos = intentos - 1
        print("Clave invalida")
        
    elif (usuario != "10334151"):
        print("Usuario no válido")

    else:
        print("Saldo cajero:", saldo_cajero)
        print("Saldo cuenta:", saldo_cuenta)
        retiro = eval(input("monto a retirar: "))
        saldo_cajero = saldo_cajero - retiro
        saldo_cuenta = saldo_cuenta - retiro
                
        frase1 = "saldo cuenta"+"="+str(saldo_cuenta)
        frase2 = "saldo cajero"+"="+str(saldo_cajero)
        print(frase1)
        print(frase2)
        
    salida = input("¿Desea continuar?, marque con cualquier letra menos la N para continuar: ")