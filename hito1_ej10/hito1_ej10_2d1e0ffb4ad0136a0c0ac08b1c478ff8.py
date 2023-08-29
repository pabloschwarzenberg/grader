#cajero automatico nivel
cajero = 1000000
cuenta = 100000
usuario = "10334151"
clave = "1803"
user = input("user: ")
if user == usuario:
    contador = 0
    while contador < 3:
        contra = input()
        if clave != contra:
            contador += 1
            print("clave invalida")
            continue
        retiro = eval(input("cuanto dinero desea retirar: "))
        if retiro > 100000:
            print("monto no permitido")
        else:
            print("monto permitido")