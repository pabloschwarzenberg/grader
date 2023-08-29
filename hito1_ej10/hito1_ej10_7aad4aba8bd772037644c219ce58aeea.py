#Cajero Automático
Usuario_u = "10334151"
ClaveCuenta_u = "1803"
menu = 0
Cajero = 1000000
Cuenta = 100000
Bloqueo = 0

while menu == 0:
    print("Si desea salir del programa, ingrese la letra Y")
    Usuario = input("\nIngrese su usuario >>> ")
    if Usuario == "Y":
        menu += 5
        print("Adios")
    while Usuario != Usuario_u:
        print("\nUsuario invalido")
        Usuario = (input("\nIngrese su usuario >>> "))    
    if Usuario == Usuario_u:
            Clave = input("\nIngrese su clave >>> ")
    while Clave != ClaveCuenta_u:
                    print("Clave invalida")
                    Bloqueo += 1
                    Clave = (input("\nIngrese su clave >>> "))              
    if Bloqueo > 3:
        menu += 10 
        print("Adios")
    if Clave != "N":
                    menu += 5
                    print("Adios")
    if Clave == ClaveCuenta_u:
        print("Monto en cajero:",Cajero)
        print("Monto en cuenta:",Cuenta)
        MontoRetiro = int(input("\nIngrese el monto a retirar >>> "))
        while MontoRetiro > Cajero:
            print("El monto a retirar no puede superar al monto en el cajero")
            print("\nMonto en cajero:",Cajero)
            MontoRetiro = int(input("\nIngrese el monto a retirar >>> "))
        if MontoRetiro < Cajero:
            Cajero = Cajero - MontoRetiro
            Cuenta = Cuenta + MontoRetiro
            print("\nTransaccion exitosa")
