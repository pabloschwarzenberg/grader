flag1 = True
flag2 = True
flag3 = True
contador = 0
user = "10334151"
password = "1803"
sic = 1000000
siu = 100000
while flag1:
    usuario = input("Usuario: ")
    if usuario == user:
        while flag2:
            contrasena = input("Contraseña: ")
            if contrasena == password:
                flag2 = False
            elif contrasena == "N":
                continue
            else:
                contador += 1
                if contador == 1 or contador == 2:
                    print("clave invalida")
                if contador == 3:
                    print("tarjeta bloqueada")
                    flag3 = False
                    flag2 = False
                    flag1 = False
        while flag3:
            retirar = eval(input("Retirar: "))
            if retirar >= 0 and retirar <= 100000:
                print("['saldo cuenta={}', 'saldo cajero={}']".format((siu-retirar),(sic-retirar)))
                siu -= retirar
                sic -= retirar
                flag3 = False
            elif retirar == "N":
                continue
            else:
                print("monto no permitido")
    elif usuario == "N":
        continue
    else: flag1 = False