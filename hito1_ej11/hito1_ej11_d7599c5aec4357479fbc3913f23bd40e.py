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
                         continue
                    b2 = retiro//20000
                    if b2 > 0 :
                        r2 = retiro - (b2*20000)
                        print("billetes 20000= ", b2)
                    else:
                        r2 = retiro
                        
                    b1 = r2//10000
                    if b1 > 0:
                        r3 = r2 -(b1*10000)
                        print("Billetes 10000= ", b1)
                    else:
                        r3 = r2
                    b5 = r3//5000
                    
                    if b5 > 0:
                        r4 = r3-(b5*5000)
                        print("Billetes 5000= ", b5)
                    else:
                        r4 = r3
                    
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