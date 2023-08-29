# Cajero Automático
usuario = str(input("Ingrese Usuario: "))
contador = 1
disponible = 100000
while usuario != "10334151":
    usuario = str(input("Error, Ingrese Usuario: "))
clave = str(input("Ingrese Clave: "))
while clave != "1803":
    usuario = str(input("Error, Ingrese Clave: "))
    contador = contador + 1
    if contador == 3:
        print("Clave Bloqueada")
        break
flag = "0"
while flag != "1":
    print("Saldo en Cuenta: ", disponible)
    retiro = int(input("Que Monto Desea Retirar: "))
    while retiro < 1 or retiro > disponible:
        retiro = int(input("Error, Que Monto Desea Retirar: "))

    disponible = disponible - retiro
    print("Saldo disponible: ", disponible)
    respuesta = str(input("Desea Otra Operacion: (S/N)"))
    while respuesta not in ["S", "N"]:
        respuesta = str(input("ERROR, Desea Otra Operacion: (S/N)"))

    if respuesta == "N":
        flag = "1"