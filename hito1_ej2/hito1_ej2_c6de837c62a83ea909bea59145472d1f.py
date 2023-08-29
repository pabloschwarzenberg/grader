#Contestador de celular
numero = int(input("Ingrese número telefonico: "))
num = str(numero)
num_tel = list(num)
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora <= 7:
    print("CONTESTAR")

elif hora < 14:
    if num_tel[5] == '9' and num_tel[6] == '0' and num_tel[7] == '9':
        print("CONTESTAR")

    else:
        print("NO CONTESTAR")

elif hora < 17:
    print("NO CONTESTAR")

elif hora >= 17 and hora <= 19:
    if num_tel[0] == '8' and num_tel[1] == '7' and num_tel[2] == '7':
        print("NO CONTESTAR")

    else:
        print("CONTESTAR")

else:
    print("NO CONTESTAR")
      