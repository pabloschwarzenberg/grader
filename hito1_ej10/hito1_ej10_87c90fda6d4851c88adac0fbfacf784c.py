p = True
while (p):
    bloqueada = False

    user = (input("Ingrese usuario: "))
    pas = (input("Ingrese clave de usuario: "))
    attemp = 0
    while (user != "10334151") or (pas != "1803"):
        user = (input("Ingrese usuario nuevamente: "))
        pas = (input("Ingrese clave de usuario nuevamente: "))
        attemp +=1
        if attemp == 2:
            print("Tarjeta bloqueada")
            bloqueada = True
            break
    if bloqueada == True:
      break

    dinero = 100000
    cajero = 1000000

    atm = eval(input("¿Cuanto dinero quisiera retirar?: "))
    
    print("Usted cuenta con $"+str(dinero))
    # pas = input("Para retirar dinero valide su contraseña: ")
    # attemp = 0
    # while pas != "1803":
    #     attemp +=1 
    #     if attemp == 2:
    #         print("Tarjeta bloqueada")
    #         pas = input("Clave erronea , Ingrese nuevamente su contraseña: ")
    #         break
    # if bloqueada == True:
    #   break


    

    if atm > dinero:
        atm = eval(input("Monto no permitido: "))
    else:
      dinero = dinero-atm
      cajero = cajero-atm
    print("saldo cuenta="+ str(dinero))
    print("saldo cajero="+ str(cajero))

    ingresar = input("Para Continuar digíte la letr N: ")
    if ingresar.upper() != "N":
        break
