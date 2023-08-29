from time import sleep              #from e import= imoort trata de usar la misma variable otra vez y from especifica que se quiero utilizar 
total_cajero = 1000000
total_usario = 100000

Y = str(int(input("Ingrese el usuario: ")))   # str = es una secuencia inmutable de caracteres
X = str(int(input("Ingrese la contraseña: ")))
while True:                                                                 #true verdadero 
    if Y == "10334151" and X == "1803":
        print("Usuario y contraseña correctos")
        sleep(1)                                                               #sleep frenar si quito sleep y break el while se vuelve infinito repentinamente 
        monto_a_retirar = int(input("Ingrese el monto a retirar: "))
        if monto_a_retirar>total_usario and monto_a_retirar>total_cajero:
            print("monto no permitido")
            break
        if monto_a_retirar<total_usario and monto_a_retirar<total_cajero:     #importante este paso juego de variables 
            total_usario_final = total_usario-monto_a_retirar
            total_cajero_final = total_cajero-monto_a_retirar
            print("saldo cuenta=", total_usario_final)
            print("saldo cajero=", total_cajero_final)
            
            x20k = int(monto_a_retirar/20000)
            monto_a_retirar = monto_a_retirar%20000
            x10k = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            x5k = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
            
            print("billetes 20000= ",x20k)
            print("billetes 10000= ",x10k)
            print("billetes 5000= ",x5k)
        if monto_a_retirar!="N":
            break
  
    if Y != "10334151" or X != "1803":  #! solo si 
        print("clave invalida")
        sleep(1)
        print("INTENTA POR SEGUNDA VEZ")
        sleep(1)
        PIN = str(int(input("Ingrese la contraseña denuevo: ")))
        if usuario != "10334151" or X != "1803":
            print("clave invalida")
            sleep(1)
            print("INTENTO N°3")
            sleep(1)
            PIN = str(int(input("Ingrese la contraseña denuevo: ")))
            if usuario != "10334151" or X != "1803":
                print("tarjeta bloqueada")
                break