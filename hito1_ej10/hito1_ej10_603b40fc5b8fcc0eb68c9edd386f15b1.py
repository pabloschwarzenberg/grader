#Cajero Automático
X = input("Ingrese el numero de Usuario: ")
Y = int(input("Ingrese la clave: "))
intentosRealizados = 0
cajero=1000000
cuenta=100000

while  intentosRealizados <= 1:
    intentosRealizados = intentosRealizados + 1
    if Y == 1803:       
        print("Clave valida")
        Z = int(input("¿Cuanto desea retirar? "))
        if Z <= cajero:
            cajero= cajero-Z
            cuenta= cuenta-Z
            print("(saldo cuenta=",(cuenta),", saldo cajero=",(cajero),")")
            
            print("salir programa")
            salir= input()
            if salir!="N":
                break
            
        else:
            print("monto no permitido")
    
    else:
        print("Clave invalida")
        print("Intente de nuevo")
        Y = int(input("Ingrese la clave: "))
    while intentosRealizados == 2 and Y!= 1803:
        print("tarjeta bloqueada")
        print("salir programa")
        salir = input()
        if salir != "N":
            break


