#Cajero Automático

user = "10334151"
passs = "1803"
cash = 1000000
saldo = 100000
intento = 0

while intento <= 3 :
    U = input("Ingrese su usuario: ")
    C = input("Ingrese su contraseña: ")    
    if U == user and C == passs:
        print("Bienvenido")
        intento = 4
        while True:
                    retiro = eval(input("Ingrese el que monto desea retirar: "))
                    if retiro > saldo:
                         print("Excede el máximo") 
                    else:
                        saldo2 = saldo - retiro
                        cajero1 = cash-retiro
                        cash = cajero1
                        saldo = saldo2
                        print("saldo cuenta = ", saldo)
                        print("Saldo cajero = ", cash)
                        opcion = input("Si desea salir, escriba algo distinto de N: ")
                        if opcion != "N":
                            break     
    else:
        intento = intento+1
        print("Usuario y/o contraseña incorrecta")
        if intento == 3:
            print("Tarjeta bloqueada")
            break