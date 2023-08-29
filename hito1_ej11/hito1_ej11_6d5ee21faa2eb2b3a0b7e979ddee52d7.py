#Cajero Automático
usuario = int(input("Ingrese su usuario: "))
if usuario == 10334151:
    saldoinicial = 1000000
    saldocuenta = 100000
    letra = "N"
    contador = 0
    scuenta = 0
    sinicial = 0
    while letra == "N":
        clave = int(input("Ingrese su clave: "))
        if clave == 1803:
            dinero = int(input("Monto a retirar: "))
            if dinero > saldocuenta :
                print("Monto no permitido")
            else :
                scuenta = abs(dinero - saldocuenta)
                sinicial = abs(dinero - saldoinicial)
                print("saldo cuenta=",scuenta)
                print("saldo cajero=",sinicial)
                veinte = 20000
                diez = 10000
                cinco = 5000
                contveinte = 0
                contdiez = 0
                contcinco = 0
                while dinero != 0:
                    if dinero > veinte :
                        contveinte = contveinte + 1
                        dinero = dinero - veinte
                    else :
                        if dinero > diez:
                            contdiez = contdiez + 1
                            dinero = dinero - diez
                        else:
                            contcinco = contcinco + 1
                            dinero = dinero - cinco
                print("billetes 20000=",contveinte)
                print("billetes 10000=",contdiez)
                print("billetes 5000=",contcinco)
        else :
            print("clave invalida")
            contador = contador + 1
        if contador == 3 :
            print("tarjeta bloqueada")
            letra = "S"
        else:
            letra = input("Ingrese la letra N si quiere repetir")
        
else :
    print("Usuario incorrecto")