#Contestador de celular
 
n = input("ingrese numero de telefono(8 digitos): ")
seguir = True
while seguir:
    if len(n) == 8:

        h = input("ingrese hora de la llamada(solo los primeros dos numeros): ")

        if h <= "07":
            print("contestas")
            break
        elif h == "14":
            if int(n[6]) == 9 and int(n[7]) == 0 and int(n[9]) == 9:
                print("contestar")
                break
            else:
                print("No contestar")
        elif "17" <= h <= "19":
            if int(n[1]) != 8 and int(n[2]) != 7 and int(n[3]) != 7:
                print("contestar")
                break
            else:
                print("no contestar")
                break
        elif h>"19":
            print("No Contestar")
            break
        else:
            print("Contestar")
            break
    else:
        n = input("numero incorrecto, ingrese nuevamente el numero ")
