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
        if Z <= cuenta:
            cajero= cajero-Z
            cuenta= cuenta-Z
            bi20= Z//20000
            tmp= Z%20000
            bi10=tmp//10000
            tmp=tmp%10000
            bi5=tmp//5000          
            print("(saldo cuenta=",(cuenta),", saldo cajero=",(cajero),")")
            if bi20 <=20:
                print(Z)
                print("billetes 20000=",bi20)
                print("billetes 10000=",bi10)
                print("billetes 5000=",bi5)                     
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
      