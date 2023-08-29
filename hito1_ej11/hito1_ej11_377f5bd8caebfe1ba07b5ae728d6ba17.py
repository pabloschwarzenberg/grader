#Cajero Automático
p = True
while (p):
    bloqueada = False
    veinte_dar="0"
    diez_dar="0"
    cinco_dar="0"


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

    print("Usted cuenta con $"+str(dinero))


    atm = eval(input("¿Cuanto dinero quisiera retirar?: "))
    guardo = atm
    if atm>20000:
      sobra = atm/20000
      veinte_dar = str(sobra)[0:1]
      guardo = guardo-(int(veinte_dar)*20000)
    if guardo>10000:
      sobra = guardo/10000
      diez_dar = str(sobra)[0:1]
      guardo = guardo-(int(diez_dar)*10000)
    if guardo>=5000:
      sobra = guardo/5000
      cinco_dar = str(sobra)[0:1]
      guardo = guardo-(int(cinco_dar)*5000)


    if atm > dinero:
        atm = eval(input("Monto no permitido: "))
    else:
      dinero = dinero-atm
      cajero = cajero-atm
    print("saldo cuenta="+ str(dinero))
    print("saldo cajero="+ str(cajero))
    print("billetes 20000="+veinte_dar)
    print("billetes 10000="+diez_dar)
    print("billetes 5000="+cinco_dar)
    ingresar = input("Para Continuar digíte la letr N: ")
    if ingresar.upper() != "N":
        break