#Contestador de celular
numero =[]
num = int(input("Ingrese numero telefonico: "))
numero.append(num)
ult_digitos = num % 1000
hora = int(input("Ingrese hora de la llamada: "))


if len(numero) > 8:
    print("Ingreso un numero de mas de 8 cifras")
else:
    if hora > 00 and hora < 7:
        print("CONTESTAR")
    elif hora< 14:
        if ult_digitos==909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif hora > 17 and hora < 19:
        if numero[:3] != 877:
            print("NO CONTESTAR")
        else:
            print("No Contestar")
    elif hora > 19:
        print("NO CONTESTAR")
    else:
        print("ERROR")      