#Cajero Automático
cajero = 1000000
cuenta = 100000
intentos = 1
salida = "N"
while((intentos <= 3) and (salida == "N")):
    usuario = int(input("Ingrese su codigo de usuario: "))
    clave = int(input("Ingrese su clave: "))
    if(intentos == 3):
        print("Tarjeta bloqueada")
    elif((clave == 1803) and (usuario == 10334151)):
        print("Saldo cajero:",cajero)
        print("Saldo cuenta:",cuenta)
        monto = int(input("Monto a retirar: "))
        cajero = cajero - monto
        cuenta = cuenta - monto
        print ("saldo cuenta=",cuenta)
        print ("saldo cajero=",cajero)
        salida = input("Para continuar ingrese  N: ")
    elif(usuario != 10334151):
        print("Usuario invalido")
        salida = input("Para continuar ingrese  N: ")
    elif(clave != "1803"):
        print("Clave invalida")
        salida = input("Para continuar ingrese  N: ")

   
        

    intentos = intentos + 1

