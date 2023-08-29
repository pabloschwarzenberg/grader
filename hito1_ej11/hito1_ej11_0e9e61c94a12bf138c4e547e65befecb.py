#Cajero Automático
billetesde20000= 20
billetesde10000= 40
billetesde5000=40
totalbilletes = [billetesde20000, billetesde10000, billetesde5000]
cuenta= 100000
cajero= 1000000

while cuenta !=0:
            contador = 1
            while contador <= 3:
                        usuario= int(input("escribe usuario: "))
                        clave= int(input("escribe clave: "))
                        if usuario==10334151 and clave==1803:
                                    print("has ingresado a tu cuenta")
                                    contador = 4
                                    break
                        
                        else:
                                    print("clave invalida")
                                    if contador == 3:
                                                print("tarjeta bloqueada")
                                    contador= contador +1

            lista = [20000, 10000, 5000]

            print("tu saldo en la cuenta es", cuenta)

            retiro = int(input("ingrese monto a retirar: "))
            if retiro >100000:
                         print("monto no permitido")

            elif retiro <=100000:

                          cuenta= cuenta - retiro
                          cajero= cajero - retiro
                          print("saldo cuenta","=", cuenta)
                          print("saldo cajero","=", cajero)
                          
                          for i in lista:
                                      if retiro >= i:
                                                   queda = retiro//i
                                                   print("Billetes", str(i),"=", str(queda))
                                                   retiro = retiro % i
                         


            salir= str(input("ingrese N para seguir o otra letra para salir: "))

            if salir=="N":
                        continue

            elif salir !="N":
                        break
             
