def Monto(monto , Cajero = 1000000, usuario = 100000):
    if monto > Cajero:
        return "El Monto seleccionado no esta permitido"
    else:
        usuario = usuario-monto
        Cajero = Cajero-monto
        print("saldo cuenta=", usuario)
        print("saldo cajero=", Cajero)
        return [usuario , Cajero]
a = 0
b = 0
intentos = 0
while b == 0:
    if a == 0:
        usuario1 = input("Ingrese su RUT: ")
        clave = input('Ingrese su clave porfavor: ')
        if clave == "1803":
            a = 1
        elif intentos == 2:
            print("Lo sentimos, su tarjeta acaba de ser bloqueada. Dirijase a alguna sucursal mas cercana")
            break
        else:
            intentos += 1
    elif a == 1:
        print("Ingrese el monto que desea sacar")
        x = input()
        incorrecto = "qwertyuiopñlkjhgfdsazxcvbm,.-{}+´¿QWERTYUIOPÑLKJHGFDSAZXCVBM"
        if x in incorrecto:
            break
        elif x == "N":
            a = 1
        else:
            Monto(float(x))