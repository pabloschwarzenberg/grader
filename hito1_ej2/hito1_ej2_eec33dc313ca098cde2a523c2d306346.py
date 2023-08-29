#Contestador de celular
numero = int(input("Ingrese un numero de telefono de 8 cifras: "))
hora = int(input("Ingrese hora: "))
if hora >= 0 and hora <= 7:
    print("Contestar")
elif numero % 1000 == 909:
    print("Contestar")
elif hora >= 17 and hora <= 19 and numero // 100000 != 877:
    print("No contestar")
elif hora > 19:
    print("No contestar")
else:
    print("No contestar")