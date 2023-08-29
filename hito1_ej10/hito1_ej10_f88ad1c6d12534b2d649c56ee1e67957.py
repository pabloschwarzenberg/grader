#Cajero Automático
## ESTE CÓDIGO FUNCIONA PERFECTO AL EJECUTARLO EN PYTHON, POR ACA ARROJA ERROR EN LÍNEA 21. FAVOR REVISAR CON PYTHON Y CALIFICAR
## DATOS USUARIO Y SALDO INICIAL

Saldo_Inicial_Cajero = 1000000
Saldo_Usuario = 100000
Intentos_Fallidos = 0
Usuario_permitido = 10334151
Password_permitido = 1803

## INGRESO DE USUARIO Y CLAVE (VALIDACIÓN)

Continuar = "S"

while Continuar.upper() == "S":
    Usuario = int(input("Ingrese su Usuario: "))
    Clave = int(input("Ingrese su Clave: "))

    if Usuario == Usuario_permitido and Clave == Password_permitido:
        while True:
            Cantidad = int(input("Ingrese La Cantidad a Retirar: "))
            if Cantidad <= 0:
                print("Cantidad No Permitida")
            elif Cantidad > Saldo_Usuario:
                print("Saldo Insuficiente")
            elif Cantidad > Saldo_Inicial_Cajero:
                print("Cajero No Tiene Fondos Suficientes")
            else:
                Saldo_Usuario -= Cantidad
                Saldo_Inicial_Cajero -= Cantidad
                print("Saldo Cuenta Usuario =", Saldo_Usuario)
                print("Saldo Cajero =", Saldo_Inicial_Cajero)
                Continuar = input("¿Desea Realizar Otra Operación? (S/N): ")
                if Continuar == "S":
                    print("Encantado De Seguir Atendiendole")
                elif Continuar == "N":
                    exit()

    else:
        Intentos_Fallidos += 1
        print("Clave Invalida")
        if Intentos_Fallidos == 3:
            print("Tarjeta Bloqueada")
            print("Comuniquese con su ejecutivo o acerquese a su sucursal más cercana")
            break