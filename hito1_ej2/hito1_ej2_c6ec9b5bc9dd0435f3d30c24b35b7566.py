#Contestador de celular
numero = int(input("Ingrese un número telefonico: "))
num = str(numero)
numero_telefono = list(num)
hora = int(input("Ingrese hora de la llamada: "))
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora < 14:
    if numero_telefono[5] == '9' and numero_telefono[6] == '0' and numero_telefono[7] == '9':
        print("Contestar")

    else:
        print("No contestar")

elif hora < 17:
    print("No contestar")

elif hora >= 17 and hora <= 19:
    if numero_telefono[0] == '8' and numero_telefono[1] == '7' and numero_telefono[2] == '7':
        print("No contestar")

    else:
        print("Contestar")

else:
    print("No contestar")