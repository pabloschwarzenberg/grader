print("Contestadora Autómatica")
numero = int(input("Número telefónico: "))
hora = int(input("Hora de la llamada: "))
if(hora > 19):
    print("NO CONTESTAR")
else:
    if(hora >= 0 and hora <= 7):
        print("CONTESTAR")
    else:
        c3 = numero % 1000
        if(hora < 14 and c3 == 909):
            print("CONTESTAR")
        else:
            if(hora >= 17 and hora <= 19 and not(numero // 100000)):
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")