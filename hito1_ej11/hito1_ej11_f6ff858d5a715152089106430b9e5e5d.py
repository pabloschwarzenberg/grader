#Cajero Automático

intentos = 3
salida = "N"

b_20mil = 400000
billetes_20mil = 0

b_10mil = 400000
billetes_10mil = 0

b_5mil = 200000
billetes_5mil = 0


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

        while (retiro > 0):
            if (retiro >= 20000):
                retiro = retiro - 20000
                billetes_20mil = billetes_20mil + 1
                
            elif (retiro >= 10000):
                retiro = retiro - 10000
                billetes_10mil = billetes_10mil + 1
                
            elif (retiro >= 5000):
                retiro = retiro - 5000
                billetes_5mil = billetes_5mil + 1
                
        frase1 = "saldo cuenta"+"="+str(saldo_cuenta)
        frase2 = "saldo cajero"+"="+str(saldo_cajero)
        print(frase1)
        print(frase2)
        
    salida = input("¿Desea continuar?, marque con cualquier letra menos la N para continuar: ")

frase20mil = "billetes 20000=" + str(billetes_20mil)
frase10mil = "billetes 10000=" + str(billetes_10mil)
frase5mil = "billetes 5000=" + str(billetes_5mil)


if billetes_20mil != 0:
    print(frase20mil)
    
if billetes_10mil != 0:
    print(frase10mil)
    
if billetes_5mil != 0:
    print(frase5mil)